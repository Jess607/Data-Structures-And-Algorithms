#Balanced parentheses are '(), (())' etc and not ), ((), ()) etc, the goal is to find balanced parenthese
def is_balanced_parentheses(string):
    #If the length of the string is less than or equal to 1, obviously the parenthese are not balanced
    if len(string)<=1:
        return False
    #Initialize a list to store the eaxh parenthesis as we iterate through
    new_list=[]
    #Append each open parenthesis to the list
    for p in string:
        if p=='(':
            new_list.append(p)
        elif p==')':
            #If no open parenthesis was appended, it means it is not balanced and return false
            if len(new_list)==0:
                return False
            #Pop each open parenthesis based on the closed parenthesis present
            new_list.pop()
    #If there's still something in the list, it is not balanced but if the list is empty, it is balanced.
    return len(new_list)<1
    

print(is_balanced_parentheses('()'))





