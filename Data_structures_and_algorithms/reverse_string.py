def reverse_string(string):
    new_string=''
    for i in range(len(string)-1,-1,-1):
        new_string+=string[i]
    return new_string


print(reverse_string('abcx'))