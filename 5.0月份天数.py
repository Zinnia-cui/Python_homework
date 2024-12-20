def month_days(year, month):
    if month in [4, 6, 9, 11]:
        return 30
    elif month == 2:
        if (year % 4 == 0 and year % 100!= 0 ) or ( year % 400 == 0):
            return 29
        else:
            return 28
    else:
        return 31

def main():
    year,month = map(int, input().split())
    print(month_days(year, month))
main()

