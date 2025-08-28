from pathlib import Path

import io, base64, json
from dataclasses import dataclass
from typing import Tuple, List, Dict, Any
import numpy as np
import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score
import joblib
import matplotlib.pyplot as plt

@dataclass
class TrainResult:
    model: Any
    X: np.ndarray
    y: np.ndarray
    y_pred: np.ndarray
    metrics: Dict[str, float]

def generate_mock_data(n_samples: int = 200, n_features: int = 3, noise: float = 5.0, random_state: int = 42) -> pd.DataFrame:
    rng = np.random.default_rng(random_state)
    X = rng.normal(size=(n_samples, n_features))
    coef = rng.uniform(-5, 5, size=n_features)
    y = X @ coef + rng.normal(0, noise, size=n_samples)
    cols = [f"f{i+1}" for i in range(n_features)]
    df = pd.DataFrame(X, columns=cols)
    df["target"] = y
    return df

def train_linear_regression(df: pd.DataFrame) -> TrainResult:
    X = df[[c for c in df.columns if c != "target"]].values
    y = df["target"].values
    model = LinearRegression()
    model.fit(X, y)
    y_pred = model.predict(X)
    metrics = {
        "rmse": float(mean_squared_error(y, y_pred, squared=False)),
        "r2": float(r2_score(y, y_pred))
    }
    return TrainResult(model, X, y, y_pred, metrics)

def save_model(model, path: str) -> str:
    Path(path).parent.mkdir(parents=True, exist_ok=True)
    joblib.dump(model, path)
    return path

def load_model(path: str):
    return joblib.load(path)

def basic_plot(y_true: np.ndarray, y_pred: np.ndarray) -> str:
    fig, ax = plt.subplots(figsize=(5,4), dpi=120)
    ax.scatter(y_true, y_pred, alpha=0.6)
    ax.plot([y_true.min(), y_true.max()], [y_true.min(), y_true.max()], ls="--")
    ax.set_xlabel("Actual")
    ax.set_ylabel("Predicted")
    ax.set_title("Actual vs Predicted")
    buf = io.BytesIO()
    fig.tight_layout()
    fig.savefig(buf, format="png")
    plt.close(fig)
    b64 = base64.b64encode(buf.getvalue()).decode("utf-8")
    return b64

def _rmse(y_true, y_pred):
    try:
        return float(mean_squared_error(y_true, y_pred, squared=False))
    except TypeError:
        return float(np.sqrt(mean_squared_error(y_true, y_pred)))

def train_linear_regression(df: pd.DataFrame) -> TrainResult:
    X = df[[c for c in df.columns if c != "target"]].values
    y = df["target"].values
    model = LinearRegression().fit(X, y)
    y_pred = model.predict(X)
    metrics = {
        "rmse": _rmse(y, y_pred),
        "r2": float(r2_score(y, y_pred))
    }
    return TrainResult(model, X, y, y_pred, metrics)