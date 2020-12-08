#!/usr/bin/env python
# coding: utf-8

# In[ ]:


#!/bin/python3

import os
import sys

#
# Complete the timeConversion function below.
#
def timeConversion(s):
    hh = int(s[0:2])
    ampm = str(s[8:10])
    
    if ampm == "PM": 
        if hh == 12: return s[0:8]
        else: return(str(hh + 12)+s[2:8]) 
    else: 
        if hh == 12: return("00"+s[2:8]) 
        else: return s[0:8]

if __name__ == '__main__':
    f = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = timeConversion(s)

    f.write(result + '\n')

    f.close()

