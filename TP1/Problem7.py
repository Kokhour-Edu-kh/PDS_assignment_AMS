# Digit sum and revers

def digit_sum(n):
    n = abs(n)      # Must be positive numbers
    total = 0
    while n > 0:
        digit =n % 10
        total +=digit
        n//= 10
    return total

def reverse_number(n):
    n = abs(n)
    reversed_num = 0
    while n >0:
        digit = n % 10
        reversed_num = reversed_num * 10 + digit
        n //= 10
    return reversed_num

def is_palindrome(n):
    if n <0:
        return False
    return n == reverse_number(n)


# (a) Test the functions
numbers = [2026,12321,9875,45654]

for n in numbers:
    print(f"\t{n}: Digit sum: {digit_sum(n)} , Reversed: {reverse_number(n)} , Palindrome: {is_palindrome(n)}")


# Count the palindrome

count = 0
for n in range(10,1000):
    if is_palindrome(n):
        count += 1

print("\n\tpalindromes from 10 to 999 : ", count)