"""
Write a function called sed that takes as arguments a pattern string, a replacement string, 
and two filenames; it should read the first file and write the contents into the second file 
(creating it if necessary). If the pattern string appears anywhere in the file, 
it should be replaced with the replacement string.
"""

def sed (patt_str,replaced_str,first_file,second_file):
    global first_fh, second_fh
    try:
        first_fh=open(first_file,'r')
    except:
        print('there is no file to read\n')

    second_fh=open(second_file,'w')
        #to do if file can't be written
    
    for line in first_fh:
        #word=line.strip()
        line=line.replace(patt_str, replaced_str)
        second_fh.write(line)
        
    first_fh.close()
    second_fh.close()

if __name__ =='__main__':   
    sed('a','bb','wordsn.txt','words_rep.txt')
    


