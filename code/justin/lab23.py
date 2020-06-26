def load_contacts():
    with open('test_file.csv', 'r') as file:
        lines = file.read().split('\n')
        heading = lines[0].split(',')
        contacts = []
        for i in range(1, len(lines)):
            content = lines[i].split(',')
            entry = dict(zip(heading, content))
            contacts.append(entry)
            
        return contacts

contacts = load_contacts()

def create_entry():
    with open('test_file.csv', 'w') as file:
        lines = file.read().split('\n')
        heading = lines[0].split(',')
        name = input("What's the person's name?: ")
        if name in lines(range(1, len(lines))):
            print("Duplicate entry detected.")
        else:
            contacts.append(name)
            
            location = input(f"What is {name}'s location?")
            # add location as value to key // contacts.append()?
            drink = input(f"What is {name}'s favorite drink?")
            # add drink as value to key



def retrieve_entry():
    with open('test_file.csv', 'w') as file:
        name = input("What name do you want to look up?:" )

def update_entry():
    with open('test_file.csv', 'w') as file:
        pass #incomplete

def delete_entry():
    with open('test_file.csv', 'w') as file:
        pass #incomplete


