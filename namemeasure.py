#Leslie Gil
#March 8, 2014
#Write a program that measures strings in terms of the length of your name.
def main():
    name = input("Please enter your name: ")
    print("The measuring string is", name)
    string = input("Please enter a string: ")
    print("Your string is", len(string)//len(name), name,"s", "long")
main()
          
    
    
