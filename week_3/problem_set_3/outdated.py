months = [
    "January",
    "February",
    "March",
    "April",
    "May",
    "June",
    "July",
    "August",
    "September",
    "October",
    "November",
    "December"
]

# MM/DD/YYYY
# YYYY/MM/DD
while True:
    try:
        date = input("Date: ")
        dates = date.split("/")
        if len(dates) == 3:
            m, d, y, = dates
            if int(d) > 31 or int(m) > 12:
                continue
            print(f"{y}-{int(m):02}-{int(d):02}")
        else:
            dates = date.split(",")
            m, d = dates[0].split(" ")
            if int(d) > 31:
                continue
            y = dates[1].strip()
            month = months.index(m) + 1
            print(f"{y}-{int(month):02}-{int(d):02}")
        break
    except ValueError:
        pass
