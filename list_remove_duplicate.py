"""
Write a function called remove_duplicates that takes a list and returns a new list with 
only the unique elements from the original. Hint: they don’t have to be in the same order
"""

def remove_duplicates(duplicate_li):
    new_li=[]
    for i in range(len(duplicate_li)-1):
        if duplicate_li[i] not in duplicate_li[(i+1):]:
            new_li.append(duplicate_li[i])

    return new_li

unique_li=remove_duplicates(["a","b","a","b","c","c","d","e","f","g"])
print(unique_li)