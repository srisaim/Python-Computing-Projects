import rsa
import stdio
import sys


# Entry point.
def main():

    # Accepts private-keys int n and d as command-line arguments.
    # Gets the number of bits & accepts the message generated by encrypt.py
    n = int(sys.argv[1])
    d = int(sys.argv[2])
    width = rsa.bitLength(n)
    msg = stdio.readAll()

    # Length is equal to length of message.
    # (NOTE): Couldn't use variable "l" because it is an ambiguous variable.
    length = len(msg)

    # For i in range [0, length - 1) in width increments.
    # Set s equal to substring of message from i to i + width.
    # Set y to binary string s converted to decimal, using bin.2dec function.
    # Decrypt y.
    # Output the character corresponding to decrypted value, using chr().
    for i in range(0, length - 1, width):
        s = msg[i:i+width]
        y = rsa.bin2dec(s)
        decrypted = rsa.decrypt(y, n, d)
        stdio.write(chr(decrypted))


if __name__ == '__main__':
    main()
