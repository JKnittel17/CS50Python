"""
Prompt:
In a file called outdated.py, implement a program that prompts the user for a date, anno Domini, in month-day-year order, formatted like 9/8/1636 or September 8, 1636, 
wherein the month in the latter might be any of the values in the list below:

Then output that same date in YYYY-MM-DD format. If the users input is not a valid date in either format, prompt the user again. Assume that every month has no more than 
31 days; no need to validate whether a month has 28, 29, 30, or 31 days.
"""

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

def main():
    
    while True:

        # While input is not in correct format - keep looping
        date = input("Date: ")

        # Try first seeing if date follows format of mm/dd/yyyy
        try:

            month, day, year = date.split("/")

            month = int(month)
            day = int(day)
            year = int(year)

            if 0 < month <= 12 and 0 <= day <= 31 and year >= 0:

                print(f"{year:04}-{month:02}-{day:02}")

        # Should that fail - try seeing if date entered in alternative format
        # What ultimately determines if the program sees this as a date is if one of the first two words matches a key in our months list
        except:

            try:

                if "," in date:

                    date = date.replace(",","")

                month, day, year = date.split(" ")
                
                # If month was first word given  ex: September 8, 1636
                if month.title() in months:

                    month = months.index(month) + 1

                    month = int(month)
                    day = int(day)
                    year = int(year)

                    if 0 < month <= 12 and 0 <= day <= 31 and year >= 0:

                        print(f"{year:04}-{month:02}-{day:02}")
                
                # If month was second word given   ex: 8 September 1636
                elif day.title() in months: 

                     day = months.index(day) + 1

                     month = int(month)
                     day = int(day)
                     year = int(year)

                     if 0 < day <= 12 and 0 <= month <= 31 and year >= 0:

                        print(f"{year:04}-{day:02}-{month:02}")

            except:

                pass


                    

main()