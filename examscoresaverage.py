# Leslie Gil
# February 3, 2014
# A simple program to average two exam scores,  Illustrates use of multiple input

def examscoresavg():
    print("This program computes the average of two exam scores.")

    score1, score2, score3 = eval(input("Enter three scores separated by a comma: "))
    average = (score1 + score2 + score3) / 3

    print("The average of the three test scores is:", average)

examscoresavg()
