import stdio
import sys

# Input values for m1, m2, and r.
m1 = float(sys.argv[1])
m2 = float(sys.argv[2])
r = float(sys.argv[3])

# Set value for G.
G = 6.674 * (10 ** -11)

# Input numbers into formula f.
f = G*((m1*m2)/(r**2))

# Output the final answer.
stdio.writeln(f)
