def median():
    numbers = input("Please enter a list of numbers separated by a comma")
    numbers.split(",")
    sort(numbers)
    if len(numbers) % 2 == 1:
        median  = numbers[len(numbers)//2]
    else:
        median = numbers[len(numbers)//2 -1] + numbers[len(numbers)//2] / 2.0
    print(median)
    #return median
median()            
