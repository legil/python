# Leslie Gil
# Febraury 10, 2014
#Write a program that asks the user for distance in feet and prints the number of yards and feet


def feetyardsmod():
    feet = eval(input("Enter distance in feet "))
    yards = feet // 3
    feetremaining = feet%3
    print("That is", yards, "yards and", feetremaining, "feet.")

feetyardsmod()
