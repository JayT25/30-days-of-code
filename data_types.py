"""
The variables i, d, and s are already declared and initialized 
for you. You must:
	1. Declare 3 variables: one of type int, one of type double, 
	and one of type String.

	2. Read 3 lines of input from stdin (according to the sequence 
	given in the Input Format section below) and initialize your 3 
	variables.

	3.Use the + operator to perform the following operations:
		1. Print the sum of i plus your int var on a new line.
		2. Print the sum of d plus your double var on a new line.
		3. Concatenate s with the string you read as input and print
		the result on a new line.

Sample Input:
	12
	4.0
	is the best place to learn and practice coding!

Sample Output:
	16
	8.0
	HackerRank is the best place to learn and practice coding!


"""
i = 4
d = 4.0
s = 'HackerRank '

# Declare second integer, double, and String variables.
num = 1
dou = 3.4
s_2 = 'String'


# Read and save an integer, double, and String to your variables.
user_int = int(input())
user_d = float(input())
user_str = input()

# Print the sum of both integer variables on a new line.
print(i+user_int)

# Print the sum of the double variables on a new line.
print(d+user_d)

# Concatenate and print the String variables on a new line
# The 's' variable above should be printed first.
print(s+user_str)
