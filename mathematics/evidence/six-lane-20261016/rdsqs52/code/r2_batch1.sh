#!/bin/bash
# R2 batch 1 (frozen in README §4 R2): doubling of cyclic SQS(26); multiplier groups M and resolution groups R.
cd "$(dirname "$0")"
PY=/Users/jinleic/.local/state/research-explorer/venv/bin/python
run() { # tag mult resmult samples timeout
  PYTHONHASHSEED=0 DOUBLING_Y=26 $PY doubling_pipeline.py runs/r2b1_$1 --mult "$2" --res-mult "$3" --samples $4 --res-timeout $5 --workers 3 > runs/r2b1_$1.out 2>&1
  echo "$1 $(tail -1 runs/r2b1_$1.out)"
}
run m7_r49 7 49 8 120
run m7_r5 7 5 8 120
run m7_r9 7 9 8 120
run m7_r25 7 25 8 120
run m17_r17 17 17 12 120
run m5_r5 5 5 12 120
run m9_r9 9 9 12 120
run m25_r25 25 25 12 120
