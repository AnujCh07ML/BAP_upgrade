from sklearn.model_selection import RandomizedSearchCV


def tune_model(
    estimator,
    param_grid,
    X_train,
    y_train,
    n_iter: int = 25,
    cv: int = 3,
    scoring: str = "neg_mean_absolute_error",
    random_state: int = 42,
    n_jobs: int = -1,
    verbose: int = 2,
):
    """
    Tune a machine learning model using RandomizedSearchCV.

    Parameters
    ----------
    estimator : sklearn estimator
        Estimator or pipeline to tune.

    param_grid : dict
        Hyperparameter search space.

    X_train : pd.DataFrame
        Training features.

    y_train : pd.Series
        Training target.

    n_iter : int, default=25
        Number of parameter settings sampled.

    cv : int, default=3
        Number of cross-validation folds.

    scoring : str, default="neg_mean_absolute_error"
        Evaluation metric.

    random_state : int, default=42
        Random seed for reproducibility.

    n_jobs : int, default=-1
        Number of parallel jobs.

    verbose : int, default=2
        Verbosity level.

    Returns
    -------
    RandomizedSearchCV
        Fitted RandomizedSearchCV object.
    """

    search = RandomizedSearchCV(
        estimator=estimator,
        param_distributions=param_grid,
        n_iter=n_iter,
        cv=cv,
        scoring=scoring,
        n_jobs=n_jobs,
        random_state=random_state,
        verbose=verbose,
    )

    search.fit(
        X_train,
        y_train,
    )

    return search
