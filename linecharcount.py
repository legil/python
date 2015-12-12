#Leslie Gil
#March 17, 2014
#Write a program that asks the user for a name of a file and then prints to the screen the number of characters and lines in the file.

def main():
    # get the input file name
    infileName = input("Please enter name of input file: ")

    # open the file:
    infile = open(infileName, "r")

    #initialize line count and character count
    lines = 0
    characters = 0

    # read each line of the input file, count number of characters in file 
    for line in infile:
        characters = characters + len(line)
        
        #count number of lines
        lines += 1

    #print total number of characters and lines in file
    print("There are",characters, "characters and ", lines, "lines in this file.")

main()
