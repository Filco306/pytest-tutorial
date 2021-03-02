# pytest tutorial
This is a repository containing a tutorial for learning pytest. 

## Oh no! 

The code inside the `source_code` folder is meant for production, but the code is really dirty, unifinished and not tested! In order to feel comfortable moving this code to a production environment, your team has advised you to create tests to ensure that things work properly. The requirements for the different functions are given in the steps below. 

## Steps

1. Create a virtual environment, either through conda or virtualenv.
2. In your virtual environment, install pytest (e.g., using `pip install pytest`)
3. For the (broken) functions in `source_code/functions_to_test.py`, create tests with the following requirements.

- `get_accuracy_for_model` is a method that takes two numpy arrays and returns the accuracy. It should be able to take the predictions in the form of both probabilities (valued between 0 and 1) and hard number (0 or 1) and output a scalar value between 0 and 1
- `add_two_numbers_together` takes two numbers (can be both floats and/or ints) and outputs the sum of these. If `a` or `b` is not a number, an error should be raised.
- `add_two_together` takes two strings or numerics and outputs the addition of the two. There are a few cases here.
  - If both are strings, a string should be returned. As an example, for `a = "5"`, `b = "6", a_first = True`, then `ans = "56"`
  - If one is a numeric string and the other a numeric, a number should be returned; e.g., `a = 5.0`, `b = "6.0", a_first = False` should return `ans = 11.0`
  - If any of `a` and `b` is a non-numeric string, the summed up string should be returned, e.g., `a = 5.0`, `b = ":::::", a_first = False` should return `ans = ":::::5.0"`
  - If any of `a` and `b` is `None`, a `ValueError` should be raised.
  - If both `a` and `b` are numeric, the sum of them should be returned.
- `url_was_found` is a function checking for pages in an API.
  - If a page exists, it will automatically and expectedly return a json response with `status_code = 200`.
  - If the page does not exist, it should return a json response with `status_code = 404`.
  - If any other `status_code` is returned, an `UnexpectedResponseError` should be thrown.
  - Some things are worth thinking about here.
    - How do you handle in a test that an error is thrown?
    - How do you handle the fact that you contact an external system? Hint: mocking.


4. Have you created the tests? Great! Do they pass your tests?
5. How sad that some of the functions do not pass all the tests! For those functions that do not pass the tests, create a replacing function called `<FAILINGFUNCTIONNAME>_new` and make sure that this new function will pass your tests instead.
