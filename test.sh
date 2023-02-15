#!/bin/bash

#Activate conda environment
#source /home/marcbo/.bashrc
[[ -f /itet-stor/${USER}/net_scratch/conda/bin/conda ]] && eval "$(/itet-stor/${USER}/net_scratch/conda/bin/conda shell.bash hook)"
conda activate deepcom_env
echo "Conda activated"


#Args
dataset=$1
model=$2

#Paths
source=/itet-stor/${USER}/codesearch-attacks_itetnas04/models_sourcecode/EMSE-DeepCom

mkdir -p $model/test

#Preprocess
python3 $source/preprocess.py $dataset/test/test.jsonl.gz $model/test "test"

#Build ASTs
python3 $source/data_utils/get_ast.py $model/test/test.token.code $model/test/test.token.ast

cd $source/source_code
#Train
python3 ./__main__.py ../config.yaml --eval --output=$model/predictions.nl -v

#Calculate BLEU
perl $source/scripts/multi-bleu.perl $model/test/test.token.nl < $model/predictions.nl
