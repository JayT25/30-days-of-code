"""

Task:
	Write a factorial function that takes a positive integer, 
	N as a parameter and prints the result of N! ( N factorial).

"""

#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the factorial function below.


def factorial(n):
	# base case to exit recursion
	if n == 0:
		
		return 1
	else:
		result = n * factorial(n-1)
		
		return(result) 




n = int(input())

result = factorial(n)

print(result)