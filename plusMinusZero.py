def plusMinus(arr):
    # Write your code here
    n = len(arr)
    positive_ratio = 0
    negative_ratio = 0
    zero_ratio = 0
    
    for element in arr:
        if element > 0:
            positive_ratio += 1
        elif element < 0:
            negative_ratio += 1
        else:
            zero_ratio += 1
            
    print(f"{positive_ratio/n:.6f}")
    print(f"{negative_ratio/n:.6f}")
    print(f"{zero_ratio/n:.6f}")
