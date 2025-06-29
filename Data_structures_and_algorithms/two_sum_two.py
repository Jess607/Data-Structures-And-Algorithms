# Define a class named Solution
class Solution:
    # Define a method that finds the two indices of the numbers that add up to the target sum
    def twoSum(self, numbers, target: int):
        # Initialize two pointers, one at the beginning and one at the end of the array
        left_pointer, right_pointer = 0, len(numbers) - 1
      
        # Iterate through the array until the two pointers meet
        while left_pointer < right_pointer:
            # Calculate the sum of the two numbers at the current pointers
            current_sum = numbers[left_pointer] + numbers[right_pointer]
          
            # If the sum equals the target, return the indices 
            if current_sum == target:
                return [left_pointer, right_pointer]
          
            # If the sum is less than the target, move the left pointer to the right to increase the sum
            if current_sum < target:
                left_pointer += 1
            # If the sum is greater than the target, move the right pointer to the left to decrease the sum
            else:
                right_pointer -= 1
        # Return an empty list if no two numbers sum up to the target (though the problem guarantees a solution)
        return []
    
a=Solution()
print(a.twoSum([1, 2, 4, 4, 6],7))