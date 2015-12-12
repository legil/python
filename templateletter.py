#Leslie Gil
#20 March 2014

#Write a program that asks for a list of names and a list of cities, as well as a file.
##Write a program that asks the user for the name of a file and a line length.
#Your program should use the file as a template to generate letters customized with the names and cities entered.
#You should generate a letter for each name/address pair on the inputted lists.
#The customized letters should replace every the **INSERT NAME HERE** with the name and **INSERT ADDRESS HERE** with the address.

def main():
    #ask user for name of input file (template)
    infileName = input("Please enter the name of the template file ")
    
    #ask user for strings: names and corresponding cities
    nameString = input("Please enter names of recipients separated by a comma ")
    cityString = input("Please list addresses separated by a comma ")

    #split string into a list at commas
    nameslist = nameString.split(",")
    citieslist = cityString.split(",")


     #for each name, read through lines in template and replace blank with name and city
    for i in range(len(nameslist)):
        for line in infile:
            namereplace = line.replace("**INSERT NAME HERE**", nameslist[i])
            print(namereplace.replace("**INSERT ADDRESS HERE**", citieslist[i]))
        infile.seek(0)
main()
