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
## STEP TWO - Convert image rgb values to array
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

'''# import modules
from PIL import Image

# create blank background
img = Image.new("RGB", (1200,1080), color="green")
# img.show() # TEST: pass - green background displayed 400x400

# save as 'green_bg
img.save("./img/green_bg.png")
# img.show() # TEST: pass - green_bg saved to location

# define x,y and offset 
x,y = img.size
offset = x // 10, y // 7

# paste image onto 
img.paste(Image.open("./img/Gnome_G017_HD_NoLogo.png").resize((200,200)), offset)
img.show()'''

#----------------------------------------------------------------------------#
## STEP FIVE - Paste multiple images on top of each other using loop
#----------------------------------------------------------------------------#
# import modules
from PIL import Image
import random

bg = Image.new("RGBA", (1200,800), (255, 255, 255, 255))
bg_w, bg_h = bg.size

# load the image
img = Image.open("./img/Gnome_G017_5K_NoLogo.png").resize((400,400))
img_w, img_h = img.size

for i in range(10):
    x = random.randint(200, 200)
    y = random.randint(200, 200)
    img2 = Image.open("./img/new_img.png").resize((x,y))
    img2_w, img2_h = img2.size

    offset = ((bg_w - img_w) // 2, (bg_h - img_h) // 2)
    offset2 = ((img_w - img2_w) // 2, (img_h - img2_h) // 2)
    
    img2.paste(img2, offset2)
    img2.save("./img/new_img.png")
img2.show()































# import random, math

# # create blank white background
# bg = Image.new("RGB", (1280,920), color="white")
# bg_w, bg_h = bg.size
# # img.show() # TEST: pass - green background displayed 400x400

# # save as 'white_bg
# bg.save("./img/white_bg.png")
# # bg.show() # TEST: pass - white_bg saved to location

# # # equation to start img in center
# offset = ((bg_w - img_w) // 2, (bg_h - img_h) // 2) 




# # paste image onto 
# img.paste(Image.open("./img/Gnome_G017_HD_NoLogo.png").resize(((200+1),(200+i))), offset)
# img.show()


#----------------------------------------------------------------------------#
## STEP SIX - Define function for 'STEP FIVE' and recursively call loop
#----------------------------------------------------------------------------#