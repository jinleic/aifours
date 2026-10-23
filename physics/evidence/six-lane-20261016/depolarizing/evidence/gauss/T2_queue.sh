#!/bin/bash
# T2 queue (launch after the NEG certificate run finishes; 2 jobs x 2 threads = 4 workers)
cd "$(dirname "$0")/../../code"
OMP_NUM_THREADS=2 nohup ../env/bin/python opt2_gauss.py --eta 0.733 --K 450 --D 590 --iters 40 --init ../evidence/gauss/g3_eta0733_padK450.pt --tag g4 > ../evidence/gauss/g4_eta0.733.log 2>&1 &
OMP_NUM_THREADS=2 nohup ../env/bin/python opt2_gauss.py --eta 0.731 --K 450 --D 590 --iters 40 --init ../evidence/gauss/g3_eta0733_padK450.pt --tag g4 > ../evidence/gauss/g4_eta0.731.log 2>&1 &
