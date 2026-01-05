import numpy as np
import matplotlib.pyplot as plt

def make_grid(n=50, obstacle_prob=0.25, seed=None):
    if seed is not None:
        np.random.seed(seed)
    return np.random.rand(n, n) > obstacle_prob

def plot_grid(grid, path=None, start=None, goal=None):
    plt.imshow(grid, cmap="gray_r")

    if path:
        y, x = zip(*path)
        plt.plot(x, y, color="red", linewidth=2)

    if start:
        plt.scatter(start[1], start[0], c="green", s=100)

    if goal:
        plt.scatter(goal[1], goal[0], c="blue", s=100)

    plt.title("Robot Path Planning")
    plt.show()
