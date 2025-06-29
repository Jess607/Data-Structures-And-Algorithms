def subarray_sum(nums, target):
    sum_index={0:-1}
    sum_total=0
    for i, num in enumerate(nums):
        sum_total+=num
        if sum_total-target in sum_index:
            return [sum_index[sum_total-target]+1, i]
        sum_index[sum_total]=i
   

print(subarray_sum([10,20,10,5, 15],35))

