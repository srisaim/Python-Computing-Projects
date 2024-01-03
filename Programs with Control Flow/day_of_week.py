import stdio
import sys

# Input values for int m, d, y.
m = int(sys.argv[1])
d = int(sys.argv[2])
y = int(sys.argv[3])

# Calculate given formulas with inputs.
y0 = y - (14 - m)//12
x0 = y0 + y0//4 - y0//100 + y0//400
m0 = m + 12 * ((14-m)//12) - 2
dow = int(d + x0 + 31 * m0//12) % 7

# if-elif statements to output correct answer.
if dow == 0:
    stdio.writeln("Sunday")
elif dow == 1:
    stdio.writeln("Monday")
elif dow == 2:
    stdio.writeln("Tuesday")
elif dow == 3:
    stdio.writeln("Wednesday")
elif dow == 4:
    stdio.writeln("Thursday")
elif dow == 5:
    stdio.writeln("Friday")
elif dow == 6:
    stdio.writeln("Saturday")
