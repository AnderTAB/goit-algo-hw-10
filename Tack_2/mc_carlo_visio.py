import numpy as np
import scipy.integrate as integrate
import matplotlib.pyplot as plt

from view import func, a, b, y_min, y_max

def monte_carlo_integrate(func, a, b, y_min, y_max, num_points, view_=False):
    x = np.random.uniform(a, b, num_points)
    y = np.random.uniform(y_min, y_max, num_points)
    under_curve = y < func(x)
    print(under_curve)
    area = (b - a) * (y_max - y_min) * (under_curve / num_points)
    if view_:
        plt.figure(figsize=(8, 8))
        plt.scatter(x[under_curve], y[under_curve], color="blue", s=1)
        plt.scatter(x[~under_curve], y[~under_curve], color="red", s=1)
        plt.axis("equal")
        plt.show()
    return area


if __name__ == "__main__":
    result, err = integrate.quad(func, a, b)  # noqa
    mc_result = monte_carlo_integrate(func, a, b, y_min, y_max, 10000, view_=True)
    print(mc_result)
    # print(result, mc_result)