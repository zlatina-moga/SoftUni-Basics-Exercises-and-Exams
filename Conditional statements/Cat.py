off_days = int(input())

week_play = (365 - off_days) * 63
weekend_play = off_days * 127
total_play = week_play + weekend_play

difference = abs(30000 - total_play)
hours = difference // 60
minutes = difference % 60

if total_play >= 30000:
    print(f"Tom will run away")
    print(f"{hours} hours and {minutes} minutes more for play")
else:
    print(f"Tom sleeps well")
    print(f"{hours} hours and {minutes} minutes less for play")