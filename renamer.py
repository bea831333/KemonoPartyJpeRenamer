from os import listdir, walk, rename
from os.path import isfile, join
import sys, math
#usage: renamer.py <root folder that you want to start renaming jpe files>
#example: renamer.py "C:/folder/deeper folder"

# renames to 1.jpg, 2.jpg... 

def get_filenames(folder):
    return [f for f in listdir(folder) if isfile(join(folder, f))]
    
def rename_files(folder, files):
    file_count = len(files)
    if (file_count) > 0:
        filename = 1
        digits = int(math.log10(len(files)))+1
        for file in files:
            rename(join(folder, file), join(folder, str(filename).zfill(digits) + ".jpg"))
            filename += 1
    return

if __name__ == "__main__":
    target_folder = sys.argv[1]
    folders = [x[0] for x in walk(target_folder)]
    for folder in folders:
        files = get_filenames(folder)
        rename_files(folder, files)