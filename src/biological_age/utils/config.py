from functools import lru_cache
from pathlib import Path

import yaml


PROJECT_ROOT = Path(__file__).resolve().parents[3]


@lru_cache(maxsize=1)
def load_config() -> dict:
    """
    Load project configuration from config.yaml.

    Returns
    -------
    dict
        Parsed configuration dictionary.
    """
    config_path = PROJECT_ROOT / "config.yaml"

    with open(config_path, "r") as file:
        return yaml.safe_load(file)
