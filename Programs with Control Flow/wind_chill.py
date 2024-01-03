import stdio
import sys

t = float(sys.argv[1])
v = float(sys.argv[2])

# Checking if value of t is greater than 50.
if t > 50:
    # If t is greater than 50, then output this message.
    stdio.writeln("Value of t must be <= 50 F")
else:
    # Checking if value of v is less than or equal to 3.
    if v <= 3:
        # If v is less than or equal to 3, then output this message.
        print("Value of v must be > 3 mph")
    else:
        # The calculation formula to find the value of w.
        w = 35.74 + (0.6215 * t) + ((0.4275 * t) - 35.75) * pow(v, 0.16)

        # Output the value of w.
        stdio.writeln(w)
