"""
compared two sorted arrays and return one that combining the two arrays 
into one which is also sorted, can't use sort function
"""

array1=[0,3,2,1,6]
array2=[1,2,4,5]
print(array2)

for i in array1:
    if i not in array2:
        array2.append(i) 
        
print(array2)



array3=[]
while array2:
    minimum = array2[0]  # arbitrary number in list 
    for x in array2: 
        if x < minimum:
            minimum = x
    array3.append(minimum)
    array2.remove(minimum)    


print(array3)
