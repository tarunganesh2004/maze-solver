from collections import deque
import numpy as np


class MazeSolver:
    def __init__(self, maze):
        self.maze = maze
        self.start = (1, 1)
        self.end = (len(maze) - 2, len(maze[0]) - 2)

    def solve(self, method="bfs"):
        if method == "dfs":
            return self._dfs()
        return self._bfs()

    def _dfs(self):
        """Depth-First Search for maze solving"""
        stack = [(self.start, [self.start])]
        visited = set()

        while stack:
            (x, y), path = stack.pop()
            if (x, y) == self.end:
                return path

            if (x, y) in visited:
                continue
            visited.add((x, y))

            for nx, ny in self._get_neighbors(x, y):
                stack.append(((nx, ny), path + [(nx, ny)]))
        return None

    def _bfs(self):
        """Breadth-First Search for shortest path"""
        queue = deque([(self.start, [self.start])])
        visited = set()

        while queue:
            (x, y), path = queue.popleft()
            if (x, y) == self.end:
                return path

            if (x, y) in visited:
                continue
            visited.add((x, y))

            for nx, ny in self._get_neighbors(x, y):
                queue.append(((nx, ny), path + [(nx, ny)]))
        return None

    def _get_neighbors(self, x, y):
        """Get valid neighbors for pathfinding"""
        neighbors = []
        for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            nx, ny = x + dx, y + dy
            if (
                0 <= nx < len(self.maze)
                and 0 <= ny < len(self.maze[0])
                and self.maze[nx][ny] == 0
            ):
                neighbors.append((nx, ny))
        return neighbors


if __name__ == "__main__":
    test_maze = np.array(
        [
            [1, 1, 1, 1, 1],
            [1, 0, 0, 0, 1],
            [1, 1, 1, 0, 1],
            [1, 0, 0, 0, 1],
            [1, 1, 1, 1, 1],
        ]
    )
    solver = MazeSolver(test_maze)
    print("DFS Path:", solver.solve("dfs"))
    print("BFS Path:", solver.solve("bfs"))