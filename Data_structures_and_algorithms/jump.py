def jump(nums):
    gas = 0
    for n in nums:
        if gas < 0:
            return False
        elif n > gas:
            gas = n
        gas -= 1
            
    return True


print(jump([3,2,1,0,4]))
