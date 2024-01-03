import stdio
import sys

# Accept int p and q as command line-arguments.
p = int(sys.argv[1])
q = int(sys.argv[2])

# Use if-else statements to know which value is greater.
# Assign lowest number to temporary value t.
if p > q:
    t = q
else:
    t = p

# Use for loop to check all numbers from 1 to t for common divisor.
# Use % to check if number is evenly divisible to p or q.
for i in range(1, t + 1):
    if p % i == 0 and q % i == 0:
        divisor = i

# Output the final answer, which is divisor after loop ended.
stdio.writeln(divisor)
