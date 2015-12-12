#Leslie Gil
#30 April 2014
##Write a function that takes a list of priorities (a list of numbers).
##The function should then compare the zero-th entry to the first entry, and interchange them if the first is bigger than the second.
##The function should continue comparing subsequent entries until it gets to the end of the list.

def main():
    nums = input(("Please enter a list of numbers, separated by a comma: "))
    numberlist = nums.split(",")
    fixLine(numberlist)

    print(numberlist)

def fixLine(numberlist):
    for i in range(len(numberlist)):
        i+=1
        if numberlist[i] > numberlist[i+1]:
            greaternumber = numberlist[i]
            numberlist[i] = numberlist[i+1]
            numberlist[i+1] = greaternumber
        



main()

