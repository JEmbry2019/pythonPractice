# Flowers.py - This program reads names of flowers and whether they are grown in shade or sun from an input 
# file and prints the information to the user's screen. 
# Input:  flowers.dat.
# Output: Names of flowers and the words sun or shade.

# Open input file
flower = open("flowers.dat", "r")
flowerData = None
growData = None

# Write while loop here
while True:
    flowerData = flower.readline().strip()
    growData = flower.readline().strip()
    if (flowerData == ""):
        break
    
    # Print flower name using the following format
    # print(var + " grows in the " + var2)
    print(flowerData + " grows in the " + growData)