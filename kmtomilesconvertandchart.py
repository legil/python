# Lab 2:  Kilometers to Miles Converter Program
# Leslie Gil, February 2014

	#Input the distance in kilometers (call it km)
	#Calculate the distance in miles as 0.621371*km
	#Output miles

def kmtomilesconverter():
    #Input the distance in kilometers (call it km)
    km = eval(input("Enter distance in kilometers "))
    #Input the distance in kilometers (call it km)
    miles = 0.621371 * km
    #Output miles
    print(km, "kilometers", "=", miles, "miles")
kmtomilesconverter()


print("-----------------------------------------------------------------")


def kmtomileschart():
    print("km\tmiles")
    for km in range(10):
        miles = km * 0.621371
        
        print(km, "\t", miles)

kmtomileschart()
        
    

    
