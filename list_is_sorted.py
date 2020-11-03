print("Write a function called is_sorted that takes a list as a parameter and returns True if the list is sorted in ascending order and False otherwise.")

def is_sorted(new_list):
    for i in range(len(new_list)-1):
        if new_list[i]> new_list[i+1]:
            return False
    return True


#result=is_sorted(["a","b","c"])
result=is_sorted(["a","d","c"])
print(result)

