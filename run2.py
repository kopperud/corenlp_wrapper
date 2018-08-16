## Imports
import pandas as pd
import numpy as np
import re
import itertools
import string
import json
import os
import types
import csv
import shlex
import requests
import glob
import time
import ntpath
import collections

from collections import namedtuple
from operator import itemgetter
from pycorenlp import StanfordCoreNLP
from tqdm import tqdm

from utils import *



nlp = StanfordCoreNLP("http://localhost:9000")
ner_path = "regexner_rules.txt"






txt_paths = glob.glob("content/**/*.txt")

existing = [ntpath.basename(x).replace(".json","") for x in glob.glob("output/**/*.json")]


        
for path in tqdm(txt_paths[2852+1085:]):
    if ntpath.basename(path).replace(".txt", "") not in existing and is_eng(path):       
        with open(path, "r") as f:
            txt = f.read()
        annotate(path, ner_path, txt, nlp)
