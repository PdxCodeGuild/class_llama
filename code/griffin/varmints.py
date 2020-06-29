import random as r
import pygame

pygame.init()

#Here is all the pre-game setup stuff
screen = pygame.display.set_mode((960,640))
background = pygame.image.load("grass background.png")
varmintImg = pygame.image.load("rabbit.png")



class Varmint:
    def __init__(self,x,y):
        self.name = self.baby_name()
        self.age = 0
        self.pregnant = False
        self.sex = self.chromosomer()
        self.x = x
        self.y = y
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


'''def draw_varmint(x,y):
    screen.blit(varmintImg,(x,y))'''

def main():
    

    testbunny = Varmint(500,300)

    running = True
    while running:
        screen.fill((0,0,0))
        screen.blit(background,(0,0))

        #All events go in this for loop
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        testbunny.draw()
        pygame.display.update()

if __name__ == "__main__":
    main()