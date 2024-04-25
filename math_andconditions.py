#Maths And Things
# This program should handle the following cases:
#If either a or b is not a numeric value, handle the TypeError with an appropriate error message.
#If the denominator is zero (i.e. a = b), handle the ZeroDivisionError with an appropriate error message.
#Your function should return the result of the operation if the input arguments are valid.

# Define the variables a and b
a = 5
b = 3

# Calculate the result of a squared + b squared divided by (a - b)squared
result = (a**2 + b**2) / (a - b)**2

# Print the result
print(f"The result of a squared + b squared divided by (a - b)squared is {result}")
