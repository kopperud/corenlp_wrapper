## Imports
#import pandas as pd
import json
import os
import shlex
import glob
import ntpath
import pandas as pd

from collections import defaultdict
from pycorenlp import StanfordCoreNLP
from tqdm import tqdm

from utils import *



nlp = StanfordCoreNLP("http://localhost:9000")
ner_path = "regexner_rules.txt"
verbose = False





txt_paths = glob.glob("content/**/*.txt")

existing = [ntpath.basename(x).replace(".json","") for x in glob.glob("output/**/*.json")]
#existing = []

df = pd.read_csv("is_english.csv")
is_english0 = {row[1]["archive_id"]: row[1]["english"] for row in df.iterrows()}
is_english = defaultdict(lambda: False, is_english0)



        
for path in tqdm(txt_paths):
#    if ntpath.basename(path).replace(".txt", "") not in existing and is_eng(path):       
    if ntpath.basename(path).replace(".txt", "") not in existing and is_english[path.split("/")[1]]:       
        with open(path, "r") as f:
            txt = f.read()
        d = annotate(path, ner_path, txt, nlp)

#        print(d)

        writepath = path.replace("content", "output").replace(".pdf", "").replace(".txt", "") + ".json"

        os.makedirs(os.path.dirname(writepath), exist_ok = True)
        with open(writepath, "w") as f:
            if verbose:
                print("Writing", writepath)
            f.write(json.dumps(d))
            f.close()


