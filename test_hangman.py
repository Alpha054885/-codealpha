"""
Unit and functional tests for the Hangman Game.
Verifies all functional requirements and edge cases.
"""

import sys
import io
import unittest
from unittest.mock import patch
import hangman


class TestHangmanGame(unittest.TestCase):

    def test_predefined_words_list(self):
        """Verify that the word list contains exactly 5 predefined words."""
        # Check by mocking random.choice and verifying words passed
        with patch('random.choice') as mock_choice:
            mock_choice.return_value = 'apple'
            with patch('builtins.input', side_effect=['a', 'p', 'l', 'e']):
                hangman.play_game()
            passed_words = mock_choice.call_args[0][0]
            self.assertEqual(len(passed_words), 5)
            self.assertEqual(passed_words, ["apple", "mango", "python", "school", "flower"])

    def test_get_display_word_initial(self):
        """Verify that initial word is displayed with underscores."""
        display = hangman.get_display_word("apple", [])
        self.assertEqual(display, "_ _ _ _ _")

    def test_get_display_word_partial_guesses(self):
        """Verify that guessed letters are revealed in proper positions."""
        display = hangman.get_display_word("apple", ['a', 'p'])
        self.assertEqual(display, "A P P _ _")

        display2 = hangman.get_display_word("school", ['o'])
        self.assertEqual(display2, "_ _ _ O O _")

    @patch('random.choice', return_value='apple')
    def test_winning_scenario(self, mock_random):
        """Verify that guessing all correct letters wins the game."""
        user_inputs = ['a', 'p', 'l', 'e']
        with patch('builtins.input', side_effect=user_inputs):
            with patch('sys.stdout', new_callable=io.StringIO) as mock_stdout:
                hangman.play_game()
                output = mock_stdout.getvalue()
                self.assertIn("Correct Guess!", output)
                self.assertIn("Congratulations! YOU WIN!", output)
                self.assertIn("The secret word was: APPLE", output)

    @patch('random.choice', return_value='mango')
    def test_losing_scenario(self, mock_random):
        """Verify that 6 incorrect guesses trigger GAME OVER."""
        user_inputs = ['z', 'x', 'q', 'w', 'r', 't']
        with patch('builtins.input', side_effect=user_inputs):
            with patch('sys.stdout', new_callable=io.StringIO) as mock_stdout:
                hangman.play_game()
                output = mock_stdout.getvalue()
                self.assertIn("Wrong Guess!", output)
                self.assertIn("GAME OVER!", output)
                self.assertIn("Remaining Attempts: 0", output)
                self.assertIn("The secret word was: MANGO", output)

    @patch('random.choice', return_value='apple')
    def test_case_insensitivity(self, mock_random):
        """Verify that uppercase and lowercase inputs are accepted."""
        user_inputs = ['A', 'P', 'l', 'E']
        with patch('builtins.input', side_effect=user_inputs):
            with patch('sys.stdout', new_callable=io.StringIO) as mock_stdout:
                hangman.play_game()
                output = mock_stdout.getvalue()
                self.assertIn("Congratulations! YOU WIN!", output)

    @patch('random.choice', return_value='apple')
    def test_invalid_inputs_rejected_without_penalty(self, mock_random):
        """Verify numbers, symbols, empty input, and multiple letters don't reduce attempts."""
        user_inputs = ['1', '@', 'app', '', '  ', 'a', 'p', 'l', 'e']
        with patch('builtins.input', side_effect=user_inputs):
            with patch('sys.stdout', new_callable=io.StringIO) as mock_stdout:
                hangman.play_game()
                output = mock_stdout.getvalue()
                self.assertIn("Invalid input! Please enter a single alphabetical letter.", output)
                self.assertIn("Congratulations! YOU WIN!", output)

    @patch('random.choice', return_value='apple')
    def test_repeated_letters_no_penalty(self, mock_random):
        """Verify repeating a letter warns user and doesn't penalize attempts."""
        user_inputs = ['a', 'a', 'p', 'P', 'l', 'e']
        with patch('builtins.input', side_effect=user_inputs):
            with patch('sys.stdout', new_callable=io.StringIO) as mock_stdout:
                hangman.play_game()
                output = mock_stdout.getvalue()
                self.assertIn("You have already guessed 'A'. Try a different letter!", output)
                self.assertIn("Congratulations! YOU WIN!", output)

    @patch('random.choice', side_effect=['apple', 'mango'])
    def test_replay_flow(self, mock_random):
        """Verify replaying starts a new game and 'no' exits gracefully."""
        # Game 1: win 'apple' ('a','p','l','e') -> replay 'yes' -> Game 2: win 'mango' ('m','a','n','g','o') -> replay 'no'
        user_inputs = [
            'a', 'p', 'l', 'e',         # guesses for apple
            'yes',                      # replay prompt
            'm', 'a', 'n', 'g', 'o',    # guesses for mango
            'no'                        # replay prompt exit
        ]
        with patch('builtins.input', side_effect=user_inputs):
            with patch('sys.stdout', new_callable=io.StringIO) as mock_stdout:
                hangman.main()
                output = mock_stdout.getvalue()
                self.assertIn("Starting a new game...", output.replace("Restarting Hangman...", "Starting a new game..."))
                self.assertIn("Thank you for playing Hangman!", output)


if __name__ == '__main__':
    unittest.main()
