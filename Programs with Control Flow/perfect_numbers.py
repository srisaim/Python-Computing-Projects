import stdio
import sys

# Accept int n as a command-line argument.
n = int(sys.argv[1])

# For loop for i in range from 2 to n.
# Set total (sum of divisors of i) to 0.
for i in range(2, n):
    total = 0

    # For loop for j in range from 1 to i.
    # If j evenly divides i, increment total by j.
    for j in range(1, i):
        if (i % j) == 0:
            total = total + j

    # If total equals i, output the final answer i. (perfect number)
    if i == total:
        stdio.writeln(i)
