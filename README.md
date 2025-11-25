Project Summary: Fair Team Sorter

🎯 1. Overview

The "Fair Team Segregator" is a command-line tool built in Python. Its goal is to address the widespread issue of assembling balanced teams for games or sports. The tool allows an organizer to enter a list of players and assign a numerical skill rating (1–10) to each.

🤔 2. Problem Description

The project tackles the problem of manually selected teams, which are often slow to form, subject to social bias, and frequently result in lopsided, unfair matchups. This imbalance can lead to frustration and unengaging activities. This tool provides a fast, simple, and objective alternative.

⚙️ 3. Essential Features & Algorithm

The program follows a straightforward workflow:

The user iteratively inputs player names and their corresponding skill levels.

Once data entry is complete (signaled by typing 'done'), the system employs a greedy algorithm.

It first sorts all players in descending order by their skill rating.

It then iterates through this sorted list, adding each player one by one to whichever of the two teams currently has the lower total skill score.

Finally, it displays the rosters for Team A and Team B, their total skill scores, and the absolute difference between them, ensuring a fair matchup.

💡 4. Important Takeaways & Upcoming Improvements

This project was a great learning experience! Here’s what we discovered and what could come next.

Key Takeaways:

Simple Solutions Win: A "greedy algorithm" sounds complex, but it's just a simple idea: "make the best choice right now." This simple heuristic (sorting players and adding them to the lower-score team) gives a fast and very effective solution to a tough problem (the "partition problem").

The Power of Sorting: The most important part of the whole program is the sort() function. By sorting the players first (from highest to lowest skill), the rest of the logic becomes incredibly simple and effective. It shows that preparing your data is often half the battle.

Defensive Programming is Crucial: Using try-except blocks to catch errors (like a user typing "five" instead of "5") is vital. It's the difference between a program that crashes and feels broken, and a program that is friendly, robust, and reliable.

Future Enhancements:

🚀 Make it a Web App: Rebuild this as a simple, good-looking website (using HTML/CSS/JS) so anyone can use it without needing to run a Python script.

💾 Save Player Lists: Add a feature to save and load player lists (maybe using Firestore or a simple file) so the organizer doesn't have to re-type everyone's name and skill for every game.

🔄 More Than Two Teams: Update the algorithm to be more flexible, allowing the user to split players into 3, 4, or even more teams.
