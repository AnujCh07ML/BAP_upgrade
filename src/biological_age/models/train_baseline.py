DEBUG = False


def train_model(
    estimator,
    preprocessor,
    X_train,
    X_test,
    y_train,
):
    """
    Train a machine learning model using the provided estimator.

    Parameters
    ----------
    estimator : sklearn estimator
        Machine learning model to train.

    preprocessor : ColumnTransformer
        Preprocessing pipeline.

    X_train : pd.DataFrame
        Training features.

    X_test : pd.DataFrame
        Test features.

    y_train : pd.Series
        Training target.

    Returns
    -------
    tuple
        (
            trained_model,
            fitted_preprocessor,
            y_pred,
        )
    """

    # -----------------------------------
    # Fit preprocessor on training data
    # -----------------------------------

    X_train_processed = (
        preprocessor.fit_transform(X_train)
    )

    X_test_processed = (
        preprocessor.transform(X_test)
    )

    feature_names = (
        preprocessor.get_feature_names_out()
    )

    # -----------------------------------
    # Debug Information
    # -----------------------------------

    if DEBUG:

        print("\n=== RAW FEATURES ===")
        print(
            f"Number of raw features: "
            f"{len(X_train.columns)}"
        )

        for col in X_train.columns:
            print(col)

        print("\n=== PROCESSED SHAPE ===")
        print(X_train_processed.shape)

        print("\n=== FIRST 20 FEATURES ===")

        for name in feature_names[:20]:
            print(name)

        print(
            f"\nTotal processed features: "
            f"{len(feature_names)}"
        )

    # -----------------------------------
    # Train model
    # -----------------------------------

    estimator.fit(
        X_train_processed,
        y_train,
    )

    # -----------------------------------
    # Predict
    # -----------------------------------

    y_pred = estimator.predict(
        X_test_processed,
    )

    return (
        estimator,
        preprocessor,
        y_pred,
    )
