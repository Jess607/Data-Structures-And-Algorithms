import math

def counter_game(n):
    counter=0
    while n>1:
        if not(math.log2(n).is_integer()):
            n-=2**int(math.log2(n))
            counter+=1
        elif math.log2(n).is_integer():
            n=n/2
            counter+=1
    if counter%2==0:
        return 'Richard'
    else:
        return 'Louise'


print(math.log2(6).is_integer())
    


print(counter_game(6))