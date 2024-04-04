###calculate_total.py
###Author: Lisa Stanley
###Date last updated: April 3, 2024
###Purpose: Inform a user of the total meal charge

#receive user input on cost and tip choice
c = float(input("What was the cost of your meal? "))
t = float(input("What is your tip percentage? (i.e. 18, 20, 25)"))

#complete tax and tip calculations
calculate_tax = float(c*.0675)
calculate_tip = (t/100)*c
total_added=(calculate_tip+calculate_tax)

#calculate final total
calculate_total = c+(total_added)
result = float(calculate_total)
print("The cost of your meal, including tax and tip is: " )

#reducing the decimal places to 2 and providing the total
thismuch = '{:.2f}'.format(result)
print(thismuch)
