import stdio
import sys

# Accept int n as a command-line argument
n = int(sys.argv[1])

# Set a equal to 1, because 1 <= a.
a = 1

# While a^3 <= n.
# Set b equal to a + 1, because a + 1 <= b.
while (a * a * a) <= n:
    b = a + 1

    # While b^3 <= n-(a^3).
    # Set c equal to a + 1, because a + 1 <= c.
    while (b * b * b) <= (n - (a * a * a)):
        c = a + 1

        # While c^3 <= n.
        # Set d equal to c + 1, because c + 1 <= d.
        while (c * c * c) <= n:
            d = c + 1

            # While d^3 <= n - (c^3).
            # If (a^3) + (b^3) = (c^3) + (d^3), output the answer.
            while (d * d * d) <= (n - (c * c * c)):
                if (a * a * a + b * b * b) == (c * c * c + d * d * d):
                    stdio.writeln(str(a * a * a + b * b * b) + " = " + str(a) + "^3 + " + str(b) +
                                  "^3 = " + str(c) + "^3 + " + str(d) + "^3")
                d = d + 1

            c = c + 1

        b = b + 1

    a = a + 1
