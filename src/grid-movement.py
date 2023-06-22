grid=[
    ['s', '_', '_', '_', '_', 's', '_', '_', '_', '_'],
    ['_', '_', '_', '_', '_', 'd', '_', '_', '_', '_'],
    ['_', '_', '_', '_', '_', 'd', '_', '_', '_', '_'],
    ['_', '_', '_', 'd', 'd', 'd', '_', '_', '_', '_'],
    ['_', '_', '_', 'd', '_', '_', '_', '_', '_', '_'],
    ['_', '_', '_', 'd', 'd', 'f', '_', '_', '_', '_']
]

def findSpace(space):
    i=0
    while i < len(grid):
        j=0
        while j<len(grid[i]):
            if grid[i][j]==space:
                return [i,j]

locationOfS=[findSpace('s')]
locationOfS[1]

# location = [i,j] (location of previous coordinates)
# direction = 'u', 'd', 'l', 'r', 's' (previous direction moved)
# returns the direction to move in
def findDirection(location, direction):
    if direction != 'u' and location[0]+1 <= len(grid) and grid[location[0]+1][location[1]] == 'd':
        return 'd'

# > opposite of <=
# < opposite of >=