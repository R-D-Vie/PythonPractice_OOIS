class Patient:
    """
    Represents the patient by getting input from an agent (the patient)
    Attributes: name(str), address(str), phone(str), registered doctor(str)
    Methods: can request an appointment (yes or no), can request prescription based on values passed    
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
    """
    Represents the doctor who inherits attributes from the Healthcare Professional class
    Additional Attributes: registered patient(str)
    Methods: can confirm issuance of prescription based on yes/no user input    
    """
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

 
class Nurse(HealthcareProfessional):
    """
    Represents the nurse who inherits attributes from the Healthcare Professional class
    Additional Attributes: none
    Currently no role/ class methods assigned   
    """
    def __init__(self, name, id):
        super().__init__(name, id, nurse)
        self.nurse = nurse

nurse = Nurse

class Appointment:
    """
    Represents the appointment class
    Attributes: staff (i.e. Healthcase professional) and assigned patient 
    """
    def __init__(self, staff, patient):
        self.staff = staff
        self.patient = patient

appointment1 = Appointment(doctor1.name, patient1.name)
appointment2 = Appointment(doctor2.name, patient2.name)
appointment3 = Appointment(doctor3.name, patient3.name)
appointment4 = Appointment(doctor4.name, patient4.name)

class AppointmentSchedule(Appointment):
    """
    Represents the appointment schedule class which inherits staff and patient data from the Appointment class
    Additional attributes: time 
    """
    def __init__(self, staff, patient, time):
        super().__init__(staff, patient)
        self.time = time

    def add_appointment(time, staff, patient):
    
        appointments = []

        index = 0
        while index < len(time):
            scheduled_appointment = [time[index], staff[index], patient[index]]
            appointments.append(scheduled_appointment)
            index += 1

        return appointments

    def cancel_appointment():

        print(f"\nToday's schedule: \n {appointments}")

        print('Which appointment would you like to cancel? 1, 2, 3 or 4?')
        selection = input()
        
        if selection == '1':
            appointments[0].pop #mistake      
        elif selection == '2':
            appointments[1].pop
        elif selection == '3':
            appointments[2].pop
        elif selection == '4':
            appointments[3].pop
        elif ValueError:
            print('appointment does not exist. Please select on 1, 2, 3 or 4.')

time = ["9am", "10am", "11am", "12am"]
staff = [doctor1.name, doctor2.name, doctor3.name, doctor4.name]
patient = [patient1.name, patient2.name, patient3.name, patient4.name]
appointments = AppointmentSchedule.add_appointment(time, staff, patient) #there is a mistake here
AppointmentSchedule.cancel_appointment()
    
class Receptionist:
    """
    Represents the receptionist. Is not child class of healthcare professional.
    Attributes: name(str), address(str), phone(str), id(str)
    Methods: can make an appointment by entering details
    In this method the appointment list created (appointments_receptionist[]) is transposed into a dictionary
    (appointments_dict{}) for easier handling in future in terms of combining with the 'find_next_available' method,
    which iterates through a dictionary 
    """

    def __init__(self, name, id):
        self.name = name
        self.id = id
    
    def make_appointment(self):
        
        appointmentLimit = 4
        
        appointments_receptionist = []
        for i in range(appointmentLimit):
            time = input('\nEnter an appointment time in format 9am, 10am etc.: \n')
            staff = input('Enter Doctor name (Dr. Green, Dr. Grey, Dr. Groom or Dr. Google): \n')
            patient = input('Enter Patient name: \n')
            appointment = [time, staff, patient]
            print(appointment)
            i = appointment
            appointments_receptionist.append(i)

        else:
            print('Daily appointment limit reached \n')
            print(f'{self.name}/ (ID: {self.id}) created following appointments: \n{appointments}\n')
            appointments.extend(appointments_receptionist)

    def cancel_appointment(self):

        appointments_dict = {}
        for x in appointments:
            appointments_dict[x[0]] = x[1:]
            print(f'Scheduled Appointments: \n {appointments_dict}')

            print('\n Enter the time of the appointment to delete')
            selection = input()

            for k in list(appointments_dict.keys()):
                if appointments_dict[k] == selection:
                    del appointments_dict[k]
        
            print(appointments_dict)

    def find_next_available(self, appointment_calendar):
        self.appointment_calendar = appointment_calendar
        
        appointment_calendar = {

            '9am' : True,
            '10am' : True,
            '11am' : False,
            '12pm' : True,
            '1pm' : False,
        }

        for time, value in appointment_calendar.items():
            print('{0} corresponds to {1}'.format(time, value))

receptionist = Receptionist('Rachel', '1234')
receptionist.make_appointment()
receptionist.cancel_appointment()
receptionist.find_next_available()