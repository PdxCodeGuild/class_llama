with open('medieval contacts new.csv', 'r') as file:
    lines = file.read().split('\n')

print(lines)

dict_list = []
temp_dict = {}
items = []
for line in lines:
    new_item = line.split(",")
    items.append(new_item)

categories = items[0]
for item in items:
    if item == categories:
        items.remove(item)

for item in items:
    temp_dict = {categories[0]:item[0],categories[1]:item[1],categories[2]:item[2],categories[3]:item[3],}
    dict_list.append(temp_dict)

print(dict_list)

contacts = dict_list
contacts_string = "name,house allegiance,house words,status\n"

for contact in contacts:
    for key in contact:
        contacts_string = contacts_string + contact.get(key) + ","
    contacts_string = contacts_string.strip(',')
    contacts_string = contacts_string + "\n"




print(contacts_string)

"""contacts_string = ""
for contact in contacts:
    for key in contact:
        contacts_string = contacts_string + key + ": " + contact[key]
        if key != "status":
            contacts_string = contacts_string + ", "
    contacts_string = contacts_string + "\n"   
contacts_string = contacts_string.strip()    
with open("medieval contacts.csv", "w") as contact_list:
    contact_list.write(contacts_string)"""

    



