def product_except_self(nums):
    output= [1] * len(nums)

    left=1
    for i in range(len(nums)):
        output[i]*=left
        left*=nums[i]

    right=1
    for j in range(len(nums)-1, -1, -1):
        output[j]*=right
        right*=nums[j]

    return output


print(product_except_self([2,4,6,8]))