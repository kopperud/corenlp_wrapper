import subprocess
import shlex
import re
import json
import os


def is_eng(txt_path):
    bashCommand = 'cat %s | franc' % shlex.quote(format(txt_path))

    p = subprocess.Popen(bashCommand, 
                         shell=True, 
                         stdout=subprocess.PIPE,
                         stderr=subprocess.PIPE,
                         stdin=subprocess.PIPE)

    b = p.stdout.read()
    res = set(b.decode("utf-8").split("\n"))
    if "eng" in res:
        return(True)
    else:
        return(False)



   
def annotate(filepath, ner_path, text, nlp, verbose = False):
    data = re.sub("\xad\n", "", text) ## Remove hyphens on linebreaks
    data = re.sub("\xad", "", data) ## Remove hyphen artifacts, e.g. "Sera\xadvellian"

    ## Strip everything after references. This pattern is likely not general enough, 
    ## and will need to be optimized to account for various ways of indicating a references-section.
    data = data[0:data.rfind("References")]



    p = {'annotators': 'tokenize,ssplit,pos,lemma,regexner,ner,depparse', 'pipelineLanguage': 'en', 
         'outputFormat':'json', 'regexner.mapping':ner_path, 
        # 'ssplit.tokenPatternsToDiscard':token_discard,
         'regexner.backgroundSymbol': "ORGANIZATION,PERSON,LOCATION,MISC,O",
         'ner.model': "edu/stanford/nlp/models/ner/english.all.3class.distsim.crf.ser.gz",
         'options': "splitHyphenated=true",
         'timeout': '540000',
         'threads': '32'}
    

    x = nlp.annotate(data, properties = p)

    if x == "CoreNLP request timed out. Your document may be too long.":
        print("Timeout (likely), perhaps doc too long. Skipping", filepath)
        return(None)

    if "Request is too long" in x:
        print(x, " -- skipping.")
        return(None)

    if x == "Could not handle incoming annotation":
        raise ValueError(x)
            
    d = [x]
        
    writepath = filepath.replace("content", "output").replace(".pdf", "").replace(".txt", "") + ".json"

    os.makedirs(os.path.dirname(writepath), exist_ok = True)
    with open(writepath, "w") as f:
        if verbose:
            print("Writing", writepath)
        f.write(json.dumps(d))
        f.close()

