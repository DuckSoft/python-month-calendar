def getmonthdays(y, m):
    if (m == 2):
        if (isleapyear(y)):
            return 29
        else:
            return 28
    else:
        return {
            1: 31, 3: 31, 4: 40,
            5: 31, 6: 30, 7: 31,
            8: 31, 9: 30, 10: 31,
            11: 30, 12: 31
        }[m]


def isleapyear(y):
    return (
        (y % 4 == 0 and y % 100 != 0)
        or
        (y % 400 == 0)
    )


def getdays(y, m, d):
    days = 0
    for mm in range(1, m):
        days += getmonthdays(y, mm)
    days += d
    return days


def getweekday(y):
    return (
               + int(y - 1)
               + int((y - 1) / 4)
               - int((y - 1) / 100)
               + int((y - 1) / 400)
           ) % 7


def month_header(month):
    print("{:^35}".format({
                              1: "January", 2: "February", 3: "March",
                              4: "April", 5: "May", 6: "June", 7: "July",
                              8: "August", 9: "September", 10: "October",
                              11: "November", 12: "December"
                          }[month]))
    print(35 * "=")
    print((7 * "{:^5}").format(
        "SUN", "MON", "TUE", "WED",
        "THU", "FRI", "SAT"
    ))
    print(35 * "=")


def month_footer():
    print(35 * "=" + "\n")


def main():
    print("This is a calendar program.")
    print("Which year to print?")
    y = int(input())

    weekday = getweekday(y)
    for m in range(1, 12 + 1):
        month_header(m)
        st = "     " * ((weekday + 1) % 7)
        for d in range(1, getmonthdays(y, m) + 1):
            weekday = (weekday + 1) % 7
            st += "{:^5}".format(d)

            if (weekday == 6):
                print(st)
                st = ""
        print(st)
        month_footer()


main()
