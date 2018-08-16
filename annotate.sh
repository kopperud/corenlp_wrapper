#!/bin/bash
#
# Environment variable, controlled by Array Jobs
#
# $TASK_ID
#


java -cp "/uio/kant/nhm-sfs-u2/bjorntko/natural_language_processing/*" -Xmx50g edu.stanford.nlp.pipeline.StanfordCoreNLP -props myprops.props -filelist ./filelist.txt.$TASK_ID
