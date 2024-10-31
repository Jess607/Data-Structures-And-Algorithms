# A palindrome is a word or sentence which has the same letters forward and in reverse when all the characters and white space have been taken out
def is_palindrome(string):
    #First we remove all characters and white space
    new_string=''.join(char for char in string if char.isalnum())
    #Change to lower case and compare the main word with its reverse form
    if new_string[::-1].lower()==new_string.lower():
        return True
    return False


print(is_palindrome('A man, a plan, a canal: Panama'))