# Orchestration Plan — Stage 15

This plan covers the end‑to‑end path used in Stage 13–14: **data → clean → train → serialize → deploy → monitor**.  
It satisfies the deliverables: tasks, dependencies (DAG), I/O per task, logging & checkpoints, and automation scope.

## 1) Jobs / Tasks
1. **ingest** — generate or pull source data
2. **clean** — validate schema, handle nulls, feature prep
3. **train_or_score** — fit linear model (or run batch scoring)
4. **serialize** — persist model with checksum
5. **deploy** — start Flask API with the persisted model
6. **monitor** — collect data/model/system/business metrics

## 2) Order / Dependencies (DAG)
```
ingest  →  clean  →  train_or_score  →  serialize  →  deploy  →  monitor
```
- Parallelizable: future “report” and “monitor” consumers can read from the same model outputs.

## 3) Inputs / Outputs (I/O) and Idempotency

| Task | Inputs | Outputs | Idempotent? | Notes |
| --- | --- | --- | --- | --- |
| ingest | seed/config | `/data/raw.csv` | **Yes** (same seed = same bytes) | external sources cached to avoid re-download |
| clean | `/data/raw.csv` | `/data/clean.csv` | **Yes** | schema hash + null counts logged |
| train_or_score | `/data/clean.csv` | `model.bin` or `preds.parquet` | **No** (unless fully seeded) | metrics saved to `/reports/metrics.json` |
| serialize | model object | `/model/model.pkl` | **Yes** | SHA256 checksum written to `/model/checksum.txt` |
| deploy | `/model/model.pkl` | running service | **No** | config in `app.env`, port in use checked |
| monitor | service logs, requests | `/reports/monitoring.jsonl` | **Continuous** | PSI/latency/error-rate tracked |

## 4) Logging & Checkpoint Strategy
- Logs: `logs/{task}.log` + console; JSON metrics appended to `/reports/*.jsonl`.
- Checkpoints: keep immutable artifacts (`/data/raw.csv`, `/data/clean.csv`, `/model/model.pkl`).  
- Failure & retry:
  - **ingest**: network fail → retry 3× with 0.5s linear backoff.
  - **train_or_score**: OOM/fit error → retry 1× with smaller batch/params; on fail, keep last known good model.
  - **deploy**: health check fails → rollback to prior model + alert owner.
- Rollback: use latest successful checksum in `/model/checksum.txt` and previous artifact in `/model/backup/`.

## 5) What to Automate Now vs Keep Manual (Rationale)
- **Automate now**: ingest, clean, train, serialize, deploy — they are deterministic and benefit most from repeatability.
- **Keep manual**: hyper‑parameter search and business KPI review — require analyst judgment and are low‑frequency.

## 6) Minimal File Layout
```
data/ raw.csv clean.csv
model/ model.pkl checksum.txt
reports/ metrics.json monitoring.jsonl
logs/ ingest.log clean.log train.log deploy.log
```