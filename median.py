"""Median calculator."""
"""ENTER YOUR SOLUTION HERE!"""

while True:
    try:
        print("Enter a list of numbers separated by commas: ")
        list =[]
        for value in input().split(","):
            list.append(int(value))
        if len(list) % 2 != 0:
            median = list[int((len(list) - 1) / 2)]
        else:
            median = (list[int((len(list) - 1) / 2)] + list[int((len(list) - 1) / 2) + 1]) / 2
    except ValueError:
        print("Some input could not be converted to a number!")
    else:
        break
print(median)
