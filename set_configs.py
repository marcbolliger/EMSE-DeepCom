import os
import sys

#Cmdline arguments:
#[1] - path to model directory
#[2] - path to config.yaml
modelpath = sys.argv[1]
yamlpath = sys.argv[2]

data_line = 90
data_entry = "data_dir: "+modelpath+"\n"
model_line = 91
model_entry = "model_dir: "+modelpath + "/model\n"

data = []

with open(yamlpath, "r") as file:
    data = file.readlines()
    data[data_line] = data_entry
    data[model_line] = model_entry
with open(yamlpath, "w") as outfile:
    outfile.writelines(data)
