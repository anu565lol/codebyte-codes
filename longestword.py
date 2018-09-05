#this code detects the longest word in the text

def LongestWord(sen): 

    # code goes here 
    words = sen.split()
    leng = 0
    word = ""
    for w in words:
        if len(w) > len(word):
            word = w
            
    return word
    
# keep this function call here  
print LongestWord(raw_input())
