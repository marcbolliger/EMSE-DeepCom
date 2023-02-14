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
    codepath=outpath+prefix+".token.code"
    nlpath=outpath+prefix+".token.nl"
    with gzip.open(datapath) as f:
        with open(codepath, 'w') as codefile:
            with open(nlpath, 'w') as nlfile:
                for line in f:
                    data = json.loads(line)
                    code = data["code"]
                    nl = data["docstring"]
                    codefile.write(code)
                    nlfile.write(nl)

preprocess(outpath, datapath, prefix)
