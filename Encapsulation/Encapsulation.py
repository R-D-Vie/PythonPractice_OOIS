class Phone:
  def __init__(self, make, storage, megapixels):
    self.make = make
    self.storage = storage
    self.megapixels = megapixels
    
my_phone = Phone("iPhone", 256, 12)
print(my_phone.make)
print(my_phone.storage)
print(my_phone.megapixels)

#A traditional class in Python does not provide any restrictions to accessing data because everything is public by default. 

my_phone = Phone("iPhone", 256, 12)
print(my_phone.storage)
my_phone.storage = 64
print(my_phone.storage)

#the above code downgrades the iphone storage to 64
#Watch out! Unexpectd changes to instance variables can cause problems to code

my_phone = Phone("iPhone", 256, 12)
my_phone.model = True
my_phone.storage = "256GB"
my_phone.megapixels = -32

#when programmers use a single _ before an attribute or method name, the attribute or method is considered private
class Phone:
  def __init__(self, model, storage, megapixels, carrier):
    self._model = model
    self._storage = storage
    self._megapixels = megapixels
    self._carrier = carrier

my_phone = Phone("iPhone", 256, 12, "AT&T")
print(my_phone.__dict__)

#is it really private? no - this is just a convention, not enforced by the python interpreter

class PrivateClass:
  def __init__(self):
    self._private_attribute = "I am a private attribute"
    
obj = PrivateClass()
print(obj._private_attribute)


class PrivateClass:
  def __init__(self):
    self._private_attribute = "I am a private attribute"
  
  def _private_method(self):
    return "I am a private method"
    
obj = PrivateClass()
print(obj._private_method())

#DOUBLE UNDERSCORE - enforces changes
class PrivateClass:
  def __init__(self):
    self.__private_attribute = "I am a private attribute"
    
  def helper_method(self):
    return self.__private_attribute
    
obj = PrivateClass()
print(obj.helper_method())

#OR

class PrivateClass:
  def __init__(self):
    self.__private_attribute = "I am a private attribute"
    
  def __private_method(self):
    return "I am a private method"
  
  def helper_method(self):
    return self.__private_method()
    
obj = PrivateClass()
print(obj.helper_method())

#the double underscore is used to avoid name collisions in inheritance.

