# Jackalope

total_jacks = [0, 0]
num_years = 0


def mature_jacks(total_jacks):
    
    mature_jacks = 0
    
    for jacks in total_jacks:
        if jacks >= 4 and jacks <= 8:
            mature_jacks += 1
    
    print(mature_jacks)

def aging_jacks(total_jacks):
    
    for jacks in total_jacks:
        jacks += 1

def new_jacks(total_jacks):

    for num in range(len(total_jacks)):
        total_jacks.append(0)

    return total_jacks

def old_yeller(total_jacks):

    for jacks in total_jacks:
        if jacks == 10:
            total_jacks.remove(jacks)
        else:
            pass

# while loop to get to 1000
# variable pop, while pop < 1000
while len(total_jacks) < 1000:

    # for inside while, for jackelope in jackalopes
    for jacks in total_jacks:
        total_mature_jacks = mature_jacks(total_jacks)
        total_new_jacks = new_jacks(total_mature_jacks)
        goodbye_old_yeller = old_yeller(total_jacks)

    num_years += 1

print(num_years)


