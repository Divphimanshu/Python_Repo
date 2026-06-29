# Import the random module to generate a random choice for the computer
import random

# Dictionary to store the game choices
# Key: Short form entered by the user
# Value: Full name of the choice
choices = {
    's': 'Snake',
    'w': 'Water',
    'g': 'Gun'
}

# Computer randomly selects one option from Snake, Water, or Gun
computer = random.choice(['s', 'w', 'g'])

# Ask the user to enter their choice
# .lower() converts the input to lowercase so that S and s are treated the same
user = input("Enter your choice (s = Snake, w = Water, g = Gun): ").lower()

# Check whether the user entered a valid choice
if user not in choices:
    print("Invalid choice! Please enter s, w, or g.")

# If the input is valid, continue the game
else:
    # Display the user's choice using the dictionary
    print(f"\nYou chose: {choices[user]}")

    # Display the computer's randomly selected choice
    print(f"Computer chose: {choices[computer]}")

    # Check if both user and computer selected the same option
    if user == computer:
        print("It's a Draw!")

    # Check all winning conditions for the user
    # Snake drinks Water → Snake wins
    # Water damages Gun → Water wins
    # Gun kills Snake → Gun wins
    elif (user == 's' and computer == 'w') or \
         (user == 'w' and computer == 'g') or \
         (user == 'g' and computer == 's'):
        print("🎉 You Win!")

    # If none of the above conditions are true,
    # then the computer is the winner
    else:
        print("💻 Computer Wins!")