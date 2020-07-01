'''
python capstone: 
use EXIF to collect metadata off of imported images
step one: pip install exif
step two: set up 
step three: 
''' 
from exif import Image
import csv

with open('IMG_7280.jpg' , 'rb') as image_file: 
    my_image = Image(image_file)

    my_image.has_exif
    True

dir(my_image)
print(dir(my_image))

for tag in dir(my_image):  
    if tag not in ['_exif_ifd_pointer' , '_segments' , 'custom_rendered' , 'compression' , 'get' , 'get_file' , 'get_thumbnail' , 'delete' , 'delete_all' , 'datetime_digitized' , 'datetime_original' , 'exif_version' , 'has_exif' , 'offset_time' , 'rescommended_exposure_index' , 'resolution_unit' , 'scene_capture_type' , 'lens_specification' , 'metering_mode' , 'subsec_time_digitized' , 'subsec_time_original']:
        print(tag , my_image[tag])

image_stats_dict = []

def convert(): 
    







    
    

