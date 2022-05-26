class Person: 
    count = 0 #static variable
    """A generic person"""
    def __init__ (self, first, last, weight, height):
        self.first_name = first
        self.last_name = last
        self.weight_in_lbs = weight
        self.height_in_inches = height
        Person.count = Person.count + 1 #increments each time a new person is created

    def calc_bmi(self): 

        return (self.weight_in_lbs * 703) / self.height_in_inches ** 2

    @classmethod #@classmethod decorator
    def print_count(cls,):
        return cls.count

    def print_self():
        return Person()

p = Person("Tom", "Thumb", 150, 62)
p2 = Person("Fred", "Flint", 225, 57)
print(p.calc_bmi())
print(p2.calc_bmi())
print(Person.count)
print(Person.print_count())