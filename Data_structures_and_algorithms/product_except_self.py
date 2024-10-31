#Product except itself calculates the product of an array without the element of consideration and stores that product in the index of the element not considered in a new array
def product_except_self(nums):
    #Output is the new array initialized with 1's representing each element
    output = [1] * len(nums)
 
    left = 1
    for i in range(len(nums)):
        output[i] *= left
        left *= nums[i]
        
    right = 1
    for i in range(len(nums) - 1, -1, -1):
        output[i] *= right
        right *= nums[i]
    
    return output