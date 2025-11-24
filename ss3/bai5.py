def is_leap_year(year):
    if  year % 400 == 0 or (year % 4 == 0  and year % 100 !=0):
        print(f"{year} là năm nhuận")
    else:
        print(f"{year} không phải năm nhuận")
    return year

print(is_leap_year(2000))