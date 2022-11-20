# Globals for the directions
# Change the values as you see fit
EAST = 'EAST'
NORTH = 'NORTH'
WEST = 'WEST'
SOUTH = 'SOUTH'
DIRECTIONS = [NORTH, EAST, SOUTH, WEST]
ADVANCE_INSTR = {NORTH: 'x, y+1', EAST: 'x+1, y', SOUTH: 'x, y-1', WEST: 'x-1, y'}

class Robot:
    def __init__(self, direction=NORTH, x_pos=0, y_pos=0):
        self.coordinates = (x_pos, y_pos)
        self.direction = direction
    
    def move(self, instructions: 'str'):
        for i in instructions:
            if i in ['R', 'L']:
                to_add = 1 if i == 'R' else -1
                current_ind = DIRECTIONS.index(self.direction)
                new_dir = current_ind + to_add
                new_dir %= 4
                self.direction = DIRECTIONS[new_dir]
            else:
                x, y = self.coordinates
                x, y = eval(ADVANCE_INSTR[self.direction])
                self.coordinates = (x, y)
                