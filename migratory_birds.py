#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'migratoryBirds' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER_ARRAY arr as parameter.
#

def migratoryBirds(arr):
    # Write your code here
    #declare a dictionary
    counts = {}
    result = 0
    max_count = 0
    n = len(arr)
    
    for element in arr:
        # add elements in the dictionary
        if element in counts: # if the element is in the dictionary it adds the value by 1
            counts[element] += 1
        else:# if the element is not the dictionary it adds the element and value by 1
            counts[element] = 1
            
    # it iterates a dictionary, .items() is used to iterate over both key and value of a dictionary
    # .key() or .value() for key or value
    for key, value in counts.items():
        if value > max_count:
            max_count = value
            result = key
        elif value == max_count:
            result = min(result, key)
            
    return result 

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    arr_count = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    result = migratoryBirds(arr)

    fptr.write(str(result) + '\n')

    fptr.close()
