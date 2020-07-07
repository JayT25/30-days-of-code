"""
Task:
    Given N names and phone numbers, assemble a phone book that maps friends' names 
    to their respective phone numbers. You will then be given an unknown number 
    of names to query your phone book for. For each name queried, print the associated 
    entry from your phone book on a new line in the form name=phoneNumber; if an entry for 
    name is not found, print Not found instead.

    Note: Your phone book should be a Dictionary/Map/HashMap data structure.

Input format:
    The first line contains an integer, N, denoting the number of entries in the phone book.
    Each of the N subsequent lines describes an entry in the form of 2 space-separated values 
    on a single line. The first value is a friend's name, and the second value is an 8-digit 
    phone number.
    After the N lines of phone book entries, there are an unknown number of lines of queries. 
    Each line (query) contains a name to look up, and you must continue reading lines until 
    there is no more input.

Output format:
    On a new line for each query, print Not found if the name has no corresponding 
    entry in the phone book; otherwise, print the full name and phoneNumber in the 
    format name=phoneNumber.


"""

# Enter your code here. Read input from STDIN. Print output to STDOUT
from sys import stdin

# read the first line to indicate the amount of entries
# for the phone book dictionary
entries = int(input())

# define a dictionary
phone_book = {}

# for x in the range of the number of entries
# take input( name and phoneNumber) for the dictionary 
for x in range(entries):
        # take user input for
        # a phone book entry.
        # input format: Name phoneNumber
        phone_book_entry = input()

        # split the string using space as a delimitter
        # format now: split_phone_book_entry = [Name, phoneNumber]
        split_phone_book_entry = phone_book_entry.split(' ')

        # split_phone_book_entry[0] = Name
        # split_phone_book_entry[1] = phoneNumber
        # add to phone_book dictionary. 
        # Name is the key, phoneNumber is the value
        phone_book[split_phone_book_entry[0]] = int(split_phone_book_entry[1])


# read input until there's
# no more
names = stdin.read().splitlines()
for x in range(len(names)):
    if names[x] in phone_book:
        print( names[x]+'='+str(phone_book.get(names[x])) )
    else:
        print('Not found')
