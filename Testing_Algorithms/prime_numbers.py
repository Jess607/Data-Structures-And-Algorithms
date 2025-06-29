def prime_numbers(n):
    prime_nums=[True for i in range(n+1)]
    p=2
    while(p*p<=n):
        if prime_nums[p]==True:
            for j in range(p*p, n+1, p):
                prime_nums[j]=False
        p+=1

    ans=[a for a in range(2, n+1) if prime_nums[a]==True]
    return ans


print(prime_numbers(10))
