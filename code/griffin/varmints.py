import random as r
import pygame
import math

pygame.init()

#Here is all the pre-game setup stuff
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

    def __repr__(self):
        return f"Name: {self.name}\nSex: {self.sex}\nAge: {self.age}\nPregnant? {self.pregnant}"

    def baby_name(self):
        prefix_list = ["Da","Ka","Sha","Ma","Gla","Tre","Ru","Ron","Tu","Sue","Fo","Jo","Jenni","Po","Minni","Deli","Aissa","Mai","Jeze","Ja","Sa","Diy","Ami","Sala","Oli","Dem","Li","Ev","Ah","Moha","Ahme","Kaja","Na","Jona","Regi","Sher","A","Sa","Ma","Ta","Shel","Wil","Rag","Ud","Uth","Aga","Ab","Dah","Bre"]
        suffix_list = ["ren","ron","ana","lyn","da","paul","ra","bu","bob","role","tana","nissa","aqua","ray","lah","tou","mouna","bel","din","ya","nata","ba","med","lith","a","vi","via","ver","than","nald","lock","sha","ley","son","nar","red","tha","dou","by","lia","ria","von","onna","doul","mad"]
        prefix = r.choice(prefix_list)
        suffix = r.choice(suffix_list)
        name = prefix+suffix
        return name

    def chromosomer(self):
        genitals = r.randint(1,2)
        if genitals == 1:
            sex = "female"
        elif genitals == 2:
            sex = "male"
        return sex
    
    def age_up(self):
        self.age+=1

    def draw(self):
        screen.blit(self.img,(self.x,self.y))

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

    def proximity(self,target,awareness):
        distance = math.sqrt((math.pow(self.x-target.x,2))+(math.pow(self.y-target.y,2)))
        if distance < awareness:
            return True
    
    def move_toward(self,target):
        #while self.x != target.x or self.y != target.y:
        if self.x > target.x:
            self.x_move = -3
        if self.x < target.x:
            self.x_move = 3
        if self.y > target.y:
            self.move_y = -3
        if self.y < target.y:
            self.move_y = 3
        '''if self.x == target.x and self.y == target.y:
            self.move_x = 0
            self.move_y = 0'''
            
        


def main():
    varmint_list = []
    for i in range(24):
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
        
        for varm in varmint_list:
            for plant in plant_list:
                prox = varm.proximity(plant,50)
                if prox == True:
                    varm.move_toward(plant)
                    
            varm.move()
            varm.draw()
        for plant in plant_list:
            plant.draw()

        pygame.display.update()

if __name__ == "__main__":
    main()