#!/bin/bash

#~/natural_language_processing/start.sh &

#python3 run.py

#ps aux | grep "CoreNLPServer" | awk '{print $2}' | xargs kill


#java -cp "/uio/kant/nhm-sfs-u2/bjorntko/natural_language_processing/*" -Xmx50g edu.stanford.nlp.pipeline.StanfordCoreNLP -props myprops.props -file ./content/bulletinunitedst961917unit/bulletinunitedst961917unit_djvu.txt

java -cp "/uio/kant/nhm-sfs-u2/bjorntko/natural_language_processing/*" -Xmx50g edu.stanford.nlp.pipeline.StanfordCoreNLP -props myprops.props -filelist ./filelist.txt
