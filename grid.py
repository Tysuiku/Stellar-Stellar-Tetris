import pygame

class Grid:
    def __init__(self):
        self.num_rows = 20
        self.num_cols = 10
        self.cell_size = 30
        self.grid = [[0 for j in range(self.num_cols)] for i in range(self.num_rows)]
        self.colors = self.get_cell_colors()
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

    def get_cell_colors(self):

        dark_gray = (57,61,71)
        green = (38,208,124)
        red = (197,70,68)
        orange = (252,143,50)
        yellow = (255,233,0)
        purple = (199,36,177)
        cyan = (89,203,232)
        blue = (65,105,225)

        return [dark_gray, green, red, orange, yellow, purple, cyan, blue]

    def draw(self, screen):
        for row in range(self.num_rows):
            for conlumn in range(self.num_cols):
                cell_value = self.grid[row][conlumn]
                # cell_rect = pygame.Rect(x,y,w,h)
                cell_rect = pygame.Rect(conlumn*self.cell_size + 1, row*self.cell_size +1, self.cell_size -1, self.cell_size -1)
                # pygame.draw.rect(surface, color, rect)
                pygame.draw.rect(screen, self.colors[cell_value], cell_rect)