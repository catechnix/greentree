""" Search a word in a list, use bisect/binary Search
"""

from bisect import bisect_left


#filename='words.txt'
def convert_list():
    word_list=[]
    fh=open('words.txt')
    for line in fh:
        word=line.strip()
        word_list.append(word)
        return word_list

def bisect_search(list_w,w):
    list_w.sort()
    for i in range(len(list_w)-1):
        if w==list_w[i]:
            print(i)

# bisect_search(word_list,"aal")

""" to check if a word is in a list using bisect_left,
    the list has to be sorted
"""

def in_bisect(word_list,w):
    i=bisect_left(word_list,w)
    if i !=len(word_list) and word_list[i]==w:
        return True
    else:
        return False

if __name__ == '__main__':
    
    word_list=convert_list()

    for word in ['alien','allen']:
        print (word, 'in list', in_bisect(word_list, word))




        

    