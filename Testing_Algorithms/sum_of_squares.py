def sum_of_squares(n):
    total=0
    while n>0:
        digit=n%10
        total+=digit**2
        n=n//10

    return total


print(sum_of_squares(245))