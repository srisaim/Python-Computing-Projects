import stdarray
import stdrandom
import stdio

# Accept the minuet measures from standard input, 2D list, 11 x 16 dimensions.
# Same concept from transpose.py.
minuet = stdarray.create2D(11, 16, 0)
for i in range(11):
    for j in range(16):
        minuet[i][j] = stdio.readInt()

# Accept the trio measures from standard input, 2D list, 6 x 16 dimensions.
trio = stdarray.create2D(6, 16, 0)
for i in range(6):
    for j in range(16):
        trio[i][j] = stdio.readInt()

# Generate 16 random minuet measures using stdrandom.uniformInt.
# Generate a number from 0 through 6.
for i in range(0, 16):
    random1 = stdrandom.uniformInt(1, 7)
    random2 = stdrandom.uniformInt(1, 7)
    random3 = random1 + random2
    stdio.write(minuet[random3 - 2][i])
    stdio.write(" ")

# Generate 16 random trio measures using stdrandom.uniformInt.
# Generate a number from 0 through 6.
for i in range(0, 16):
    random = stdrandom.uniformInt(1, 7)
    stdio.write(trio[random - 1][i])
    stdio.write(" ")
