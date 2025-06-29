def balanced_parentheses(str):
    new_list=[]
    if len(str)<=1:
        return False
    for i in str:
        if i=='(':
            new_list.append(i)
        elif i==')':
            if len(new_list)==0:
                return False
            else:
                new_list.pop()

    return len(new_list)<1


print(balanced_parentheses('(())'))
