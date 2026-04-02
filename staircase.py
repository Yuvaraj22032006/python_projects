def staircase(n):
    # Write your code here
    
    for i in range (1, n + 1):
        space = n - i
        hash_value = i
        print(f"{' ' * space}{'#' * hash_value}")
