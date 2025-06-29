def sum_of_squares(num):
            """Helper function to calculate the sum of squares of digits."""
            total = 0
            while num > 0:
                digit = num % 10
                total += digit ** 2
                num //= 10
            return total


print(sum_of_squares(19))


