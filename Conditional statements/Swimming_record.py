record = float(input())
distance = float(input())
swim_meter_distance = float(input())

import math
time_needed = distance * swim_meter_distance
delay = (distance / 15)
delay = math.floor(delay)
delay = delay * 12.5
total_time = time_needed + delay

if total_time < record:
    print(f"Yes, he succeeded! The new world record is {total_time:.2f} seconds.")
else:
    print(f"No, he failed! He was {abs(total_time - record):.2f} seconds slower.")