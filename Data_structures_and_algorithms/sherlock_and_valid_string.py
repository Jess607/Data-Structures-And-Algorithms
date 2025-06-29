from collections import Counter

def is_valid(s):
    dict={}
    for i in s:
        dict[i]=dict.get(i,0) +1

    set_val=set(val for val in dict.values())

    if len(set_val)>2:
        return 'No'
    
    if len(set_val)==1:
        return 'Yes'

    return set_val

print(is_valid('aaabbbcccddd'))
