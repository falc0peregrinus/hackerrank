#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the migratoryBirds function below.
def migratoryBirds(arr):
    
    #create a list of counts for each bird type
    #each list index is (bird type - 1)
    typecounts = list((0,0,0,0,0)) 
    
    #instead of traversing arr 5 times using count(), traverse arr once
    #and build a list of counts for each bird type
    for sighting in arr:
        typecounts[sighting-1]+=1 #add 1 to each bird type that was sighted
    
    return (typecounts.index(max(typecounts))+1)

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    arr_count = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    result = migratoryBirds(arr)

    fptr.write(str(result) + '\n')

    fptr.close()