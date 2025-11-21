Tic-Tac-Toe Game (Python Project)
------------------------------------------

1. Introduction
---------------
This project is a simple, beginner-friendly Tic-Tac-Toe game created using Python.
It runs in the console and allows two players (X and O) to play by entering
positions from 1 to 9. The game demonstrates basic Python concepts such as
lists, loops, functions, and conditional statements.

2. How the Game Works
----------------------
- The game uses a list with 9 elements to represent the 3x3 board.
- A function prints the board after every move so players can see the updated grid.
- Players enter a number (1–9) to place their symbol (X or O).
- The program checks if the chosen spot is empty. If not, the player must try again.
- After every move, the game checks if the current player has won.
- The game switches turns between Player X and Player O.
- If all 9 spots are filled with no winner, the game ends in a draw.

3. Winning Logic
----------------
The game checks 8 possible winning combinations:
- 3 rows
- 3 columns
- 2 diagonals

If any of these contain the same symbol three times in a row, that player wins.

4. How to Run the Game
-----------------------
1. Install Python (if not installed).
2. Save the script as: tic_tac_toe.py
3. Open Command Prompt or Terminal.
4. Run the game using:

   python tic_tac_toe.py

5. Follow the instructions displayed on screen.

5. What You Learn From This Project
---------------------------------
- How to store game data using a Python list
- How to create and call functions
- How loops and conditions control the game flow
- How user input is handled and validated
- How basic game logic is built

6. File Structure
-----------------
project-folder/
│
├── tic_tac_toe.py
└── README.txt

7. Conclusion
-------------
This project is perfect for beginners learning Python. It covers all the basic
concepts while building something fun and interactive. You can expand this game
later with features like an AI opponent, a GUI using Tkinter, or a scoreboard.
