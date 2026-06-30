from pathlib import Path
import joblib


def save_model(model, model_path: str | Path) -> None:
    """
    Save a fitted sklearn pipeline/model.

    Parameters
    ----------
    model : object
        Fitted sklearn Pipeline or estimator.
    model_path : str | Path
        Destination path.
    """
    model_path = Path(model_path)
    model_path.parent.mkdir(parents=True, exist_ok=True)

    joblib.dump(model, model_path)

    print(f"Model saved to: {model_path}")


def load_model(model_path: str | Path):
    """
    Load a saved sklearn pipeline/model.

    Parameters
    ----------
    model_path : str | Path
        Path to saved model.

    Returns
    -------
    object
        Loaded sklearn Pipeline or estimator.
    """
    model_path = Path(model_path)

    model = joblib.load(model_path)

    print(f"Model loaded from: {model_path}")

    return model
