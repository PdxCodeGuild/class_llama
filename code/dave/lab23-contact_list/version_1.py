"""
This program manages a list of contacts utilizing a CSV(comma seperated value) file 
and CRUD (Create, Retrieve, Update, Delete).
"""

# open and read contacts.csv file
with open('./contacts.csv', 'r') as f:
    lines = f.read().split('\n')
    # print(lines) #works

    people = []
    contacts = []

    for i in range(len(lines)):
        dict_keys = lines[0]
        # print(dict_keys) #works
        dict_keys = dict_keys.split(',')
        # print(dict_keys)

        dict_values = lines[i] # slice off headers at index 0, start at index 1
        # print(dict_values) #works
        dict_values = dict_values.split(',')
        # print(dict_values) # works

        dict_items = dict(zip(dict_keys, dict_values))
        print(dict_items) #works

        people.append(dict_items)
    print(people) # works

    # print(people[1]['status']) # how to retrieve