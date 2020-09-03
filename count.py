def count(word, letter):
    count=0
    for char_a in word:
        if letter == char_a:
            count = count+1
    print (count)

#count("bannassra", "a")

def find (word, letter, index):
    while index<len(word):
        if word[index] == letter:
            print(index)
        index=index+1
    return -1

find ("bannadafdsaa","a",3)