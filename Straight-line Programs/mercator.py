import math
import stdio
import sys

# Input the numbers.
lat = float(sys.argv[1])
long = float(sys.argv[2])

# Convert to radians.
lat = math.radians(lat)

# Create x & y variables with formula.
x = long
y = math.log((1+math.sin(lat))/(1-math.sin(lat)))/2

# Output the final x & y.
stdio.writeln(str(x) + ' ' + str(y))
