class Parent():

    def print_last_name(self):
        print('Doherty')

class Child(Parent): #just inherited from Parent clas

    def print_first_name(self):
        print('Rachel')

#Now child has 2 functions

    def print_last_name(self):
        print('Sandrin')

#now have overridden last name

rachel = Child()
rachel.print_first_name()
rachel.print_last_name()