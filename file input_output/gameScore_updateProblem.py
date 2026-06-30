'''The game() function in a program lets a user play a game and returns the score as an integer. 
You need to read a file ‘Hi-score.txt’ which is either blank or contains the previous Hi-score.
 You need to write a program to update the Hi-score whenever the game() function breaks the Hi-score.'''



# Function that returns the player's score
def game():
    return 95        # Example score

# Get the current score
score = game()

# Open the file in read mode
with open("Hi-score.txt", "r") as file:
    high_score = file.read()

# If the file is blank, set high score to 0
if high_score == "":
    high_score = 0
else:
    high_score = int(high_score)

# Compare current score with high score
if score > high_score:
    # Open the file in write mode and update the high score
    with open("Hi-score.txt", "w") as file:
        file.write(str(score))

print("Current Score:", score)
print("Previous High Score:", high_score)