class Person: 
    count = 0 #static variable
    """A generic person"""
    def __init__ (self, first, last, weight, height):
        self.first_name = first
        self.last_name = last
        self.weight_in_lbs = weight
        self.height_in_inches = height
        Person.count = Person.count + 1 #increments each time a new person is created

    def calc_bmi(self): #This method uses the name calc_bmi and is an instance method, 
                        #so we pass in self, to ensure that Python knows it will act on this object

        return (self.weight_in_lbs * 703) / self.height_in_inches ** 2

p = Person("Tom", "Thumb", 150, 62)

#What we have accomplished here is to create a new Person object, called p, 
# assigned some values to the attributes, and then, using a print statement, 
# we called the calc_bmi() method on our instance, and it output the BMI for that object. 

p2 = Person("Fred", "Flint", 225, 57)
print(p.calc_bmi())
print(p2.calc_bmi())
print(Person.count) #will count the number of objects created