"""
This program converts an image into greyscale using the Pillow library, which is a fork of PIL 'python image library'.
"""

from PIL import Image
img = Image.open("./national-geographic-best-photo-winner.jpeg") # must be in same folder
width, height = img.size
pixels = img.load()

for i in range(width):
    for j in range(height):
        r, g, b = pixels[i, j]

        Y = int(0.299*r + 0.587*g + 0.114*b)

        pixels[i, j] = (Y, Y, Y)

img.show()