import os
#from tkinter import Tk
#from tkinter.filedialog import askdirectory
#path = askdirectory()

os.chdir('../Desktop/First Test')
path = os.walk('.')

def audio_lister(path):
    audios = []
    for root, dirs, files in path:
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

def average_size(size):
    total_size = 0
    for root, dirs, files in os.walk(start_path):
        for f in files:
            fp = os.path.join(root, f)
            if not os.path.islink(fp):
                total_size += os.path.getsize(fp)
    return total_size

audio_files = audio_lister(path)
print(audio_files)
print(get_size())

# size of given directory
num_bytes = get_size()
num_mb = (num_bytes / 1000000)













