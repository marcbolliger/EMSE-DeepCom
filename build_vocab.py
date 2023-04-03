from collections import Counter
import os
import sys

#Cmdline arguments:
#[1] - path to source file
#[2] - vocab file path
datapath = sys.argv[1]
outpath = sys.argv[2]

vocab = Counter()

with open(datapath,'r') as f:
    with open(outpath,'w') as outfile:
        for line in f:
            vocab.update(line.split())
        #Write back 30k most frequent words, line by line
        for word,count in vocab.most_common(30000):
            outfile.write(word+"\n")

