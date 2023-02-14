#!/bin/bash

#Prepare the dataset from mlmfc and train the model
dataset=$1
model=$2

python3 ./source_code/__main__.py config.yaml --train -v
