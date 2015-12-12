def main():
    fname = input("Enter filename: ")
    infile = open(fname,"r")
    outfile = open("out.txt","w")
    data = infile.read().lower()
    print(data, file=outfile)
main()

