detergent_bottles = int(input())
detergent_quantity = 750 * detergent_bottles
dishwasher_run = washed_dishes = washed_pots = 0

line = input()

while line != 'End':
    line = int(line)

    dishwasher_run += 1

    if dishwasher_run == 3:
        detergent_quantity -= line * 15
        washed_pots += line
        dishwasher_run = 0
    else:
        detergent_quantity -= line * 5
        washed_dishes += line

    if detergent_quantity < 0:
        print(f'Not enough detergent, {abs(detergent_quantity)} ml. more necessary!')
        break

    line = input()

if detergent_quantity >= 0:
    print(f'Detergent was enough!')
    print(f'{washed_dishes} dishes and {washed_pots} pots were washed.')
    print(f'Leftover detergent {detergent_quantity} ml.')