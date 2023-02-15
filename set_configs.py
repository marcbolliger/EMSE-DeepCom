import os
import sys

#Cmdline arguments:
#[1] - path to model directory
#[2] - path to config.yaml
modelpath = sys.argv[1]
yamlpath = sys.argv[2]

data_line = 91
data_entry = "data_dir: "+modelpath+"\n"
model_line = 92
model_entry = "model_dir: "+modelpath + "/model\n"

with open(yamlpath, "r+") as file:
    data = file.readlines()
    data[data_line] = data_entry
    data[model_line] = model_entry
    file.writelines(data)
