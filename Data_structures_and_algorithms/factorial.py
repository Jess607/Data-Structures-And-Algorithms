def factorial(n):
    if n==0:
        return 1 
    answer=n
    while n>1:
        answer*=n-1
        n-=1

    return answer


print(factorial(0))