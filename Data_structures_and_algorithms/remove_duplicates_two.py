# The objective here is to remove duplicates but still have at most 2 of the same elements
def remove_duplicates_from_array(nums):
    # Initialize the index, this is what we'd return
    index=0
    # A dictionary to keep track of numbers we've iterated through
    dict={}
    #Store the distinct numbers with 0 value in the dict(this can be optimized)
    for i in set(nums):
        dict[i]=0
    # Iterate through the list 
    for i in nums:
        # If the value stored for that number in the dictionary is 0(which means we've not iterated) or 1 which means we've iterated once we modify our nums list
        if dict[i]<=1:
            #Modifying our nums list to store our number
            nums[index]=i
            # Incrementing what is in our dictionary
            dict[i]= dict[i]+1
            #Incrementing index
            index+=1
    nums=nums[:index]
    #Return index which is inherently the number of elements in nums
    return index

print(remove_duplicates_from_array([1,2,2,2,3,3,3,3,3,4]))
