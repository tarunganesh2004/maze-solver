import pygame
import numpy as np
from maze_generator import MazeGenerator
from solver import MazeSolver
import time

# Pygame settings
CELL_SIZE = 20
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)


def draw_maze(screen, maze, path=None):
    """Draws the maze and highlights the solving path (if available)."""
    screen.fill(WHITE)
    for y in range(len(maze)):
        for x in range(len(maze[y])):
            color = BLACK if maze[y][x] == 1 else WHITE
            pygame.draw.rect(
                screen, color, (x * CELL_SIZE, y * CELL_SIZE, CELL_SIZE, CELL_SIZE)
            )

    if path:
        for x, y in path:
            pygame.draw.rect(
                screen, GREEN, (y * CELL_SIZE, x * CELL_SIZE, CELL_SIZE, CELL_SIZE)
            )
            pygame.display.update()
            pygame.time.delay(50)  # Animation effect


def main():
    """Main function to generate and solve the maze interactively."""
    pygame.init()

    # User inputs for maze size and algorithm
    width, height = 21, 21  # Must be odd numbers for proper generation
    algorithm = (
        input("Choose maze generation algorithm (backtracking/prim): ").strip().lower()
    )
    solver_method = input("Choose solver (dfs/bfs): ").strip().lower()

    # Generate the maze
    generator = MazeGenerator(width, height, algorithm)
    maze = generator.generate_maze()

    # Initialize the screen
    screen = pygame.display.set_mode((width * CELL_SIZE, height * CELL_SIZE))
    pygame.display.set_caption("Maze Generator & Solver")

    # Draw the generated maze
    draw_maze(screen, maze)
    pygame.display.update()

    # Solve the maze
    solver = MazeSolver(maze)
    path = solver.solve(solver_method)

    if path:
        print("Path found! Visualizing...")
        time.sleep(1)  # Small delay before visualization
        draw_maze(screen, maze, path)
    else:
        print("No solution found!")

    # Event loop
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

    pygame.quit()


if __name__ == "__main__":
    main()
