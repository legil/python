def main():
    print("This program prints a file.")

    # get the input file name
    infileName = input("Please enter name of input file: ")

    # open the files:
    infile = open(infileName, "r")

    # read each line of the input file and print it to outfile
    #   
    for line in infile:
        print(line)

main()
