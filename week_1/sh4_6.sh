

#!/bin/bash
#BSUB -J seleper
#BSUB -q hpc
#BSUB -W 2
#BSUB -R "rusage[mem=512MB]"
#BSUB -o sleeper_%J.out
#BSUB -e sleeper_%J.err


### -- number of cores -- 
#BSUB -n 64

### -- node nomber -- 
#BSUB -R "span[hosts=1]"

sleep 60
