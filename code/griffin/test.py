class Point:
    def __init__(self,x,y): #this is the initializer
        self.x = x #these are member variables
        self.y = y

p = Point(5,2) # calls initializer. instantiates class
print(p.x)
print(p.y)

print(type(p))