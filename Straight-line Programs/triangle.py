import stdio
import sys

# Accept x (int), y (int), and z (int) as command-line arguments.
# Accept inputs as integers.
x = int(sys.argv[1])
y = int(sys.argv[2])
z = int(sys.argv[3])

# Set expr to an expression which is True if each of x, y, and z is less than or equal to the sum
# of the other two, and False otherwise.
# Use Boolean logic.
expr = x <= y + z and y <= x + z and z <= x + y

# Write expr to standard output.
# Expr will give true or false statement.
stdio.writeln(expr)
