def main():
    infile = open("random_input.txt", "r")

    longOutfile = open("longOutput.txt", "w")
    shortOutfile = open("shortOutput.txt", "w")
    capsOutfile = open("capsOutput.txt", "w")

    lineNum = 1
    for line in infile:
        if len(line) > 20:
            print(str(lineNum) + '.' + line, file = longOutfile)
        else:
            print(str(lineNum) + '.' + line, file = shortOutfile)
        print(str(lineNum) + '.' + line.upper(), file = capsOutfile)
        lineNum += 1
            
            
    
                       

        
