campaign_days = int(input())
chefs = int(input())
cakes = int(input())
waffles = int(input())
pancakes = int(input())

chef_profit_1 = cakes * 45
chef_profit_2 = waffles * 5.8
chef_profit_3 = pancakes * 3.2

daily_profit = (chef_profit_1 + chef_profit_2 + chef_profit_3) * chefs
campaign_sum = daily_profit * campaign_days
result_sum = campaign_sum - (1/8 * campaign_sum)

print(result_sum)