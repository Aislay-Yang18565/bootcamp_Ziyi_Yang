# Short Project Summary
This project develops and evaluates a trading strategy for soybean meal futures based on the Moving Average Convergence Divergence (MACD) indicator, specifically focusing on peak and trough signals. By backtesting the strategy, the project assesses its profitability, risk levels, and robustness compared to baseline benchmarks. The problem it addresses is how to systematically capture short- and medium-term price trends in agricultural commodities, where volatility, seasonality, and supply-demand shocks often make traditional trading approaches unreliable.

This matters because soybean meal is a globally traded commodity that plays a key role in the livestock and food industries. Developing systematic, data-driven strategies helps traders and risk managers reduce reliance on subjective decision-making, improve timing of market entry and exit, and potentially enhance returns while managing risk exposure.

# Stakeholder Persona / Context
The primary stakeholders are **commodity traders**, **portfolio managers**, and **risk management analysts** who deal with agricultural futures markets. They care about reliable strategies that balance profitability with risk control, particularly in volatile markets like soybean meal where prices are influenced by global supply chains, weather conditions, and policy changes. These stakeholders value backtested evidence, clear risk-return metrics, and practical trading rules that can be integrated into broader portfolio or hedging strategies.

# Workflow & Lifecycle Mapping — Soybean Meal MACD Strategy
This project implements and analyzes a **MACD-based trading strategy** on soybean meal futures.  
The workflow is structured into phases, each corresponding to specific code modules, data folders, and outputs.

---

## 1. Data Ingestion
- **Purpose**: Load historical soybean meal futures prices (OHLCV).
- **Notebook Section**: Data import cell.
- **Artifacts**: `data/raw/*.xlsx`
- **Checks**: Ensure correct columns (`Date, Open, High, Low, Close`).

## 2. Data Cleaning & Preprocessing
- **Purpose**: Handle missing values, duplicate dates, and type conversions.
- **Notebook Section**: Cleaning steps (`dropna`, `astype`, reindex).
- **Artifacts**: `data/processed/clean.csv`
- **Checks**: Dates are unique and sorted, no NaNs in price series.

## 3. Feature Engineering - MACD
- **Purpose**: Compute:
  - Fast EMA (12-period)
  - Slow EMA (26-period)
  - MACD line = EMA(12) - EMA(26)
  - Signal line (9-period EMA of MACD)
  - Histogram (MACD - Signal)
  - CNN: It is used for extracting local features and is particularly suitable for processing local patterns in images or time series.
  - LSTM: It is used to capture long-term dependencies and is suitable for handling time series data.
  - Transformer: It is used to capture global dependencies, especially through the self-attention mechanism, and can process sequential data in parallel.
- **Notebook Section**: MACD calculation cells.
- **Artifacts**: MACD curves together with price curves and deep learning models to predict prices.
- **Checks**: MACD = EMA_fast - EMA_slow.

## 4. Signal Generation
- **Golden Cross**: `MACD` crosses above `Signal`  **Buy/Long**.
- **Death Cross**: `MACD` crosses below `Signal`  **Sell/Exit/Short**.
- **Notebook Section**: Crossover detection logic.
- **Artifacts**: Dataset column `cross` with {golden, death, none}.
- **Checks**: Signals only occur at true line crossings.

## 5. Strategy Backtesting
- **Purpose**: Apply trading rules with entry/exit based on crossovers.
- **Notebook Section**: Backtest implementation (PnL calculation).
- **Artifacts**: 
  - Equity curve plot
  - Performance metrics (`Sharpe`, `Max Drawdown`, `Win Rate`)
  - JSON/CSV backtest reports under `reports/backtests/`
- **Checks**: No look-ahead bias, metrics finite.

## 6. Analysis & Reporting
- **Purpose**: Evaluate performance and visualize results.
- **Notebook Section**: 
  - Trade signal plots (price + MACD overlays)
  - Backtest metrics summary
- **Artifacts**: 
  - `reports/figures/*.png`
  - Jupyter notebooks as reproducible reports

## 7. Reproducibility & Lifecycle
- **Entry Point**: `src/pipeline/run.py` (optional script) runs all phases.
- **Lifecycle Mapping**:
  1. **Ingest → Clean → Features → Signals → Backtest → Report**
  2. Each step has defined inputs/outputs.
  3. Unit tests validate MACD math, signals, and backtest logic.

## 8. Continuous Improvement
- **Next Steps**:
  - Parameter sweep (fast/slow/signal periods).
  - Walk-forward testing.
  - Risk overlays (stop-loss, volatility targeting).
  - Multi-asset extension.

# Assumptions & Risks — Soybean Meal MACD Strategy

> Scope: MACD (12, 26, 9) crossover strategy on soybean meal (with soybean oil as a comparative leg), backtested from cleaned OHLCV data. Metrics include Annualized Return, Sharpe, Max Drawdown, and Win Rate. Capital withdrawals are logged as “consumption”.

## Assumptions

### 1) 1.1 Data & Instruments
- **Instrument series**: Continuous futures for Soybean Meal (and Soybean Oil for comparison) built with a **volume/open-interest based roll** and **no price back-adjustment gaps** (or adjusted consistently).
- **Data fields**: OHLCV present, timestamps are **trading-day close in local exchange timezone**, strictly increasing and **de-duplicated**.
- **No survivorship bias**; **delistings/contract changes** handled through the roll logic.
- **Currency**: All PnL and capital tracked in **CNY**; no FX conversion applied unless explicitly configured.

### 1.2 Strategy Logic
- **Signal definition**:  
  - *Golden cross*: `MACD` crosses **above** its `Signal` line → **enter/hold long**.  
  - *Death cross*: `MACD` crosses **below** its `Signal` line → **exit/flip short or go flat** (as configured).
- **Execution timing**: Signals generated on bar *t* are **executed on bar t+1** at the **open** (or close, but keep it consistent). No partial fills.
- **Positioning**: Fixed notional (or fixed units) per signal without dynamic leverage unless configured.
- **Transaction costs**: Commission and slippage are **assumed constant** per trade (bps or per contract). If unset, defaults to **0** (backtest-optimistic).

### 1.3 Metrics & Conventions
- **Returns frequency**: Equity curve sampled at the strategy’s bar frequency (default **daily**).
- **Sharpe Ratio**: Uses **simple returns**, annualized with **252** periods/year; **risk-free rate = 2%** unless overridden.
- **Max Drawdown (MDD)**: Peak-to-trough **on equity curve** (percentage).
- **Win Rate**: If trade PnLs provided → **trade-level** win rate; else falls back to **positive-bar** percentage.
- **Annualized Return**:  
  - *User formula*: assumes **2 years** for comparability with prior outputs.  
  - *CAGR*: computed from actual start/end dates.

### 1.4 Capital & Withdrawals
- **Initial capital** fixed and known at start.  
- **Consumption withdrawals** (e.g., min 5,000 / max 50,000 CNY lines) are **exogenous** to the signal logic and reduce equity when triggered; they **do not retroactively alter signals**.

### 1.5 Backtest Hygiene
- **No look-ahead**: Indicators use **past and current bar only**.  
- **No data snooping**: MACD parameters not repeatedly tuned on the same sample without out-of-sample testing.  
- **Stable calendar**: Exchange holidays and limit-up/limit-down sessions are treated as **no-trade** (or skipped) consistently.

## 2) Key Risks & Mitigations

| Risk | Why it matters | Likelihood | Impact | Mitigations |
|---|---|:--:|:--:|---|
| **Roll/contract stitching errors** | Mispriced gaps distort MACD and equity | Med | High | Use audited roll rules; visualize pre/post-roll continuity; unit tests on roll dates |
| **Transaction costs & slippage understated** | Overstates Sharpe/returns | High | High | Calibrate fees/slippage to broker quotes; sensitivity analysis (+/− 2–3× costs) |
| **Liquidity gaps / limit moves** | Orders not filled at assumed prices | Med | High | Use conservative fills (next bar open + slippage), filter illiquid days, add “no fill” logic |
| **Execution-timing mismatch** | Using same-bar fills creates look-ahead | Med | Med | Enforce t+1 execution; assert no indicator uses future bars |
| **Regime shift / seasonality** | Indicator stops working in new regime | Med | High | Walk-forward, rolling windows; add risk overlays (vol targeting, stops) |
| **Overfitting / parameter bias** | Inflated in-sample performance | Med | High | Holdout periods, cross-validation; report **Calmar**, **out/ in** ratios |
| **Data quality issues** | Bad ticks → false signals | Med | Med | Schema & range checks; NA handling; vendor cross-checks |
| **Currency/fee drift** | Changing tick/fee specs alter PnL | Low | Med | Centralize config; snapshot fees/tick size per backtest |
| **Leverage / position sizing errors** | Amplifies drawdowns/liquidation risk | Low | High | Risk caps, max DD/VaR guardrails; unit tests on sizing math |
| **Correlation breakdown (meal vs oil)** | Comparative analysis misleads | Med | Med | Monitor rolling correlations; avoid implicit hedges unless modeled |
| **Tail risk / black swans** | Sharpe understates fat tails | Med | High | Stress tests; EVT-style tail checks; scenario analysis |
| **Holiday/Timezone misalignment** | Misordered bars, wrong returns | Low | Med | Normalize timezones; assert monotonic dates; holiday calendar map |

## 3) Validation Checklist (pre-merge)

- [ ] Indicators computed with **no future leakage** (unit tests for index alignment)  
- [ ] **Costs/slippage** applied and sensitivity run recorded  
- [ ] **Sharpe/MDD/WinRate** recomputed after costs; values within expected bands  
- [ ] **Equity curve** visually inspected around **roll dates**  
- [ ] **Walk-forward** or **out-of-sample** slice reported  
- [ ] Re-run on **alternative data vendor** (spot check)  
- [ ] Results saved to `reports/backtests/*` with **timestamp + config snapshot**

## 4) Triggers to Revisit Assumptions

- Exchange changes tick, margin, or fee schedule  
- Rolling rule or primary contract behavior changes (e.g., delivery rules)  
- Sharpe falls by > **50%** on last **N** trades or **CAGR < treasury yield**  
- MDD exceeds risk budget or breaches **Calmar < 1.0** for 3 consecutive months  
- Material data vendor corrections or backfills

## 5) Change Log (example)
- **v1.0** — Initial MACD (12,26,9) daily strategy, t+1 open fills, rf=2%, costs set to X bps/side  
- **v1.1** — Added walk-forward; slippage doubled; added Calmar to summary; introduced roll continuity tests

