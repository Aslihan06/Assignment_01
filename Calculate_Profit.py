"""
If you had deposited a coin on the cryptocurrency exchange that brought 7% fixed profit daily for a week, how much would your $ 1000 reach at the end of the 7th day?
"""

total = 1000
day = 0

while day<7 :
  sum_interest = total * 7/100
  total = sum_interest + total
  day = day + 1
  
print(total)  
