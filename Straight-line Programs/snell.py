import math
import stdio
import sys

# Input 3 floats.
t1 = float(sys.argv[1])
n1 = float(sys.argv[2])
n2 = float(sys.argv[3])

# Convert theta 1 to radians.
t1 = math.radians(t1)

# Find theta 2 with formula.
t2 = math.asin((n1*math.sin(t1))/n2)

# Convert theta 2 to degrees.
t2 = math.degrees(t2)

# Output final answer.
stdio.writeln(t2)
