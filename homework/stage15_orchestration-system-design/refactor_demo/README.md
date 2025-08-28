# Refactor Demo (Optional Stretch)

This is a minimal **reusable function + CLI wrapper** with logging.
It reads a text/JSON file, normalizes it to JSON, and writes an output with metadata.

## How to Run
```bash
python refactor_demo/my_task_cli.py --input data/sample.txt --output reports/out.json --logfile logs/demo.log
# or
./refactor_demo/my_task_cli.py --input data/sample.txt --output reports/out.json
```
Outputs a JSON file with `payload` and `meta` and logs to console/file.