def mouse_was_pressed(direction):
    pass
def get_collision(obj1, obj2):
    pass
def set_animation(obj, animation):
    pass
def destroy(obj):
    pass

class Player:
    def __init__(self):
        self.p2op1 = 0
        self.p2op2 = 0
        self.form = "p2op1"

class Game:
    def __init__(self):
        self.player = Player()
        self.bernard2 = 0
        self.dh = 0

class Play:
    def __init__(self):
        self.byebyeStuff = [1,1,1,1]
        

    def loop(self):
        game = Game()

        if mouse_was_pressed("left"):
            try:
                if game.bernard2:
                    self.hand = game.bernard2
            except:
                pass

            try:
                if game.dh:
                    self.hand = game.dh
            except:
                pass

            if get_collision(self.hand, self.byebyeStuff[1]):
                game.player.form = "p2op2"
                set_animation(game.player, game.player.p2op2)
                self.closeShop = True

            elif get_collision(self.hand, self.byebyeStuff[0]):
                game.player.form = "p2op1"
                set_animation(game.player, game.player.p2op1)
                self.closeShop = True
            
            if self.closeShop:
                for stuff in self.byebyeStuff:
                    destroy(stuff)