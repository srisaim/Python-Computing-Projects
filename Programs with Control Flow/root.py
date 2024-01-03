import stdio
import sys

# Create int and float command-line arguments.
# Int k, float c, float epsilon as e.
k = int(sys.argv[1])
c = float(sys.argv[2])
e = float(sys.argv[3])

# Set t (our guess) to c
t = c

# Use while loop and change t in each iteration.
# While |1 - c/(t^k)| is greater than e, continue with loop.
# Use given formulas in the loop.
while abs(1 - c / pow(t, k)) > e:
    ft = pow(t, k) - c
    ft2 = k * pow(t, k-1)
    t = t - ft/ft2

stdio.writeln(t)
