appointments = [
    ['9am', 'Dr. Green', 'Rachel'],
    ['10am', 'Dr. Green', 'Rachel'],
    ['11am', 'Dr. Green', 'Rachel'],
    ['12pm', 'Dr. Green', 'Rachel'],
]


def cancel_appointment():

    print(f"\nToday's schedule: \n {appointments}")

    print('Which appointment would you like to cancel? 1, 2, 3 or 4?')
    selection = input()
    if selection == '1':
        appointments[0].pop        
    elif selection == '2':
        appointments[1].pop
    elif selection == '3':
        appointments[2].pop
    elif selection == '4':
        appointments[3].pop
    elif ValueError:
        print('appointment does not exist. Please select on 1, 2, 3 or 4.')

    print(appointments)
        
cancel_appointment()        
