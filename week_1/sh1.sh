#!/bin/bash
#BSUB  -j seleper
#BSUB  -q hcp
#BSUB  -w 2
#BSUB -R "rusage[mem=512MB]"
#BSUB -o sleeper_%J.out
#BSUB -e sleeper_%J.err

sleep 60