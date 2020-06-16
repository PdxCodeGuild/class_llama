"""
The goal is to calculate how many years it will take for two jackalopes to create a population of 1000.

    Jackalopes are reproductive from ages 4-8 and die at age 10.
    Gestation is instantaneous. Each gestation produces two offspring.
    Jackalopes are hermaphrodites, it takes a pair to reproduce, but any pair will do

With these conditions in mind, we can represent our population as a list of ints.
"""

# initialize age
age = 0

# initialize years
year = 0

# initialize jackalope count and list

jackalope = [4,10]
jackalope_count = len(jackalope)



# conditional statement to compare age to reproduction
# increase age every year by adding one to the age 
#jack_age = [x + 1 for x in jackalope]
#print(jack_age)

while jackalope_count <= 1000:
    mate_counter = 0

    for jack in jackalope: 
    
        if jack >= 4 and jack <= 8:    # ages not producing offspring and a year 
            mate_counter += 1                         
              
    jack_pop = jackalope.count(10)
    print(jack_pop)
    # removing 10 from the list
    for jack in range(0, jack_pop): 
        jackalope.remove(10)
        print(jackalope)
# # offspring produced between ages 4 - 8 , produce heir and add a year age
        #for i in the range 
        
    print()


# jackalopes = [0,0]
# jackalopes = [1,1] year + 1
# jackalopes = [2,2] year + 2

# jackalopes = [0,0,4,4] year + 4
# jackalopes = [0,0,1,1,5,5]

# length