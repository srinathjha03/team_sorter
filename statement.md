Objective:
This program takes a list of players along with their associated skill levels (1-10) and divides them into two teams (Team A and Team B). The objective remains to make the teams as "fair" as possible by balancing the **total skill points** in each team.

Input:
1. The program will first prompt you to enter the **Player name**.
2. Once you input a name, it will ask for that player's **Skill (1-10)**. The skill must be an integer.
3. The program will continue to ask for new players until you enter **`done`** when prompted for a player's name.

> **Note:** If you enter a non-integer for skill, such as "five," the program displays an error and asks you to re-enter the skill for that same player.

Balancing Algorithm:
1. **Sorting:** It first collects all players and then sorts them in descending order-from **highest skill to the lowest skill.

2.  **Assign:** It then iterates through this sorted list one player at a time.

3. **Balance:** For any player, it compares the current total skill score of Team A and Team B. The player is assigned to whichever team has the **lower total score** at that moment.

This process ensures that the highest-skilled players are distributed first, and the subsequent players are used to "catch up" the score of the trailing team, minimizing the final difference.
.

Output
After all the players have been assigned, the program will output:
1. **Team A:** A list of all players in Team A, with their individual skills, and the total combined skill score of the team. 
2. **Team B:** A similar list for Team B and its total score.
3. **Difference:** It is the final absolute difference between the total scores of Team A and Team B.
