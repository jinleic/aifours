#!/bin/bash
set -eu
export TMPDIR="$(pwd)/tmp"
for c in ctl_dup_exact ctl_dup_disguised ctl_corrupt_entry ctl_par_swap ctl_par_change ctl_omit ctl_invariance; do
  src/run.sh "${c}_norm" 900 ./build/ls147_norm "controls/$c/input.txt" 17000000
  src/run.sh "${c}_autpar" 900 ./build/ls147_autpar "controls/$c/input.txt"
  if [ "$c" = ctl_invariance ]; then
    src/run.sh "${c}_check" 300 /usr/bin/python3 -B src/ls147_check.py check "controls/$c/input.txt" "runs/${c}_norm.out" "runs/${c}_autpar.out" inputs/parent-k1-route1/full_run.out inputs/MANIFEST.json "controls/$c/verdict.json" runs/norm_main_union.out runs/autpar_main.out
  else
    src/run.sh "${c}_check" 300 /usr/bin/python3 -B src/ls147_check.py check "controls/$c/input.txt" "runs/${c}_norm.out" "runs/${c}_autpar.out" inputs/parent-k1-route1/full_run.out inputs/MANIFEST.json "controls/$c/verdict.json"
  fi
done
