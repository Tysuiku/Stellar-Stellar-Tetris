from grid import Grid
from blocks import *
import random
import pygame
import os


# Add the resource_path function
def resource_path(relative_path):
    """Get absolute path to resource, works for dev and for PyInstaller"""
    try:
        # PyInstaller creates a temp folder and stores path in _MEIPASS
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")

    return os.path.join(base_path, relative_path)


class Game:
    def __init__(self):
        self.grid = Grid()
        self.blocks = [
            IBlock(),
            JBlock(),
            LBlock(),
            OBlock(),
            SBlock(),
            TBlock(),
            ZBlock(),
        ]
        self.current_block = self.get_random_block()
        self.next_block = self.get_random_block()
        self.game_over = False
        self.score = 0

        # Update the sound paths
        self.rotate_sound = pygame.mixer.Sound(resource_path("Sounds/rotate.ogg"))
        self.clear_sound = pygame.mixer.Sound(resource_path("Sounds/clear.ogg"))

        pygame.mixer.init()  # Initialize the mixer

        # Update the music path
        pygame.mixer.music.load(resource_path("Sounds/music.ogg"))

        pygame.mixer.music.play(-1)  # Start playback
        volume_level = 0.1  # Set to % volume
        pygame.mixer.music.set_volume(volume_level)

    # ... rest of the code remains unchanged ...

    def update_score(self, lines_cleared, moved_down_points):
        if lines_cleared == 1:
            self.score += 100
        elif lines_cleared == 2:
            self.score += 300
        elif lines_cleared == 3:
            self.score += 500
        elif lines_cleared == 4:
            self.score += 1000
        self.score += moved_down_points

    def get_random_block(self):
        if len(self.blocks) == 0:
            self.blocks = [
                IBlock(),
                JBlock(),
                LBlock(),
                OBlock(),
                SBlock(),
                TBlock(),
                ZBlock(),
            ]
        block = random.choice(self.blocks)
        self.blocks.remove(block)
        return block

    def move_left(self):
        self.current_block.move(0, -1)
        if self.block_inside() == False or self.block_fits() == False:
            self.current_block.move(0, 1)

    def move_right(self):
        self.current_block.move(0, 1)
        if self.block_inside() == False or self.block_fits() == False:
            self.current_block.move(0, -1)

    def move_down(self):
        self.current_block.move(1, 0)
        if self.block_inside() == False or self.block_fits() == False:
            self.current_block.move(-1, 0)
            self.lock_block()

    def lock_block(self):
        tiles = self.current_block.get_cell_positions()
        for position in tiles:
            self.grid.grid[position.row][position.column] = self.current_block.id
        self.current_block = self.next_block
        self.next_block = self.get_random_block()
        rows_cleared = self.grid.clear_full_rows()
        if rows_cleared > 0:
            self.clear_sound.play()
            self.update_score(rows_cleared, 0)
        if self.block_fits() == False:
            self.game_over = True

    def reset(self):
        self.grid.reset()
        self.blocks = [
            IBlock(),
            JBlock(),
            LBlock(),
            OBlock(),
            SBlock(),
            TBlock(),
            ZBlock(),
        ]
        self.current_block = self.get_random_block()
        self.next_block = self.get_random_block()
        self.score = 0

    def block_fits(self):
        tiles = self.current_block.get_cell_positions()
        for tile in tiles:
            if self.grid.is_empty(tile.row, tile.column) == False:
                return False
        return True

    def rotate(self):
        self.current_block.rotate()
        if self.block_fits() == False or self.block_inside() == False:
            self.current_block.undo_rotation()
        else:
            self.rotate_sound.play()

    def block_inside(self):
        tiles = self.current_block.get_cell_positions()
        for tile in tiles:
            if self.grid.is_inside(tile.row, tile.column) == False:
                return False
        return True

    def hard_drop(self):
        # Move the current block down until it collides.
        while True:
            self.current_block.move(1, 0)
            if self.block_inside() == False or self.block_fits() == False:
                # When collision occurs, move it back up by one step
                # and then lock the block in place.
                self.current_block.move(-1, 0)
                self.lock_block()
                break

    def draw(self, screen):
        self.grid.draw(screen)
        self.current_block.draw(screen, 11, 11)

        if self.next_block.id == 3:
            self.next_block.draw(screen, 255, 290 - 50)
        elif self.next_block.id == 4:
            self.next_block.draw(screen, 255, 280 - 50)
        else:
            self.next_block.draw(screen, 270, 270 - 50)
