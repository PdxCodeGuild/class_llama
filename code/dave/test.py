class Point:
	def __init__(self, x, y): # this is the initializer
		self.x = x #these are member variables
		self.y = y

x = input("x: ")
y = input("y: ")

p = Point(x,y) # call initializer, instanciate the class
print(p.x) #5
print(p.y) #2

print(type(p)) # Point
