count=0
total_count=0
def has_no_e(words):
    for letter in words:
        if letter =="e":
            return False
    
    print (words)
    return True
    

fin=open("words.txt")

for line in fin:
    line=fin.readline()
    total_count=total_count+1
    word=line.strip()
    if has_no_e(word) == True:
        count=count+1

percentage=(round(count/total_count,2)) *100
print("The percentage of words without e letter is "+ str(percentage) +"%")




