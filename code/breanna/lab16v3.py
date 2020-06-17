# Image Manipulation Version 3

from PIL import Image, ImageDraw


width = 500
height = 500

img = Image.new('RGB', (width, height))

draw = ImageDraw.Draw(img)

# white background
# the origin (0, 0) is at the top-left corner
draw.rectangle(((0, 0), (width, height)), fill="white")

# draw Sticky a head
circle_x = width/2
circle_y = height/2
circle_radius = 45
draw.ellipse((circle_x-circle_radius, circle_y-circle_radius, circle_x+circle_radius, circle_y+circle_radius), outline="red", fill=None)

# draw Sticky a body
draw.line([(250, 295), (250, 427)], fill="orange")

# draw Sticky some arms and legs
draw.line([(250, 345), (175, 300)], fill="yellow")
draw.line([(250, 345), (325, 300)], fill="green")

draw.line([(250, 427), (175, 500)], fill="blue")
draw.line([(250, 427), (325, 500)], fill="purple")

img.show()