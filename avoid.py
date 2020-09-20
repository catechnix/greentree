def avoid(words,letters):
    for l in words:
        if l not in letters:
            continue
        else:
            print ("has avoided letters")
            return False
           
    print ("Words have no avoided letters")
    return True

avoid("good","aer")
avoid("bedd","aer")

def avoids(letters):
    count=0
    new_list=list(letters)
    fin=open("words.txt")
    for line in fin:
        words=line.strip()
        for letter in words:
            if not letter in new_list:
                print(letter)
                continue
            
            else:
                break

    print(words)
    
        #count=count+1
    #print ("Number of words that don't contain avoided letters: ", count)

 
#avoided_letters=input("Please type some avoided letters \n")
#avoids("cd")
