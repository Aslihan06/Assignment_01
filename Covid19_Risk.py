"""
Task :
 Estimating the risk of death from coronavirus.

Consider the following questions in terms of True/False regarding anyone else.

Are you a cigarette addict older than 75 years old? Variable → age

Do you have a severe chronic disease? Variable → chronic

Is your immune system too weak? Variable → immune

Set a logical algorithm using boolean logic operators (and/or) and the given variables in order to give us True (there is a risk of death) or False (there is not a risk of death) as a result.

age =  # can be assigned only True/False
chronic =  # can be assigned only True/False
immune =  # can be assigned only True/False
risk = ? (True or False)
"""

age= False
chronic= True
immune= False

risk= age or chronic or immune
risk
True
