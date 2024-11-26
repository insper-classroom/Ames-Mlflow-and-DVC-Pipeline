RANDOM_SEED = 42

import pickle
import pathlib

import numpy as np
import pandas as pd

from sklearn.model_selection import train_test_split

DATA_DIR = pathlib.Path.cwd() / 'data'

clean_data_path = DATA_DIR / 'processed' / 'top_15_features.pkl'

with open(clean_data_path, 'rb') as file:
    data = pickle.load(file)

model_data = data.copy()

X = model_data.drop(columns=['SalePrice']).copy()
y = model_data['SalePrice'].copy()

# Separando os dados em treino e teste
Xtrain, Xtest, ytrain, ytest = train_test_split(
    X,
    y,
    test_size=0.25,
    random_state=RANDOM_SEED,
)

# save train and test data
train_data_path = DATA_DIR / 'processed' / 'train.pkl'
test_data_path = DATA_DIR / 'processed' / 'test.pkl'

with open(train_data_path, 'wb') as file:
    pickle.dump((Xtrain, ytrain), file)

with open(test_data_path, 'wb') as file:
    pickle.dump((Xtest, ytest), file)
