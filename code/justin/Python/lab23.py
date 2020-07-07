with open('test_file.csv', 'r') as file:
    lines = file.read().split('\n')
    heading = lines[0].split(',')
    contacts = []
    for i in range(1, len(lines)):
        content = lines[i].split(',')
        entry = dict(zip(heading, content))
        contacts.append(entry)

keys = 
data =


def create_entry(data, keys):
    new_contact = {}
    for key in keys:
        new_contact[key] = input("What is your new contact's {key}?" )
    data.append(new_contact)

def retrieve_entry(file):
    pass

def update_entry(file):
    pass #incomplete

with open('test_file.csv', 'w') as write_file:

def delete_entry(file):
    pass #incomplete


