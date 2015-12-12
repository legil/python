#Leslie Gil
#April 7, 2014
#Write a function that takes as a parameter a list of strings and returns a list containing the last letter of each of the strings.

def lastcharmethod(namelist):
    lastchars = []
    for i in namelist:
        lastchars.append(i[-1:])
    print(lastchars)

def main():
    names = ["Daniel","Nashyl","Orla", "Simone","Zakaria"]
    lastcharmethod(names)

main()


     
            
         
