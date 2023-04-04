#! python3
#
# Surface area of a cone
# Find the surface area of a cone given the height and the radius.
# You will need to ask the user to enter in both variables, and will 
# need to use the Pythagorean relationship to find the slant height. 
# (2 points)
#
# Inputs:
# height, radius
#
# Outputs:
# surface area
#
# Test output
# r = 3
# h = 5
# sa = 83.2297607912

import math

r = float(input("Enter height: "))
h = float(input("Enter radius: "))

slant_height = math.sqrt(h**2 + r**2)
sa = math.pi * r * slant_height + math.pi * r**2
print(f"The surface area of the cone is {sa}")