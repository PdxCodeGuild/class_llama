"""
The goal is to calculate how many years it will take for two jackalopes to create a population of 1000.

    Jackalopes are reproductive from ages 4-8 and die at age 10.
    Gestation is instantaneous. Each gestation produces two offspring.
    Jackalopes are hermaphrodites, it takes a pair to reproduce, but any pair will do

With these conditions in mind, we can represent our population as a list of ints.

Version 2: 
Now let's give the jackalopes distinct sexes and extend their gestation period to one year. We can represent each jackalope with a dictionary, thus our population will be a list of dictionaries. A jackalope will have the following properties:

name
age
sex
whether they're pregnant
Jackalopes can only mate with those immediately around them. Every generation Jackalopes are randomly shuffled.
"""
import random 

# initialize age
age = 0

# initialize years
year = 0

# jack_xx = female 
# jack _xy = male 
# initialize jackalope count and list

jackalope = [0,0]
jackalope_count = len(jackalope)
jack_babies = [0]


# conditional statement to compare age to reproduction
# increase age every year by adding one to the age 
#jack_age = [x + 1 for x in jackalope]
#print(jack_age)

while jackalope_count <= 1000:
    mate_counter = 0
    jackalope_count = len(jackalope)

    for jack in jackalope: 
    
        if jack >= 4 and jack <= 8: # offspring produced between ages 4 - 8 , produce heir and add a year age
            mate_counter += 1                      
              
    jack_pop = jackalope.count(10)
   # print(jack_pop)
    # removing 10 from the list
    for jack in range(0, jack_pop): 
        jackalope.remove(10)
        

# total number of mates divided by two, multiply by two for total number of babies produced
    jack_babies = mate_counter // 2 * 2  
    for x in range(jack_babies):
        jackalope.append(0)
    
    jackalope = [x + 1 for x in jackalope]

    year += 1 
    
    
   
        

    print(jackalope)
    print("Jackalope population:" , jackalope_count)
    print("Years:" , year)
     

        
        
 