<<<<<<< HEAD
# Jackalope brought to you by Justin, Breanna, and Marcus

# function to age jacks by one year
def aging_jacks(x):
    new_list = []
    for jack in x:
        jack += 1
        new_list.append(jack)   
    
    return new_list
    

# function to make new jacks when their age is between 4 and 8
def new_jacks(old):
    offspring = [0]
    
    return [old.extend(offspring) for jacks in old if jacks >= 4 and jacks <= 8]


# function to kill off jacks that are older than 10
def old_yeller(x):
    return [jack for jack in x if jack < 10]



total_jacks = [0, 0]
num_years = 0

# put it all together y'all
while len(total_jacks) < 1000:

    total = new_jacks(total_jacks)

    total_jacks = old_yeller(total_jacks)

    total_jacks = aging_jacks(total_jacks)

    num_years += 1
    
    print(total_jacks)
    print(num_years)

=======
# Jackalope brought to you by Justin, Breanna, and Marcus

# function to age jacks by one year
def aging_jacks(x):
    new_list = []
    for jack in x:
        jack += 1
        new_list.append(jack)   
    
    return new_list
    

# function to make new jacks when their age is between 4 and 8
def new_jacks(old):
    offspring = [0]
    
    return [old.extend(offspring) for jacks in old if jacks >= 4 and jacks <= 8]


# function to kill off jacks that are older than 10
def old_yeller(x):
    return [jack for jack in x if jack < 10]



total_jacks = [0, 0]
num_years = 0

# put it all together y'all
while len(total_jacks) < 1000:

    total = new_jacks(total_jacks)

    total_jacks = old_yeller(total_jacks)

    total_jacks = aging_jacks(total_jacks)

    num_years += 1
    
    print(total_jacks)
    print(num_years)

>>>>>>> f3d370e3e894e7aaa988237f1ebaade842a9680c
