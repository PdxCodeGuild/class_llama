# Version 1

from PIL import Image
img = Image.open('./class_llama/code/justin/test_image.png')
width, height = img.size
pixels = img.load()

def greyscaler(img):
    for i in range(width):
        for j in range(height):
            r, g, b = pixels[i, j]
            y = int(0.299*r + 0.587*g + 0.114*b)
            r = y
            g = y
            b = y
            pixels[i, j] = (r, g, b)
    img.show()

greyscaler(img)