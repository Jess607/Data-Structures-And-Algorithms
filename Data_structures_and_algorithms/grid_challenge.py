def grid_challenge(grid):
    grid = [sorted(row) for row in grid]
    
    # Check if each column is sorted in non-decreasing order
    for col in range(len(grid[0])):
        for row in range(1, len(grid)):
            if grid[row][col] < grid[row - 1][col]:
                return "NO"
    
    return "YES"