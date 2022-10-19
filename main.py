contacts = []

while(True):
    response = input('(1)Add Contact (2)Print Contacts (3)Exit: ')
    
    if response == '1':
        person_name = input('Name: ')
        person_surname = input('Surname: ')
        person_phone = input('Phone: ')
        person_email = input('Email: ')

        person_data = {
            'Name': person_name,
            'Surname': person_surname,
            'Phone': person_phone,
            'Email': person_email
        }

        contacts.append(person_data)
    elif response == '2':
        for contact in contacts:
            print("---CONTACT---")
            print(f"{contact['Name']} {contact['Surname']}")
            print(f"Phone: {contact['Phone']}")
            print(f"Email: {contact['Email']}")
    elif response == '3':
        print('Bye!')
        exit()
