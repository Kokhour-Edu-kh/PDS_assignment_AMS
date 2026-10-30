# Leap Year 


def leapyear(year):
    return (year % 4 == 0 and year % 100 != 0) or year % 400 == 0

def days_in_month(month, year):
    if month < 1 or month > 12:
        return None
    elif month == 2:
        return 29 if leapyear(year) else 28
    elif month in (4, 6, 9, 11):
        return 30
    else:
        return 31


#  years
years = [1905, 2010, 2034, 2026]

for year in years:
    print(f"{year} is a leap year: {leapyear(year)}")


# the number of days in a month
print("\nDays in February 2014:", days_in_month(2, 2014))
print("Days in February 2026:", days_in_month(2, 2026))
print("Days in April 2024:", days_in_month(4, 2024))
print("Day in August 2022:", days_in_month(8,2022))
print("month 13:", days_in_month(13, 2024))


#Count leap years from 2000 to 2100
count = 0

for year in range(2000, 2101):
    if leapyear(year):
        count += 1

print("\nNumber of leap years:", count)