#Return the length of the last word in a string
def length_of_the_last_word(str):
    #Remove all trailing spaces and then split on space and return length
    return len(str.strip().split(' ')[-1])

print(length_of_the_last_word('   fly me to   the moon  '))