class Person:
    '''represents a generic person'''

    def __init__(self, first, last, weight, height):
        self.first_name = first
        self.last_name = last
        self.weight_in_lbs = weight
        self.height_in_inches = height

p1 = Person('Tom', 'Jones', 50, 170)
p2 = Person('Fred', 'Astaire', 78, 190)
p3 = Person('George', 'Benson', 99, 200)
p4 = Person('Tanya', 'Babe', 56, 168)
p5 = Person('Mary', 'Jane', 67, 190)

People_List = [p1, p2, p3, p4, p5]
for x in People_List:
    print(x.first_name)
