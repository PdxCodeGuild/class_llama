import colorsys
from PIL import Image
from PIL import ImageDraw

# must be in same folder
img = Image.open("lenna_image.png") 
width, height = img.size
pixels = img.load()

for i in range(width):
    for j in range(height):
        r, g, b = pixels[i, j]

        Y = int(0.299*r + 0.587*g + 0.114*b)

        pixels[i, j] = (Y, Y, Y)

img.show()

def hd_color():
    

    for i in range(width):
        for j in range(height):
            r, g, b = pixels[i, j]        
            
            # colorsys uses colors in range [0, 1]
            h, s, v = colorsys.rgb_to_hsv(r/255, g/255, b/255)

            # math at pixels
            h = h/2
            s = s * 2
            v = v*1.3 
                         
            r, g, b = colorsys.hsv_to_rgb(h, s, v)        
            
            # convert back to [0, 255]                     
            r = int(r*255)
            g = int(g*255)
            b = int(b*255)        
            
            pixels[i, j] = (r, g, b)
        
    img.show()

    
def get_creative():
    width = 500
    height = 500

    img = Image.new('RGB', (width, height))
    draw = ImageDraw.Draw(img)
    # the origin (0, 0) is at the top-left corner

    draw.rectangle(((0, 0), (width, height)), fill="yellow")

    
    color = ["256", "128", "128"]

    for color in range(color):

    # draw a line from x0, y0, x1, y1
        circle_x = width/2
        circle_y = height/4
        circle_radius = 50
        draw.ellipse((circle_x-circle_radius, circle_y-circle_radius, circle_x+circle_radius, circle_y+circle_radius), fill='lightgreen')

    draw.line((circle_x,circle_y,width/3,height*.55), fill ="lightblue", width = 12)
    draw.line((width/4,height/2,width*.75,height/3), fill = "lightblue", width = 12)
    draw.line((width/2,height*.75, width/3,height*.9), fill = "lightblue", width = 15)
    draw.line((width/2,height*.75, width *.76,height*.9), fill = "lightblue", width = 15)

    img.show()

get_creative()