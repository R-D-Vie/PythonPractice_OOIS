class Person:
  def __init__(self, name, age):
    self._name = name
    self._age = age
  
  @property
  def name(self):
    return self._name
  
  @property
  def age(self):
    return self._age

#getter
  
c = Person("Calvin", 6)
print(c.name)
print(c.age)


class Person:
  def __init__(self, name):
    self._name = name
  
  @property
  def name(self):
    return self._name
  
  @name.setter
  def name(self, new_name):
    self._name = new_name
  
c = Person("Calvin")
print(c.name)
c.name = "Hobbes"
print(c.name)

#setter with property class
