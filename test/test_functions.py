from source_code.functions_to_test import get_accuracy_for_model, add_two_together, add_two_numbers_together
import pandas as pd

def test_get_accuracy_for_model():
    assert True

def test_add_two_together():
    assert True

def test_add_two_numbers_together():
    assert True



def readcsvpandas():
    # Mock value for reading a csv file.
    return pd.DataFrame({"a" : [1,2,3], "b" : [4,5,6]})


def test_get_function(mocker):
    mocker.patch("pandas.read_csv", return_value= readcsvpandas())
    data = pd.read_csv("hello")
    assert data.equals(pd.DataFrame({"a" : [1,2,3], "b" : [4,5,6]}))
