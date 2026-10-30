# Temparature convertor

def celsius_to_fahrenheit(c, round_to=1):
    return  (c * 9 / 5 )+ 32

def fahrenheit_to_celsius(f,round_to=1):
    return (f - 32) * 5 / 9

print("="*30)
print("\n")

for c in range(0,101,20):
    F =celsius_to_fahrenheit(c)
    print(f"{c} | {F}")

print("\n")
print("="*30)


print(f"\n 98.6F = {fahrenheit_to_celsius(98.6)} c")
