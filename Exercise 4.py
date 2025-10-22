"""
EXERCISE 4
"""

# Ask the user a single question
answer = input("What is the capital of France? ")

# Check the answer (ignore capitalization)
if answer.strip().lower() == "paris":
    print("Correct! 🎉")
else:
    print("Wrong! ❌ The correct answer is Paris.")
    
    # Dictionary of countries and their capitals
quiz = {
    "France": "Paris",
    "Germany": "Berlin",
    "Italy": "Rome",
    "Spain": "Madrid",
    "Portugal": "Lisbon",
    "Netherlands": "Amsterdam",
    "Belgium": "Brussels",
    "Sweden": "Stockholm",
    "Norway": "Oslo",
    "Greece": "Athens"
}

score = 0  # To keep track of correct answers

# Shuffle questions so they appear in random order
countries = list(quiz.keys())

# Loop through each country
for country in countries:
    answer = input(f"What is the capital of {country}? ")
    
    # Check answer (case-insensitive)
    if answer.strip().lower() == quiz[country].lower():
        print("Correct! 🎉\n")
        score += 1
    else:
        print(f"Wrong! ❌ The correct answer is {quiz[country]}.\n")

# Display total score at the end
print(f"Quiz completed! You got {score} out of {len(quiz)} correct.") 