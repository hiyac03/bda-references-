import sys

from functools import reduce

def min_max(items):
    temperature, count = items[0]
    min_temp = temperature
    max_temp = temperature
    for temp, _ in items[1:]:
        min_temp = min(min_temp, temp)
        max_temp = max(max_temp, temp)
    return min_temp, max_temp

for line in sys.stdin:
    year, data = line.strip().split("\t")
    temperature, count = data.split(",")
    count = int(count)
    
    average = int(temperature) / count  # Calculate average
    min_temp, max_temp = reduce(min_max, ((int(temperature), count),))  # Find min and max

    print(f"{year}\t{average:.2f},{min_temp},{max_temp}")  # Print results

