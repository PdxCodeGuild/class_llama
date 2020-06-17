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

    


hsvify()