def getFare(zone, tktType): # I gave my function a name with a verb
    fare = -1 # This is the default. If none of the later conditions is true,
              # fare will still have a value, and I won't get weird errors.
              # Also, -1 is the value when there's an error, so I can avoid
              # having extra else: clauses
    if tktType == "adult": # first, sort by type, we'll look at the zones later
        if zone <= 2:
            fare = 23
        elif zone == 3:
            fare = 34.5
        elif zone == 4:
            fare = 46
        
    else: # type is child
        if zone <= 2:
            fare = 11.5
        elif zone <= 4:
            fare = 23

    return fare


def main():
    for zone in range(1,6):
        for myType in ["adult", "child"]: # iterate over a list of strings
            # note that my output tells the user (who might not be the programmer)
            # exactly what the inputs and outputs are
            print("For zone", zone, "and ticket type", myType, "the fare is:", getFare(zone, myType))


main()
