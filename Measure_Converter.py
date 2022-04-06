"""
Task-1:

Write a short Python program that asks the user to enter Celsius temperature (it can be a decimal number), converts the entered temperature into Fahrenheit degree and prints the result.

Task-2:
Write a short Python program that asks the user to enter a distance (it can be a decimal number) in kilometers, converts the entered distance into miles and prints the result."""

Task-1:

C = float(input("Please Write the temperature in Celsius."))
F = ((9/5)*C + 32)

print(F)


Task-2:

km=float(input("Write the value in kilometers."))
conversion_fac= 0.621371
mil= km * conversion_fac

print('%0.2f km equals %0.2f mil' %(km,mil))

