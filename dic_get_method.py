"""
Use dictionary get method to create a histogram function
"""
"""
def histogram(s):
    d = dict()
    for c in s:
        if c not in d:
            d[c] = 1
        else:
            d[c] += 1
    return d

"""
def histogram(s):
    d=dict()
    for c in s:
       print(d.get('c',0))
        
    return d

if __name__=='__main__':
    h=histogram('cdbefgefefeds')
    print(h)

    