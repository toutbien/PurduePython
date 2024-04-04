#measure_it.py
#Lisa Stanley
#formulate a script
#April 3, 2024

#import thy libraries
import math

#ask the user for a length of a segment
length = float(input("Enter a length of a segment: "))

#perform input validation
while length <= 0:
  length = float(input("Enter a length of a segment: "))
  if length > 0:
    break
  print("The segment should be greater than zero.")

#Calculate a circle's area rounded to 2 decimal points
area = math.pi * length ** 2
area = round(area,2)
print("area of a circle =" , area)

#Calculate the area of a triangle rounded to 3 decimcal places
area = (math.sqrt(3)/4)*length**2
area = round(area,3)
print("area of a triangle =", area)

#calculate the area of a square rounded to 4 decimal places
area = length**2
area = round(area,4)
print('area of the square is =', area)

#calculate the area of a pentagon rounded to 5 decimals
area = 1/4 *math.sqrt(5 * (5 + 2 * math.sqrt(5))) + length **2
area = round(area, 5)
print("area of the pentagon is =", area)