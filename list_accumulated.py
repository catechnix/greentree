print ("write a function that takes a list and return a culmulative sum\n")

def culmulative_sum(list_num):
    
    list_sum=[]
    for i in range (len(list_num)):
        
        listsum=list_sum.append(sum(list_num[:i+1]))
    return list_sum

    
list_num=[1,3,4,3,5,6]
new_list=culmulative_sum(list_num)
print(new_list)