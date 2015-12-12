#Leslie Gil
#March 24 2014
#Write a program that asks the user for a file containing a list of items to be completed and a name for an output file.
#Your program should then write the list, with item numbers to the output file.

def main():
    fileName = input("Please enter name of task file: ")
    file = open(fileName, 'r')
    taskcount = 0
    for line in file:
            taskcount = count + 1
            print(count,".  ", line)
main()
