#!/bin/bash

#Activate conda environment
#source /home/marcbo/.bashrc
[[ -f /itet-stor/${USER}/net_scratch/conda/bin/conda ]] && eval "$(/itet-stor/${USER}/net_scratch/conda/bin/conda shell.bash hook)"
conda activate deepcomenv
echo "Conda activated"


#Args
dataset=$1
model=$2

#Paths
source=/itet-stor/${USER}/codesearch-attacks_itetnas04/models_sourcecode/EMSE-DeepCom

mkdir -p $model/train
mkdir -p $model/test

#Preprocess
python3 $source/preprocess.py $dataset/train/train.jsonl.gz $model/train "train"
python3 $source/preprocess.py $dataset/test/test.jsonl.gz $model/test "test"

#Build ASTs
python3 $source/data_utils/get_ast.py $model/train/train.token.code $model/train/train.token.ast
python3 $source/data_utils/get_ast.py $model/test/test.token.code $model/test/test.token.ast

#Build vocab
python3 $source/build_vocab.py $model/train/train.token.code $model/vocab.code
python3 $source/build_vocab.py $model/train/train.token.nl $model/vocab.nl
#Copy in AST vocab file
cp $source/vocab/vocab.ast $model/vocab.ast

#Edit configs
python3 $source/set_configs.py $model $source/config.yaml

cd $source/source_code
#Train
python3 ./__main__.py ../config.yaml --train -v
