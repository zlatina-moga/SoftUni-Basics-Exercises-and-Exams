hours = int(input())
days = int(input())
extra_workers = int(input())

work_hours = (days - (days * 0.1)) * 8
extra_work = extra_workers * (2 * days)
import math
total_work = work_hours + extra_work
difference = abs(hours - total_work)
difference = math.floor(difference)
diff = abs(total_work - hours)
diff = math.floor(diff)

if total_work >= hours:
    print(f"Yes!{difference} hours left.")
else:
    print(f"Not enough time!{diff} hours needed.")