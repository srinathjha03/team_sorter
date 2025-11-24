def main():
    print(" Fair Team Segregator ")
    players = []

    while True:
        name = input("Player name (or 'done'): ").strip()
        if name.lower() == 'done': break
        try:
            skill = int(input(f"Skill (1-10) for {name}: "))
            players.append({"name": name, "skill": skill})
        except ValueError: print("Please enter a valid integer.")

    players.sort(key=lambda x: x["skill"], reverse=True)

    team_a, team_b = [], []
    score_a, score_b = 0, 0

    for p in players:
        if score_a <= score_b:
            team_a.append(p)
            score_a += p["skill"]
        else:
            team_b.append(p)
            score_b += p["skill"]

    print(f"\n TEAM A (Total: {score_a})")
    for p in team_a: print(f" - {p['name']} ({p['skill']})")

    print(f"\n TEAM B (Total: {score_b})")
    for p in team_b: print(f" - {p['name']} ({p['skill']})")

    print(f"\nDifference: {abs(score_a - score_b)}")

if __name__ == "__main__":
    main()
