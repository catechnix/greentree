""" walk function in os package
"""

import os

def walk(dirname):
    """prints the names of all files in the dirname and its subsdirectories.
    """
    for name in os.listdir(dirname):
        path = os.path.join(dirname, name)

        if os.path.isfile(path):
            print (path)
        else:
            walk(path)
         
def walk2(dirname):
    """prints the names of all files in dirname and its subdirectories
    """
    for root, dirs, files in os.walk(dirname):
        for filename in files:
            print (os.path.join(root, filename))

if __name__ =="__main__":
    #for (root, dirs, files) in os.walk('greentea', topdown=True):
    #   print(root)
    #  print(dirs)
    # print(files)

    walk('.')
    walk2('.')