#!/bin/bash
### -- job name -- 
#BSUB -J runpython

### -- que -- 
#BSUB -q hpc

### -- time -- 
#BSUB -W 8

### -- memory per core  -- 
#BSUB -R "rusage[mem=4GB]"

### -- chagne output name -- 
#BSUB -o opg1_2_%J.out
#BSUB -e opg1_2_%J.err

#--- Select the model of the CPU  can get list by 'nodestat -F hpc'---
#BSUB -R "select[model ==  XeonGold6226R]"

### -- number of cores -- 
#BSUB -n 1

#--- print the hardweare you are using ---
lscpu
### -use a specific conda env
source /dtu/projects/02613_2025/conda/conda_init.sh
conda activate 02613

python ~/Documents/python-and-hpc/week_3/python_opg1.py

