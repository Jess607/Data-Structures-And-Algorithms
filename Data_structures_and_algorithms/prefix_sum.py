def prefix_sum(arr):
    sum=0
    lis=[]
    for i in range(len(arr)):
        sum+=arr[i]
        lis.append(sum)
    return lis


print(prefix_sum([1,2,3,4,5,6]))