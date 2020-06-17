from PIL import Image
import colorsys

img = Image.open("lenna.png") # must be in same folder
width, height = img.size
pixels = img.load()



def greyscale():
    for i in range(width):
        for j in range(height):
            r, g, b = pixels[i, j]

            y = int(0.299*r + 0.587*g + 0.114*b)
            r = y
            g = y
            b = y

            pixels[i, j] = (r, g, b)

    
    img.show()

greyscale()
