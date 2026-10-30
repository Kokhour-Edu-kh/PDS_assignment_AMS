
# safe int_text

# Part B

def safe_int(text):
    text =text.strip()

    if text.lstrip("-").isdigit():
        return int(text)
    try:
        return int(float(text.strip()))
    except(ValueError,TypeError):
        return None

text =["42","-8","3.9","abc",""]

for sample in text:
    print(f" {repr(sample)} -> {safe_int(sample)}")


print("\n")

# Part C

num1 = safe_int(input("Enter the first number: "))
num2 = safe_int(input("Enter the second number: ")) 

if num1 is None or num2 is None: 
    print("Please enter valid numbers!") 
else:
    
    print("Sum =", num1 + num2)