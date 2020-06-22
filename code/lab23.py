with open('lab23csv.csv', 'r') as file:
    lines = file.read().split('\n')


phonebook = []

for line in range(len(lines)):
    keytool = lines[0]
    keytool = keytool.split(',')
    
    val = lines[line]
    val = val.split(',')
    valuedict = dict(zip(keytool, val))
    phonebook.append(valuedict)


def updatefile(phonebook):
    # create some lists from dictionary
    phonebook[0].value()
    list(phonebook[0].values())
    list(phonebook[0].values())
    phonebook[0].keys()
    ','.join(phonebook[0].keys())
    ','.join(phonebook[0].values())

    uploadlist = []
    for i in range(len(phonebook)):
        uploadlist.append(','.join(phonebook[i].values()))
        '\n'.join(uploadlist)
    

    with open('lab23csv.csv', 'r') as file
        file.write('\n'.join(uploadlist)





# print(phonebook[1]['favorite sport'])
    
# def picknpull():
#     sherlockuser = input('Who are you looking for?: ')
#     for person in phonebook:
#         if person['name'] == sherlockuser:
#             print(person)
# always define a new function for each step in CRUD
# remember keys are stored in keytool
# don't overthink how to put keys and values together

def newentry():
    sherlocknew = input('Who would you like to add?: '),input('What is their favorite show?: '),input('What is their favorite sport?: ')
    
    sherlockadded = dict(zip(keytool,sherlocknew))
   
    phonebook.append(sherlockadded)
   
    # for name in 'names':
    #     zip(val.append(sherlockwho))
    # for show in 'favorite show':
    #     zip(val.append(sherlockshow))
    # for sport in 'facorite sport':
    #     zip(val.append(sherlocksport))














    