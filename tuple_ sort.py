"""
Write a function called most_frequent that takes a string and prints the letters in decreasing order of frequency.
"""

str='adbdfdfadfdsfa'
def most_frequent(str):
    
    d=dict()
    for c in str:
        if c not in d:
            d[c] =1
        else: 
            d[c] +=1
    print (d)
    # it is a tuple from d.items()
    c_freq=d.items() 
    c_freq_list=list(c_freq)
    print (c_freq_list) 
    return c_freq_list


t_char_list=most_frequent(str)

#t_char_list.sort(reverse=True)
t_char_list=sorted(t_char_list,key=lambda x:x[1], reverse=True)
for c, n in t_char_list:
    print (c,n)





