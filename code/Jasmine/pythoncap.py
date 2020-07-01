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

dir(my_image) #lists out all the 
print(dir(my_image))


#convert list of image stats to create a keys:values dict (k eys would dir() and tags would be values)
# dir() == keys,  my_image[tag] == values
def convert(): 
    tag_list = []
    for tag in dir(my_image):  #returns all the metadata of the image
        if tag not in ['_exif_ifd_pointer' , '_segments' , 'custom_rendered' , 'compression' , 'get' , 'get_file' , 'get_thumbnail' , 'delete' , 'delete_all' , 'datetime_digitized' , 'datetime_original' , 'exif_version' , 'has_exif' , 'offset_time' , 'rescommended_exposure_index' , 'resolution_unit' , 'scene_capture_type' , 'lens_specification' , 'metering_mode' , 'subsec_time_digitized' , 'subsec_time_original']: #
            tag_list.append(tag)
    imagemeta_dict = {}
    for tag in tag_list: 
        imagemeta_dict[tag] = my_image[tag]
    print(imagemeta_dict)


convert()

metadata = []






    
    

