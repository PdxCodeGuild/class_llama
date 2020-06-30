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

    def draw(self):
        screen.blit(self.img,(self.x,self.y))

class Varmint:
    def __init__(self,x,y):
        self.name = self.baby_name()
        self.age = 0
        self.pregnant = False
        self.sex = self.chromosomer()
        self.x = x
        self.y = y
        self.x_move = 0
        self.y_move = 0
        self.img = pygame.image.load("rabbit.png")
        self.awareness = 50

    def __repr__(self):
        return f"Name: {self.name}\nSex: {self.sex}\nAge: {self.age}\nPregnant? {self.pregnant}"

    #names the varmint
    def baby_name(self):
        prefix_list = ["Da","Ka","Sha","Ma","Gla","Tre","Ru","Ron","Tu","Sue","Fo","Jo","Jenni","Po","Minni","Deli","Aissa","Mai","Jeze","Ja","Sa","Diy","Ami","Sala","Oli","Dem","Li","Ev","Ah","Moha","Ahme","Kaja","Na","Jona","Regi","Sher","A","Sa","Ma","Ta","Shel","Wil","Rag","Ud","Uth","Aga","Ab","Dah","Bre"]
        suffix_list = ["ren","ron","ana","lyn","da","paul","ra","bu","bob","role","tana","nissa","aqua","ray","lah","tou","mouna","bel","din","ya","nata","ba","med","lith","a","vi","via","ver","than","nald","lock","sha","ley","son","nar","red","tha","dou","by","lia","ria","von","onna","doul","mad"]
        prefix = r.choice(prefix_list)
        suffix = r.choice(suffix_list)
        name = prefix+suffix
        return name

    #determines the sex of the varmint
    def chromosomer(self):
        genitals = r.randint(1,2)
        if genitals == 1:
            sex = "female"
        elif genitals == 2:
            sex = "male"
        return sex
    
    #this method is probably not necessary and will likely be deleted
    def age_up(self):
        self.age+=1

    #draws the varmint on the screen
    def draw(self):
        screen.blit(self.img,(self.x,self.y))

    #randomly decides which direction the varmint wants to travel in
    def choose_path(self):
        self.x_move = r.randint(-3,3)
        self.y_move = r.randint(-3,3)

    def move(self):
        #moves the varmints according to their randomly chosen path. Execute this once per loop
        self.x +=self.x_move
        self.y +=self.y_move
        if self.x > 960 or self.x <0:
            self.x_move*=-1
        if self.y > 640 or self.y <0:
            self.y_move*=-1

    #determines how far away an object is from the varmint
    def proximity(self,target):
        distance = math.sqrt((math.pow(self.x-target.x,2))+(math.pow(self.y-target.y,2)))
        return distance

    #determines whether a varmint is occupying the same space as an object
    def adjacent(self,target):
        distance = self.proximity(target)
        if distance < 10:
            return True
    
    def move_toward(self,target):
        #while self.x != target.x or self.y != target.y:
        if self.x > target.x:
            self.x_move = -3
        elif self.x < target.x:
            self.x_move = 3
        if self.y > target.y:
            self.move_y = -3
        elif self.y < target.y:
            self.move_y = 3
                    
        


def main():
    #Setting a timer to go off every 4 seconds; each time the timer ticks, this will indicate 1 in-simulation year and will trigger various events
    pygame.time.set_timer(pygame.USEREVENT,4000)
    year_counter = 0

    #Creates a bunch of grass and varmints at random points
    varmint_list = []
    for i in range(48):
        varm = Varmint(r.randint(0,920),r.randint(0,600))
        varmint_list.append(varm)
    for varm in varmint_list:
        varm.choose_path()
    plant_list = []
    for i in range(16):
        plant = Grass(r.randint(0,920),r.randint(0,600))
        plant_list.append(plant)    

    

    running = True
    while running:
        

        screen.fill((0,0,0))
        screen.blit(background,(0,0))

        #All events go in this for loop
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.USEREVENT:
                year_counter+=1
                print(f"Happy new year! {year_counter}")
                for varm in varmint_list:
                    varm.age+=1
                    
        
        #figures out which plants the varmint is aware of; then the varmint moves toward the closest one; then eats it
        #nearby_plants = {}
        for varm in varmint_list:
            for plant in plant_list:
                prox = varm.proximity(plant)
                eat = varm.adjacent(plant)
                if eat == True:
                    plant_list.remove(plant)
                    del plant    
                elif prox < varm.awareness:
                    varm.move_toward(plant)
                    
            #this code was supposed to create a sorted dictionary of nearby plants and then have the varmint go toward the closest one... but it didn't work        
            ''' nearby_plants[plant]=prox
            food = sorted(nearby_plants,key=nearby_plants.get)
            if nearby_plants != {}:
                varm.move_toward(food[0]) '''   
            
            #moves varmints according to their AI
            varm.move()

            #refreshes varmints in their new spot
            varm.draw()

            #kills old varmints
            if varm.age > 9:
                varmint_list.remove(varm)
                del varm
                
        #refreshes the plant
        for plant in plant_list:
            plant.draw()

        plant = Grass(r.randint(0,920),r.randint(0,600))
        plant_list.append(plant)

        pygame.display.update()

if __name__ == "__main__":
    main()