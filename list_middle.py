print("Write a function called middle that takes a list and returns a new list that contains all but the first and last elements. So middle([1,2,3,4]) should return [2,3].\n")

def middle(list_whole):
        del list_whole[0]
        del list_whole[-1]
        return list_whole

def middle_2(listwhole):
    listwhole.pop(0)
    listwhole.pop(-1)
    return listwhole

#new_list=middle([1,4,66,3,22,"a"])
new_list=middle_2([1,4,66,3,22,"a"])
print(new_list)