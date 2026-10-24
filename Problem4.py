
# safe int_text

# Part B

def safe_int(text):
    try:
        return int(float(text.strip()))
    except(ValueError,TypeError):
        return None

print(f" ' 123' -> {safe_int("123")}")
print(f" '42' -> {safe_int("42")}")
print(f" '3.9' -> {safe_int("3.9")}")
print(f" 'abc' -> {safe_int("abc")}")
print(f" '' -> {safe_int("''")}")


print("\n")

# Part C

num1 = safe_int(input("Enter the first number: "))
num2 = safe_int(input("Enter the second number: ")) 

if num1 is None or num2 is None: 
    print("Please enter valid numbers!") 
else:
    
    print("Sum =", num1 + num2)