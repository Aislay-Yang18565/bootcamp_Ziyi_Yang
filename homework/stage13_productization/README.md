# Stage 13 Productization Demo

This repo demonstrates productization: clean structure, pickled model, Flask API, and simple testing.

## How to run
1. Create venv and install requirements: `pip install -r requirements.txt`
2. Run the notebook in `notebooks/` to train and pickle the model.
3. Start the API: `python app.py`
4. Test: use curl or scripts in the notebook cells.

## Structure
- data/ — (optional raw/processed data)
- notebooks/ — main notebook
- src/ — reusable utilities
- model/ — saved model (`model.pkl`)
- reports/ — artifacts (plots/metrics)
- app.py — Flask API

## API
- `POST /predict` JSON: `{"features":[f1,f2,f3]}`
- `GET /predict/<x1>` (pads missing features with 0)
- `GET /predict/<x1>/<x2>`
- `GET /plot` — returns an HTML page with an embedded PNG.

