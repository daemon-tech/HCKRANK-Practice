#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the miniMaxSum function below.
def miniMaxSum(arr):
    listmax = []
    listmin = []
    for number in arr:
        if number > min(arr):
            listmax.append(number)    
    for number in arr:
        if number < max(arr):
            listmin.append(number)
    maxnum = sum(listmax)
    minnum = sum(listmin)
    print (minnum, maxnum)
    
if __name__ == '__main__':
    arr = list(map(int, input().rstrip().split()))

    miniMaxSum(arr)
