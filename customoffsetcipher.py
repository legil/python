# Leslie Gil
# March 6, 2014 
# A program to convert a textual message into a Caesar cipher

def main():
    print("This program converts a textual message into a sequence")
    print("of numbers representing the Unicode encoding of the message.\n")
    
    # Get the message to encode
    message = input("Please enter the message to encode - ")
    offset = eval(input("Please enter an offset value - "))

    print("\nHere are the Unicode codes:")

    # Loop through the message and print out the Unicode values
    for ch in message.upper():
        index = (ord(ch) - ord('A')+offset) %26
        print(chr(ord('A')+index), end=" ")    
        
    print() # blank line before prompt

main()
