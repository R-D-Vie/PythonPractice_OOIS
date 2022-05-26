class Patient:
    def __init__ (self, first, last, address, phone, doctor):
        self.first = input(first)
        self.last = input(last)
        self.adress = input(address)
        self.phone = input(phone)
        self.doctor = input(doctor)

    @property
    def fullname(self):
        return '{} {}'.format(self.first, self.last)

    @fullname.setter
    def fullname(self, name):
        first, last = name.split(' ')
        self.first = first
        self.last = last

    def request_repeat(self):
        pass
        
    def request_appointment(self): 
        pass

p1 = Patient("Tom", "Thumb", "25 Brooke Road", "1234567", "Dr. Grove")
p2 = Patient("Fred", "Flint", "67 Imperial Street", "3456789", "Dr. Harley")
p3 = Patient("Hannah", "Mason", "15 Something Street", "67891011", "Dr. Manning")
p4 = Patient("Gary", "Rogers", "16 Fleet Street", "0123456", "Dr. Grove")
p5 = Patient("Sarah", "Sander", "14 Park Street", "00246810", "Dr. Manning")

PatientList = [p1, p2, p3, p4, p5]

print(PatientList)




    
