"""

Task:
	Given an array, A, of N integers, print A's elements in reverse order 
	as a single line of space-separated numbers.

Input Format:
	The first line contains an integer, N (the size of our array).
	The second line contains N space-separated integers describing 
	array A's elements.

Sample input:
	4
	1 4 3 2
Sample output:
	2 3 4 1



"""

#!/bin/python3

import math
import os
import random
import re
import sys

def reverse_arr(an_array):
    index = (len(an_array) - 1)
    result = ''
    for x in range((len(an_array))):
        result += str(an_array[index]) + ' '
        index -= 1
    return result    



if __name__ == '__main__':
    n = int(input())

    arr = list(map(int, input().rstrip().split()))

    print(reverse_arr(arr))
