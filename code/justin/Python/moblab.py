# # Jackalope


def aging_jacks(x):
    new_list = []
    for jack in x:
        jack += 1
        new_list.append(jack)   
    
    return new_list
    


# NEEDS WORK
def new_jacks(old):
    offspring = [0]
    return [offspring + jack for jack in old if jack>4 and jack<8]



def old_yeller(x):
    return [jack for jack in x if jack < 10]



total_jacks = [0, 0]
num_years = 0


while len(total_jacks) < 60:

    total = new_jacks(total_jacks)

    total_jacks = old_yeller(total_jacks)

    total_jacks = aging_jacks(total_jacks)

    num_years += 1
    
    print(total_jacks)
    # print(num_years)




