print ("Write a function called nested_sum that takes a nested list of integers and add up the elements from all of the nested lists.")

whole_list=[1,2,3,[1,2,3,4],[2,4,5,6],[3,4,5,6,66]]


def nested_sum(list_v):
    sum_list=[]
    for e in whole_list:
        if type(e) is list:
            sum_list.append(sum(e))
    return sum_list


print(nested_sum(whole_list))
 