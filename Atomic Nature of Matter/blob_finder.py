import luminance
import stdarray
import stdio
import sys
from blob import Blob
from picture import Picture


# A data type to identify blobs in a picture.
class BlobFinder:
    # Constructs a blob finder to find blobs in the picture pic, using a luminance threshold tau.
    def __init__(self, pic, tau):
        # Initialize an empty list for the blobs in pic.
        self._blobs = []

        # Create a 2D list of booleans called marked, having the same dimensions as pic.
        # X is pic width while y is pic height.
        x = pic.width()
        y = pic.height()
        marked = stdarray.create2D(x, y, False)

        # Enumerate the pixels of pic, and for each pixel (i, j):
        # 1. Create a Blob object called blob.
        # 2. Call self._findBlob() with the right arguments.
        # 3. Add blob to self.blobs if it has a non-zero mass.
        for i in range(x):
            for j in range(y):
                blob = Blob()
                self._findBlob(pic, tau, i, j, marked, blob)
                if blob.mass() > 0:
                    self._blobs += [blob]

    # Returns a list of all beads (blobs with mass >= pixels).
    # Using a for loop, it will return a list of blobs that have a mass >= pixels.
    def getBeads(self, pixels):
        temp = []
        for i in range(len(self._blobs)):
            if self._blobs[i].mass() >= pixels:
                temp += [self._blobs[i]]
        return temp

    # Identifies a blob using depth-first search. The parameters are the picture (pic), luminance
    # threshold (tau), pixel column (i), pixel row (j), 2D boolean matrix (marked), and the blob
    # being identified (blob).
    def _findBlob(self, pic, tau, i, j, marked, blob):
        # Base case: return if pixel (i, j) is out of bounds, or if it is marked, or if its
        # luminance is less than tau.
        if i < 0 or i >= pic.width():
            return
        if j < 0 or j >= pic.height():
            return
        if marked[i][j]:
            return
        if luminance.luminance(pic.get(i, j)) < tau:
            return

        # Mark the pixel.
        marked[i][j] = True

        # Add the pixel to blob.
        blob.add(i, j)

        # Recursively call self._findBlob() on the N, E, W, S pixels.
        self._findBlob(pic, tau, i - 1, j, marked, blob)
        self._findBlob(pic, tau, i, j + 1, marked, blob)
        self._findBlob(pic, tau, i, j - 1, marked, blob)
        self._findBlob(pic, tau, i + 1, j, marked, blob)


# Unit tests the data type (DO NOT EDIT).
def _main():
    pixels = int(sys.argv[1])
    tau = float(sys.argv[2])
    pic = Picture(sys.argv[3])
    bf = BlobFinder(pic, tau)
    beads = bf.getBeads(pixels)
    stdio.writef('%d Beads:\n', len(beads))
    for blob in beads:
        stdio.writeln(str(blob))
    blobs = bf.getBeads(1)
    stdio.writef('%d Blobs:\n', len(blobs))
    for blob in blobs:
        stdio.writeln(str(blob))


if __name__ == '__main__':
    _main()
