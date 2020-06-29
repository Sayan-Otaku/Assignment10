def printWords(s): 
      
    # split the string  
    s = s.split(' ')  
      
    # iterate in words of string  
    for word in s:  
          
        # if length is even  
        if len(word)%2==0: 
            print(word)  
  
  
# Driver Code  
st = 'Print every word in this sentence that has an even number of letters' 
printWords(st)  
