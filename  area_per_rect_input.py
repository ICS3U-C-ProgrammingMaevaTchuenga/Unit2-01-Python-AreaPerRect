#!/usr/bin/env python3
# Created By: Maeva Tchuenga
# Date: sep 29 2026
# This program asks for the length and the width 
# of a rectangle, calculares and displays the area and perimeter
# back to the proper units


def main ():

 # get the length from the user and convert to an integer 
 length = int(input("Enter length of the rectangle (cm): "))

 
 #get the width from the user and convert to an integer
width = int(input("Enter width of the rectangle (cm): "))

    # Calculate the area and perimeter of a rectangle.
area = length * width
perimeter = 2 * (length + width)

    # Display the area and perimeter to the user with proper units.
print("Area: {} cm²".format(area))
print("Perimeter: {} cm".format(perimeter))


main()  