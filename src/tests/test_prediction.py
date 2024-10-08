import pytest 
import numpy as np
from employee_attrition.config import config
from employee_attrition.preprocessing.data_handling import load_dataset
from employee_attrition.predict import generate_predictions


@pytest.fixture
def single_prediction():
    test_dataset = load_dataset(config.TEST_FILE)
    single_row = test_dataset[:1]
    print(single_row)
    result = generate_predictions(single_row)
    return result['prediction']

def test_single_pred_not_none(single_prediction):
    assert single_prediction is not None

def test_single_pred_int_type(single_prediction): 
    assert isinstance(single_prediction[0], (np.integer,int))

def test_single_pred_validate(single_prediction):
    assert single_prediction[0] == 1