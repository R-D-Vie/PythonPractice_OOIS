class Tuna:

    def __init__(self): #init stands for instantiate/initialise - the code will get called as soon as you create your object
        print('ghsjflksjflkysd')

    def swim(self): #compared with normal function
        print('I am swimming!')

Flipper = Tuna()
Flipper.swim()

#this will call the init function as well! without explicitly calling it

class Enemy:
    def __init__(self, x):
        self.energy = x

    def get_energy(self):
        print(self.energy)

jason = Enemy(5)
sandy = Enemy(18)

jason.get_energy()
sandy.get_energy()