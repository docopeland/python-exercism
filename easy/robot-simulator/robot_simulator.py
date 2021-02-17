# Globals for the directions
# Change the values as you see fit
NORTH = 0
EAST = 1
SOUTH = 2
WEST = 3

class Robot:
    advance = {NORTH: (0,1), EAST: (1,0), SOUTH: (0,-1), WEST: (-1,0)}

    def __init__(self, direction=NORTH, x=0, y=0):
        self.direction = direction
        self.coordinates = (x,y)

    def move(self, movement):
        for moves in movement:
            if moves == "L":
                self.direction = (self.direction-1) % 4
            elif moves == "R":
                self.direction = (self.direction+1) % 4
            else:
                self.coordinates = tuple(map(lambda x, y: x + y, self.coordinates, self.advance[self.direction]))
