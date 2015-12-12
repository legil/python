#Leslie Gil
#11 April 2014
#Write a function that returns the number of positive integers in a list of integers.
#Include your function in a program that allows the user to enter a list of numbers which is then used to demonstrate your function.

def main():
    integers = eval(input("please enter a list of integers (both positive and negative) separated by a comma: "))
    print("list of integers is : ", integers)
    
    print("number of positive integers from list is: ", countpositives(integers))

def countpositives(listofints):
    positiveintegers = []
    count = 0
    for i in listofints:
        if i>=0:
           positiveintegers.append(i)
           count+=1
        i+=1
    print("list of positive integers from list is: ", positiveintegers)
    return count
main()
        
           
                          
                           
