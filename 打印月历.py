# Print the calendar for a month in a year
def printMonth(year, month):
    # Print the headings of the calendar
    printMonthTitle(year, month)
    # Print the body of the calendar
    printMonthBody(year, month)

# Print the month title, e.g., May, 1999
def printMonthTitle(year, month):
    print("{:8s}{} {}".format(' ', getMonthName(month),  year))
    print("{:29s}".format('-'*29))
    print(" Sun Mon Tue Wed Thu Fri Sat")

# Print month body
def printMonthBody(year, month):
    # Get start day of the week for the first date in the month
    startDay = getStartDay(year, month)

    # Get number of days in the month
    numberOfDaysInMonth = getNumberOfDaysInMonth(year, month)

    # Pad space before the first day of the month
    i = 0
    for i in range(startDay):
       print("    ", end = "")

    for i in range(1, numberOfDaysInMonth + 1):
        print(format(i, '4d'), end = "")

        if (i + startDay) % 7 == 0:
            print() # Jump to the new line

# Get the English name for the month
def getMonthName(month):
    if month == 1:
        monthName = "January"
    elif month == 2:
        monthName = "February"
    elif month == 3:
        monthName = "March"
    elif month == 4:
        monthName = "April"
    elif month == 5:
        monthName = "May"
    elif month == 6:
        monthName = "June"
    elif month == 7:
        monthName = "July"
    elif month == 8:
        monthName = "August"
    elif month == 9:
        monthName = "September"
    elif month == 10:
        monthName = "October"
    elif month == 11:
        monthName = "November"
    else:
        monthName = "December"

    return monthName

# Get the start day of month/1/year
def getStartDay(year, month):
    # Get the total number of days since January 1, 1800
    startDayOfJan_1_1800 = 3
    totalNumberOfDays = getTotalNumberOfDays(year, month)
    return (totalNumberOfDays + startDayOfJan_1_1800) % 7

def getTotalNumberOfDays(year, month):
    total = 0
    for i in range(1800,year):
        if isLeapYear(i):
            total += 366
        else:
            total += 365
    for i in range(1,month):
        total += getNumberOfDaysInMonth(year,i)
    return total


# Get the number of days in a month
def getNumberOfDaysInMonth(year, month):
    if month in [4,6,9,11]:
        return 30
    elif month == 2 :
        return 29 if isLeapYear(year) else 28
    elif month in [1,3,5,7,8,10,12]:
        return 31
    return 0 #if month is incorrect

# Determine if it is a leap year
def isLeapYear(year):
    if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
        return True

def main():
    # Prompt the user to enter year and month
    year = eval(input("Enter full year (e.g., 2001):"))
    month = eval(input(("Enter month as number between 1 and 12:")))

    # Print calendar for the month of the year
    printMonth(year, month)

main() # Call the main function