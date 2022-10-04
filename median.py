"""Median calculator."""
"""ENTER YOUR SOLUTION HERE!"""

while True:
    try:
        print("Enter a list of numbers separated by commas: ")
        numbers = [float(value) for value in input().split(",")]
        sortedNumbers = sorted(numbers);
        listSize = len(numbers);
        if ((listSize % 2) == 0):
            medianIndexUpper = int(listSize/2);
            medianIndexLower = medianIndexUpper - 1;
            median = (sortedNumbers[medianIndexLower] + sortedNumbers[medianIndexUpper])/2;
        else:
            medianIndex = int((listSize-1) / 2)
            median = sortedNumbers[medianIndex];
    except ValueError:
        print("Some input could not be converted to a number!")
    else:
        break
return median;
#print(sortedNumbers);
