import math
import stdio
import sys

# Input all the x & y variables.
x1 = float(sys.argv[1])
y1 = float(sys.argv[2])
x2 = float(sys.argv[3])
y2 = float(sys.argv[4])

# Convert to radians.
x1 = math.radians(x1)
y1 = math.radians(y1)
x2 = math.radians(x2)
y2 = math.radians(y2)

# Input all variables in formula d.
d = math.acos(math.sin(x1)*math.sin(x2)+math.cos(x1)*math.cos(x2)*math.cos(y1-y2))

# Convert back to degrees & multiply 111.
d = 111 * math.degrees(d)

# Output the final answer.
stdio.writeln(d)
