def diagonalDifference(arr):
    # Write your code here
    n = len(arr)
    right_diagonal = 0
    left_diagonal = 0
    
    for i in range(n):
        right_diagonal += arr[i][i]
        left_diagonal += arr[i][n - i - 1]
        
    result = right_diagonal - left_diagonal
                
    return abs(result)
