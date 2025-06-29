def convert_int_to_roman(num):
    # Define a list of tuples with Roman numerals and their integer values
    val_to_roman = [
        (1000, 'M'), (900, 'CM'), (500, 'D'), (400, 'CD'),
        (100, 'C'), (90, 'XC'), (50, 'L'), (40, 'XL'),
        (10, 'X'), (9, 'IX'), (5, 'V'), (4, 'IV'),
        (1, 'I')
    ]
    
    # Initialize an empty string to build the Roman numeral result
    result = ""
    
    # Loop through each (value, numeral) pair
    for value, numeral in val_to_roman:
        # Find out how many times the current value fits into `num`
        count = num // value
        # Append the corresponding numeral that many times to the result
        result += numeral * count
        # Decrease `num` by the equivalent integer value
        num -= value * count
    
    return result


print(convert_int_to_roman(3241))