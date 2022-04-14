"""
Task : Create a list consisting of Fibonacci numbers from 1 to 55 using control flow statements and range() function.
The desired output is like this:
fibonacci →  [1, 1, 2, 3, 5, 8, 13, 21, 34, 55]
"""
liste=[1,1]

for i in range (1,9):
  x=liste[i-1]+liste[i]
  liste.append(x)

print(liste)
