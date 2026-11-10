# Hangman Game – Word Guessing Game Using Python

**Python Programming Internship – Task 1**

---

## 1. Project Description

The **Hangman Game** is an interactive, text-based word guessing game developed in Python for the terminal/console environment. In this game, the computer selects a secret word at random from a predefined list of words, and the player attempts to guess the secret word letter by letter within a limited number of allowed incorrect attempts (6 attempts).

The game reveals the letters in their correct positions as the user makes correct guesses, keeps track of already guessed letters, rejects invalid entries (such as numbers, special symbols, or multiple letters) without penalty, and provides a replay mechanism once the game concludes.

---

## 2. Project Objectives

- **Develop a command-line game** without relying on complex frameworks or graphical interfaces.
- **Implement core programming logic** such as loops, conditional statements, and collections.
- **Apply Python's standard library** (`random` module) for dynamic word selection.
- **Ensure robust input validation** to prevent program crashes from user error.
- **Maintain clean, readable, beginner-friendly code** with clear comments explaining each section.

---

## 3. Key Features

- **Predefined Word Bank:** Contains exactly 5 predefined words (`apple`, `mango`, `python`, `school`, `flower`).
- **Randomized Word Selection:** Uses Python's built-in `random.choice()` function to ensure unpredictability for each round.
- **Dynamic Word Display:** Displays underscores representing hidden letters and reveals correctly guessed letters in their exact positions (e.g., `_ _ _ _ _` -> `A P P _ _`).
- **Attempt Tracking & Guess Feedback:**
  - Displays `"Correct Guess!"` when a letter is found.
  - Displays `"Wrong Guess!"` and reduces remaining attempts when a letter is not in the word.
  - Limits incorrect guesses to a maximum of 6.
  - Displays remaining attempts before every turn.
- **Comprehensive Input Validation:**
  - Converts all inputs to lowercase for seamless case-insensitivity.
  - Rejects numbers, special characters, blank lines, and multiple letters without deducting attempts.
  - Detects repeated letters and informs the player without deducting attempts.
- **Win & Game Over Handling:**
  - Congratulates the user and displays the full secret word upon winning.
  - Declares `"GAME OVER!"` and reveals the secret word if all 6 attempts are exhausted.
- **Replay Option:** Allows users to play multiple rounds in a single session without having to restart the script.

---

## 4. Python Concepts Used

| Concept | Application in Project |
| :--- | :--- |
| **`random` module** | Used `random.choice()` to pick one secret word at random from the predefined list. |
| **`while` loop** | Used to run the guessing loop until the player wins or exhausts 6 attempts, and used in the replay mechanism. |
| **`if-else` statements** | Evaluates input validity, checks whether a letter was already guessed, verifies correct vs. incorrect guesses, and determines win/loss states. |
| **Strings** | Handles word comparison, letter case conversion (`.lower()`, `.strip()`), alphabetic checking (`.isalpha()`), and display string formatting. |
| **Lists** | Stores the predefined word bank (`words = [...]`) and keeps an active history of all valid guessed letters (`guessed_letters = [...]`). |
| **Input / Output** | Interacts with the user via formatted terminal output (`print()`) and console input prompts (`input()`). |

---

## 5. Requirements

- **Python Version:** Python 3.6 or higher.
- **External Dependencies:** None. The project strictly uses Python's built-in standard library (`random`, `sys`, `unittest`).

---

## 6. How to Run the Project

### Step 1: Open Terminal / Command Prompt
Open your terminal (macOS/Linux) or Command Prompt / PowerShell (Windows).

### Step 2: Navigate to Project Directory
```bash
cd /Users/asiyaimran/.gemini/antigravity/scratch/hangman_project
```

### Step 3: Run the Game
```bash
python3 hangman.py
```
*(On Windows systems where Python 3 is mapped to `python`, execute `python hangman.py`)*

### Step 4 (Optional): Run the Unit Tests
To verify all game logic and edge cases:
```bash
python3 test_hangman.py
```

---

## 7. Sample Terminal Output

### Scenario A: Winning the Game

```text
================================
      WELCOME TO HANGMAN        
================================
Instructions:
- Guess one letter at a time.
- You have 6 incorrect attempts.
- Try to guess the secret word!
================================

Word: _ _ _ _ _
Remaining Attempts: 6
Enter your guess: a
Correct Guess!

Word: A _ _ _ _
Remaining Attempts: 6
Enter your guess: p
Correct Guess!

Word: A P P _ _
Remaining Attempts: 6
Enter your guess: l
Correct Guess!

Word: A P P L _
Remaining Attempts: 6
Enter your guess: e
Correct Guess!

================================
Word: A P P L E
Congratulations! YOU WIN!
The secret word was: APPLE
================================

Do you want to play again? (yes/no): no

Thank you for playing Hangman!
```

---

### Scenario B: Input Validation & Game Over

```text
================================
      WELCOME TO HANGMAN        
================================
Instructions:
- Guess one letter at a time.
- You have 6 incorrect attempts.
- Try to guess the secret word!
================================

Word: _ _ _ _ _
Remaining Attempts: 6
Enter your guess: 12
Invalid input! Please enter a single alphabetical letter.

Word: _ _ _ _ _
Remaining Attempts: 6
Enter your guess: z
Wrong Guess!

Word: _ _ _ _ _
Remaining Attempts: 5
Enter your guess: z
You have already guessed 'Z'. Try a different letter!

Word: _ _ _ _ _
Remaining Attempts: 5
Enter your guess: x
Wrong Guess!

Word: _ _ _ _ _
Remaining Attempts: 4
Enter your guess: q
Wrong Guess!

Word: _ _ _ _ _
Remaining Attempts: 3
Enter your guess: w
Wrong Guess!

Word: _ _ _ _ _
Remaining Attempts: 2
Enter your guess: r
Wrong Guess!

Word: _ _ _ _ _
Remaining Attempts: 1
Enter your guess: k
Wrong Guess!

================================
GAME OVER!
Remaining Attempts: 0
The secret word was: MANGO
================================

Do you want to play again? (yes/no): no

Thank you for playing Hangman!
```

---

## 8. Project Structure

```text
hangman_project/
├── hangman.py          # Main executable Python program
├── test_hangman.py     # Automated unit test suite verifying all requirements
├── requirements.txt    # Project dependencies (Standard library only)
└── README.md           # Complete project documentation and guide
```
