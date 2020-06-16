import random as r

def name(baby):
    prefix_list = ["Da","Ka","Sha","Ma","Gla","Tre","Ru","Tu","Sue","Fo","Jo","Jenny"]
    suffix_list = ["ren","ana","lyn","da","ra","bu","bob","role","tana","nissa","aqua"]
    prefix = r.choice(prefix_list)
    suffix = r.choice(suffix_list)
    name = prefix+suffix
    baby["name"] = name
    return baby

def birth():
    new_jack = {"age":0,"pregnant":False}
    new_jack = name(new_jack)
    genitals = r.randint(1,2)
    if genitals == 1:
        new_jack["sex"] = "f"
    elif genitals == 2:
        new_jack["sex"] = "m"
    return new_jack

def aging_jacks(pop):
    new_list = []
    for jack in pop:
        jack["age"] += 1
        new_list.append(jack)
    return new_list


#Sometimes line 35 throws an index error, saying the list index is out of range... I'm not sure why, because it should refer to list index 1.
def jack_off(pop):    
    for i, jack in enumerate(pop):
        if 4 <= jack["age"] <= 8 and jack["sex"] == "f":
            if i == 0:
                if pop[i+1]["sex"] == "m" and 4 <= pop[i+1]["age"] <= 8:
                    pop[i]["pregnant"] = True                
            elif i == len(pop)-1:
                if pop[i-1]["sex"] == "m" and 4 <= pop[i-1]["age"] <= 8:
                    pop[i]["pregnant"] = True                
            elif pop[i-1]["sex"] == "m" and 4 <= pop[i-1]["age"] <= 8 or pop[i+1]["sex"] == "m" and 4 <= pop[i+1]["age"] <= 8:
                pop[i]["pregnant"] = True
    return pop    

def miracle_of_life(pop):
    for jack in pop:
        if jack["pregnant"] == True:
            crotch_goblin = birth()
            pop.append(crotch_goblin)
            jack["pregnant"] = False  
    return pop          
        
def old_yeller(pop):
    new_pop = []
    for jack in pop:
        if jack["age"] < 10:
           new_pop.append(jack)
    return new_pop 

num_years = 0
jackalopes = [{"name":"Adam","age": 0, "sex": "f","pregnant":False},{"name":"Steve","age":0,"sex":"m","pregnant":False}]
scope = 10

print("start\n\n\n")
while len(jackalopes) < scope:
    print("Happy New Year!")
    jackalopes = miracle_of_life(jackalopes)
    print(jackalopes)
    jackalopes = jack_off(jackalopes)
    print(jackalopes)
    jackalopes = old_yeller(jackalopes)
    print(jackalopes)
    jackalopes = aging_jacks(jackalopes)
    print(jackalopes)
    r.shuffle(jackalopes)
    if len(jackalopes) == 0:
        break
        
    num_years += 1

if len(jackalopes) == 0:
    print("all the jackalopes are dead")
else:
    print(f"it took {num_years} years to reach {scope} jackalopes")








    




