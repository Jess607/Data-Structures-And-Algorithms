#Finds majority element using the Boyer-Moore Majority Algorithm
def majority_element(nums):
    
    res = majority = 0
        
    for n in nums:
        if majority == 0:
            res = n
            
        majority += 1 if n == res else -1
        
    return res




    

print(majority_element([2,2,3,4,5,5,5,6,7]))
