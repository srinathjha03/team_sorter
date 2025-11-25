Fair Team Sorter 

1. Overview
The "Fair Team Segregator" is a Python command-line tool. Its goal is to address the widespread issue of assembling balanced teams for games or sports. An organizer can enter a list of players and give each one a numerical skill rating (1–10) using the tool.

2. Problem Description
The project tackles the problem of manually selected teams, which frequently lead to unfair, lopsided matchups, are slow to form, and are susceptible to social bias. Frustration and boring activities may result from this imbalance. This tool offers a quick, easy, and impartial substitute.
Essential Features & Algorithm

3.The program follows a straightforward workflow:

Player names and skill levels are entered iteratively by the user.

The system uses a greedy algorithm after data entry is finished (marked by typing 'done').

All players are first sorted by skill rating in descending order.

After that, it iterates through this sorted list, adding each player one at a time to the team with the lower total skill score at the moment.

In order to ensure a fair matchup, it lastly shows the rosters for Teams A and B, their total skill scores, and the absolute difference between them.

4. Important Takeaways & Upcoming Improvements
The project shows how a straightforward heuristic (a greedy algorithm) can solve a complicated problem (the "partition problem") quickly and very successfully. Important lessons learned include the value of defensive programming (such as try-except blocks) for user input and the strength of sorting data as a fundamental algorithmic step.

Future improvements might include developing a web-based graphical user interface (GUI), enabling the saving of player lists, and extending the algorithm to enable segregation into more than two teams.
