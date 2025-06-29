#The objective is to find the longest substring wihtout repeating characters in a string snd return the length of such substring
#To solve we will be leveraging sliding windows
def longest_substring(str):
    #First we create a set to store the characters we encounter as we iterate through the list
    unique_chars=set()
    #We will be making use of two pointers, a left pointer and a right pointer, the left pointer will move when we encounter a character that is alreday in the set and the right pointer slides through the string
    left_pointer=0
    #Initialize a max length variable to track the length which we will eventually return
    max_length=0
    #Now we iterate through the string
    for right_pointer, char in enumerate(str):
        while char in unique_chars:
            unique_chars.remove(str[left_pointer])
            left_pointer+=1

        unique_chars.add(char)
        max_length=max(max_length, right_pointer-left_pointer +1)

    return max_length
        