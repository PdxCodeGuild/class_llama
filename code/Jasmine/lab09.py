''' 
Unit Conversion

''' 

units = {"ft" : 0.3048 ,
"mi" : 1609.34 , 
"m" : 1 , 
"km" : 1000 , 
"yd" : .9144 , 
"inch" : .0254}

num = int(input("what is the distance?"))
unit = input("what it is the unit of measurement?")
unit_2 = input("what would you like to convert to?")
#num = num * units[unit]
#print(num)


unit = num/units[unit_2]
print(unit)
