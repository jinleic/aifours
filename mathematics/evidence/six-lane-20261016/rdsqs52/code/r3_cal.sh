#!/bin/bash
# R3 calibration at known orders (frozen in README §4 R3).
cd "$(dirname "$0")"
PY=/Users/jinleic/.local/state/research-explorer/venv/bin/python
run() { # tag q corder extra...
  tag=$1; q=$2; c=$3; shift 3
  PYTHONHASHSEED=0 $PY r3_pipeline.py $q runs/r3cal_$tag --c-order $c "$@" --samples 4 --res-timeout 60 --workers 4 > runs/r3cal_$tag.out 2>&1
  echo "$tag $(head -1 runs/r3cal_$tag.out | cut -c1-160) || $(tail -1 runs/r3cal_$tag.out)"
}
run q7_c3 7 3
run q7_c6 7 6
run q7_c3_sw 7 3 --swap
run q13_c3 13 3
run q13_c4 13 4
run q13_c6 13 6
run q13_c12 13 12
run q13_c3_sw 13 3 --swap
run q13_c6_sw 13 6 --swap
run q19_c3 19 3
run q19_c9 19 9
run q19_c9_sw 19 9 --swap
