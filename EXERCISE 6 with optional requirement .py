"""
EXERCISE 6 
"""

# Define the correct password
correct_password = "12345"

# Ask the user to enter the password for the first time
password = input("Enter the password: ")

# Keep asking until the correct password is entered
while password != correct_password:
    print("Incorrect password. Please try again.")
    password = input("Enter the password: ")

# Output an appropriate message when the correct password is entered
print("Access granted. Welcome!")


"""
optional Requirment
"""


# Define the correct password
correct_password = "12345"

# Define the maximum number of attempts
max_attempts = 5
attempts = 0

# Loop until the user enters the correct password or uses all attempts
while attempts < max_attempts:
    password = input("Enter the password: ")
    attempts += 1

    if password == correct_password:
        print("Access granted. Welcome!")
        break
    else:
        remaining_attempts = max_attempts - attempts
        if remaining_attempts > 0:
            print(f"Incorrect password. You have {remaining_attempts} attempt(s) remaining.")
        else:
            print("Maximum attempts reached. Authorities have been alerted!")
