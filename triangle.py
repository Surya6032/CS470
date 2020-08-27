#Program to print hello world
#Written by Surya Singh
#CS 470
#Date:- 8/27/2020
import math
print("Compute the hypotenuse of right triangle")
leg1 = float(input("Enter first length:"))
leg2 = float(input("Enter second length:"))
leg3=math.sqrt(leg1*leg1+leg2*leg2)
print("Hypotenuse is ",round(leg3,2))
