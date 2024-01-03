import math
import stdio
import sys
from blob_finder import BlobFinder
from picture import Picture


# Entry point
def main():

    # Accept pixels as command-line argument int.
    # Accept tau & delta as command-line arguments float.
    # Accepts a sequence of JPEG filenames as command-line argument to check.
    # Variable n equals the length of jpg_files.
    pixels = int(sys.argv[1])
    tau = float(sys.argv[2])
    delta = float(sys.argv[3])
    jpg_files = sys.argv[4:]

    # Get a list of beads "prevBeads" that have at least pixels pixels.
    prevBeads = BlobFinder(Picture(jpg_files[0]), tau).getBeads(pixels)

    # Loop through the list using for loop.
    # Get list of beads "currBeads" that have at least pixels pixels.
    for i in sys.argv[5:]:
        # Construct a blobFinder and get a list of beads.
        currBeads = BlobFinder(Picture(i), tau).getBeads(pixels)

        # For each "currBead" find a "prevBead" that is no further than delta.
        # And it should be closest to "currBead," if a bead is found, write the distance.
        # Write a newline character and set prevBeads to currBeads.
        for currBead in currBeads:
            distance = min(currBead.distanceTo(x) for x in prevBeads)
            if distance <= delta:
                stdio.writef('%.4f\n', distance)
        stdio.writeln()
        prevBeads = currBeads


if __name__ == '__main__':
    main()
