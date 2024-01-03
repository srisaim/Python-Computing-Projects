import stdio
import sys

# Accept int n as command-line argument.
n = int(sys.argv[1])

# Set a and b to 1. (The first two Fibonacci numbers)
a = 1
b = 1

# Use for loop as i is not greater than n.
# Exchange using temporary variable t.
# Exchange using temporary variable until it finds the nth number from the fibonacci sequence.
for i in range(3, n+1):
    t = a + b
    a = b
    b = t

# Output the final answer b after for loop ends.
stdio.writeln(b)
