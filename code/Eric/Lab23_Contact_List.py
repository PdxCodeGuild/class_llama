# Golf League Contact List

'''
dict_data = {'key1': [1, 2, 3], 'key2': [4, 5, 6]}

with open("dict2csv.txt", 'w') as outfile:
   csv_writer = csv.writer(outfile, delimiter=',', quotechar='|', quoting=csv.QUOTE_MINIMAL)

   for k,v in dict_data.items():
       csv_writer.writerow([k] + v)
'''
import csv


with open('golf_league_list.csv', 'r') as file:
    lines = file.read().split('\n')

# creating or adding new golfers to the contact list
def new_golfer(contact_list):
    
    while True:
        golf_league = {}
        
        name = input("Enter your first and last name: ")
        golf_league["name"] = name
        
        team_name = input("Enter your team name: ")
        golf_league["team_name"] = team_name
        
        putter_name = input("What is your putter's name? ")
        golf_league["putter_name"] = putter_name

        contact_list.append(golf_league)
        return contact_list

# search or lookup contacts w/ for loops
def retrieve_golfer(contact_list):
    lookup_golfer = input("Enter the golfer's name: ")
    for contact in contact_list:
        if contact["name"] == lookup_golfer:
            print(contact)
            return contact

# change the value of a specific item by referring to its key name
def update_golfer(contact_list):
    contact = retrieve_golfer(contact_list)
    change_info = input("Change name, team name, or putters name? ")
    for n in contact_list:
        if n == contact:
            n[change_info] = change_info
        return contact_list

# deleting contacts or 
def erase_contact(contact_list):
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
            with open("golf_league_list.csv", "w") as contact_list:
                contact_list.write(contact_string)

# storing a dictionary
def main():
    with open('golf_league_list.csv', 'r') as file:
        lines = file.read().split('\n')

    dict_list = []

    for line in lines:




