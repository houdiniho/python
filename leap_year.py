#!/usr/bin/env python3
def is_leap(year):
    leap = False
    
    # Write your logic here
    if year%4==0:
        if year %100 == 0:
            if year % 400 ==0:
                leap = True
        else:
            leap = True
n = int(input())
if __name__ == "__main__":
    is_leap(n)

