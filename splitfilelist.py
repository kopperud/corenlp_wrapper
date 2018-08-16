import glob
import itertools

with open("filelist.txt", "r") as f:
    filelist = f.read().splitlines()

for i, items in enumerate(itertools.tee(filelist, 165)):
    with open("filelist/filelist.txt.{}".format(i), "w") as f:
        for line in items:
            f.write(line + "\n")
