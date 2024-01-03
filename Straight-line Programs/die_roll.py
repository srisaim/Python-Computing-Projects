import stdio
import stdrandom
import sys

# Input number for n.
n = int(sys.argv[1])

# Roll dice two times with n sides.
roll1 = stdrandom.uniformInt(1, n)
roll2 = stdrandom.uniformInt(1, n)

# Find sum of roll 1 & 2.
sum = roll1 + roll2

# Output the final sum.
stdio.writeln(sum)
