"""Freecodecamp Python Exerise 2"""
"""Build a Bill Splitter"""

running_total = 0
num_of_friends = int(input("How many are you altogether: ? \n"))
appetizers = 37.89 
food = 57.34
desserts = 39.39
drinks = 64.21
running_total += appetizers + food + desserts + drinks
print('Total bill so far: ', running_total)
tip = running_total * 0.25 
print('Tip amount:', tip)
running_total += tip 
print("Total with tip:", running_total)
#each bill allocated to each person on the table 
final_bill = (running_total)/(num_of_friends)
print("Bill per person:", final_bill)

each_pays= round(final_bill , 2)
print('Each person pays:', each_pays)