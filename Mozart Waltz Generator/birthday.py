import stdarray
import stdio
import stdrandom
import sys

# Variables in upper case is a constant.
DAYS_PER_YEAR = 365

# Accept trials (int) as command-line argument.
trials = int(sys.argv[1])

# Set count, denoting the total number of individuals sampled across the trials number of
# experiments, to 0.
count = 0

# For i in range from 0 to trials. Other way is (0, trials - 1).
for i in range(trials):
    # Perform trials number of experiments, where each experiment involves sampling individuals
    # until a pair of them share a birthday...

    # Setup a 1D list birthdaysSeen of DAYS_PER_YEAR booleans, all set to False by default.
    # This list will keep track of the birthdays encountered in this experiment.
    birthdaysSeen = stdarray.create1D(DAYS_PER_YEAR, False)

    while True:
        # Sample individuals until match...

        # Increment count by 1.
        # This is when someone entered the room.
        count = count + 1

        # Set birthday to a random integer from [0, DAYS_PER_YEAR).
        # Starting from 0, so up to 364 days not 365.
        birthday = stdrandom.uniformInt(0, DAYS_PER_YEAR)

        if birthdaysSeen[birthday]:
            # Same as birthdaysSeen[birthday] == True
            # If birthday has been encountered, abort this experiment, ie, break.
            # Someone has the same birthday in the room.
            break
        else:
            # Record the fact that we are seeing this birthday for the first time.
            # Someone with a new birthday entered the room.
            # Change the position False to True because someone has that birthday.
            birthdaysSeen[birthday] = True

# Write to standard output the average number of people that must be sampled before a match,
# as an int.
# Use float division to make sure individuals are counted as whole.
stdio.writeln(count//trials)
