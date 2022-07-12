# -*- coding: utf-8 -*-
"""Student Do: E-Commerce Traffic.

This script will parse through a text file and sum the total
number of customers and the count of days in the text file to
calculate the daily average of customer traffic for an e-commerce
business.
"""

# @TODO: From the pathlib library, import the main class Path
from pathlib import Path


# @TODO: Check the current directory where the Python program is executing from
print(f"current working directory: {Path.cwd()}")

# @TODO: Set the path using Pathlib
filepath = Path('C:/Users/tjfoo/Desktop/Fintech/Week2/FintechWeek2/customer_traffic.txt')


# Initialize variables
customer_total = 0
day_count = 0

# @TODO: Open the file in "read" mode ('r') and store the contents in the variable 'file'
with open(filepath, "r") as file:

    # @TODO: Parse the file line by line
    #text = file.read()
    #print(text)

        # @TODO: Convert the number in the text file from string to int (allows for numerical calculations)
    for line in file:
        number = int(line)
        customer_total += number
        day_count += 1

        # @TODO: Sum the total and count of the numbers in the text file
        print(f"customer_total: {customer_total}")
        print(f"day_count: {day_count}")


# @TODO: Print out customer_total and day_count




# @TODO: Calculate the average



# @TODO: Set output file name


# @TODO: Open the output path as a file object

    # @TODO: Write daily_average to the output file, convert to string
