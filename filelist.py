import glob, tqdm, json

from utils import *

fpaths = glob.glob("content/*/*.txt")

filelist = []

print("Checking if contents is in english, and appending to filelist.txt")

for path in tqdm.tqdm(fpaths):
    if is_eng(path):
        res = "./" + path
        filelist.append(res)

with open("filelist.txt", "w") as f:
    for line in filelist:
        f.write(line + "\n")
