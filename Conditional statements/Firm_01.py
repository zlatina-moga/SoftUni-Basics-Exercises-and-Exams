hours = int(input())
days = int(input())
extra_work = int(input())

time = (days - (days * 0.1)) * 8
extra_time = (extra_work * 2) * days
total_time = time + extra_time
import math
total_time = math.floor(total_time)

if total_time >= hours:
    diff = abs(hours - total_time)
    print(f"Yes!{diff} hours left.")
else:
    difference = abs(total_time - hours)
    print(f"Not enough time!{difference} hours needed.")