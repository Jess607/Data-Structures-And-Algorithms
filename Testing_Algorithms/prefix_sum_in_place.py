def prefix_sum(arr, a,j):
    sum=0
    for i in range(len(arr)):
        sum+=arr[i]
        arr[i]=sum
    prefix_sum_num=arr[j]-arr[a-1]
    return arr, prefix_sum_num


print(prefix_sum([1,2,3,4,5,6],1,3))