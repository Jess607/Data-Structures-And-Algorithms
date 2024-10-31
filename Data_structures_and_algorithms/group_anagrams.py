#An anagram is a word that went spelt in another way creates another way e.g ban and nab, eat and ate
#Here we have a list of strings of anagrams and are meant to group them

def group_anagrams(strings):
    #First create a dictionary to store the lists
    anagram_groups = {}
    #Iterate through the list of strings and store the sorted form which would be same for all anagrams
    for string in strings:
        canonical = ''.join(sorted(string))
        #If sorted is in the dictionary we append to the list created
        if canonical in anagram_groups:
            anagram_groups[canonical].append(string)
        #Else we create a new list
        else:
            anagram_groups[canonical] = [string]
    #Return the list of values of the dictionary
    return list(anagram_groups.values())
    

print(group_anagrams(['eat', 'ate', 'ban', 'nab']))