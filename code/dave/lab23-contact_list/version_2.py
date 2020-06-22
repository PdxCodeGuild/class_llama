"""
This program manages a list of contacts utilizing a CSV(comma seperated value) file 
and CRUD (Create, Retrieve, Update, Delete).
"""


# create func that opens csv 'file_path' and creates list of dictionaries
def file_to_list(file_path):
    # open and read contacts.csv file
    with open(file_path, 'r') as f:
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
        return people


# create func that creates a record
def create_contact(people):
    pass

# create func that retrieves a record
def retrieve_contact(people):
    pass

# create func that updates a record
def update_contact(people):
    pass

# create func that deletes a record
def delete_contact(people):
    pass





# create main func
if __name__ == "__main__":

    file_path = "./contacts.csv"
    file_to_list(file_path)
    
    while True:
        try:
            choices = input("\nWhat do you want to do?\nSelect and option from below:\n" +
                            "\nCREATE enter(c)" + "\nRETRIEVE enter(r)" + "\nUPDATE enter(u)" +
                            "\nDELETE enter(d)" + "\n\nEnter Your Selection Here: ").lower()
            print("\n_______________________________________________________" +
                  "\nvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvv")
            if choices == 'c':
                print("\nYou chose create")
                choice = 'create'
                create_contact()
                break
            elif choices == 'r':
                print("\nYou chose retrieve")
                choice = 'retrieve'
                retrieve_contact()
                break
            elif choices == 'u':
                print("\nYou chose update")
                choice = 'update'
                update_contact()
                break
            elif choices == 'd':
                print("\nYou chose delete")
                choice = 'delete'
                delete_contact()
                break
            else:
                input("\nWHOOPS, WRONG INPUT. Try Again (Press Enter To Continue)")
        except ValueError:
            print("\nSorry, try one of the options again. ")
    print("\nTEST Complete you selected to", choice)

