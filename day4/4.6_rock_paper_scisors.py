import random

rock = '🪨'
paper = '📄'
scissors = '✂️'

# User input
user = input("Choose your input: rock, paper, or scissors: ").lower()

# Convert user input to emoji
if user == "rock":
    user = rock
elif user == "paper":
    user = paper
elif user == "scissors":
    user = scissors
else:
    print("Invalid input. Please choose rock, paper, or scissors.")
    exit()

print(f"You chose: {user}")

# Computer choice
choices = [rock, paper, scissors]
computer = random.choice(choices)
print(f"Computer chose: {computer}")

# Determine the winner
if user == computer:
    print("Tie")
elif (user == rock and computer == scissors) or (user == paper and computer == rock) or (user == scissors and computer == paper):
    print("You win!")
else:
    print("Computer wins!")
