"""
Python Web Development Techdegree
Project 1 - Number Guessing Game
--------------------------------

For this first project we will be using Workspaces. 

NOTE: If you strongly prefer to work locally on your own computer, you can totally do that by clicking: File -> Download Workspace in the file menu after you fork the snapshot of this workspace.

"""

import random


def start_game():
    """Psuedo-code Hints
    
    When the program starts, we want to:
    ------------------------------------
    1. Display an intro/welcome message to the player.
    2. Store a random number as the answer/solution.
    3. Continuously prompt the player for a guess.
      a. If the guess greater than the solution, display to the player "It's lower".
      b. If the guess is less than the solution, display to the player "It's higher".
    
    4. Once the guess is correct, stop looping, inform the user they "Got it"
         and show how many attempts it took them to get the correct number.
    5. Let the player know the game is ending, or something that indicates the game is over.
    
    ( You can add more features/enhancements if you'd like to. )
    """
    # write your code inside this function.
    print("Welcome to the number guessing game!\n")

    # Create Loop and set variables
    repeat = 0
    HighScore = 0
    GoAgain = "y"
    while GoAgain == "y":
        # Displays the high score (Even on the first go)
        if HighScore == 0 or repeat < HighScore:
            HighScore = repeat

        # Random number
        win = random.randint(1, 10)
        print("The high score is {}. Good Luck!".format(HighScore))

        repeat = 0

        TryAgain = "y"
        while TryAgain == "y":
            # Prompt user
            repeat += 1
            guess_number = input("Pick a number between 1 and 10!: ")
            # Check to see if the number is an integer
            if guess_number.isdigit():
                guess_number = int(guess_number)
                if guess_number < 0 or guess_number > 10:
                    print("Please pick a valid number.")
                else:
                    if guess_number > win:
                        print("It's lower!")
                    elif guess_number < win:
                        print("It's higher!")
                    else:
                        print("You win!")
                        print("You guessed the right number in {} tries! Good job!".format(repeat))
                        break
            else:
                print("Please pick a valid number.")

        # Validates if the user would like to play again
        yorn = 0
        while yorn == 0:
            GoAgain = input("Would you like to play again? (y/n): ").lower()
            if GoAgain == "":
                print("Please enter a y or n.")
            else:
                GoAgain = GoAgain[0]
                if GoAgain == "y" or GoAgain == "n":
                    yorn = 1
                else:
                    print("Please enter a y or n.")


# Kick off the program by calling the start_game function.
start_game()
print("Thanks for playing!")
