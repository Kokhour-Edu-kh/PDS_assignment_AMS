

# Descibe data 

#part A

def describe(*numbers, decimals=2, label="Data"):
    if len(numbers) == 0:
        print(f"{label}: no values")
        return None

    count = len(numbers)
    minimum = min(numbers)
    maximum = max(numbers)
    mean = sum(numbers) / count

    print(f"\n{label} count: {count}")
    print(f"{label} min: {minimum:.{decimals}f}")
    print(f"{label} max: {maximum:.{decimals}f}")
    print(f"{label} mean: {mean:.{decimals}f}")

    return (count, round(minimum, decimals),
            round(maximum, decimals), round(mean, decimals))

describe(12,4,9,70,55,34,28)
describe(3.14159, 2.71828, decimals=3, label="Constants")


#part B

def make_tag(text, **style):
    attributes = ""
    for key, value in style.items():
        attributes += f' {key}="{value}"'

    return f"\n<span{attributes}>{text}</span>"

print(make_tag("Hello", color="red", size=14))

#part C

def square(x):
    return x ** 2
def is_adult(age):
    return age >= 18

print(square(19),is_adult(17),is_adult(67))





