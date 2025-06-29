def remove_duplicates(nums):
    dict={}
    index=0
    for i in set(nums):
        dict[i]=0
    for j in nums:
        if dict[j]<=1:
            nums[index]=j
            dict[j]=dict[j]+1
            index+=1
    nums=nums[:index]
    return index

print(remove_duplicates([1,2,2,2,3,3,3,3,3,4]))