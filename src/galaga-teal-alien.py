import math

class Game:
    def __init__(self):
        self.player = Player()

class Player:
    def __init__(self):
        self.x = 0
        self.y = 0

game = Game()

class TealAlien:
    # start
    def __init__(self):
        self.speed = 5 # speed the alien moves
        self.targetdirection = 0 # 0 = player on right side of alien, 1 = player on left side of alien
                                 # alien does a flip to left if player is on right and vice versa   
        self.diving = False # if the alien is flipping
        self.frames = 0 # frames since alien spawned in

    # loop
    def loop(self):
        # start with ahving temp move
        temp = TealAlien()
        self.frames += 1 # count frames
        if self.frames == 120: # once 2 seconds have passed
            self.vertical = game.player.y - self.y # get vertical distance between player and alien
            self.horizontal = game.player.x - self.x # get horizontal distance between player and alien

            if self.horizontal == 0: # prevent division by 0
                self.horizontal = 1

            if self.x < game.player.x: # if player is on right side of alien
                """
                    number to round to: self.speed
                    formula for rounding: self.speed * round(number / self.speed)
                    get angle in radians using pythagorean theorem:
                        a^2 + b^2 = c^2
                            a = self.vertical
                            b = self.horizontal

                        soh cah toa
                        tangent = opposite / adjacent
                            opposite = self.vertical
                            adjacent = self.horizontal
                        tangent = self.vertical / self.horizontal

                        find angle with arctan
                        angle = arctan(tangent)
                        angle = math.atan(self.vertical / self.horizontal)

                        multiply self.vertical by -1 because the y axis is inverted

                        angle is in radians, convert to degrees
                        angle = angle * (360 / (math.pi * 2))
                """
                self.targetangle = self.speed * round((math.atan((self.vertical * -1) / self.horizontal) * (360 / (math.pi * 2)) + 90) / self.speed)
                self.targetangle *= -1 # flip angle

            else: # if player is on left side of alien
                self.targetangle = self.speed * round((math.atan((self.vertical) / self.horizontal) * (360 / (math.pi * 2)) + 90) / self.speed) # flipping y axis is not necessary
                # flipping angle is not necessary

            if self.x < game.player.x: # if player is on right side of alien
                self.targetdirection = 0 # flip to left
            else: # if player is on left side of alien
                self.targetdirection = 1 # flip to right

            self.diving = True # start diving

            if self.diving == True: # when diving

                if temp.angle != self.targetangle: # while angle is not equal to target angle
                    if self.targetdirection == 0: # if target direction is left
                        temp.angle += self.speed # flip to left

                    else: # if target direction is right
                        temp.angle -= self.speed # flip to right

                else: # if angle is equal to target angle
                    self.diving = False # stop diving

                if temp.angle + 360 == self.targetangle or temp.angle - 360 == self.targetangle: # account for angle going over 360 or under 0
                    self.diving = False
                
                # move temp
                temp.x += self.speed * -math.sin(temp.angle * math.pi / 180)
                temp.y += self.speed * math.cos(temp.angle * math.pi / 180)




            else: # once diving is done
                # move actual alien
                self.vertical = game.player.y - temp.y # get vertical distance between player and temp
                self.horizontal = game.player.x - temp.x # get horizontal distance between player and temp

                if self.horizontal == 0: # prevent division by 0
                    self.horizontal = 1

                if temp.x < game.player.x: # if player is on right side of alien
                    self.targetangle = self.speed * round((math.atan((self.vertical * -1) / self.horizontal) * (360 / (math.pi * 2)) + 90) / self.speed)
                    self.targetangle *= -1 # flip angle

                else: # if player is on left side of alien
                    self.targetangle = self.speed * round((math.atan((self.vertical) / self.horizontal) * (360 / (math.pi * 2)) + 90) / self.speed) # flipping y axis is not necessary
                    # flipping angle is not necessary

                if temp.x < game.player.x: # if player is on right side of alien
                    self.targetdirection = 0 # flip to left
                else: # if player is on left side of alien
                    self.targetdirection = 1 # flip to right

                self.diving2 = True # start diving

                if self.diving2 == True: # when diving

                    if self.angle != self.targetangle: # while angle is not equal to target angle
                        if self.targetdirection == 0: # if target direction is left
                            self.angle += self.speed # flip to left

                        else: # if target direction is right
                            self.angle -= self.speed # flip to right

                    else: # if angle is equal to target angle
                        self.diving2 = False # stop diving

                    if self.angle + 360 == self.targetangle or self.angle - 360 == self.targetangle: # account for angle going over 360 or under 0
                        self.diving2 = False
                    
                    # move alien
                    self.x += self.speed * -math.sin(self.angle * math.pi / 180)
                    self.y += self.speed * math.cos(self.angle * math.pi / 180)