print("Check if the word use all the required letters at least once")

def use_all(words, required):
    for l in required:
        if l not in words:
            print("words contain letter not in required")
            return False
    print("Words")
    return True

#words=input("Input words\n")
#required=input("Input required letters\n")

#use_all(words,required)

fin=open("words_org.txt")
for line in fin:
    word=line.strip()
    use_all(word,"aeiou")
    

    
