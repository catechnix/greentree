"""
Write a program that searches a directory and all of its subdirectories, recursively, 
and returns a list of complete paths for all files with a given suffix (like .mp3). 
Hint: os.path provides several useful functions for manipulating file and path names.
To recognize duplicates, you can use md5sum to compute a “checksum” for each files. 
If two files have the same checksum, they probably have the same contents.
To double-check, you can use the Unix command diff.
"""

import os
dir='/home/catechnix'
path_li=[]
def search_dir(dir):
    if os.path.isdir(dir):
        for name in os.listdir(dir): 
            new_dir= os.path.join(dir, name)
            #print(new_dir[-3:])
            if os.path.isfile(new_dir) and new_dir[-3:] == 'mp3':
                path_li.append(new_dir)
                print(new_dir)

        else:
            search_dir(new_dir)
search_dir(dir)
