def avoid(words,letters):
    
    for l in words:
        if l not in letters:
            continue
        else:
            print ("has avoided letters")
            return False
           
    print ("Words have no avoided letters")
    print(words)
    return True

#avoid("good","aer")
#avoid("bedd","aer")

def avoids(letters):
    count=0
    fin=open("words_org.txt")
    for line in fin: 
         
        words=line.strip()
          
        result=avoid(words,letters)
        if result == True:
            count=count+1

    print(count)
 
letters=input("Please type some avoided letters \n")
avoids(letters)
