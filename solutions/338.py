import sys

def is_leap_year(year_no):
    divisible_by_4 = (year_no % 4 == 0)
    divisible_by_100 = (year_no % 100 == 0)
    divisible_by_400 = (year_no % 400 == 0)
    if divisible_by_4:
        if divisible_by_100:
            if divisible_by_400:
                return True
            return False
        return True
    return False

month_map = {
    1:31, #jan
    2:28, #feb
    3:31, #mar
    4:30, #apr
    5:31, #may
    6:30, #jun
    7:31, #jul
    8:31, #aug
    9:30, #sep
    10:31, #oct
    11:30, #nov
    12:31 #dec
}

day_map = {
    0:'sunday',
    1:'monday',
    2:'tuesday',
    3:'wednesday',
    4:'thursday',
    5:'friday',
    6:'saturday',
}

def days_since_year_begin(year, month, day):
    days = day
    month -= 1
    while month > 0:
        days += month_map[month]
        month = month - 1
    if is_leap_year(year):
            days = days + 1
    return days


def days_since_epoch(year, month, day):
    days = days_since_year_begin(year,month,day)
    year = year - 1
    while year > 0:
        if is_leap_year(year):
            days += 366
        else:
            days += 365
        year -= 1
    return days

def date_to_day(year, month, day):
    return day_map[days_since_epoch(year, month, day) % 7]

def main():
    while sys.stdin.readable():
        ytd = sys.stdin.readline().split()
        try:
            print(date_to_day(int(ytd[0]),int(ytd[1]),int(ytd[2])))
        except:
            break

main()
