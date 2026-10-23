#!/bin/bash
# R3 main batch 1 at q=25 (v=52): C in {24,12,8,6,4,3,2}, with/without swap; R(∞)=translations, R(finite)=C.
cd "$(dirname "$0")"
PY=/Users/jinleic/.local/state/research-explorer/venv/bin/python
run() { tag=$1; c=$2; shift 2
  PYTHONHASHSEED=0 $PY r3_pipeline.py 25 runs/r3q25_$tag --c-order $c --rinf-c 1 "$@" --samples 8 --res-timeout 120 --workers 4 > runs/r3q25_$tag.out 2>&1
  echo "$tag | $(head -1 runs/r3q25_$tag.out | cut -c1-150) | SATlines $(grep -c '"status": "SAT"' runs/r3q25_$tag.out) | $(grep CERT runs/r3q25_$tag.out | head -1) | $(tail -1 runs/r3q25_$tag.out)"
}
for c in 24 12 8 6 4 3 2; do run c${c} $c; run c${c}_sw $c --swap; done
