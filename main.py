import pygame
import numpy as np
from maze_generator import MazeGenerator
from solver import MazeSolver
from maze_utils import save_maze, load_maze
import time

# Pygame settings
CELL_SIZE = 20  # Increased cell size for better visibility
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GREEN = (0, 255, 0)


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
            pygame.time.delay(30)  # Animation effect


def main():
    """Main function to generate and solve the maze interactively."""
    pygame.init()

    # User choice to load or generate a new maze
    load_choice = input("Load saved maze? (yes/no): ").strip().lower()
    if load_choice == "yes":
        maze = load_maze()
        if maze is None:
            print("No saved maze found. Generating a new maze instead.")
    else:
        width = int(input("Enter maze width (odd number, e.g., 21): "))
        height = int(input("Enter maze height (odd number, e.g., 21): "))

        algorithm = (
            input("Choose maze generation algorithm (backtracking/prim): ")
            .strip()
            .lower()
        )
        generator = MazeGenerator(width, height, algorithm)
        maze = generator.generate_maze()

        save_choice = input("Save this maze for later? (yes/no): ").strip().lower()
        if save_choice == "yes":
            save_maze(maze)

    solver_method = input("Choose solver (dfs/bfs): ").strip().lower()

    # Initialize the screen size dynamically
    screen_width = len(maze[0]) * CELL_SIZE
    screen_height = len(maze) * CELL_SIZE
    screen = pygame.display.set_mode((screen_width, screen_height))
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