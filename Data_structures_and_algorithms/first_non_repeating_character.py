def first_non_repeating_character(string):
    #first non repeating character means the character is the first that only appears once in the string 
    #first create a new dictionary
    new_dict={}
    #iterate through the string and store the count of each character in the dictionary
    for i in string:
        new_dict[i]=new_dict.get(i,0) +1

    #Get the first non repeating character
    for char in string:
        if new_dict[char]==1:
            return char
        
    return None


print(first_non_repeating_character('llaah'))
    