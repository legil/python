# Leslie Gil
# February 4, 2014
# Write a program that converts pounds to kilograms. One kilogram is approximately 2.2 pounds.

def poundstokilograms():
    pounds = eval(input("Enter weight in pounds "))
    kilograms = pounds * 0.453592
    print(pounds, "pounds is equal to", kilograms, "kilograms")

poundstokilograms()
