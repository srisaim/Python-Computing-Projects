import stdio
import sys

# Input integers x, y, and z.
x = int(sys.argv[1])
y = int(sys.argv[2])
z = int(sys.argv[3])

# Find minimum number.
min = min(x, y, z)

# Find maximum number.
max = max(x, y, z)

# Find middle number.
middle = (x+y+z)-(min+max)

# Output the numbers from lowest to highest.
stdio.writeln(str(min) + ' ' + str(middle) + ' ' + str(max))
