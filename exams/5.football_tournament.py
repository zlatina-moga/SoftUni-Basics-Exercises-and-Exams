name = input()
games = int(input())
points = 0
W_counter = 0
D_counter = 0
L_counter = 0

for game in range(games):
    outcome = input()
    if outcome == "W":
        points += 3
        W_counter += 1
    elif outcome == "D":
        points += 1
        D_counter += 1
    elif outcome == "L":
        L_counter += 1
if games == 0:
    print(f"{name} hasn't played any games during this season.")
else:
    print(f"{name} has won {points} points during this season.")
    print(f"Total stats:")
    print(f"## W: {W_counter}")
    print(f"## D: {D_counter}")
    print(f"## L: {L_counter}")
    print(f"Win rate: {W_counter/games*100:.2f}%")
