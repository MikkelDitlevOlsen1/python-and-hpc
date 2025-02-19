#!/bin/bash
### -- job name -- 
#BSUB -J seleper

### -- que -- 
#BSUB -q hpc

### -- time -- 
#BSUB -W 2

### -- memory per core  -- 
#BSUB -R "rusage[mem=512MB]"

### -- chagne output name -- 
#BSUB -o sleeper_%J.out
#BSUB -e sleeper_%J.err

#--- Select the model of the CPU  can get list by 'nodestat -F hpc'---
#BSUB -R "select[model == XeonE5_2660v3]"

### -use a specific conda env
source /dtu/projects/02613_2025/conda/conda_init.sh
conda activate 02613

#--- print the hardweare you are using ---
lscpu
sleep 60
