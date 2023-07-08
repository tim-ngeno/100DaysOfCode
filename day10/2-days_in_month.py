"""days in month / leap year"""


def is_leap(year):
    """Checks if a year is leap or not
    Args:
        year (int): input year to check
    Return:
        True, if year is leap, False otherwise
    """
    if year % 4 == 0 or year % 100 != 0 and year % 400 == 0:
        return True
    return False


def days_in_month(year, month):
    """Returns the number of days in a particular month
    according to index in the list, starting from 0"""
    month_days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

    if is_leap(year) and month == 2:
        return 29
    else:
        return month_days[month - 1]


year = int(input("Enter year:\n"))
month = int(input("Enter month number:\n"))
days = days_in_month(year, month)

print(days)
