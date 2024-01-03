import rsa
import stdio
import sys


# Entry point.
def main():

    # Accepts public-key int n & e as command-line arguments.
    n = int(sys.argv[1])
    e = int(sys.argv[2])

    # Gets the number of bits per character, using bitLength function.
    # Accepts user message.
    width = rsa.bitLength(n)
    msg = stdio.readAll()

    # For each c in message, use ord() to convert c into an integer.
    # Encrypt x.
    # Write encrypted value as width-long binary string using dec2bin function.
    for c in msg:
        x = ord(c)
        ans = rsa.encrypt(x, n, e)
        stdio.write(rsa.dec2bin(ans, width))

    stdio.writeln()


if __name__ == '__main__':
    main()
