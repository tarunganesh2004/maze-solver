import numpy as np
import random


class MazeGenerator:
    def __init__(self, width, height, algorithm="backtracking"):
        self.width = width
        self.height = height
        self.algorithm = algorithm
        self.grid = np.ones((height, width), dtype=int)  # 1 = Wall, 0 = Path

    def generate_maze(self):
        if self.algorithm == "backtracking":
            self._recursive_backtracking(1, 1)
        elif self.algorithm == "prim":
            self._prims_algorithm()
        return self.grid

    def _recursive_backtracking(self, x, y):
        """Recursive Backtracking Algorithm"""
        directions = [(0, 2), (2, 0), (0, -2), (-2, 0)]
        random.shuffle(directions)

        for dx, dy in directions:
            nx, ny = x + dx, y + dy
            if (
                1 <= nx < self.height - 1
                and 1 <= ny < self.width - 1
                and self.grid[nx][ny] == 1
            ):
                self.grid[nx][ny] = 0
                self.grid[x + dx // 2][y + dy // 2] = 0  # Remove wall between
                self._recursive_backtracking(nx, ny)

    def _prims_algorithm(self):
        """Prim’s Algorithm for Maze Generation"""
        walls = [(1, 1)]
        self.grid[1][1] = 0

        while walls:
            x, y = random.choice(walls)
            walls.remove((x, y))

            directions = [(0, 2), (2, 0), (0, -2), (-2, 0)]
            random.shuffle(directions)

            for dx, dy in directions:
                nx, ny = x + dx, y + dy
                if (
                    1 <= nx < self.height - 1
                    and 1 <= ny < self.width - 1
                    and self.grid[nx][ny] == 1
                ):
                    self.grid[nx][ny] = 0
                    self.grid[x + dx // 2][y + dy // 2] = 0  # Remove wall between
                    walls.append((nx, ny))


if __name__ == "__main__":
    mg = MazeGenerator(21, 21, algorithm="backtracking")
    maze = mg.generate_maze()
    print(maze)