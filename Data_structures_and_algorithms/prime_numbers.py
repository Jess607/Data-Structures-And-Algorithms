#Get all prime numbers between 1 and n using sieve of eratosthenes
def prime_numbers(n):
    #Initialize a list assuming all numbers between 1 and n are prime numbers
    prime_num=[True for i in range(n+1)]
    #Start iterating from n=2 because 2 is the first prime number
    p=2
    #The sieve of eratosthenes assumes that all non prime numbers will have factors within the square root of n 
    while (p*p <=n):
        if prime_num[p]==True:
            for j in range(p*p, n+1, p):
                prime_num[j]=False
        p+=1
    prime_numbers=[i for i in range(2, n+1) if prime_num[i]==True]

    return prime_numbers



#prime_numbers(100)
print('\n')
print(prime_numbers(30))
    

