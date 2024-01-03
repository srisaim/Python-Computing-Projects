import stdio
import stdrandom
import sys


# Generates and returns the public/private keys as a tuple (n, e, d). Prime numbers p and q.
# Needed to generate the keys are picked from the interval [lo, hi).
def keygen(lo, hi):

    # List of primes from [lo, hi).
    primes = _primes(lo, hi)

    # Use _choice function to get random prime value from list primes.

    p = _choice(primes)
    q = _choice(primes)

    # Set n = (pq), and m = (p-1)(q-1).
    n = p * q
    m = (p - 1) * (q - 1)

    # Get a random prime e from the list, that e does not divide m.
    # Use _primes function to get list of primes from [2, m).
    # Use _choice function to get a random value from e_primes list.
    # Find d [1, m), such that ed mod m = 1.
    # Return tuple (n, e, d)
    while True:
        e_primes = _primes(2, m)
        e = _choice(e_primes)
        if m % e != 0:
            break
    d = 0
    for i in range(1, m):
        if (e * i) % m == 1:
            d = i
            break
    return n, e, d


# Encrypts x (int) using the public key (n, e) and returns the encrypted value.
# Use given formula to return answer.
def encrypt(x, n, e):
    return (x**e) % n


# Decrypts y (int) using the private key (n, d) and returns the decrypted value.
# Use given formula to return answer.
def decrypt(y, n, d):
    return (y**d) % n


# Returns the least number of bits needed to represent n.
def bitLength(n):
    return len(bin(n)) - 2


# Returns the binary representation of n expressed in decimal, having the given width, and padded
# with leading zeros.
def dec2bin(n, width):
    return format(n, '0%db' % (width))


# Returns the decimal representation of n expressed in binary.
def bin2dec(n):
    return int(n, 2)


# Returns a list of primes from the interval [lo, hi).
# Checks all prime numbers from [lo, hi), and then returns all prime numbers in list primes.
# Uses primality test from textbook.
def _primes(lo, hi):
    list = []
    for p in range(lo, hi):
        if p > 1:
            for i in range(2, p):
                if p % i == 0:
                    break
            else:
                list += [p]
    return list


# Returns a list containing a random sample (without replacement) of k items from the list a.
# Create b list that is a copy of a, and then slice the first k elements of b, which is a new list.
# Shuffle the list and return the new list.
def _sample(a, k):
    b = a.copy()
    list = b[0:k]
    list_rand = len(list)
    for i in range(list_rand):
        r = stdrandom.uniformInt(i, list_rand)
        temp = list[r]
        list[r] = list[i]
        list[i] = temp
    return list


# Returns a random item from the list a.
# Set c equal to length of list a and then find random number from [0, c), which will equal r.
# Find the rth element in list a and return that.
# (NOTE): Couldn't set len(a) to variable "l" because it is an ambiguous variable.
def _choice(a):
    c = len(a)
    r = stdrandom.uniformInt(0, c)
    answer = a[r]
    return answer


# Unit tests the library [DO NOT EDIT].
def _main():
    x = ord(sys.argv[1])
    n, e, d = keygen(25, 100)
    encrypted = encrypt(x, n, e)
    stdio.writef('encrypt(%c) = %d\n', x, encrypted)
    decrypted = decrypt(encrypted, n, d)
    stdio.writef('decrypt(%d) = %c\n', encrypted, decrypted)
    width = bitLength(x)
    stdio.writef('bitLength(%d) = %d\n', x, width)
    xBinary = dec2bin(x, width)
    stdio.writef('dec2bin(%d) = %s\n', x, xBinary)
    stdio.writef('bin2dec(%s) = %d\n', xBinary, bin2dec(xBinary))


if __name__ == '__main__':
    _main()
