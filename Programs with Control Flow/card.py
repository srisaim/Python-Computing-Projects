import stdio
import stdrandom

# Setting rank to random integers from 2 to 14.
rank = stdrandom.uniformInt(2, 15)

# Setting rank as a string.
# If-elif statements to get a random card depending on random number.
rankStr = str(rank)
if rank == 11:
    rankStr = "Jack"
elif rank == 12:
    rankStr = "Queen"
elif rank == 13:
    rankStr = "King"
elif rank == 14:
    rankStr = "Ace"

# Setting suit to random integers from 1 to 4.
suit = stdrandom.uniformInt(1, 5)

# Setting suit as a string.
# If-elif statements to get a random card depending on random number.
suitStr = str(suit)
if suit == 1:
    suitStr = "Clubs"
elif suit == 2:
    suitStr = "Diamonds"
elif suit == 3:
    suitStr = "Hearts"
elif suit == 4:
    suitStr = "Spades"

# Output final answer.
stdio.writeln(rankStr + ' of ' + suitStr)
