with open('medieval contacts.csv', 'r') as file:
    lines = file.read().split('\n')
    print(lines)

dict_list = []

for line in lines:
    temp_list = line.split(",")
    temp_dict = {}
    for line in temp_list:
        very_temp_list = line.split(":")
        temp_dict[very_temp_list[0]] = very_temp_list[1]
    dict_list.append(temp_dict)

print(dict_list)
    