import math

prime_numbers = []
number = 1
while len(prime_numbers) != 10001:
    if math.factorial((number - 1)) + 1 % number == 0:
        prime_numbers.append(number)
    number += 1

print(prime_numbers[-1])

    
