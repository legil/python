#Leslie Gil
#18 March 2014
#Write a program that asks the user for the name of a file and a line length.
#Your program should then "wrap" all lines that are longer than line length, and print the result on the screen.

def main():
  # get the input file name
    infileName = input("Please enter name of input file: ")

  #ask user for line length
    userlength = eval(input("Please enter a number that represents the length of a string "))

    # open the file:
    infile = open(infileName, "r")

 


    # read each line of the input file, compare length of file & input length 
    for line in infile:
        if(len(line) >= userlength):
            #wrap lines longer than input length and display
            print(line[:userlength],"\n",line[userlength:])

main()
