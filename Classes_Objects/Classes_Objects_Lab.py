class Person:
    '''represents a generic person'''

    #__init__ is a reseved method in python classes. 
    # It is called as a constructor in object oriented terminology. 
    # This method is called when an object is created from a class and 
    # it allows the class to initialize the attributes of the class

    def __init__(self, first, last, weight, height):
        self.first_name = first
        self.last_name = last
        self.weight_in_lbs = weight
        self.height_in_inches = height

p = Person('Tom', 'Thumb', 150, 78)

print(p.first_name + ' ' + p.last_name + ' weighs ' + str(p.weight_in_lbs) + 'lbs.')

p.first_name = 'George'

print(p.first_name + ' ' + p.last_name + ' weighs ' + str(p.weight_in_lbs) + 'lbs.')


