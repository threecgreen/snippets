""" Calculate the coefficient of determination for a given x, y and linear
regression function."""
import numpy as np


def r_squared(x, y, func):
    y_mean = np.mean(y)
    ss_tot = np.sum(np.square(y - y_mean))
    ss_res = np.sum(np.square(func(x) - y))
    return 1 - (ss_res / ss_tot)


if __name__ == "__main__":
    # Test
    test_x = np.arange(1, 10)
    test_y = np.arange(2, 20, 2)
    test_func = lambda x: 2 * x

    assert r_squared(test_x, test_y, test_func) == 1
    print("Test passed.")
