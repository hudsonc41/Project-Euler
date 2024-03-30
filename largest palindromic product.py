
def is_palindrome(number):
    number = str(number)
    if list(number) == list(reversed(number)):
        return True
    
    else:
        return False

largest_palindrome = 0
for i in range(100, 1000):
    for j in range(100, 1000):
        product = i * j
        if is_palindrome(product) == True:
            if product > largest_palindrome:
                 largest_palindrome = product

print(largest_palindrome)

    
