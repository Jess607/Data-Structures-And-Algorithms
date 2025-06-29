def group_anagrams(list):
    new_dict={}
    for i in list:
        canonical=''.join(sorted(i))
        if canonical in new_dict:
            new_dict[canonical].append(i)
        else:
            new_dict[canonical]=[i]

    return new_dict


print(group_anagrams(['eat', 'ate', 'nab', 'ban']))