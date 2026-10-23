#!/bin/bash
# T2 structural alternatives at eta=0.733 (compare: rank-2 mod-3 (0,1) K=220 grid+25 iters -> 5.0e-9, g2 run)
cd "$(dirname "$0")/../../code"
run() { OMP_NUM_THREADS=1 nohup ../env/bin/python opt2_gauss.py --eta 0.733 --K 220 --D 320 --iters 25 --k $1 --res $2 --qs "$3" --tag s_k$1_r${2//,/} > ../evidence/gauss/s_k$1_r${2//,/}.log 2>&1 & }
run 3 0,1,2 "0.4,0.33"
run 4 0,1 "0.4,0.45,0.5"
run 4 0,2 "0.4,0.45,0.5"
run 5 0,1 "0.4,0.45,0.5"
