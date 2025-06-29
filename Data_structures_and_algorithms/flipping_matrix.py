def flippingMatrix(matrix):
    max_total = 0
    n = int(len(matrix)/2)
    
    for i in range(n):
        for j in range(n):
            max_s = max(matrix[i][j], matrix[i][(2*n-1)-j], matrix[(2*n-1)-i][j], matrix[(2*n-1)-i][(2*n-1)-j])
            max_total += max_s
    
    return max_total