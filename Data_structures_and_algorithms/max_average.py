#The objective here is to find the contiguous array of length k with the highest average
def max_average(nums, k):
    #Get a current sum of the first k numbers in the array
    current_sum=sum(nums[:k])
    #Initialize a max sum variable equal to the current sum, since a higher sum will equal a higher average, we calculate a sum
    max_sum=current_sum
    #Iterate through the array using a sliding window of k
    for i in range(k, len(nums)):
        current_sum+=nums[i]-nums[i-k]
        max_sum=max(current_sum, max_sum)
    #Return the max average
    return max_sum/k



print(max_average([1, 12, -5, -6, 50, 3], 4))
        
