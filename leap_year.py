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
	return leap

n = int(input("Enter the year:"))
if __name__ == "__main__":
	if is_leap(n):
		print("{} is leap year".format(n))
	else: 
		print("{} is not leap year".format(n))

