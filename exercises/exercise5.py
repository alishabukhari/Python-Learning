#hypotenuse of a triangle

import math
side = float(input("Enter the side of the trangle: "))
base = float(input("Enter the base of the triangle: "))
hypotenuse = math.sqrt(pow(side,2) + pow(base,2))

print(f"The hypotenuse of the triangle is {hypotenuse}cm")