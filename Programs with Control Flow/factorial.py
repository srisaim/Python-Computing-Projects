import stdio
import sys

# Accept n (int) as command-line argument.
n = int(sys.argv[1])

# Set result to 1.
result = 1

for i in range(2, n + 1):
    # For each value of i from [2, n], set result to its current value times i.
    # Result will change as it goes through the for loop.
    result = result * i

# The for loop ends after it completes the cycle from 2 to the n value.
# Write result to standard output.
stdio.writeln(result)
