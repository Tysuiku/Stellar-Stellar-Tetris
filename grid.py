import pygame
from colors import Colors

class Grid:
    def __init__(self):
        self.num_rows = 20
        self.num_cols = 10
        self.cell_size = 30
        self.grid = [[0 for j in range(self.num_cols)] for i in range(self.num_rows)]
        self.colors = Colors.get_cell_colors()
        # self.grid = [
        # [0,0,0,0,0,0,0,0,0,0],
        # [0,0,0,0,0,0,0,0,0,0],
        # [0,0,0,0,0,0,0,0,0,0],
        # [0,0,0,0,0,0,0,0,0,0],
        # [0,0,0,0,0,0,0,0,0,0],
        # [0,0,0,0,0,0,0,0,0,0],
        # [0,0,0,0,0,0,0,0,0,0],
        # [0,0,0,0,0,0,0,0,0,0],
        # [0,0,0,0,0,0,0,0,0,0],
        # [0,0,0,0,0,0,0,0,0,0],
        # [0,0,0,0,0,0,0,0,0,0],
        # [0,0,0,0,0,0,0,0,0,0],
        # [0,0,0,0,0,0,0,0,0,0],
        # [0,0,0,0,0,0,0,0,0,0],
        # [0,0,0,0,0,0,0,0,0,0],
        # [0,0,0,0,0,0,0,0,0,0],
        # [0,0,0,0,0,0,0,0,0,0],
        # [0,0,0,0,0,0,0,0,0,0],
        # [0,0,0,0,0,0,0,0,0,0],
        # [0,0,0,0,0,0,0,0,0,0],
        # ]
    def print_grid(self):
        for row in range(self.num_rows):
            for conlumn in range(self.num_cols):
                print(self.grid[row][conlumn], end = " ")
            print()

    def draw(self, screen):
        for row in range(self.num_rows):
            for conlumn in range(self.num_cols):
                cell_value = self.grid[row][conlumn]
                # cell_rect = pygame.Rect(x,y,w,h)
                cell_rect = pygame.Rect(conlumn*self.cell_size + 1, row*self.cell_size +1, self.cell_size -1, self.cell_size -1)
                # pygame.draw.rect(surface, color, rect)
                pygame.draw.rect(screen, self.colors[cell_value], cell_rect)