#loops

for letter in "Python"
    print("Curent letter is ", letter)

#iterating through the loop
a = ["apple", "banana", "orange"]
for b in a:
      print(b)

#break
#terminates the loop and executes what immediately follows the loop

#continue
#loop with skip the remainder of its body and reset its condition prior to reiterating

#refer to LoopStatements image

------------------
#Assignment
from __future__ import print_function

fruitPrices = {'apples': 2.00, 'oranges': 1.50, 'pears': 1.75,
               'limes': 0.75, 'strawberries': 1.00}


def buyLotsOfFruit(orderList):
    """
        orderList: List of (fruit, numPounds) tuples

    Returns cost of order
    """
    totalCost = 0.0
    
    for fruit in orderList:
        print(fruit[0])
        print(fruit[1])
        print(fruit[2])
        print(fruit[3:4])
        
    return totalCost
