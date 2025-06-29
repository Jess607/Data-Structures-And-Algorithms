def new_year_chaos(q):
    bribes = 0
    for i in range(len(q)):
        # Check if position is too chaotic
        if q[i] - (i + 1) > 2:
            print("Too chaotic")
            return
        
        # Count swaps by checking how many times q[i] was overtaken
        for j in range(max(0, q[i] - 2), i):
            if q[j] > q[i]:
                bribes += 1
    
    print(bribes)


print(new_year_chaos([1,2,5,3,7,8,6,4]))

