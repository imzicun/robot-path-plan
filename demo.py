from path_planning.grid import make_grid, plot_grid
from path_planning.astar import astar

def main():
    grid = make_grid(n=50, obstacle_prob=0.25, seed=1)
    start = (0, 0)
    goal = (49, 49)

    path = astar(grid, start, goal)
    plot_grid(grid, path, start, goal)

if __name__ == "__main__":
    main()
