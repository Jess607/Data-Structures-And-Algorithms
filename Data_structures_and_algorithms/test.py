def som_function(target, arr):
    i,j, sum, curr_seq=0,0,0,0
    while j<len(arr):
        if sum>=target:
            sum-=arr[j]
            curr_seq-=1
            j+=1
        else:
            sum+=arr[i]
            curr_seq+=1
            i+=1
