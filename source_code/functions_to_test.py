import requests
import numpy as np
from .exceptions import UnexpectedResponseError
import re
from collections.abc import Iterable


def get_accuracy_for_model(y_pred, y_true, preds_are_probs=True):
    if np.any(y_pred is None):
        return 1
    return (y_pred == y_true).sum()


def get_accuracy_for_model_new(y_pred, y_true, preds_are_probs=True):
    if np.any(y_pred is None):
        raise ValueError("NaN values in array {}".format(y_pred))
    if preds_are_probs is False and ((y_pred == 0) | (y_pred == 1)).all() is False:
        raise ValueError(
            "Expected only 0s and 1s in predictions, got {}".format(y_pred)
        )
    return np.mean(np.round(y_pred) == y_true)


def add_two_numbers_together(a: int, b: int):
    return a + b


def add_two_numbers_together_new(a: int, b: int):
    assert isinstance(a, int) or isinstance(a, float), "a is not numeric. "
    assert isinstance(b, int) or isinstance(b, float), "b is not numeric. "
    return a + b


def add_two_together(a, b, a_first=True):

    return a + b


def add_two_together_new(a, b, a_first=True):
    assert any(
        [isinstance(a, t_) for t_ in [str, int, float]]
    ), "a is neither string, int or float"
    assert any(
        [isinstance(b, t_) for t_ in [str, int, float]]
    ), "b is neither string, int or float"

    if isinstance(a, str) or isinstance(b, str):
        if re.match(r"^\d+(\.\d+)?$", str(a)) and re.match(r"^\d+(\.\d+)?$", str(b)):
            return float(a) + float(b)
        if a_first:
            return str(a) + str(b)
        else:
            return str(b) + str(a)

    return a + b


# requests.models.Response.json


def url_was_found(url="localhost:5000/health"):
    """
        Simple checking function whether an url exists or not for an API
        for which we expect


    """
    res = requests.get(url).json()

    if res["status_code"] == 200:
        return True
    elif res["status_code"] == 404:
        return False
    else:
        raise UnexpectedResponseError(
            "Expected 200 OK or 404, got {}.\nFull response : {}".format(
                res["status_code"], res
            )
        )


def url_was_found_new(url="localhost:5000/health"):
    """
        Simple checking function whether an url exists or not for an API
        for which we expect


    """
    res = requests.get(url).json()

    if res["status_code"] == 200:
        return True
    elif res["status_code"] == 404:
        return False
    else:
        raise UnexpectedResponseError(
            "Expected 200 OK or 404, got {}.\n".format(res["status"]),
            "Full response : {}".format(res),
        )


def remove_value_from_iterable(li, val):
    assert isinstance(li, Iterable), "Variable li is not an iterable. "
    return [x for x in li if x != val]
