class Solution:
    def candy(self, ratings: List[int]) -> int:
        # Length of the ratings list
        num_children = len(ratings)
      
        # Initialize lists to represent the minimum candies for each child from left and right perspectives
        candies_from_left = [1] * num_children
        candies_from_right = [1] * num_children
      
        # Calculate the minimum candies required from the left perspective
        for i in range(1, num_children):
            # If the current child has a higher rating than the previous child, 
            # give one more candy than the previous child
            if ratings[i] > ratings[i - 1]:
                candies_from_left[i] = candies_from_left[i - 1] + 1
      
        # Calculate the minimum candies required from the right perspective
        for i in range(num_children - 2, -1, -1):
            # If the current child has a higher rating than the next child,
            # give one more candy than the next child
            if ratings[i] > ratings[i + 1]:
                candies_from_right[i] = candies_from_right[i + 1] + 1
      
        # Sum the max number of candies required from both perspectives for each child
        # to ensure all conditions are met
        total_candies = sum(max(candies_left, candies_right) for candies_left, candies_right in zip(candies_from_left, candies_from_right))
      
        return total_candies
        