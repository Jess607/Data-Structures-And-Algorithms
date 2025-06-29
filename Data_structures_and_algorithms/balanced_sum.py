def balanced_sum(arr):
    sum_left=[0]*len(arr)
    sum_right=[0]* len(arr)
    left=0
    right=0
    for i in range(len(arr)):
        sum_left[i]+=left
        left+=arr[i]
    for j in range(len(arr)-1, -1, -1):
        sum_right[j]+=right
        right+=arr[j]
    for i,j in zip(sum_left, sum_right):
        if i==j:
            return 'YES'
    return 'NO'

        
    
print(balanced_sum([1,2,3,3]))