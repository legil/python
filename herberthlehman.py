def main():
    string = "H e r b e r t   H . L e h m a n "
    #for i in range(len(string)):
     #   print(string[1:i])
    
    for i in range(0, len(string),2):
        print(string[i:] + string[0:i])

main()
