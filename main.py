"""
Number Guessing Game
A console-based Python game where the user tries to guess a randomly 
generated number between 1 and 100. Includes error handling for bad 
inputs and tracks the total number of attempts.
"""

import random


# Handles a single round of the guessing game
def playRound():

    attempts = 0
    # Generate a random integer between 1 and 100 (inclusive)
    computerNumber = random.randint(1, 100) 
    
    while True:
        # Error handling: Ensure the user enters a valid integer
        try:
            userNumber = int(input("Guess a number between 1 to 100 (Enter -1 to quit): "))
        except ValueError:
            print("Invalid input! Please enter a whole number.")
            continue # Skip the rest of the loop and prompt the user again
        
        # Check for the exit condition first
        if userNumber == -1:
            print("Quitting this round...")
            print(f"The number was {computerNumber}")
            return

        attempts += 1 

        # Evaluate the guess and provide feedback
        if userNumber == computerNumber:
            print("Hurray! You have correctly guessed the number.")
            break 
        elif userNumber > computerNumber:
            print("Enter a lower number.")
        else:
            print("Enter a higher number.")
    
    # Display round statistics after a successful guess
    print(f"The number was {computerNumber}")
    print(f"No. of attempts: {attempts}")



# Allows the user to play multiple rounds continuously till they choose to stop
def play():

    choice = 'y'

    while choice.lower() == 'y': 
        playRound()
        choice = input("\nWant to play another round? (Y/N): ")

    print("Thanks for playing!")


# Ensure the game only runs if the script is executed directly 
# (not if it is imported as a module into another script)
if __name__ == "__main__":
    play()