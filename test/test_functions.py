from source_code.functions_to_test import (
    get_accuracy_for_model,
    get_accuracy_for_model_new,
    add_two_together,
    add_two_numbers_together,
    add_two_numbers_together_new,
    url_was_found,
    add_two_together_new,
)
from source_code.exceptions import UnexpectedResponseError
import pandas as pd
import pytest
import numpy as np


def test_get_accuracy_for_model():
    with pytest.raises(ValueError):
        _ = get_accuracy_for_model(None, None)

    assert (
        get_accuracy_for_model(np.array([0.1, 0.2, 0.7, 0.4]), np.array([1, 0, 1, 0]))
        == 0.75
    )
    with pytest.raises(ValueError):  # noqa : F841
        _ = get_accuracy_for_model(
            np.array([0.1, 0.2, 0.7, 0.5]),
            np.array([1, 0, 1, 0]),
            preds_are_probs=False,
        )
    assert (
        get_accuracy_for_model(np.array([1, 1, 1, 0]), np.array([1, 0, 1, 0])) == 0.75
    )
    # assert get_accuracy_for_model()


def test_get_accuracy_for_model_new():
    with pytest.raises(ValueError):  # noqa : F841
        _ = get_accuracy_for_model_new(None, None)

    assert (
        get_accuracy_for_model_new(
            np.array([0.1, 0.2, 0.7, 0.4]), np.array([1, 0, 1, 0])
        )
        == 0.75
    )
    with pytest.raises(ValueError):  # noqa : F841
        _ = get_accuracy_for_model_new(
            np.array([0.1, 0.2, 0.7, 0.5]),
            np.array([1, 0, 1, 0]),
            preds_are_probs=False,
        )
    assert (
        get_accuracy_for_model_new(np.array([1, 1, 1, 0]), np.array([1, 0, 1, 0]))
        == 0.75
    )


def test_add_two_together():
    assert add_two_together("a", "b") == "ab"
    assert add_two_together("a", "b", False) == "ba"
    assert add_two_together(1, "2", False) == 3
    assert add_two_together(1, "2") == 3
    assert add_two_together(3, 4) == 7
    assert add_two_together("3_", "4") == "3_4"
    assert add_two_together("3", "4", False) == 34
    with pytest.raises(AssertionError):
        _ = add_two_together(None, "4")
    with pytest.raises(AssertionError):
        _ = add_two_together("4", None)


def test_add_two_together_new():
    assert add_two_together_new("a", "b") == "ab"
    assert add_two_together_new("a", "b", False) == "ba"
    assert add_two_together_new(1, "2", False) == 3
    assert add_two_together_new(1, "2") == 3
    assert add_two_together_new(3, 4) == 7
    assert add_two_together_new("3_", "4") == "3_4"
    assert add_two_together_new("3", "4", False) == 7
    with pytest.raises(AssertionError):
        _ = add_two_together_new(None, "4")
    with pytest.raises(AssertionError):
        _ = add_two_together_new("4", None)


def test_add_two_numbers_together():
    with pytest.raises(AssertionError):  # noqa : F841
        _ = add_two_numbers_together("a", "b")
    with pytest.raises(AssertionError):  # noqa : F841
        _ = add_two_numbers_together("1", "2")
    with pytest.raises(AssertionError):  # noqa : F841
        _ = add_two_numbers_together(0, "-2")
    with pytest.raises(AssertionError):  # noqa : F841
        _ = add_two_numbers_together("-2", 0)
    with pytest.raises(AssertionError):  # noqa : F841
        _ = add_two_numbers_together(None, 0)
    with pytest.raises(AssertionError):
        _ = add_two_numbers_together(0, None)
    assert add_two_numbers_together(1, 2) == 3
    assert add_two_numbers_together(-1.0, 2) == 1
    assert add_two_numbers_together(-1.0, -2) == -3

    assert True


def test_add_two_numbers_together_new():
    with pytest.raises(AssertionError):
        _ = add_two_numbers_together_new("a", "b")
    with pytest.raises(AssertionError):
        _ = add_two_numbers_together_new("1", "2")
    with pytest.raises(AssertionError):
        _ = add_two_numbers_together_new(0, "-2")
    with pytest.raises(AssertionError):
        _ = add_two_numbers_together_new("-2", 0)
    with pytest.raises(AssertionError):
        _ = add_two_numbers_together_new(None, 0)
    with pytest.raises(AssertionError):
        _ = add_two_numbers_together_new(0, None)
    assert add_two_numbers_together_new(1, 2) == 3
    assert add_two_numbers_together_new(-1.0, 2) == 1
    assert add_two_numbers_together_new(-1.0, -2) == -3


class RequestsMocker:
    def __init__(self, return_value):
        self.return_value = return_value

    def json(self):
        return self.return_value


def test_url_was_found_unexpected_response(mocker):
    mocker.patch("requests.get", return_value=RequestsMocker({"status_code": 123234}))
    with pytest.raises(UnexpectedResponseError):
        _ = url_was_found(url="test_url")


def test_url_was_found_correct_response(mocker):
    mocker.patch("requests.get", return_value=RequestsMocker({"status_code": 200}))
    assert url_was_found(url="test_url")


def test_url_was_found_not_found(mocker):
    mocker.patch("requests.get", return_value=RequestsMocker({"status_code": 404}))
    assert url_was_found(url="test_url") is False


def readcsvpandas():
    # Mock value for reading a csv file.
    return pd.DataFrame({"a": [1, 2, 3], "b": [4, 5, 6]})


def test_get_function(mocker):
    mocker.patch("pandas.read_csv", return_value=readcsvpandas())
    data = pd.read_csv("hello")
    assert data.equals(pd.DataFrame({"a": [1, 2, 3], "b": [4, 5, 6]}))
