"""
exercise 10
"""
# This function checks whether a number is even or odd
def check_even_odd(number):
    # If the number is divisible by 2 (remainder 0), it’s even
    if number % 2 == 0:
        return f"The number {number} is even."
    else:
        # Otherwise, it’s odd
        return f"The number {number} is odd."

# The main function controls the flow of the program
def main():
    # Ask the user to enter a number and convert it to an integer
    num = int(input("Enter a number: "))
    
    # Call the check_even_odd function and store its result
    result = check_even_odd(num)
    
    # Print the message returned by the function
    print(result)

# This line ensures that main() runs only when this file is executed directly
if __name__ == "__main__":
    main()
