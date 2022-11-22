def is_leap(year):
    if ((year%400==0) or not year%100==0) and year%4==0:
        leap=True
    else: 
        leap=False
    return(leap)
year = int(input())
print(is_leap(year))