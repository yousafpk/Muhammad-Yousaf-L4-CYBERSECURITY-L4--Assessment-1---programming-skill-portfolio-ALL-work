# Dictionary mapping month numbers to number of days
month_days = {
    1: 31,
    2: 28,
    3: 31,
    4: 30,
    5: 31,
    6: 30,
    7: 31,
    8: 31,
    9: 30,
    10: 31,
    11: 30,
    12: 31
}

# Ask the user for the month number
month = int(input("Enter the month number (1-12): "))

# Check if the month number is valid
if 1 <= month <= 12:
    print(f"The month {month} has {month_days[month]} days.")
else:
    print("Invalid month number! Please enter a number between 1 and 12.")
    
#Advance

# Dictionary mapping month numbers to number of days
month_days = {
    1: 31,
    2: 28,  # Default for February
    3: 31,
    4: 30,
    5: 31,
    6: 30,
    7: 31,
    8: 31,
    9: 30,
    10: 31,
    11: 30,
    12: 31
}

# Ask the user for the month number
month = int(input("Enter the month number (1-12): "))

# Check if the month number is valid
if 1 <= month <= 12:
    # Special check for February (month 2)
    if month == 2:
        leap = input("Is it a leap year? (yes/no): ").strip().lower()
        if leap == "yes":
            print("February has 29 days in a leap year.")
        else:
            print("February has 28 days.")
    else:
        print(f"The month {month} has {month_days[month]} days.")
else:
    print("Invalid month number! Please enter a number between 1 and 12.")
