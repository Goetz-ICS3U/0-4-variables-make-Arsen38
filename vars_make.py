"""
author: Arsen Zymbovych
date: February 12, 2026 
"""

# input
import math 
radius = int(input("Enter the rasius of the circle"))
rect_length = int(input("Enter the length of the rectangle"))
rect_width = int(input("Ener the width of the rectangle"))
oct_side = int(input("Enter the side length of the octagon"))

# processing
circle_area = math.pi * radius * radius 
circle_perimeter = 2 * math.pi * radius 

rect_area = rect_length * rect_width 
rect_perimeter = 2 * (rect_length + rect_width)

oct_area = 2 * (oct_side ** 2) * (1 + math.sqrt(2))
oct_perimeter = 8 * oct_side

# output 

print(f"The circle has an area of {circle_area} and a perimeter of {circle_perimeter}")
print(f"The rectangle has an area of {rect_area} and a perimeter of {rect_perimeter}")
print(f"The octagon has an area of {oct_area} and a perimeter of {oct_perimeter}")