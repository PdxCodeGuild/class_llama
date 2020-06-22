"""
This program manages a list of contacts utilizing a CSV(comma seperated value) file 
and CRUD (Create, Retrieve, Update, Delete).
"""


# create func that opens csv 'file_path' and creates list of dictionaries
def file_to_list(file_path):
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

# create main func
if __name__ == "__main__":
    
    while True:
        try:
            choices = input("What do you want to do?\n\nSelect and option from below:\n" +
                            "\nCREATE enter(c)" + "\nRETRIEVE enter(r)" + "\nUPDATE enter(u)" + "\nDELETE enter(D)" + 
                            "\n\nEnter Your Selection Here: ").lower()
            if choices == 'c':
                print("\nYou chose create")
                break
            elif choices == 'r':
                print("\nYou chose retrieve")
                break
            elif choices == 'u':
                print("\nYou chose update")
                break
            elif choices == 'd':
                print("\nYou chose delete")
                break
            else:
                print("whoops, invalid input, try again! ")
        except ValueError:
            print("Sorry, try one of the options again. ")
    print("\nTEST Complete")

                