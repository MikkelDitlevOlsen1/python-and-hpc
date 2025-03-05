#!/bin/bash
### -- job name -- 
#BSUB -J runpython

### -- que -- 
#BSUB -q hpc

### -- time -- 
#BSUB -W 8

### -- memory per core  -- 
#BSUB -R "rusage[mem=4GB]"
#BSUB -R "span[hosts=1]"

### -- chagne output name -- 
#BSUB -o opg2_1_%J.out
#BSUB -e opg2_1_%J.err

#--- Select the model of the CPU  can get list by 'nodestat -F hpc'---
#BSUB -R "select[model ==  XeonGold6226R]"

### -- number of cores -- 
#BSUB -n 10

#--- print the hardweare you are using ---
lscpu
### -use a specific conda env
source /dtu/projects/02613_2025/conda/conda_init.sh
conda activate 02613

###python -m cProfile -s cumulative ~/Documents/python-and-hpc/week_4/task2.py /dtu/projects/02613_2025/data/locations/locations_500.csv
time python ~/Documents/python-and-hpc/week_5/Task2_1.py
time python ~/Documents/python-and-hpc/week_5/Task2_2.py
time python ~/Documents/python-and-hpc/week_5/Task2_3.py

###python  task2.py input.csv 
