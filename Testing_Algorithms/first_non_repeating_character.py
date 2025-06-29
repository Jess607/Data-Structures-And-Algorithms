def first_non_repeating_character(str):
    new_dict={}
    for i in str:
        new_dict[i]=new_dict.get(i,0)+1
    for i in new_dict:
        if new_dict[i]==1:
            return i
        

print(first_non_repeating_character('llllaaaah'))