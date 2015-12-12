#Leslie Gil
#February 6, 2014
#A program that will print out a conversion table for dollars and another currency.

def main():
    print("Dollars\tCurrency in Lebanese Pounds")
    for dollars in range(1,11):
	    currency = 0.000664 * dollars
	    print(dollars, "\t", currency)
main()
