import random

class BaseballPlayer:  
  def hit(self):
    """Generate a random integer 1 to 4 and return the type of hit"""
    total_bases = random.randint(1, 4)
    if total_bases == 1:
      return "single"
    elif total_bases == 2:
      return "double"
    elif total_bases == 3:
      return "triple"
    else:
      return "home run"
    
class Dancer:
  def pirouette(self):
    return "Spin, spin, spin"

def print_hit(obj):
  try:
    print(obj.hit())
  except AttributeError as e:
    print(e)
    #error will print without crashing the program

my_player = BaseballPlayer()
my_dancer = Dancer()

print_hit(my_player)
print_hit(my_dancer)