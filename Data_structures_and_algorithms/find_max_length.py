from typing import List

class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        # Initialize the current balance between 0s and 1s and the maximum length found
        balance = max_length = 0
        # Create a hash map to store the first occurrence of each balance
        balance_map = {0: -1}
      
        # Iterate over the elements in the array
        for index, value in enumerate(nums):
            # Update the balance (+1 for 1, -1 for 0)
            balance += 1 if value == 1 else -1
          
            # Check if the same balance has been seen before
            if balance in balance_map:
                # If we have seen this balance before, calculate the length of the subarray
                # between the previous index and the current index
                max_length = max(max_length, index - balance_map[balance])
            else:
                # If this is the first time we've seen this balance,
                # store the index for this balance in the hash map
                balance_map[balance] = index
      
        # Return the maximum length of the subarray with equal number of 0s and 1s
        return max_length