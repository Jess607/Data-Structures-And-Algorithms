def remove_element(nums, val):
    index=0
    for i in nums:
        if i!=val:
            nums[index]=i
            index+=1
    nums=nums[:index]
    return nums


print(remove_element([1,2,3,4,5,6],4))