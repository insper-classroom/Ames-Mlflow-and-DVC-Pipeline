RANDOM_SEED = 42

import pickle
import pathlib
import mlflow
from sklearn.metrics import mean_squared_error

def test_model():

    DATA_DIR = pathlib.Path.cwd() / 'data'
    MODEL_DIR = pathlib.Path.cwd() / 'models'


    test_data_path = DATA_DIR / 'processed' / 'test.pkl'
    model_path = MODEL_DIR / 'stack_reg.pkl'

    with open(test_data_path, 'rb') as file:
        Xtest, ytest = pickle.load(file)

    # log test data
    mlflow.log_artifact(test_data_path)

    # log test data shapes
    mlflow.log_param('Xtest_shape', Xtest.shape)
    mlflow.log_param('ytest_shape', ytest.shape)

    # log test data types
    mlflow.log_param('Xtest_dtype', Xtest.dtypes.to_dict())
    mlflow.log_param('ytest_dtype', ytest.dtype)

    # load model
    with open(model_path, 'rb') as file:
        stack_reg = pickle.load(file)

    # predict
    ytest_pred = stack_reg.predict(Xtest)

    # log metrics
    mse = mean_squared_error(ytest, ytest_pred)

    mlflow.log_metric('mse', mse)
    mlflow.sklearn.log_model(stack_reg, 'stack_reg')

    # log model
    model_path = MODEL_DIR / 'stack_reg.pkl'
    with open(model_path, 'wb') as file:
        pickle.dump(stack_reg, file)
    mlflow.log_artifact(model_path)

    # log model params
    mlflow.log_param('model', 'stack_reg')
    mlflow.log_param('model_params', stack_reg.get_params())

    # log model metrics
    mlflow.log_param('mse', mse)

if __name__ == '__main__':
    mlflow.set_tracking_uri("http://localhost:5000")
    mlflow.set_experiment('house-prices')
    with mlflow.start_run():
        test_model()