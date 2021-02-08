"""
Modify reverse_lookup so that it builds and returns a list of all keys that map to v, 
or an empty list if there are none.
"""

s='abdbcdfafe'
def histogram(s):
    d=dict()
    for c in s:
        if c not in d:
            d[c]=1
        else:
            d[c] +=1
    return d

def reverse_lookup(d,v):
    list_keys=list()
    for k in d:
        if d[k] == v:
            list_keys.append(k)
        else:
            list_keys
    return list_keys
    

if __name__=='__main__':
    dict=histogram(s)
    li_keys=reverse_lookup(dict,3)
    print(li_keys)



