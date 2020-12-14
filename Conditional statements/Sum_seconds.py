competitor_1 = int(input())
competitor_2 = int(input())
competitor_3 = int(input())

total_time = competitor_1 + competitor_2 + competitor_3

minutes = total_time / 60
seconds = total_time % 60

import math
minutes = math.floor(minutes)

if seconds < 10:
    print(f"{minutes}:0{seconds}")
else:
    print(f"{minutes}:{seconds}")