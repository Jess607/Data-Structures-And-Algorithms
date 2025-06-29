def length_of_longest_substring(str):
    max_length=0
    start=0
    set_a=set()
    for end in range(len(str)):
        while str[end] in set_a:
            set_a.remove(str[start])
            start+=1
        set_a.add(str[end])
        max_length=max(max_length, end-start +1)
    return max_length


print(length_of_longest_substring('abcdabbb'))
print(length_of_longest_substring('abvgftaghjduygh'))