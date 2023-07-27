class Tower():
    def __init__(self):
        self.i=3
        self.j=6

class Badguy():
    def __init__(self, num):
        self.i=3
        self.j=6
        self.num = num

tower = Tower()
enemies = []
for i in range(10):
    enemies.append(Badguy(i))

# find the Badguy that is closest to the exit that is in a range of 2
def findTargetRange2(enemies, tower):
    # loops through every badguy on screen until it finds the correct one
    for badguy in enemies:
        # loops through all grid spaces in a range of 2 around the tower
        for i in range(tower.i - 2, tower.i + 2):
            for j in range(tower.j - 2, tower.j + 2):
                # if the badguy is not in the corners
                if (i != tower.i - 2 and j != tower.j - 2) and (i != tower.i + 2 and j != tower.j + 2) and (i != tower.i - 2 and j != tower.j + 2) and (i != tower.i + 2 and j != tower.j - 2):
                    # if badguy is in range
                    if (i == badguy.i and j == badguy.j):
                        return badguy
    return " "
                    
target = findTargetRange2(enemies, tower)
print(target.num)