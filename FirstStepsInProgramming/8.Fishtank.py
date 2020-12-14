length = int(input())
width = int(input())
height = int(input())
volume_percentage = float(input())

volume = length * width * height
liters = volume * 0.001
percent = volume_percentage * 0.01
liters_needed = liters * (1 - percent)

print(liters_needed)