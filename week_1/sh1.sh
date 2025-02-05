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

sleep 60
