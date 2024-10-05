# Mastermind
Repository for my Year 12 CS Mastermind Project

There are 3 working versions
* v1: Basic game
* v1.1: Adds a main menu and local save/load game functionality
* v2: Adds a score (linked to the number of rows used and the time taken), and created an account and global leaderboard system

The Client GUI is written in Pygame and KivyMD. 

You can see the remote backend server repo (for v2) (implemented using Flask and MongoDB) [here](https://github.com/tjfacos/mastermind_server_flask)

TO START/RUN GAME (V2):
* Use "pip install -r requirements.txt"
* You can run sign_in.py to create, sign in or sign out of an account.
* If your already signed in, they you can run main.py directly

Written by Thomas Facos, SLBS
