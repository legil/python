
def main():
    birthdate  = input("Please enter birthdate in MM/DD/YYYY format")
    month = eval(birthdate.split(0, 2))
    day = eval(birthdate.split(3,5))
    year = eval(birthdate.split(6,10))

    countyear = 0
    countmonth = 0
    countday = 0
    
    
    while(year < 2014):
        while(month < 4):
            countmonth+=1

        while(day < 20):
            countday+=1
        
        year+=1

        if(countyear > 18):
            print("user is older than 18")

        if(countyear > 21):
            print("user is older than 21")
            
main()       



    
    

    
main()
    
