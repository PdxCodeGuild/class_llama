# Golf League Contact List

# with open('employee_file2.csv', mode='w') as csv_file:
#     fieldnames = ['emp_name', 'dept', 'birth_month']
#     writer = csv.DictWriter(csv_file, fieldnames=fieldnames)

#     writer.writeheader()
#     writer.writerow({'emp_name': 'John Smith', 'dept': 'Accounting', 'birth_month': 'November'})

# a_file = open("sample.csv", "w")
# a_dict = {"a": 1, "b": 2}

# writer = csv.writer(a_file)
# for key, value in a_dict.items():
#     writer.writerow([key, value])
# a_file.close()

import csv

with open('golf_league_list.csv', mode='w') as f:
        fieldnames = ['name', 'team_name', 'putter_name']
        writer = csv.DictWriter(f, fieldnames=fieldnames)

        writer.writeheader()
        writer.writerow({'name': 'Ty Webb', 'team_name': 'Caddy Shackers', 'putter_name': 'Mitch Cumstein'}) 
        writer.writerow({'name': 'Judge Smails', 'team_name': 'Brown Nosers', 'putter_name': 'Billy Baroo'})
        writer.writerow({'name': 'Carl Spackler', 'team_name': 'Cannon Ball Comin', 'putter_name': 'Ye Old Flat Wedge'})


# creating or adding new golfers to the contact list
def new_golfer(f):
    while True:
        golf_league_list = {}

        name = input("Enter your first and last name: ")
        golf_league_list["name"] = name
        
        team_name = input("Enter your team name: ")
        golf_league_list["team_name"] = team_name
        
        putter_name = input("What is your putter's name? ")
        golf_league_list["putter_name"] = putter_name

    f.append(golf_league_list)
    return (f) 

            
def retrieve_golfer(f):
    look_for = input("Enter the golfer's name: ")
    for contact in (f):
        if contact["name"] == look_for:
            print(contact)
            return contact

# change the value of a specific item by referring to its key name
def update_golfer(f):
    contact = retrieve_golfer(f) 
    change_info = input("Change name, team name, or putters name? ")
    for n in (f) :
        if n == contact:
            n[change_info] = change_info
        return (f)  

# deleting contacts or 
def erase_golfer(contact_list):
    contact = retrieve_golfer(contact_list)
    contact_list.remove(contact)
    return contact_list

# updating info
def commit_changes(contacts):
    contact_string = ""
    for contact in contacts:
        for key in contact:
            contact_string = contact_string + key + ":" + contact[key]
            if key != "status":
                contact_string = contact_string + "," 
                contact_string = contact_string + "\n"
                contact_string = contact_string.strip()
            with open("golf_league_list.csv", mode= "w") as contact_list:
                contact_list.write(contact_string)

# with open('employee_file2.csv', mode='w') as csv_file:
#     fieldnames = ['emp_name', 'dept', 'birth_month']
#     writer = csv.DictWriter(csv_file, fieldnames=fieldnames)

#     writer.writeheader()
#     writer.writerow({'emp_name': 'John Smith', 'dept': 'Accounting', 'birth_month': 'November'})

def main():
       

    dict_list = []

    for line in dict_list:
        alt_list = line.split(",")
        alt_dict = {}
    for line in alt_list:
        auth_alt_list = line.split(":")
        auth_alt_list[0] = auth_alt_list[0].strip()
        auth_alt_list[0] = auth_alt_list[1].strip()
        alt_dict[auth_alt_list[0]] = auth_alt_list[1]
        dict_list.append(alt_dict)       

    while True:
        option = int(input("""Choose an option: 
        (1) Register new golfer
        (2) Search for league golfers
        (3) Update info for a golfer
        (4) Delete a golfer profile
        (5) Show all current league golfers
        (6) Save changes
        (7) Quit
        """))

        if option == 1:
            new_golfer(dict_list)
        elif option == 2:
            retrieve_golfer(dict_list)
        elif option == 3:
            update_golfer(dict_list)
        elif option == 4:
            erase_golfer(dict_list)
        elif option == 5:
            print(dict_list)
        elif option == 6:
            commit_changes(dict_list)
        elif option == 7:
            break
    
    
# if __name__ == "__main__":
#     main()  
        








