import sys

for line in sys.stdin:
    year, temperature = line.strip().split()
    print(f"{year}\t{temperature},1")  # Emit key-value pairs with temperature and count (1)

