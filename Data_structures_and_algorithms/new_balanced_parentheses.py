def isValid(s):
    if len(s)<=1 :
        return False
    new_list=[]
    for p in s:
        if p in ['{', '(', '[']:
            new_list.append(p)
        elif p in ('}', ')', ']'):
            a=new_list[-1]
            if (a=='{' and p=='}') or (a=='(' and p==')') or (a=='[' and p==']'):
                new_list.pop()
            else:
                return False
        else:
            return False            
    return len(new_list)<1



print(isValid('ia'))