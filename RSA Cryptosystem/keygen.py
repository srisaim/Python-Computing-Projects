import rsa
import stdio
import sys


# Entry point.
def main():

    # Accept int lo & hi as command-line arguments.
    lo = int(sys.argv[1])
    hi = int(sys.argv[2])

    # Gets public & private keys as tuple.
    list = rsa.keygen(lo, hi)

    # Outputs the three values, separated by a space.
    a = list[0]
    b = list[1]
    c = list[2]

    stdio.writeln(str(a) + " " + str(b) + " " + str(c))


if __name__ == '__main__':
    main()
