import math
import os
import random
import re
import sys

"""
Task:
	Given a string, S, of length N that is indexed from 0 to N - 1 , 
	print its even-indexed and odd-indexed characters as 2 space-separated 
	strings on a single line (see the Sample below for more detail).

	The first line contains an integer, T (the number of test cases).
	Each line i of the T subsequent lines contain a String, S .

Constraints:
	1 <= T <= 10
	2 <= length of S <= 10000


Sample Input:
	2
	Hacker
	Rank

Sample Outpur:
	Hce aKr
	Rn ak

"""

def foo(s):
	even_result = ""
	odd_result = ""
	for x in range(len(s)):
		if x%2 == 0:
			even_result += s[x]
		else:
			odd_result += s[x]
	return(even_result + " " + odd_result)

test_cases = input()
user_str = []
for x in range(int(test_cases)):
	
	user_str.append(input())

for x in range(int(test_cases)):
	print(foo(user_str[x]))



