import matplotlib.pyplot as plt
import numpy as np

a = 0
b = 2

y_min = 0
y_max = 1

def func(x):
    return np.cos(x)**2


if __name__ == "__main__":
    x = np.linspace(0, 2, 100)
    y = func(x)

    fig, ax = plt.subplots()
    ax.plot(x, y,'r', linewidth=1)

    ax.axhline(y=y_min, color='k', linestyle="--")
    ax.axhline(y=y_max, color='k', linestyle="--")
    ax.axvline(x=a, color='k', linestyle="--")
    ax.axvline(x=b, color='k', linestyle="--")

    fill_x = np.linspace(a, b, 100)
    fill_y = func(fill_x)
    ax.fill_between(fill_x, fill_y, color='grey', alpha=0.3)

    plt.grid(True)
    plt.show()