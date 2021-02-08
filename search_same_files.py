"""
Write a program that searches a directory and all of its subdirectories, recursively, 
and returns a list of complete paths for all files with a given suffix (like .mp3). 
Hint: os.path provides several useful functions for manipulating file and path names.
To recognize duplicates, you can use md5sum to compute a “checksum” for each files. If two files have the same checksum, they probably have the same contents.
To double-check, you can use the Unix command diff.

"""

cmd='cd '