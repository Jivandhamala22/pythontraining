yr = int(input("enter a year\n"))

if ( yr%4==0 or (yr%100 == 0 and yr%400==0)):
    print( " a leap year")