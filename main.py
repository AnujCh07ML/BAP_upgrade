from data.make_interim import run_make_interim


def load_config():
    return {
        "paths": {
            "raw": "data/raw",
            "interim": "data/interim/nhanes_merged.parquet"
        }
    }


if __name__ == "__main__":
    config = load_config()
    run_make_interim(config)
