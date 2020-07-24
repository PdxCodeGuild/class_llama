import os

#from tkinter import Tk
#from tkinter.filedialog import askdirectory
#path = askdirectory()

os.chdir('../Desktop/First Test')
path = os.walk('.')

def audio_lister(start_path = '.'):
    audios = []
    for root, dirs, files in start_path:
        for f in files:
            if f.endswith(('.wav', '.aif')):
                audios.append(f)
    return audios

def get_size(start_path = '.'):
    total_size = 0
    for root, dirs, files in os.walk(start_path):
        for f in files:
            fp = os.path.join(root, f)
            if not os.path.islink(fp):
                total_size += os.path.getsize(fp)
    return total_size

def average_size(files, size, units):
    num_files = int(len(files))
    if units == 'gb':
        converted_size = size / 1000000000
    elif units == 'mb':
        converted_size = size / 1000000
    average = (int(converted_size) / num_files)
    print(f'The average size per file is {int(average)} {units}')

audio_files = audio_lister(path)
num_bytes = get_size()

def convert_units(num, units):
    if units == 'gb':
        print(f'This folder contains {int(num / 1000000000)} GB of audio files.')
    elif units == 'mb':
        print(f'This folder contains {int(num / 1000000)} MB of audio files.')
    

units = input('Units in MB or GB?: ').lower()
convert_units(num_bytes, units)
average_size(audio_files, num_bytes, units)












