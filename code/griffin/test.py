class Point:
    def __init__(self,x,y): #this is the initializer
        self.x = x #these are member variables
        self.y = y

    def distance(self, p):
        dx = self.x - p.x
        dy = self.y - p.y
        return math.sqrt(dx*dx + dy*dy)

    def scale(self,v):
        self.x *= self.y *= v


p = Point(5,2) # calls initializer. instantiates class
print(p.x)
print(p.y)

print(type(p))