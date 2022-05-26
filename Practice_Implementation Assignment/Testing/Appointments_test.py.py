
appointments = [
    ['9am', 'Dr. Grey', 'x'], 
    ['10am', 'Dr. Green', 'x'], 
    ['11am', 'Dr. Groom', 'f'], 
    ['12am', 'Dr. Google', 'x'], 
    ['10am', 'x', 'x'], 
    ['4', 'g', 'h'], 
    ['9am', 'g', 'h'], 
    ['50am', '', 'f']
    ]

appointments_dict = {}
for x in appointments:
    appointments_dict[x[0]] = x[1:]

def cancel_appointment():
    print(appointments_dict)

    

cancel_appointment()
