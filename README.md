# CLI Minesweeper Game

This is a command-line interface (CLI) implementation of the classic Minesweeper game using Python's object-oriented programming (OOP) concepts.

## Files

The game consists of the following Python files:

1. `main.py`: The main entry point of the game, responsible for initializing and running the game menu.
2. `game.py`: Defines the `Game` class responsible for the game's logic and mechanics.
3. `log.py`: Contains the `Log` class, which manages the leaderboard and player data.
4. `menu.py`: Defines the `Menu` class, handling the game menu, user interactions, and navigation.
5. `scoreboard.py`: Implements the `Scoreboard` class for tracking and updating player scores.

## How to Play

1. Run the game by executing `main.py` in your terminal.

2. You will be presented with a menu that includes options for login, signup, accessing the scoreboard, and exiting the game.

3. Choose "Login" if you have an existing account or "Signup" to create a new one. Provide your username and password to proceed.

4. Once logged in, you can select a game mode: Easy, Medium, or Hard. The Minesweeper game will start, and you'll interact with it by entering commands like "step" or "flag" followed by row and column coordinates.

5. Try to reveal as many safe squares as possible without triggering any bombs. Identify the number of bombs adjacent to each square based on the displayed numbers.

6. Your goal is to score points by revealing safe squares. Your score is updated in real-time.

7. After the game, you can access the scoreboard to view the top players and their high scores. If you beat your previous high score, it will be updated automatically.

8. You can return to the main menu at any time or exit the game when you're done.

## Game Rules

- Reveal safe squares by selecting "step." The number in a square indicates how many bombs are adjacent.
- Use "flag" to mark squares you suspect contain bombs.
- Be cautious and strategic to avoid bombs. Stepping on a bomb square ends the game.
- Your goal is to reveal all safe squares and achieve the highest score.

## Dependencies

This Minesweeper game relies on Python and the `pandas` library for data manipulation. Ensure you have Python installed on your system.

## Notes

- This game is intended for educational and entertainment purposes.
- The provided code can be extended and customized further to enhance gameplay, add features, and improve user experience.
