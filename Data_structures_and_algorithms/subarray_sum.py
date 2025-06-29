# The sub array sum function takes a list of numbers and a target and seeks to find a contiguous sub array that sums up to the target number
def subarray_sum(nums, target):
    # First we create a dictionary which acts as a placeholder in the real sense
    sum_index = {0: -1}
    # Initialize a sum 
    current_sum = 0
    #We iterate through the numbers getting both their index and the number
    for i, num in enumerate(nums):
        # Incrementing sum with each number
        current_sum += num
        #If the current sum minus the target exists in our dictionary we get our array, if the first number in our array is our target we get zero which is what is initially in our dictionary
        if current_sum - target in sum_index:
            # Return the index of the difference and where index of our current iteration
            return [sum_index[current_sum - target] + 1, i]
        # We add our current sum to the dictionary to continue our iteration
        sum_index[current_sum] = i
    #Return an empty list if there's no contiguous array that meets our target
    return []


print(subarray_sum([10,20,10,5], 35))


    