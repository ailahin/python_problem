year= input("Please type the year")
year= int(year)
if (year%4==0 and year%100!=0 or year%400==0):
    print(f"{year} is a leap year")

else:
    print (year, "isn't a leap year")

