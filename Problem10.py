# Prime Numbers and Goldbach's Conjecture


def is_prime(n):
    if n < 2:
        return False
    d = 2
    while d * d <= n:
        if n % d == 0:
            return False
        d += 1
    return True


# Print all prime numbers below 50

print("Primes Below 100 : ")
for n in range(2, 50): 
    if is_prime(n):
        print(n, end=" ") 
print()


# Count prime numbers below 100

count = 0 
for n in range(2, 100): 
    if is_prime(n): 
        count += 1 
print("Number of primes below 100:", count)
print("\n")
# Part C 

def goldbach(n): 
    for p in range(2, n): 
        q = n - p 
        if is_prime(p) and is_prime(q): 
            return p, q
    return None 

for n in range(4,31,2):
    f,g =goldbach(n)
    print(f"{n} = {f} + {g}")


#Part D
for n in range(4, 10001, 2):
    pair = goldbach(n)

    if pair is None:
        print("Counterexample found:", False)
        break
else:
    print("Goldbach's conjecture holds for every even number from 4 to 10000 :",True)





