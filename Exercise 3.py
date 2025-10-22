"""
exercise 3
"""

# Create a dictionary to store personal information
person = {
    "name": "Mohammed Yousaf",
    "hometown": "Dubai",
    "age": 16
}

# Print all values on separate lines using one print statement
print(person["name"], person["hometown"], person["age"], sep="\n")

#Advance requirment 
# Ask the user for their name, hometown, and age
name = input("Enter your full name: ")           # Accepts multiple words
hometown = input("Enter your hometown: ")

# Handle invalid age input
while True:
    try:
        age = int(input("Enter your age: "))     # Converts input to integer
        break
    except ValueError:
        print("Please enter a valid number for age!")

# Store in a dictionary
person = {
    "name": name,
    "hometown": hometown,
    "age": age
}

# Print values on separate lines
print(person["name"], person["hometown"], person["age"], sep="\n")