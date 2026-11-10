"""
=============================================================
Project Title: Hangman Game – Word Guessing Game Using Python
Internship Task: Python Programming Internship Task 1
Description: A beginner-friendly, text-based Hangman game where
             the player guesses a secret word letter by letter.
=============================================================
Python Concepts Used:
1. random module   - To randomly select a secret word from the list.
2. while loop      - To control the game flow and replay mechanism.
3. if-else checks  - To validate user inputs, evaluate guesses, and 
                     determine win/loss conditions.
4. strings         - For word storage, case conversion, and letter display.
5. lists           - To store predefined words and track guessed letters.
6. input/output    - To display game state and receive player guesses.
=============================================================
"""

# Concept 1: random module
import random


def get_display_word(secret_word, guessed_letters):
    """
    Builds the formatted display string for the secret word.
    Reveals letters that have been guessed and shows underscores
    for letters that have not yet been guessed.
    
    Concept 4 (strings) & Concept 5 (lists)
    """
    display_letters = []
    for letter in secret_word:
        if letter in guessed_letters:
            display_letters.append(letter.upper())
        else:
            display_letters.append("_")
    return " ".join(display_letters)


def play_game():
    """
    Runs a single round of the Hangman game.
    Manages secret word selection, turn-by-turn guessing,
    input validation, attempts tracking, and win/loss states.
    """
    # Concept 5: lists - Predefined list of exactly 5 words
    words = ["apple", "mango", "python", "school", "flower"]

    # Concept 1: random module - Select one random word
    secret_word = random.choice(words)

    # Concept 5: lists - List to store all guessed letters
    guessed_letters = []

    # Maximum allowed incorrect attempts
    max_incorrect_attempts = 6
    incorrect_attempts = 0

    # Concept 6: input/output - Display welcome banner and rules
    print("\n" + "=" * 32)
    print("      WELCOME TO HANGMAN        ")
    print("=" * 32)
    print("Instructions:")
    print("- Guess one letter at a time.")
    print(f"- You have {max_incorrect_attempts} incorrect attempts.")
    print("- Try to guess the secret word!")
    print("=" * 32)

    # Concept 2: while loop - Runs until player wins or runs out of attempts
    while incorrect_attempts < max_incorrect_attempts:
        remaining_attempts = max_incorrect_attempts - incorrect_attempts
        display_word = get_display_word(secret_word, guessed_letters)

        # Concept 6: input/output - Display current game state
        print(f"\nWord: {display_word}")
        print(f"Remaining Attempts: {remaining_attempts}")

        # Concept 6: input/output - Receive guess from player
        user_input = input("Enter your guess: ").strip()

        # Concept 3: if-else statements & Concept 4: strings - Input Validation
        # Reject empty input, multiple characters, or non-alphabetical characters
        if len(user_input) != 1 or not user_input.isalpha():
            print("Invalid input! Please enter a single alphabetical letter.")
            continue

        # Convert input to lowercase for case-insensitive matching
        guess = user_input.lower()

        # Check if the letter was already guessed (do not penalize)
        if guess in guessed_letters:
            print(f"You have already guessed '{guess.upper()}'. Try a different letter!")
            continue

        # Add valid new guess to our list of guessed letters
        guessed_letters.append(guess)

        # Concept 3: if-else statements - Evaluate the guess
        if guess in secret_word:
            print("Correct Guess!")
        else:
            print("Wrong Guess!")
            incorrect_attempts += 1

        # Check Winning Condition: all letters revealed
        current_display = get_display_word(secret_word, guessed_letters)
        if "_" not in current_display:
            print("\n" + "=" * 32)
            print(f"Word: {current_display}")
            print("Congratulations! YOU WIN!")
            print(f"The secret word was: {secret_word.upper()}")
            print("=" * 32)
            return

    # Losing Condition: reached when maximum incorrect guesses are reached
    print("\n" + "=" * 32)
    print("GAME OVER!")
    print(f"Remaining Attempts: 0")
    print(f"The secret word was: {secret_word.upper()}")
    print("=" * 32)


def main():
    """
    Main program entry point with replay option.
    Concept 2: while loop for restarting the game.
    """
    try:
        while True:
            play_game()

            # Replay Option prompt (Concept 2: while loop & Concept 3: if-else)
            while True:
                replay_choice = input("\nDo you want to play again? (yes/no): ").strip().lower()
                if replay_choice in ["yes", "y"]:
                    print("\nStarting a new game...")
                    break
                elif replay_choice in ["no", "n"]:
                    print("\nThank you for playing Hangman!")
                    return
                else:
                    print("Invalid input. Please enter 'yes' or 'no'.")
    except (KeyboardInterrupt, EOFError):
        print("\n\nGame exited. Thank you for playing Hangman!")


if __name__ == "__main__":
    main()
