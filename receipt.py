#Leslie Gil
#March 8, 2014
#Write a program that asks the user for a list of prices of items purchased and prints out each price and the total, formatted nicely
 
def main():
    listofprices = []
    total = 0
    stringofprices = input("Please enter prices of items ")
    listofprices = stringofprices.split(", ")
    print("Your receipt: ")
    
    for i in listofprices:
        total = total + float(i)
        print("\t","\t", float(i))

        
    print("----------------------")
    print("Your total is: {0:0.2f}".format(total))
main()
