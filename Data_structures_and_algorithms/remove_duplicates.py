# The objective here is to remove duplicates from a sorted array in place and return the eventual length of the array
def remove_duplicates_from_sorted_array(nums):
    # First we initialize an index and set it to zero
    index=0
    # Next we create a dictionary to keep track of numbers we have iterated through
    dict={}
    #Iterate through the numbers
    for i in nums:
        # If it is not in the dictionary put it in the dictionary and keep it as part of your original list
        if i not in dict.keys():
            nums[index]=i
            #Putting the number in the dictionary
            dict[i]=1
            #Increment your index
            index+=1
    #We want our list to only have the numbers we added
    nums=nums[:index]
    #Return index which is the length of the list
    return index


print(remove_duplicates_from_sorted_array([1,1,2,3]))