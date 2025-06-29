def remove_duplicates(nums):
    dict={}
    index=0
    for i in nums:
        if i not in dict.values():
            nums[index]=i
            dict[index]=i
            index+=1

    nums=nums[:index]
    return len(nums)

print(remove_duplicates([1,1,2,2,3,3,3,3,44]))