class Mario():
    def move(self):
        print('I am moving!')

class Shroom():
    def eat_shroom(self):
        print('Now I am big!')

class Fire():
    def jump_on_flower(self):
        print('I have fire in my tummy!')

class BigMario(Mario, Shroom, Fire): #inheriting from Mario and Shroom - saves from rewriting code
    pass #to handle the syntax error

bm = BigMario()
bm.move()
bm.eat_shroom()
bm.jump_on_flower()


