# Jackalope



def aging_jacks(x):
    new_list = []
    for jack in x:
        jack += 1
        new_list.append(jack)   
    
    return new_list
    

def new_jacks(x):
    offspring = [0, 0]
    for jacks in x:
        if jacks >= 4 and jacks <= 8 and jacks%2 == 0:
            [x.extend(offspring) for jacks in x]
    return x

def old_yeller(x):

    for jacks in x:
        if jacks == 10:
            x.remove(jacks)
    return x


total_jacks = [0, 0]
num_years = 0

# while loop to get to 1000
# variable pop, while pop < 1000
while len(total_jacks) < 10:

    babies = new_jacks(total_jacks)

    deceased = old_yeller(total_jacks)

    total_jacks = aging_jacks(total_jacks)

    num_years += 1
    
    print(total_jacks)
    # print(num_years)




