""" Write a function to put an element from words.txt to list
"""

import time

def words_list_1(file):
    word_list=[]
    fh=open(file)
    for line in fh:
        word=line.strip()
        word_list.append(word)
    return word_list

def words_list_2(file):
    word_list=[]
    fh=open(file)
    for line in fh:
        word=line.strip()
        word_list=word_list+[word]
    return word_list

start_time=time.time()
word_list=words_list_1("words.txt")
elapsed_time=time.time()-start_time

print (len(word_list))
print (word_list[:10])
print (elapsed_time, "seconds")

start_time=time.time()
word_list=words_list_2("words.txt")
elapsed_time=time.time()-start_time

print (len(word_list))
print (word_list[:10])
print (elapsed_time, "seconds")

