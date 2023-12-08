# Script Name:	                python-Conditional-Statements
# Author:				        Juan Maldonado
# Date of lastest revision:		12/07/2023
# Purpose:				        This program creates and outputs logical conditonal results.


# These are values for a and b
a = 25
b = 91

# This creates and outputs a == b
if a == b:
    print("a is equal to b.")
else:
    print("a is not equal to b.")

# This creates and outputs a != b
if a != b:
    print("a is not equal to b.")
else:
    print("a is equal to b.")

# This creates and outputs a < b
if a < b:
    print("a is less than b.")
else:
    print("a is not less than b.")

# This creates and outputs a <= b
if a <= b:
    print("a is less than or equal to b.")
else:
    print("a is greater than b.")

# This creates and outputs a > b
if a > b:
    print("a is greater than b.")
else:
    print("a is not greater than b.")

# This creates and outputs a >= b
if a >= b:
    print("a is greater than or equal to b.")
else:
    print("a is less than b.")

# Logical conditional of choice
c = 7

# Using elif and else
if c % 2 == 0:
    print("c is an even number.")
elif c % 2 != 0:
    print("c is an odd number.")
else:
    print("This should not happen!")

# This creates & outputs "and" between conditions
if a < b and c % 2 == 0:
    print("Both conditions are true.")
else:
    print("At least one condition is false.")

# This creates & outputs "or" between conditions
if a < b or c % 2 == 0:
    print("At least one condition is true.")
else:
    print("Both conditions are false.")

# These are nested if statement
if a < b:
    print("a is less than b.")
    if c % 2 == 0:
        print("c is an even number.")
    else:
        print("c is an odd number.")
else:
    print("a is not less than b.")

# This uses a "pass" to avoid errors
if a < b:
    print("a is less than b.")
else:
    pass  
