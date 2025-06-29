def super_digit(n):
    def digit_sum(x):
        if len(x) == 1:
            return int(x)
        return digit_sum(str(sum(int(d) for d in x)))

    # Compute initial sum of n's digits, then multiply by k
    initial_sum = sum(int(d) for d in n) * k
    return digit_sum(str(initial_sum))

    


