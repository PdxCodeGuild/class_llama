from PIL import Image
import numpy
import cv2

n = numpy.arange(27)

n.reshape(3,3,3)

m = numpy.asarray(([[123, 12, 123, 12, 33],[],[]]))
type(m)

# img = Image.open("./square.png")

# img_array = numpy.array(img)



'''
## TEST 1: fail - ValueError: cannot copy sequence with size 3 to array axis with dimension 2
im = Image.open("square.png")

# create numpy array
np_im = numpy.array(im)

# iterate through array to create fractal pattern
for x in range(510):
    for y in range(512):
        np_im[x][y] = [255,255,255] # Error is thrown here. asks for 3 params when only 2 are present 

np_im[510][512] = [0,0,0]

for i in range(3):
    for x in range(510):
        for y in range(512):
            if np_im[x][y][0] == 0:
                np_im[x-(1*(3**i))][y] = [0,0,0]
                np_im[x][y-(1*(3**i))] = [0,0,0]
                np_im[x-(2*(3**i))][y] = [0,0,0]
                np_im[x][y-(2*(3**i))] = [0,0,0]
                np_im[x-(1*(3**i))][y-2] = [0,0,0]
                np_im[x-(2*(3**i))][y-(1*(3**i))] = [0,0,0]
                np_im[x-(2*(3**i))][y-(2*(3**i))] = [0,0,0]

new_im = Image.fromarray(np_im)
new_im.save("fractal.png")'''