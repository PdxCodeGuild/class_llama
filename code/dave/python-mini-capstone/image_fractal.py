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
import time
import psutil

# bg = Image.new("RGBA", (1200,800), (255, 255, 255, 255))
# bg_w, bg_h = bg.size

# load the image
img = Image.open("./img/Gnome_G017_HD_NoLogo.png").resize((800,800))
img_w, img_h = img.size

def fractal_img():

    # load the image
    img = Image.open("./img/Gnome_G017_HD_NoLogo.png").resize((800,800))
    img_w, img_h = img.size

    for i in range(1,5):
        x = img_w // 2
        y = img_h // 2

        img2 = Image.open("./img/Gnome_G017_HD_NoLogo.png").resize((x,y))

        if i == 1:
            offset_tl = 0,0
            img.paste(img2, offset_tl)
            img.save("./img/new_image_file.png")
        elif i == 2:
            # pass
            offset_tr = img_w // 2, 0
            img.paste(img2, offset_tr)
            img.save("./img/new_image_file.png")
        elif i == 3:
            # pass
            offset_br = img_w // 2, img_h // 2
            img.paste(img2, offset_br)
            img.save("./img/new_image_file.png")
        elif i == 4:
            # pass
            offset_bl = 0, 400
            img.paste(img2, offset_bl)
            img.save("./img/new_image_file.png")
        else:
            break

        for j in range(1,5):
            x = x // 2
            y = y // 2

            img2 = Image.open("./img/Gnome_G017_HD_NoLogo.png").resize((x,y))

            if j == 1:
                offset_tl = 0,0
                img.paste(img2, offset_tl)
                img.save("./img/new_image_file.png")
            elif j == 2:
                # pass
                offset_tr = img_w // 2, 0
                img.paste(img2, offset_tr)
                img.save("./img/new_image_file.png")
            elif j == 3:
                # pass
                offset_br = img_w // 2, img_h // 2
                img.paste(img2, offset_br)
                img.save("./img/new_image_file.png")
            elif j == 4:
                # pass
                offset_bl = 0, 400
                img.paste(img2, offset_bl)
                img.save("./img/new_image_file.png")
            else:
                break

            for k in range(1,5):

                img2 = Image.open("./img/Gnome_G017_HD_NoLogo.png").resize((x,y))

                if k == 1:
                    offset_tl = 0,0
                    img.paste(img2, offset_tl)
                    img.save("./img/new_image_file.png")
                elif k == 2:
                    # pass
                    offset_tr = img_w // 2, 0
                    img.paste(img2, offset_tr)
                    img.save("./img/new_image_file.png")
                elif k == 3:
                    # pass
                    offset_br = img_w // 2, img_h // 2
                    img.paste(img2, offset_br)
                    img.save("./img/new_image_file.png")
                elif k == 4:
                    # pass
                    offset_bl = 0, 400
                    img.paste(img2, offset_bl)
                    img.save("./img/new_image_file.png")
                else:
                    break
    img.show()
    
    # display image for 5 seconds then kill after user hits enter
    


    # hide image once timer runs out
    for proc in psutil.process_iter():
        if proc.name() == "display":
            proc.kill()


fractal_img()



'''# Mandelbrot fractal
# FB - 201003254
from PIL import Image
# drawing area
xa = -2.0
xb = 1.0
ya = -1.5
yb = 1.5
maxIt = 255 # max iterations allowed
# image size
imgx = 512
imgy = 512
image = Image.new("RGB", (imgx, imgy))

for y in range(imgy):
    zy = y * (yb - ya) / (imgy - 1)  + ya
    for x in range(imgx):
        zx = x * (xb - xa) / (imgx - 1)  + xa
        z = zx + zy * 1j
        c = z
        for i in range(maxIt):
            if abs(z) > 2.0: break 
            z = z * z + c
        image.putpixel((x, y), (i % 4 * 64, i % 8 * 32, i % 16 * 16))

image.save("mandel.png", "PNG")'''


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