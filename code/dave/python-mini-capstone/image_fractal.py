"""
This program performs the follow steps to create a fractal image:
    1. takes an image path uploaded from user
    2. resizes the image and stores it in an array as 'new_image'
    3. changes location of cursor
    4. resizes the 'new_image' and appends the array

    ref: https://www.codespeedy.com/convert-a-numpy-array-to-image-in-python/

    # keep trying different methods but failing. 

    # all test files are located in 'tutorials-and-tests section with comments
"""

#----------------------------------------------------------------------------#
## STEP ONE - Load Image
#----------------------------------------------------------------------------#

'''
This snippet loads the image, displays format,size,mode and then 
displays the image in a new window.

# import modules
from PIL import Image

# load image
img = Image.open("./img/Gnome_G017_5K_NoLogo.png")

# check details of image for testing
print(img.format)
print(img.size)
print(img.mode)

# display the image
img.show()
'''

#----------------------------------------------------------------------------#
## STEP TWO
#----------------------------------------------------------------------------#

'''
This snippet takes an image and stores its rgb values as n-dimensional array.
This allows for manipulation and storing of an image as a numpy array.

# import modules
from PIL import Image
from numpy import asarray

# load image
img2 = Image.open("./img/Gnome_G017_HD_NoLogo.png")

# convert img2 to numpy array and print the array
data = asarray(img2)

# get some info on the array
print(type(data)) # prints object type

# print shape of data
print(data.shape)

# print data array
print(data)
'''

#----------------------------------------------------------------------------#
## STEP (optional 1) - Convert to grayscale
#----------------------------------------------------------------------------#

'''
This snippet converts an image to grayscale

# import modules
from PIL import Image
import numpy as np

# load image and store in an array
img = np.array(Image.open('./img/Gnome_G018_5K_NoLogo.png').convert('L')) # can pass multiple arguments on same line

# print the type of object 'img'
print(type(img))

#create grayscale version
gr_img = Image.fromarray(img).save('gr_Gnome_G018_5K_NoLogo.png')
'''

#----------------------------------------------------------------------------#
## STEP THREE - Resizing image
#----------------------------------------------------------------------------#

'''
This snippet resizes

# import modules
from PIL import Image
import numpy as np

# load and resize the image in one line and print new shape
img_new_rz = np.array(Image.open('./img/Gnome_G018_5K_NoLogo.png').resize((400,400)))
print(img_new_rz.shape)
'''

#----------------------------------------------------------------------------#
## STEP FOUR - Image on top of another image
#----------------------------------------------------------------------------#

# import modules



