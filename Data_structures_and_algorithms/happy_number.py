#A happy number is one whose sum of squares of individual digits sums up to 1 
def isHappy(n: int) -> bool:
        def sum_of_squares(num):
            """Calculate the sum of squares of digits."""
            total = 0
            while num > 0:
                digit = num % 10
                total += digit ** 2
                num //= 10
            return total

        # Initialize slow and fast pointers
        slow = n
        fast = sum_of_squares(n)

        while fast != 1 and slow != fast:
            slow = sum_of_squares(slow)              # Move slow pointer one step
            fast = sum_of_squares(sum_of_squares(fast))
        return fast==1  # Move fast pointer two steps

print(isHappy(9))

        
