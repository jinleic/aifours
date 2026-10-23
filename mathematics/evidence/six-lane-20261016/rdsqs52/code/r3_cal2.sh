#!/bin/bash
# R3 calibration 2: R at ∞ = translations only (--rinf-c 1); R at finite points = C.
cd "$(dirname "$0")"
PY=/Users/jinleic/.local/state/research-explorer/venv/bin/python
run() { tag=$1; q=$2; c=$3; shift 3
  PYTHONHASHSEED=0 $PY r3_pipeline.py $q runs/r3cal2_$tag --c-order $c --rinf-c 1 "$@" --samples 8 --res-timeout 60 --workers 4 > runs/r3cal2_$tag.out 2>&1
  echo "$tag $(grep -c '"status": "SAT"' runs/r3cal2_$tag.out) SAT-lines || $(grep CERT runs/r3cal2_$tag.out | head -2) || $(tail -1 runs/r3cal2_$tag.out)"
}
run q7_c3 7 3
run q7_c3_sw 7 3 --swap
run q13_c3 13 3
run q13_c3_sw 13 3 --swap
run q19_c3 19 3
run q19_c9 19 9
run q19_c9_sw 19 9 --swap
