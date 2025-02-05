
#!/bin/bash
#BSUB -J seleper
#BSUB -q hpc
#BSUB -W 2
#BSUB -R "rusage[mem=512MB]"
#BSUB -o sleeper_%J.out
#BSUB -e sleeper_%J.err
#BSUB -notify "[exit ] [done ] [start ] [suspend]"

sleep 60
