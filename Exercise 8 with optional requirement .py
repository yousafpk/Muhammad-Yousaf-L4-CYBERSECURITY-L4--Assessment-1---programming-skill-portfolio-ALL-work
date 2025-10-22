"""
Exercise 8 
"""

# Initialize the list of names
names = ["Jake", "Zac", "Ian", "Ron", "Sam", "Dave"]

# Predefined search term
search_name = "Sam"

# Search for the name
if search_name in names:
    print(f"{search_name} was found in the list.")
else:
    print(f"{search_name} was not found in the list.")

# OPTIONAL REQUIREMENTS 

# Allow user to input the search term
user_input = input("\n(Optional) Enter a name to search: ")

# Implement search based on user input
if user_input in names:
    print(f"{user_input} was found in the list.")
else:
    print(f"{user_input} was not found in the list.")
    
    
    
