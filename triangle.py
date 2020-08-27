#Program to print hello world
#Written by Surya Singh
#CS 470
#Date:- 8/27/2020
import math
print("Compute the hypotenuse of right triangle")


again="Y"

while again == "Y" :
    leg1 = float(input("Enter first length:"))
    leg2 = float(input("Enter second length:"))
    if leg1<=0:
        print("Leg #1 must be positive")
    elif leg2<=0:
        print("Leg #2 must be positive")
    else:
        leg3=math.sqrt(leg1*leg1+leg2*leg2)
        print("Hypotenuse is ",round(leg3,2))
    again = input("Go again(Y/N)?")
