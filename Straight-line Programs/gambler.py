import stdio
import sys

# Input int n1, n2, and float p.
n1 = int(sys.argv[1])
n2 = int(sys.argv[2])
p = float(sys.argv[3])

# Define q.
q = 1 - p

# Formula to find p1 & p2.
p1 = (1-((p/q)**n2))/(1-((p/q)**(n1+n2)))
p2 = (1-((q/p)**n1))/(1-((q/p)**(n1+n2)))

# Output final answer.
stdio.writeln(str(p1) + ' ' + str(p2))
