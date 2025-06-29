#Convert roman numerals to integers
def convert_roman_to_integer(str):
    #First we create a dictionary of the roman numeral numbers with their corresponding letters
    dict={'I':1,
          'V':5,
          'X':10,
          'L':50,
          'C':100,
          'D':500,
          'M':1000}
    #The idea is to iterate from behind and then add or subtract a number depending on whether or not it is higher or lower than the number before it
    #Our answer is stored in a variable as the last roman numeral
    answer=dict[str[-1]]
    #Iterate from behind and stop just before the last letter
    for i in range(len(str)-1, 0, -1):
        #If the number before the previous is greater than or equal to where you are in the iteration, add it
        if dict[str[i]]<=dict[str[i-1]]:
            answer+=dict[str[i-1]]
        #Else subtract it
        else:
            answer-=dict[str[i-1]]
    #Return the answer
    return answer


print(convert_roman_to_integer('LVIII'))





