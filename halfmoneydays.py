#Leslie Gil
#February 18, 2014
#Write a program to calculate how much money you would have if your money was cut in half every day.

def main():
    money = 1000.0
    days = eval(input("Please enter number of days "))
    
    for days in range(1, days + 1):
        print("Day", days,":", "\t$", money)
        money = money/2
        

main()
        
