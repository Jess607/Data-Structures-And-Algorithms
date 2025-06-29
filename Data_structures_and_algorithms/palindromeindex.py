#The aim of the palindrome index is to return the index of the character that when removed will make the string a palindrome
def palindrome_index(str):
    #First check if string is already a palindrome
    if str==str[::-1]:
        return -1
    #Get length of string 
    n=len(str)
 
    #Iterate to the middle of the string
    for i in range(n//2):
        #If the characters on both sides are not equal
        if str[i]!=str[n-1-i]:
            #Check if the removal of the character on the other end would create a palindrome , if it does return said character
            if str[i:n-1-i]==str[i:n-1-i][::-1]:
                return n-1-i, str[n-1-i]
            #Check if the removal of the character at the beginning end would create a palindrome, if it does return character
            elif str[i+1:n-i]==str[i+1:n-i][::-1]:
                return i, str[i]
  
            
    return -1  



print(palindrome_index('aabcbcaa'))



