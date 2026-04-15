from src.data.load_data import load_all_data
from src.data.merge_data import merge_all_years
from src.data.create_datasets import create_datasets

from src.preprocessing.cleaning import clean_data
from src.split.split_data import split_data

from src.models.trainers import train_models
from src.models.stacked import train_stacking

from src.evaluation.evaluate import evaluate_model
from src.interpret.shap_analysis import run_shap

from src.utils.io import save_model, save_metrics


def main():

    print("Loading data...")
    raw_data = load_all_data("data/raw")

    print("Merging yearly data...")
    merged_data = merge_all_years(raw_data)

    print("Creating datasets (with / without inflammation)...")
    df_no_crp, df_with_crp = create_datasets(merged_data)

    datasets = {
        "no_crp": df_no_crp,
        "with_crp": df_with_crp
    }

    for name, df in datasets.items():

        print(f"\nProcessing dataset: {name}")

        df = clean_data(df)

        X_train, X_test, y_train, y_test = split_data(df)

        model = train_models(X_train, y_train)

        metrics = evaluate_model(model, X_test, y_test)

        run_shap(model, X_test)

        save_model(model, f"models/{name}_model.pkl")
        save_metrics(metrics, f"outputs/{name}_metrics.json")

    print("Pipeline finished.")


if __name__ == "__main__":
    main()
