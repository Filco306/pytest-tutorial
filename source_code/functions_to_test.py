import requests
from .exceptions import UnexpectedResponseError


def get_accuracy_for_model(y_pred, y_true, preds_are_probs=True):
    if y_pred == None:
        return 1
    return (y_pred == y_true).sum()

def get_accuracy_for_model_new(y_pred, y_true, preds_are_probs=True):
    pass

def add_two_numbers_together(a : int, b : int):
    return a + b


def add_two_numbers_together_new(a : int, b : int):
    pass

def add_two_together(a, b, a_first = True):
    if isinstance(a, str) is True:
        return int(a) + int(b)
    return a + b

def add_two_together_new(a, b, a_first = True):
    pass

# requests.models.Response.json

def url_was_found(url="localhost:5000/health"):
    """
        Simple checking function whether an url exists or not for an API
        for which we expect


    """
    res = requests.get(url).json()

    if res['status_code'] == 200:
        return True
    elif res['status_code'] == 404:
        return False
    else:
        raise UnexpectedResponseError("Expected 200 OK or 404, got {}.\n".format(res['status']), "Full response : {}".format(res))

def url_was_found(url="localhost:5000/health"):
    pass



from collections.abc import Iterable

def remove_value_from_iterable(li, val):
    assert isinstance(li, Iterable), "Variable li is not an iterable. "
    return [x for x in li if x != val]
