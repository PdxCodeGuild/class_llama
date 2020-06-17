from PIL import Image, ImageDraw
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



def hsvify():
    

    for i in range(width):
        for j in range(height):
            r, g, b = pixels[i, j]        
            
            # colorsys uses colors in the range [0, 1]
            h, s, v = colorsys.rgb_to_hsv(r/255, g/255, b/255)

            #doing math at pixels
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

    
def draw_something():
    width = 500
    height = 500

    img = Image.new('RGB', (width, height))

    draw = ImageDraw.Draw(img)


    # the origin (0, 0) is at the top-left corner

    draw.rectangle(((0, 0), (width, height)), fill="yellow")

    # using the color pink
    color = (256, 128, 128)  # pink

    # draw a line from x0, y0, x1, y1
    


    circle_x = width/2
    circle_y = height/4
    circle_radius = 50
    draw.ellipse((circle_x-circle_radius, circle_y-circle_radius, circle_x+circle_radius, circle_y+circle_radius), fill='lightgreen')

    draw.line((circle_x,circle_y,width/2,height*.65), fill ="lightgreen", width = 10)
    draw.line((width/4,height/2,width*.75,height/2), fill = "lightgreen", width = 10)
    draw.line((width/2,height*.65, width/3,height*.9), fill = "lightgreen", width = 10)
    draw.line((width/2,height*.65, width *.66,height*.9), fill = "lightgreen", width = 10)

    img.show()

draw_something()