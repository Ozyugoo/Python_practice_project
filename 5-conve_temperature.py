"""
    This program prompts a user for a Celsius temperature,
    convert the temperature to Fahrenheit,
    and print out the convert temperature
"""


temperature = input("Enter Temperature in Celsius: ")
celsius = float(temperature)

""" Convert input from Celsius to Fahrenheit """

fahrenheit = (celsius * 9 / 5) + 32
print(celsius, "degree Celsius is equivalent to", fahrenheit, "degree Fahrenheit")
