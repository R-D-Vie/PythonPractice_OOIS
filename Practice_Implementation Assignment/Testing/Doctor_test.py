class Patient:
    """
    Represents the patient by getting input from an agent (the patient)
    Attributes: name(str), address(str), phone(str), registered doctor(str)    
    """
    def __init__(self):
        
        self.name = input('Patient name: ')
        self.address = input('Patient address: ')
        self.phone = input('Phone number: ')
        self.patientDetails = [self.name, self.address, self.phone]
        
        print('\nPatient details entered: \n', self.patientDetails)   

    def request_appointment(self):

        checking_appointment = input('Request appointment? Y/N \n')
        if checking_appointment == 'Y':
            print('\nReceptionist arrange appointment.')
        elif checking_appointment == 'N':
            print('Patient does not need appointment.\n')

    def request_prescription(self, quantity, dosage):
        self.quantity = quantity
        self.dosage = dosage

        print(f'Request Prescription: medication in quantity {self.quantity}, and dose {self.dosage}.\n')        
        
patient1 = Patient()
patient1.request_appointment()
patient1.request_prescription(1, 2.30)
patient2 = Patient()
patient2.request_appointment()
patient2.request_prescription(2, 6.7)
patient3 = Patient()
patient3.request_appointment()
patient3.request_prescription(3, 4.5)
patient4 = Patient()
patient4.request_appointment()
patient4.request_prescription(5, 1.0)

directory_patientDetails = [patient1.patientDetails, patient2.patientDetails, patient3.patientDetails, patient4.patientDetails]
print('\nPatient Directory: \n', directory_patientDetails)

class HealthcareProfessional:
    """
    Represents the parent class for all staff (receptionist, doctor, nurse)
    Attributes: name(str), id(str)  
    """
    def __init__ (self, name, id):
        self.name = name
        self.id = id

class Doctor(HealthcareProfessional):
    def __init__(self, name, id, registered_patient):
        super().__init__(name, id)
        self.registered_patient = registered_patient

    def issuePrescription(self, registered_patient):
        self.registered_patient = registered_patient

        print(f'\nShow prescriptions to issue for {self.registered_patient}: Y/N ')
        response = input()
        while response == 'Y':
            print(f'\n{self.name} issues prescription to: {self.registered_patient}\n')
            break
        else:
            print(f'Do not show issued prescriptions for {self.registered_patient}\n')
            

doctor1 = Doctor('Dr. Grey', '12345', patient1.name)
doctor1.issuePrescription(patient1.name)
doctor2 = Doctor('Dr. Green', '45678', patient2.name)
doctor2.issuePrescription(patient2.name)
doctor3 = Doctor('Dr. Groom', '78910', patient3.name)
doctor3.issuePrescription(patient3.name)
doctor4 = Doctor('Dr. Google', '132536', patient4.name)
doctor4.issuePrescription(patient4.name)