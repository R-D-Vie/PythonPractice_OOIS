class Person:
    count = 0 #added static variable

    """Represents a generic Person."""
    def __init__(self, first, last, weight, height):
        self.first_name = first
        self.last_name = last
        self.weight_in_lbs = weight
        self.height_in_inches = height
        Person.count = Person.count + 1 #references static variable and increments for each new Person object

    def calc_bmi(self):
    
        return (self.weight_in_lbs * 703) / self.height_in_inches ** 2
    
    @classmethod #this is a static method
    def print_count(cls,):
        return cls.count


p = Person('Tom', 'Thumb', 150, 62)
p2 = Person('Fred', 'Flint', 225, 57)

print(p.calc_bmi())
print(p2.calc_bmi())
print(Person.count) #prints number of objects created

print(Person.print_count())

def print_self(self):

        return (self.first_name, self.last_name, self.weight_in_lbs, self.height_in_inches, self.calc_bmi)


#incomplete from challenge