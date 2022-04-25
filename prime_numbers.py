"""
Task :
 Print the prime numbers which are between 1 to entered limit number (n).
You can use a nested for loop. Collect all these numbers into a list The desired output for n=100
"""
def is_prime(n):
    if n == 1:
        return False

    for i in range(2,n):
        if n % i == 0:
            return False
    return True

prime_number = []
for n in range(1,100):
    if is_prime(n) == True:
        prime_number.append(n)

print(prime_number)
prime_number = []
for i in range(2,101):
    for j in range(2,i):
        if i % j == 0:
            break
    else:
        prime_number.append(i)
    
print(prime_number)



