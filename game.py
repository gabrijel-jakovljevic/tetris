from grid import Grid
from blocks import *
import random


class Game:
    def __init__(self):
        self.grid = Grid()
        self.blocks = [IBlock(), LBlock(), SBlock(), DBlock()]
        self.current_block = self.get_random_block()
        self.next_block = self.get_random_block()
        self.game_over = False
        self.score = 0
        self.sum_cleared_rows = 0

    def progress_game(self):
        if self.sum_cleared_rows >= 3:
            self.sum_cleared_rows %= 3
            return True
        return False

    def update_score(self, lines_cleared, move_down_points):
        if lines_cleared == 1:
            self.score += 100
        elif lines_cleared == 2:
            self.score += 300
        elif lines_cleared >= 3:
            self.score += 500
        self.score += move_down_points

    def get_random_block(self):
        if len(self.blocks) == 0:
            self.blocks = [IBlock(), LBlock(), SBlock(), DBlock()]
        block = random.choice(self.blocks)
        self.blocks.remove(block)
        return block

    def move_left(self):
        self.current_block.move(0, -1)
        if not self.block_inside() or not self.block_fits():
            self.current_block.move(0, 1)

    def move_right(self):
        self.current_block.move(0, 1)
        if not self.block_inside() or not self.block_fits():
            self.current_block.move(0, -1)

    def move_down(self):
        self.current_block.move(1, 0)
        if not self.block_inside() or not self.block_fits():
            self.current_block.move(-1, 0)
            self.lock_block()

    def lock_block(self):
        tiles = self.current_block.get_cell_positions()
        for position in tiles:
            self.grid.grid[position.row][position.column] = self.current_block.id
        self.current_block = self.next_block
        self.next_block = self.get_random_block()
        rows_cleared = self.grid.clear_full_rows()
        self.sum_cleared_rows += rows_cleared
        self.progress_game()
        self.update_score(rows_cleared, 0)
        if not self.block_fits():
            self.game_over = True

    def reset(self):
        self.grid.reset()
        self.blocks = [IBlock(), LBlock(), SBlock(), DBlock()]
        self.current_block = self.get_random_block()
        self.next_block = self.get_random_block()
        self.score = 0

    def block_fits(self):
        tiles = self.current_block.get_cell_positions()
        for tile in tiles:
            if not self.grid.is_empty(tile.row, tile.column):
                return False
        return True

    def rotate(self):
        self.current_block.rotate()
        if not self.block_inside() or not self.block_fits():
            self.move_left()
            self.move_right()

    def mirror(self):
        self.current_block.mirror()
        if not self.block_inside() or not self.block_fits():
            self.move_left()
            self.move_right()

    def fall(self):
        while self.block_inside() and self.block_fits():
            self.current_block.move(1, 0)
        self.current_block.move(-1, 0)
        self.lock_block()

    def block_inside(self):
        tiles = self.current_block.get_cell_positions()
        for tile in tiles:
            if not self.grid.is_inside(tile.row, tile.column):
                return False
        return True

    def draw(self, screen):
        self.grid.draw(screen)
        self.current_block.draw(screen, 11, 11)

        if self.next_block.id == 3:
            self.next_block.draw(screen, 270, 260)
        else:
            self.next_block.draw(screen, 260, 260)
