
import time

import math

def is_sqrt(n):
    x = n
    y = (x + 1) // 2
    while y < x:
        x = y
        y = (x + n // x) // 2
    if x*x==n:
        return True
    else:
        return False


while True:
    remg=int(raw_input())
    while True:
        remg+=4000000007
        print remg
        if(is_sqrt(remg)):
            
            break
    p=time.gmtime(math.sqrt(remg))
    print time.asctime(p)

