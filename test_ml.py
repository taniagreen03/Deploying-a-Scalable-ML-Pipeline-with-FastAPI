import pytest
# TODO: add necessary import
import os
import pandas as pd
import numpy as np
from ml.data import process_data
from ml.model import train_model
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split

# loading dataset in the test file
project_path = os.getcwd()
data_path = os.path.join(project_path, "data", "census.csv")
data = pd.read_csv(data_path)

# Define categorical features (same as in train_model.py)
cat_features = [
    "workclass",
    "education",
    "marital-status",
    "occupation",
    "relationship",
    "race",
    "sex",
    "native-country",
]

# TODO: implement the first test. Change the function name and input as needed
def test_train_model_type():
    """
    Test if train_model returns a RandomForestClassifier
    """
    # Your code here
    X, y, encoder, lb = process_data(data, categorical_features=cat_features, label="salary", training=True)
    model = train_model(X, y)

    assert isinstance(model, RandomForestClassifier), "Model should be a RandomForestClassifier"

# TODO: implement the second test. Change the function name and input as needed
def test_process_data_output():
    """
    # Test if process_data returns correct types (NumPy arrays).
    """
    # Your code here
    X, y, encoder, lb = process_data(data, categorical_features=cat_features, label="salary", training=True)

    assert isinstance(X, np.ndarray), "X should be a NumPy array"

# TODO: implement the third test. Change the function name and input as needed
def test_train_test_split_size():
    """
    Test if train dataset and test dataset are the correct size.
    """
    # Your code here
    train, test = train_test_split(data, test_size=0.2, random_state=42, stratify=data["salary"])

    expected_train_size = round(len(data) * 0.8)
    expected_test_size = round(len(data) * 0.2)

    assert abs(len(train) - expected_train_size) <= 1, f"Train set should have ~{expected_train_size} rows, but got {len(train)}"
    assert abs(len(test) - expected_test_size) <= 1, f"Test set should have ~{expected_test_size} rows, but got {len(test)}"




