#Leslie Gil
#1 May 2014
#Write a program that asks the user to enter a number between 1900 and 1012.
#If they enter a number out of range, print a message that the number is out of range and prompt them again for a number between 1900 and 2012.
#When the user enters a number in range, print the number to the screen and end the program.

def main():
          
    while True:
        number = input(eval("Please enter a number between 1900 and 2012: ")
        if 1900 <= number <= 2012:
            print("Your number is: ", number)
        break
    else:
        print("number is out of range, please enter another, this time between 1900 and 2012")
main()
