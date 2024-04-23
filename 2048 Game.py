"""
Clone of 2048 game.
"""

import poc_2048_gui
import random

# Directions, DO NOT MODIFY
UP = 1
DOWN = 2
LEFT = 3
RIGHT = 4

# Offsets for computing tile indices in each direction.
# DO NOT MODIFY this dictionary.
OFFSETS = {UP: (1, 0),
           DOWN: (-1, 0),
           LEFT: (0, 1),
           RIGHT: (0, -1)}

def merge(line):
    """
    Helper function that merges a single row or column in 2048
    """
    # replace with your code from the previous mini-project
    def sort(line):
        """
        Sub-fonction to sort the nonzero_values at the beginning
        """
        output_line1 = [0] * len(line)
        dummy_n = 0
        dummy_m = 0
        while dummy_n < len(line) and dummy_m < len(output_line1):
            if line[dummy_n] != 0:
                output_line1[dummy_m] = line[dummy_n]
                dummy_n += 1
                dummy_m += 1
            else:
                dummy_n +=1
        return output_line1
    def combine(line):
        """
        Sub-function to combine two identical juxtaposed values
        """
        line1 = sort(line)
        for dummy_i in range(len(line) - 1):
            if line1[dummy_i] == line1[dummy_i + 1]:
                line1[dummy_i] *= 2
                line1[dummy_i + 1] = 0
        return line1
    line1 = sort(line)
    line2 = sort(combine(line1))
    return line2 

class TwentyFortyEight:
    """
    Class to run the game logic.
    """

    def __init__(self, grid_height, grid_width):
        
        self._grid_height = grid_height
        self._grid_width = grid_width
        self._grid = [0]
        self.reset()
        self._indices = {UP: [(0, dummy_i) for dummy_i in range(self._grid_width)],
                   DOWN: [(self._grid_height - 1, dummy_i) for dummy_i in range(self._grid_width)],
                   LEFT: [(dummy_i, 0) for dummy_i in range(self._grid_height)],
                   RIGHT: [(dummy_i, self._grid_width - 1) for dummy_i in range(self._grid_height)]}

    def reset(self):
        """
        Reset the game so the grid is empty except for two
        initial tiles.
        """
        
        self._grid = [ [0 for dummy_col in range(self._grid_width)] for dummy_row in range(self._grid_height)]
        self.new_tile()
        self.new_tile()

    def __str__(self):
        """
        Return a string representation of the grid for debugging.
        """
        temp = list(self._grid)
        return str(temp)

    def get_grid_height(self):
        """
        Get the height of the board.
        """
        return self._grid_height

    def get_grid_width(self):
        """
        Get the width of the board.
        """
        return self._grid_width

    def move(self, direction):
        """
        Move all tiles in the given direction and add
        a new tile if any tiles moved.
        """
        # replace with your code
        if direction == UP or direction == DOWN:
            cross_start = self._grid_width
            cross_merge = self._grid_height
        else:
            cross_start = self._grid_height
            cross_merge = self._grid_width
        
        temp = []
        ind = []
        
        for dummy_j in range(cross_start):
            
            start_cell = self._indices[direction][dummy_j]
            
            for step in range(cross_merge):
                row = start_cell[0] + step * OFFSETS[direction][0]
                col = start_cell[1] + step * OFFSETS[direction][1]
                temp.append(self._grid[row][col])
                ind.append((row,col))
            
            temp = merge(temp)
            
            for dummy_i in range(len(ind)):
                
                self._grid[ind[dummy_i][0]][ind[dummy_i][1]] = temp[dummy_i]
            
            temp = []
            ind = []
          
        self.new_tile()
            

    def new_tile(self):
        """
        Create a new tile in a randomly selected empty
        square.  The tile should be 2 90% of the time and
        4 10% of the time.
        """
        # replace with your code
        tile = random.choice(9 * [2] + [4])
        
        
        
        temp = []
        for dummy_i in range(self._grid_height):
            for dummy_j in range(self._grid_width):
                if self._grid[dummy_i][dummy_j] == 0:
                    temp.append([dummy_i, dummy_j])
        if temp == []:
            print ("Game Over")
        else:
            pos = random.choice(temp)
            self._grid[pos[0]][pos[1]] = tile
        

    def set_tile(self, row, col, value):
        """
        Set the tile at position row, col to have the given value.
        """
        self._grid[row][col] = value

    def get_tile(self, row, col):
        """
        Return the value of the tile at position row, col.
        """
        return self._grid[row][col]

poc_2048_gui.run_gui(TwentyFortyEight(4, 4))
