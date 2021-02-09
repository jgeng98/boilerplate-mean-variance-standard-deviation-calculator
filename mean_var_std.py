import numpy as np

# applies a function to the rows, columns, and the entire matrix and returns the results as a list
def compute(fn, arr):
    return [fn(arr, axis=0).tolist(), fn(arr, axis=1).tolist(), fn(arr)]


def calculate(list):
    # raise exception if the passed list doesn't contain 9 arguments
    if len(list) != 9:
        raise ValueError("List must contain nine numbers.")

    # convert the passed list into a 3x3 numpy array
    arr = np.array(list).reshape((3, 3))

    # create a dictionary with empty lists as values
    calculations = dict.fromkeys(
        ["mean", "variance", "standard deviation", "max", "min", "sum"], []
    )

    # create a dictionary with the corresponding numpy functions as values
    funcs = {
        "mean": np.mean,
        "variance": np.var,
        "standard deviation": np.std,
        "max": np.max,
        "min": np.min,
        "sum": np.sum,
    }

    # applies each of the numpy functions to the numpy array, populating the dictionary
    for key in calculations.keys():
        calculations[key] = compute(funcs[key], arr)

    return calculations
