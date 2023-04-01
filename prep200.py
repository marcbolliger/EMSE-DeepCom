import json
import os
import sys
import gzip

#Cmdline arguments:
#[1] - path to dataset/attack(direct path to json)
#[2] - path to output/processed data
#[3] - prefix is either 'train' or 'test'
datapath = sys.argv[1]
outpath = sys.argv[2]
prefix = sys.argv[3]

def preprocess(outpath, datapath, prefix):
    print("Preprocessing "+datapath+"...", flush=True)
    codepath=outpath+"/"+prefix+".token.code"
    nlpath=outpath+"/"+prefix+".token.nl"
    with gzip.open(datapath) as f:
        with open(codepath, 'w') as codefile:
            with open(nlpath, 'w') as nlfile:
                for i,line in enumerate(f):
                    if i >=200:
                        break
                    data = json.loads(line)
                    code = data["code"]
                    code = code.split()
                    code = ' '.join(code)
                    nl = data["docstring"]
                    nl = nl.split()
                    nl = ' '.join(nl)
                    codefile.write(code+"\n")
                    nlfile.write(nl+"\n")

preprocess(outpath, datapath, prefix)
