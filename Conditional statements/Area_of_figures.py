a = input()
import math
from math import pi

if a == "square":
    b = float(input())
    print(f"{b * b:.3f}")

if a == "rectangle":
    b = float(input())
    c = float(input())
    print(f"{b * c:.3f}")

if a == "circle":
    b = float(input())
    print(f"{pi * b * b:.3f}")

if a == "triangle":
    b = float(input())
    c = float(input())
    print(f"{(b * c) / 2:.3f}")