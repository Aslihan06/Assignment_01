"""
Task : Find out the most frequent number and its frequency.

Write a program that;

Finds out the most frequent number in the given list.
Calculates its frequency.
Prints out the result such as :

Example;

Given list                                                Desired Output
numbers = [1, 3, 7, 4, 3, 0, 3, 6, 3]                     the most frequent number is 3 and it was 4 times repeated
"""

list = [2,4,6,8,0,4,1,3,5,4]
most_comman = max(list, key = list.count)
print(most_comman)
