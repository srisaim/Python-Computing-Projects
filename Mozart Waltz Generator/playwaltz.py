import stdaudio
import stdio
import sys

# Reads the input from generatewaltz program.
playwaltz = stdio.readAllStrings()

# Setting n equal to length of string.
n = len(playwaltz)

# Checking if waltz contain exactly 32 measures.
if n != 32:
    sys.exit("A waltz must contain exactly 32 measures")

# Checking if minuet measures, the first 16, are >= 1 and <= 176.
# If conditions fail, program will call sys.exit(message).
# If all is good, it will play the desired tune.
for i in range(0, 16):
    if int(playwaltz[i]) < 1 or int(playwaltz[i]) > 176:
        sys.exit("A minuet measure must be from [1, 176]")
    else:
        music1 = playwaltz[i]
        stdaudio.playFile("data/M" + music1)

# Checking if trio measures, the last 16, are >= 1 and <= 96.
# If conditions fail, program will call sys.exit(message).
# If all is good, it will play the desired tune.
for i in range(16, 32):
    if int(playwaltz[i]) < 1 or int(playwaltz[i]) > 96:
        sys.exit("A trio measure must be from [1, 96]")
    else:
        music2 = playwaltz[i]
        stdaudio.playFile("data/T" + music2)
