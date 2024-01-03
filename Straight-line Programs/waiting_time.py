import math
import stdio
import sys

# Input float c & t.
c = float(sys.argv[1])
t = float(sys.argv[2])

# Formula to find p.
p = math.exp(-c*t)

# Output final value of p.
stdio.writeln(p)
