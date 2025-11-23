 Fair Team Generator

A simple Python tool designed to solve the real-life problem of creating balanced sports teams for pickup games or PE classes.

 Problem It Solves:

In casual sports (football, basketball, volleyball), picking teams manually often leads to one side being much stronger than the other. This script distributes skill evenly, ensuring a fair and competitive match.

How to Run:

Ensure you have Python installed.
Download fair_teams.py.
Open your terminal or command prompt.

Usage:

Enter a player's Name.
Enter their Skill Level (1 to 10).
Repeat for all players.
Type done when finished adding players.
The program will instantly calculate and display two balanced teams (Team A and Team B) and show the total skill difference.

 How it Works:
Data Collection: The program collects a list of players and their skill ratings.
Sorting: It sorts all players from strongest to weakest.
Distribution: It iterates through the sorted list and assigns the next player to whichever team currently has the lower total skill score. This minimizes the skill gap between the two sides.
