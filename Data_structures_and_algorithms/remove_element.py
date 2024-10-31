#The idea is to remove all occurrences of the element val and return the number of elements left in place
def remove_element(nums, val):
    # Begin your index with 0
    index=0
    #Iterate through nums
    for i in range(len(nums)):
            #Iterate a number is not the value keep it if not discard it
            if nums[i]!=val:
                nums[index]=nums[i]
                index+=1
    #Simply return index
    return index
    

print(remove_element([1,2,18,7,6,6,3],3))