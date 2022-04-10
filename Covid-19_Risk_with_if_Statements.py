"""
Task : Estimating the risk of death from coronavirus. Write a program that;

Takes "Yes" or "No" from the user as an answer to the following questions :

Are you a cigarette addict older than 75 years old? Variable → age

Do you have a severe chronic disease? Variable → chronic

Is your immune system too weak? Variable → immune

Set a logical algorithm using boolean logic operators (and/or) and use if-statements with the given variables in order to print out us a message : "You are in risky group"(if True ) or "You are not in risky group" (if False).



age =  # can be assigned only True/False
chronic =  # can be assigned only True/False
immune =  # can be assigned only True/False
risk = ?
"""

age = True
chronic = False
immune = True
risk = age and immune or chronic
risk

risk=input("please enter your answer")
if risk == "yes":
  print("you are in risk group")
if risk =="no":
  print("you are not in risk group") 
