while True:
    destination = input()
    if destination == "End":
        break

    cost = int(input())
    budget = 0

    while cost > budget:
        budget += int(input())
    print(f"Going to {destination}!")


