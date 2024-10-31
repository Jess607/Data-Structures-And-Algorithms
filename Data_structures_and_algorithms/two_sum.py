#Two sums tries to find the indexes of two numbers in the list that sum up to the target.
def two_sum(nums, target):
    #First we initialize an empty dictionary
    num_map = {}
    for i, num in enumerate(nums):
        # We iterate through the numbers and find their complement
        complement = target - num
        #If the complement is in the dictionary we return the index of the complement and the index we are currently iterating through
        if complement in num_map:
            return [num_map[complement], i]
        #Add the number to the dictionary
        num_map[num] = i
    return []

print ( two_sum([1,2,3,4,5,5], 10) ) 