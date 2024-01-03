import stdio
import sys

# Accept int n in a command-line argument.
n = int(sys.argv[1])

# Set dragon and nogard to F.
dragon = "F"
nogard = "F"

# For loop from i in range from 1 to n.
# Use temporary variable t to set L, F, and R in correct order.
for i in range(1, n+1):
    t = dragon
    dragon = (dragon + "L" + nogard)
    nogard = (t + "R" + nogard)

# Output final answer dragon.
stdio.writeln(dragon)
