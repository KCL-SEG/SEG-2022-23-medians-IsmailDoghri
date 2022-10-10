"""Median calculator."""
"""ENTER YOUR SOLUTION HERE!"""

while True:
    try:
        print("Enter a list of numbers separated by commas: ")
        initList = []
        for value in input().split(","):
            initList.append(float(value))
            lenList = len(initList)
            sortedList = sorted(initList)
        if lenList % 2:
            median = sortedList[(lenList - 1) // 2]
        else:
            median = (sortedList[lenList // 2] + sortedList[(lenList // 2) - 1]) / 2
    except ValueError:
        print("Some input could not be converted to a number!")
    else:
        break
print(median)
