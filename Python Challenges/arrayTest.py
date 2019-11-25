# MichiganCities.py - This program prints a message for invalid cities in Michigan.  
# Input:  Interactive
# Output:  Error message or nothing

# Initialized list of cities
citiesInMichigan = ["Acme", "Albion", "Detroit", "Watervliet", "Coloma", "Saginaw", "Richland", "Glenn", "Midland", "Brooklyn"] 

# Get user input
inCity = input("Enter name of city: ")


# Write your test statement here to see if there is a match.
for i in range(len(citiesInMichigan)):
    if citiesInMichigan[i] == inCity:
        test = True
        break
    else:
        test = False
        
# If the city is found, print "City found."
if test:
    print("City found.")
# Otherwise, "Not a city in Michigan" message should be printed. 
else: print("Not a city in Michigan.")
