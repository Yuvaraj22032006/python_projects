#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'timeConversion' function below.
#
# The function is expected to return a STRING.
# The function accepts STRING s as parameter.
#

def timeConversion(s):
    # Write your code here
    
    parts = s.split(':')
    
    hours = int(parts[0])
    minutes = parts[1]
    seconds = parts[2][:2]
    ampm = parts[2][2:]
    
    if ampm == "AM":
        if hours == 12:
            hours = 0
            
            result = f"{hours:02d}:{minutes}:{seconds}"
            
        else:
            
            result = f"{hours:02d}:{minutes}:{seconds}"
             
        
    elif ampm == "PM":
        if hours == 12:
            hours = str(hours)
            result = f"{hours}:{minutes}:{seconds}"
        elif hours >= 1 and hours <= 11:
            hours += 12
            hours = str(hours)
            result = f"{hours}:{minutes}:{seconds}"
        
    return result

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = timeConversion(s)

    fptr.write(result + '\n')

    fptr.close()
