#The idea is to reverse the words in a string and remove whatever white spaces might be between the words or trailing
def reverse_words_in_a_string(str):
    #Get the length of the string necessary for in place operation
    len_of_str=len(str)
    #Split the string and also strip whitespace
    a=str.strip().split()[::-1]
    #Join the string together
    str+=' '.join(a)
    #Get only what is required
    str=str[len_of_str:]
    return str



b=['','']
str='the sky is   blue'
print(str.split())
print(reverse_words_in_a_string(str))