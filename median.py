"""Median calculator."""
"""ENTER YOUR SOLUTION HERE!"""

from statistics import median

while True:
    try:
        print("Enter a list of numbers separated by commas: ")
        list =[]
        for value in input().split(","):
            list.append(float(value))
    except ValueError:
        print("Some input could not be converted to a number!")
    else:
        break
print(median(list))
