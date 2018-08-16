import glob
import itertools
import numpy as np

with open("filelist.txt", "r") as f:
    filelist = f.read().splitlines()

n = 37

for i, items in enumerate(np.array_split(filelist, n)):
    with open("filelist/filelist.txt.{}".format(i), "w") as f:
        for line in items:
            f.write(line + "\n")
