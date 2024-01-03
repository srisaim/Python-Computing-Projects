import stdio
import sys

# Input numbers for t & v.
t = float(sys.argv[1])
v = float(sys.argv[2])

# Input values t & v into formula w.
w = 35.74 + 0.6215 * t + (0.4275 * t - 35.75) * (v ** 0.16)

# Output the final answer.
stdio.writeln(w)
