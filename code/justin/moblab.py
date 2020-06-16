# # Jackalope


def aging_jacks(x):
    new_list = []
    for jack in x:
        jack += 1
        new_list.append(jack)   
    
    return new_list
    


# NEEDS WORK
def new_jacks(old):
    offspring = [0, 0]
    
    for jacks in old:
        if jacks >=4 and jacks <=8:
            old.extend(offspring)
            print(old)



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




