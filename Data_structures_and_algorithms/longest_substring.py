def longest_substring(str):
    i=0
    current_sub=0
    longest_sub=0
    dict={}
    while i<len(str)-1:
        if str[i] in dict:
            current_sub=0
            dict={}
        current_sub+=1
        dict[str[i]]=i
        i+=1
        longest_sub=max(longest_sub, current_sub)
    return dict


def length_of_longest_substring(s: str) -> int:
    char_set = set()
    max_length = 0
    start = 0

    for end in range(len(s)):
        while s[end] in char_set:
            char_set.remove(s[start])
            start += 1
        char_set.add(s[end])
        max_length = max(max_length, end - start + 1)

    return max_length

# Example Usage
s = "abcabcbb"
print("Length of the longest substring:", length_of_longest_substring(s))


print(longest_substring(' '))
