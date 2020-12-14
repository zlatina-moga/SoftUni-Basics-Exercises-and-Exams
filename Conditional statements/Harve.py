vineyard_area = int(input())
grape_per_square = float(input())
needed_liters = int(input())
workers = int(input())

harvest_per_vine = vineyard_area * grape_per_square * 0.4
vine = harvest_per_vine / 2.5

import math
if needed_liters < vine:
    vine_left = vine - needed_liters
    print(f"Good harvest this year! Total wine: {vine} liters.".format(math.floor(vine_left)))

else:
    diff = needed_liters - vine
    diff = math.floor(diff)
    print(f"It will be a tough winter! More {diff} liters wine needed.")
