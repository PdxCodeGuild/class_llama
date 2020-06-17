from PIL import Image
img = Image.open("c:/Users/Super/Desktop/PDXGUILD_Master/class_llama/code/marcus/Lenna.png") # must be in same folder
width, height = img.size
pixels = img.load()

for i in range(width):
    for j in range(height):
        r, g, b = pixels[i, j]

        Y = int(0.299*r + 0.587*g + 0.114*b)

        pixels[i, j] = (Y, Y, Y)

img.show()