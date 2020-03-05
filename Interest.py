#Write a python program to calculate compund interest. Use formula A=P(1+R/100)t
import math
Amount = float(input(" Please Enter the Amount : "))
Rate = float(input(" Please Enter the Rate Of Interest   : "))
Time = float(input(" Please Enter Time period in Years   : "))
ci_future = Amount * (math.pow((1 + Rate / 100), Time)) 
compound_int = ci_future - Amount
print("Compound Interest  {0} = {1}".format(Amount, compound_int))