import pygame
import numpy as np
from maze_generator import MazeGenerator
from solver import MazeSolver

# Pygame settings
CELL_SIZE = 20
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
BLUE = (0, 0, 255)
GREEN = (0, 255, 0)


def visualize_maze(maze, path=None):
    pygame.init()
    width, height = len(maze[0]) * CELL_SIZE, len(maze) * CELL_SIZE
    screen = pygame.display.set_mode((width, height))
    running = True

    while running:
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
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
    pygame.quit()