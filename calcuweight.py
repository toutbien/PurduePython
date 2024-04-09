#######################
# Name: Lisa Stanley      
# Course: Python Fundamentals
# Date: 08 April 2024
# Description: This program will get input from a user, product an output, perform simple calculations and make a decision. 
#######################

# ask user to input their height
hv = int(input("Please enter your height in inches: "))

# ask user to input their waist measurement
wv = int(input("Please enter your waist measurement in inches: "))


#validate height and waist measurements with output statements
if hv < 40 or hv > 90:
  print("Invalid height for this program.")

if wv <26 or wv > 60:
  print("Invalid waist measurement for this program.")

#determine the value to represent four categories optimal if his or her waist/height ratio is 45-50%. If the ratio # is < 45 = underweight. If the ratio is # greater than 50 = overweight. If the # ratio is greater than 60 = obese.
calcuweight = wv / hv
if calcuweight >= .45 and calcuweight <= .50:
  print("Your weight is optimal.")
else:
  if calcuweight < .45:
    print("You are potentially underweight.")
  else:
    if calcuweight > .50 and calcuweight < .61:
      print("You are potentially overweight.")
    else:
      if calcuweight >= .60:
        print("You are potentially obese.")
        
print("Thank you for using this program.")


#this can also be solved using elif statements to reduce the use of space above