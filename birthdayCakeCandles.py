#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'birthdayCakeCandles' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER_ARRAY candles as parameter.
#

def birthdayCakeCandles(n, ar):
    max_height=0
    double=0
    for x in range(n):
        if ar[x]>max_height:
            max_height=ar[x]
    for y in range(n):
        if ar[y] == max_height:
            double+=1
    return double

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    ar = list(map(int, input().rstrip().split()))

    result = birthdayCakeCandles(n, ar)

    fptr.write(str(result) + '\n')

    fptr.close()
