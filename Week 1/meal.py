"""
Prompt:
In meal.py, implement a program that prompts the user for a time and outputs whether its breakfast time, lunch time, or dinner time. If its not time for a meal, dont output 
anything at all. Assume that the users input will be formatted in 24-hour time as #:## or ##:##. And assume that each meals time range is inclusive. 
For instance, whether its 7:00, 7:01, 7:59, or 8:00, or anytime in between, its time for breakfast.

Structure your program per the below, wherein convert is a function (that can be called by main) that converts time, a str in 24-hour format, to the 
corresponding number of hours as a float. For instance, given a time like "7:30" (i.e., 7 hours and 30 minutes), convert should return 7.5 (i.e., 7.5 hours).

"""

def main():

    # Prompt user for a time
    time = input("What time is it? ").strip()

    # Call convert
    new_time = convert(time)

    # Return Meal of Day
    if 7 <= new_time <= 8:
        print("Breakfast Time.")
    elif 12 <= new_time <= 13:
        print("Lunch Time.")
    elif 18 <= new_time <= 19:
        print("Dinner Time.")
    else:
        pass


# Split time into hours and minutes - remove ":" - add hours and minutes together and return as float
def convert(time):
    
    hours, minutes = time.split(":")
    minutes = float(minutes) / 60

    return float(hours) + minutes


if __name__ == "__main__":
    main()