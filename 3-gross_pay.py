"""
    This program prompts user for hours and rate per hour
    and then compute gross pay.
"""


hour = input("Enter Hours: ")
rate = input("Enter Rates: ")
fh = float(hour)
fr = float(rate)
pay = fh * fr
print("Pay: ", pay)
