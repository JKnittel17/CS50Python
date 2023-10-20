"""
In the United States, its customary to leave a tip for your server after dining in a restaurant, typically an amount equal to 15% or 
more of your meals cost. Not to worry, though, weve written a tip calculator for you, below!

Well, weve written most of a tip calculator for you. Unfortunately, we didnt have time to implement two functions:

dollars_to_float, which should accept a str as input (formatted as $##.##, wherein each # is a decimal digit), remove the leading $, and return 
the amount as a float. For instance, given $50.00 as input, it should return 50.0.

percent_to_float, which should accept a str as input (formatted as ##%, wherein each # is a decimal digit), remove the trailing %, and return 
the percentage as a float. For instance, given 15% as input, it should return 0.15.

Assume that the user will input values in the expected formats.

"""

def main():
    dollars = dollars_to_float(input("How much was the meal? "))
    percent = percent_to_float(input("What percentage would you like to tip? "))
    tip = dollars * percent
    print(f"Leave ${tip:.2f}")


def dollars_to_float(d):
    # Strip left most digit from variable d. When returning - cast variable to float. 
    temp = d.lstrip("$")

    return float(temp)


def percent_to_float(p):
    # Strip right most digit from variable p, making sure to first cast as an int so we can divide by 100. When returning - cast variable to float. 
    temp2 = int(p.rstrip("%")) / 100

    return float(temp2)


main()