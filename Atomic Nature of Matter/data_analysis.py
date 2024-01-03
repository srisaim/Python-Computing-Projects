import math
import stdio


# Entry point.
def main():

    # Initialize ETA, RHO, T, and R to appropriate values.
    # "p_to_m" is value to multiply to convert pixel to meter.
    R = 8.31457
    T = 297
    ETA = 9.135 * 10 ** (-4)
    RHO = 0.5 * 10 ** (-6)
    P_TO_M = 0.175 * 10 ** (-6)

    # Receive a string of numbers from bead_tracker.py output.
    # Set n to the length of string.
    # Set var equal to 0.
    values = stdio.readAllFloats()
    n = len(values)
    var = 0

    # Use a for loop to add sum of the squares of n displacements.
    # (Converted from pixels to meters).
    for i in values:
        i = i * P_TO_M
        var += i * i
    var = var/(2 * n)

    # Estimate Boltzmann's Constant.
    k = 6 * math.pi * var * ETA * RHO / T

    # Estimate Avogadro's Constant.
    avo = (R / k)

    # Output the final answer.
    stdio.write('%e' % k)
    stdio.write(" ")
    stdio.writeln('%e' % avo)


if __name__ == '__main__':
    main()
