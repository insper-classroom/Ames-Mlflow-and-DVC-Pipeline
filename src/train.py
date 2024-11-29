RANDOM_SEED = 42

import pickle
import pathlib

import numpy as np
import pandas as pd

from sklearn.linear_model import Lasso, Ridge
from sklearn.ensemble import StackingRegressor, GradientBoostingRegressor
from sklearn.ensemble import RandomForestRegressor
from sklearn.model_selection import GridSearchCV

import mlflow
#t
def train_model():
    
    DATA_DIR = pathlib.Path.cwd() / 'data'
    MODEL_DIR = pathlib.Path.cwd() / 'models'

    train_data_path = DATA_DIR / 'processed' / 'train.pkl'
    test_data_path = DATA_DIR / 'processed' / 'test.pkl'

    with open(train_data_path, 'rb') as file:
        Xtrain, ytrain = pickle.load(file)

    # log train data
    mlflow.log_artifact(train_data_path)

    # log train data shapes
    mlflow.log_param('Xtrain_shape', Xtrain.shape)
    mlflow.log_param('ytrain_shape', ytrain.shape)

    # log train data types
    mlflow.log_param('Xtrain_dtype', Xtrain.dtypes.to_dict())
    mlflow.log_param('ytrain_dtype', ytrain.dtype)

    grid_search_forest = GridSearchCV(
        RandomForestRegressor(n_estimators=100, random_state=RANDOM_SEED, n_jobs=-1),
        {'n_estimators': [300, 675, 900]},
        cv=4, 
        n_jobs=-1, 
        scoring='neg_mean_squared_error', 
        return_train_score=True
    )

    grid_search_forest.fit(Xtrain, ytrain)
    forest_reg = grid_search_forest.best_estimator_

    # Grid search for Gradient Boosting Regressor
    grid_search_gbr = GridSearchCV(
        GradientBoostingRegressor(random_state=RANDOM_SEED),
        {'n_estimators': [100, 600, 900], 'max_depth': [3, 5, 7]},
        cv=4,
        n_jobs=-1,
        scoring='neg_mean_squared_error',
        return_train_score=True
    )

    grid_search_gbr.fit(Xtrain, ytrain)
    gbr_reg = grid_search_gbr.best_estimator_

    # Lasso GridSearch
    grid_search_lasso = GridSearchCV(
        Lasso(random_state=RANDOM_SEED),
        {'alpha': [0.1,0.5,1]},
        cv=4,
        n_jobs=-1,
        scoring='neg_mean_squared_error',
        return_train_score=True
    )

    grid_search_lasso.fit(Xtrain, ytrain)
    lasso_reg = grid_search_lasso.best_estimator_


    estimators = [
        ('rf', forest_reg),
        ('ls', lasso_reg),
        ('gb', gbr_reg)
        
    ]

    stack_reg = StackingRegressor(
        estimators=estimators,
        final_estimator=Ridge()
    )

    stack_reg.fit(Xtrain, ytrain)

    # save model
    model_path = MODEL_DIR / 'stack_reg.pkl'
    # create models directory
    MODEL_DIR.mkdir(exist_ok=True)
    with open(model_path, 'wb') as file:
        pickle.dump(stack_reg, file)
    mlflow.log_artifact(model_path)

    # model signature
    input_schema = mlflow.models.infer_signature(Xtrain, stack_reg.predict(Xtrain))

    # log model
    mlflow.sklearn.log_model(stack_reg, 
                            'stack_reg',
                            registered_model_name='house-prices', 
                            signature=input_schema,
                            input_example=Xtrain.iloc[:3])


if __name__ == '__main__':
    mlflow.set_tracking_uri("http://localhost:5000")
    mlflow.set_experiment('house-prices')
    with mlflow.start_run():
        train_model()