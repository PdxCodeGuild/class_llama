import random as r
import pygame
import math

#Here is all the pre-game setup stuff
pygame.init()
screen = pygame.display.set_mode((960,640))
background = pygame.image.load("grass background.png")


class Grass:
    def __init__(self,x,y):
        self.x = x
        self.y = y
        self.img = pygame.image.load("grass.png")
        self.energy = 10

    def draw(self):
        screen.blit(self.img,(self.x,self.y))

class Animal:
    def __init__(self,x,y):
        self.name = self.baby_name()
        self.age = 0
        self.pregnant = False
        self.sex = self.chromosomer()
        self.x = x
        self.y = y
        self.awareness = 25
        self.start_energy = 10
        self.energy = 10
        self.metabolism = 3
        self.speed = 3
        self.libido = r.randint(10,30)

    #names the animal
    def baby_name(self):
        prefix_list = ["Da","Ka","Sha","Ma","Gla","Tre","Ru","Ron","Tu","Sue","Fo","Jo","Jenni","Po","Minni","Deli","Aissa","Mai","Jeze","Ja","Sa","Diy","Ami","Sala","Oli","Dem","Li","Ev","Ah","Moha","Ahme","Kaja","Na","Jona","Regi","Sher","A","Sa","Ma","Ta","Shel","Wil","Rag","Ud","Uth","Aga","Ab","Dah","Bre"]
        suffix_list = ["ren","ron","ana","lyn","da","paul","ra","bu","bob","role","tana","nissa","aqua","ray","lah","tou","mouna","bel","din","ya","nata","ba","med","lith","a","vi","via","ver","than","nald","lock","sha","ley","son","nar","red","tha","dou","by","lia","ria","von","onna","doul","mad"]
        prefix = r.choice(prefix_list)
        suffix = r.choice(suffix_list)
        name = prefix+suffix
        return name

    #determines the sex of the animal
    def chromosomer(self):
        genitals = r.randint(1,2)
        if genitals == 1:
            sex = "female"
        elif genitals == 2:
            sex = "male"
        return sex

    def die(self):
        self.sex = "none"
        self.speed = 0

    def __repr__(self):
        return f"Name: {self.name}\nSex: {self.sex}\nAge: {self.age}\nEnergy: {self.energy}\nPregnant? {self.pregnant}"

    #draws the animal on the screen
    def draw(self):
        screen.blit(self.img,(self.x,self.y))

    def move(self):
        #moves the animal according to their randomly chosen path. Execute this once per loop
        self.x +=self.x_move
        self.y +=self.y_move
        if self.x > 936 or self.x <24:
            self.x_move*=-1
        if self.y > 606 or self.y <24:
            self.y_move*=-1

    #determines how far away an object is from the varmint
    def proximity(self,target):
        #distance = math.sqrt((math.pow(self.x-target.x,2))+(math.pow(self.y-target.y,2)))
        distance_x = abs(self.x - target.x)
        distance_y = abs(self.y-target.y)
        distance = math.sqrt(pow(distance_x,2)+pow(distance_y,2))
        #print(distance)
        return distance

    #determines whether a varmint is occupying the same space as an object
    def adjacent(self,target):
        distance = self.proximity(target)
        if distance < 16:
            return True
    
    def move_toward(self,target):
        #while self.x != target.x or self.y != target.y:
        if self.x >= target.x:
            self.x_move = -1 * self.speed
        elif self.x <= target.x:
            self.x_move = self.speed
        if self.y >= target.y:
            self.y_move = -1 * self.speed
        elif self.y <= target.y:
            self.y_move = self.speed

    def move_away(self,target):
        #while self.x != target.x or self.y != target.y:
        if self.x >= target.x:
            self.x_move = self.speed
        elif self.x <= target.x:
            self.x_move = -1 * self.speed
        if self.y >= target.y:
            self.y_move = self.speed
        elif self.y <= target.y:
            self.y_move = -1 * self.speed

    def eat(self,a_list):
        for item in a_list:
            prox = self.proximity(item)
            eat = self.adjacent(item)
            if eat == True:
                self.energy+=item.energy
                a_list.remove(item) 
                del item    
            elif prox < self.awareness:
                self.move_toward(item)

    def mate(self,species_list):
        if self.sex == "female" and self.age >= 1 and self.energy >= (self.start_energy * self.libido/10):
            for v in species_list:
                if v.sex == "male" and v.age >= 1:
                    mateable = self.proximity(v)
                    if mateable < self.awareness:
                        self.pregnant = True
                        v.energy -= (v.energy/math.ceil(v.parental_investment))
                        self.energy += (v.energy/math.ceil(v.parental_investment))
                        break

   
                        
                        

class Predator(Animal):
    def __init__(self,x,y):
        super().__init__(x,y)
        self.img = pygame.image.load("fox.png")
        self.x_move = r.randint(-3,3)
        self.y_move = r.randint(-3,3)
        self.awareness = r.randint(50,100)
        self.start_energy = 10
        self.energy = 10
        self.speed = r.randint(3,6)
        self.metabolism = (self.speed/6) + (self.awareness/70)
        self.parental_investment = r.randint(10,20)
        self.libido = r.randint(10,30)  

    def mate(self,species_list):
        if self.sex == "female" and self.age >= 1 and self.energy >= (self.start_energy * self.libido/10):
            for v in species_list:
                if v.sex == "male" and v.age >= 1:
                    mateable = self.proximity(v)
                    if mateable < self.awareness:
                        self.pregnant = True
                        '''v.energy -= (v.energy/4)
                        self.energy += (v.energy/4)
                        break'''

       

class Varmint(Animal):
    def __init__(self,x,y, mom = None):
        super().__init__(x,y)
        self.img = pygame.image.load("rabbit.png")
        self.x_move = r.randint(-3,3)
        self.y_move = r.randint(-3,3)
        if mom == None:
            self.awareness = r.randint(40,80)
        else:
            self.awareness = r.randint(int(.75 * mom.awareness),int(1.25*mom.awareness))
        if mom == None:
            self.speed = r.randint(2,5)
        else:
            self.speed = r.randint(int(.75*mom.speed),int(1.25*mom.speed))  
        self.start_energy = 10
        self.energy = 10
        self.metabolism = (self.speed/6) + (self.awareness/70)
        if mom == None:
            self.parental_investment = r.randint(2,10)
        else:
            self.parental_investment = r.randint(int(.75*mom.parental_investment),int(1.25*mom.parental_investment))
        if mom == None:
            self.libido = r.randint(10,30)
        else:
            self.libido = r.randint(int(.75*mom.libido),int(1.25*mom.libido))

    

    


def main():
    #Setting a timer to go off every 4 seconds; each time the timer ticks, this will indicate 1 in-simulation year and will trigger various events
    NEW_YEAR = pygame.USEREVENT + 1
    pygame.time.set_timer(NEW_YEAR,4000)
    ENERGY_LOSS = pygame.USEREVENT + 2
    pygame.time.set_timer(ENERGY_LOSS,500)
    year_counter = 0

    #Creates a bunch of grass and varmints at random points
    varmint_list = []
    for i in range(60):
        varm = Varmint(r.randint(40,920),r.randint(40,600))
        varmint_list.append(varm)
    
    plant_list = []
    for i in range(60):
        plant = Grass(r.randint(40,920),r.randint(40,600))
        plant_list.append(plant)    

    predator_list = []
    for i in range(8):
        pred = Predator(r.randint(40,920),r.randint(40,600))
        predator_list.append(pred)

    running = True
    while running:
        screen.fill((0,0,0))
        screen.blit(background,(0,0))

        #All events go in this for loop
        for event in pygame.event.get():
            #Quits the simulation if the 'X' button in the top right corner is clicked
            if event.type == pygame.QUIT:
                running = False
            #Causes varmints and predators to lose some energy every .5 seconds, and if their energy is 0 or less, they die
            elif event.type == ENERGY_LOSS:
                for varm in varmint_list:
                    varm.energy -= varm.metabolism
                    
                    if varm.energy <= 0:
                        varmint_list.remove(varm)
                        del varm
                for pred in predator_list:
                    pred.energy -= pred.metabolism
                    
                    if pred.energy <= 0:
                        predator_list.remove(pred)
                        del pred
            #simulates 1 in-game year every 4 seconds            
            elif event.type == NEW_YEAR:
                year_counter+=1                
                print(f"Happy new year! {year_counter}")
                for varm in varmint_list:
                    
                    varm.age+=1
                    '''if varm.age >= 8:
                        varm.die()'''
                    
                    if varm.pregnant == True:                        
                        for n in range(r.randint(3,5)):
                            baby_varm = Varmint(varm.x,varm.y,varm)
                            varmint_list.append(baby_varm)
                            varm.energy -= varm.start_energy
                        varm.pregnant = False
                for pred in predator_list:
                    print(repr(pred))
                    
                    pred.age+=1
                    '''if pred.age >= 10:
                        pred.die()'''
                    if pred.pregnant == True:
                        for n in range(1):
                            baby_pred = Predator(pred.x,pred.y)
                            predator_list.append(baby_pred)
                            pred.energy -= pred.start_energy
                        pred.pregnant = False
                print(f"there are {len(varmint_list)} varmints and {len(predator_list)} predators")
                        
        #instructs varmints to eat and mate
        for varm in varmint_list:
            for pred in predator_list:
                danger = varm.proximity(pred)
                if danger < varm.awareness:
                    varm.move_away(pred)
            varm.mate(varmint_list)
            
            varm.eat(plant_list)
            
            
            #moves varmints according to their AI
            varm.move()

            #refreshes varmints in their new spot
            varm.draw()

        for pred in predator_list:
            pred.move()
            pred.mate(predator_list)
            if pred.energy <= 60:            
                pred.eat(varmint_list)
            pred.draw()

        #refreshes the plant
        for plant in plant_list:
            plant.draw()
            
        for n in range(1):
            plant = Grass(r.randint(40,920),r.randint(40,600))
            plant_list.append(plant)

        pygame.display.update()

if __name__ == "__main__":
    main()