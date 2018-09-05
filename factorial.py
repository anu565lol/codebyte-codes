def FirstFactorial(num): 

    # code goes here
    fact = 1
    if num != 0:
        for r in range(1,num+1):
            
            fact = fact*r
    if num ==0:
        fact = 1
    return fact
    
# keep this function call here  
print FirstFactorial(raw_input("Enrter the numbet for the factorial: "))
