steps_home = 0
total_steps = 0

while total_steps < 10000:
    line = input()


    if line == "Going home":
        steps_home = int(input())
        total_steps += steps_home
        break
        
    else:
        total_steps += int(line)

if total_steps >= 10000:
    print(f"Goal reached! Good job!")
    print(f"{abs(total_steps-10000)} steps over the goal!")
else:
    print(f"{abs(10000 - total_steps)} more steps to reach goal.")


