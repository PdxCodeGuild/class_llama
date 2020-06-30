'''
python capstone: 
use EXIF to collect metadata off of imported images
step one: pip install exif
step two: set up 
step three: 
''' 
from exif import Image

with open('IMG_7280.jpg' , 'rb') as image_file: 
    my_image = Image(image_file)

    my_image.has_exif
    True

    #dir(my_image)

class exif.Image(self, image_file): 
    
    def dir(): 



    
    

