"""
Task:

Find out if a given number is an "Armstrong Number".

An n-digit number that is the sum of the nth powers of its digits is called an n-Armstrong number. Examples :
371 = 33 + 73 + 13;
9474 = 94 + 44 + 74 + 44;
93084 = 95 + 35 + 05 + 85 + 45.

Write a Python program that;
takes a positive integer number from the user,
checks the entered number if it is Armstrong,
consider the negative, float and any entries other than numeric values then display a warning message to the user.


                           Examples

Sample inputs                                          Outputs
 407	                                  407 is an Armstrong number
   5	                                  5 is an Armstrong number
 -153	                                  It is an invalid entry. Don't use non-numeric, float, or negative values!
 153.87 or 153,87	                  It is an invalid entry. Don't use non-numeric, float, or negative values!
 one	                                  It is an invalid entry. Don't use non-numeric, float, or negative values!
 121	                                  121 is not an Armstrong number

"""

num=input("please enter a number")
length = len(num)
sonuc = 0

if num.startswith("-") or "." in num or (not num.isdigit()):
  print("it is an invalid entry.Don't use non-numeric,float,or nagative values!")
else:
  for i in num:
    sonuc += int(i)** length
  if int(num) == sonuc:
    print(num + " is an Armstrong number") 
  else:
    print(num + " is not an Armstrong number")  
