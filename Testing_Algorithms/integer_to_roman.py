def integer_to_roman(num):
    result=''
    int_to_roman=[('M', 1000), ('CM', 900), ('D', 500),
                  ('CD', 400), ('C', 100), ('XC', 90),
                  ('L', 50),('XL', 40), ('X', 10),
                  ('IX', 9), ('V',5), ('IV', 4), ('I', 1)]
    
    for val, int in int_to_roman:
        count= num//int
        result+=(val *count)
        num-=(count*int)

    return result

print(integer_to_roman(2789))
