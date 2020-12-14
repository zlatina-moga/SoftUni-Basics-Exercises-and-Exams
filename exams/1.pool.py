people = int(input())
entrance_fee = float(input())
sunbed_fee = float(input())
umbrella_fee = float(input())

import math
entry = entrance_fee * people

umbrella_people = people / 2
umbrella_people = math.ceil(umbrella_people)
umbrella = umbrella_fee * umbrella_people

sunbed_people = people * 0.75
sunbed_people = math.ceil(sunbed_people)
sunbed = sunbed_fee * sunbed_people

total = entry + umbrella + sunbed
print(f"{total:.2f} lv.")