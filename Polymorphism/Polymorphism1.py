a = 5
b = 10
print(a + b)

c = '5'
d = '10'
print(c + d)

#a single interface (the plus operator) working with different data types 
# (integers and strings). This is an example of polymorphism


class Alpha:
    def show(self):
        print("I am Alpha")

    def hello(self):
        print("Hello from Alpha")

class Bravo(Alpha):
    def show(self):
        print("I am Bravo")

    def hello(self):
        print("Hello from Bravo")

test_object = Bravo()
test_object.hello()