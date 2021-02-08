""" print dictionary keys in order
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

#list_s=list(s)
#list_s.sort()
#print (list_s)

d=histogram(s)
list_k=list(d.keys())
list_k.sort()
for k in list_k:
    print(k)
    
        