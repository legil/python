# Leslie Gil
# February 19, 2014
# Modify the book's factorial program to calculate the double factorial.
# The double factorial is similar to the factorial, except you multiply every other number.

def main():
    n = eval(input("Please enter a whole number: "))
    fact = 1

    #Illustrates for loop with an accumulator
    for factor in range(n,1,-2):
        fact = fact * factor
    print("The factorial of", n, "is", fact)

main()
