print("Check if words contain only letters in the letters\n")
def use_only(words,letters):
  
    for l in words:
        if l in letters:
            continue
        else:
            print("Words contain letters that it is not in letters input")
            return False 
    print("Words contain only letters in letters input\n")
    return True


words=input("Input words to check\n")
letters=input("Input letters to check\n")
use_only(words, letters)

    

