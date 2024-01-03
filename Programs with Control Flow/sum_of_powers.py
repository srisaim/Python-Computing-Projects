import stdio
import sys

# Accepts int n and k as command-line arguments.
n = int(sys.argv[1])
k = int(sys.argv[2])

# Set total to 0
total = 0

# Using for loop set i in the range from 1 to n.
# Set new total to total + (i^k) and cycle through loop.
for i in range(1, n + 1):
    total = total + pow(i, k)

# Output the final answer, total.
stdio.writeln(total)
