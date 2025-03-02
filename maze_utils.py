import numpy as np


def save_maze(maze, filename="saved_maze.txt"):
    """Saves the maze to a text file."""
    np.savetxt(filename, maze, fmt="%d")
    print(f"Maze saved to {filename}")


def load_maze(filename="saved_maze.txt"):
    """Loads a maze from a text file."""
    try:
        maze = np.loadtxt(filename, dtype=int)
        print(f"Maze loaded from {filename}")
        return maze
    except FileNotFoundError:
        print("Error: No saved maze found!")
        return None


if __name__ == "__main__":
    # Example usage
    test_maze = np.array(
        [
            [1, 1, 1, 1, 1],
            [1, 0, 0, 0, 1],
            [1, 1, 1, 0, 1],
            [1, 0, 0, 0, 1],
            [1, 1, 1, 1, 1],
        ]
    )
    save_maze(test_maze)
    loaded_maze = load_maze()
    print(loaded_maze)