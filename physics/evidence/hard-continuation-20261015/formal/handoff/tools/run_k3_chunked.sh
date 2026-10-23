#!/bin/sh
# Chunked k = 3 certificate pipeline. Every Lean process runs alone under an RSS cap (default
# 4 GiB) enforced by tools/watch_cmd.py; each run appends its peak to logs/memory-k3.jsonl.
# Usage: run_k3_chunked.sh <formal-dir> data
#        run_k3_chunked.sh <formal-dir> checks <table-chunk-size> <moment-chunk-terms>
set -u
F=$1; PHASE=$2
CAP=${CAP_KB:-4194304}
export PATH=$F/env/toolchains/lean-4.24.0-darwin_aarch64/bin:$PATH
export LEAN_NUM_THREADS=${LEAN_NUM_THREADS:-2} MATHLIB_CACHE_DIR=$F/env/mathlib-cache
W="python3 $F/tools/watch_cmd.py $CAP $F/logs/memory-k3.jsonl --"
cd $F/lean
run() { log=$1; shift; "$@" > "$log" 2>&1; rc=$?; echo "$(basename $log): $(tail -1 $log)"; return $rc; }
if [ "$PHASE" = data ]; then
  run $F/logs/build-k3-tables.log $W lake build KSatUpper.NumericalCriterionTables || exit 1
  run $F/logs/gen-k3-tables.out $W lake env lean $F/audit/GenK3Tables.lean || exit 1
  grep -E '^[ABCD] value' $F/logs/gen-k3-tables.out
  python3 $F/tools/gen_k3_tables.py data $F/logs/gen-k3-tables.out || exit 1
  run $F/logs/build-k3-data.log $W lake build KSatUpper.K3Data || exit 1
fi
if [ "$PHASE" = checks ]; then
  mkdir -p $F/logs/k3-chunks
  for m in $(python3 $F/tools/gen_k3_tables.py checks ${3:-6} ${4:-600}); do
    run $F/logs/k3-chunks/build-$m.log $W lake build KSatUpper.$m || { echo "FAILED $m"; exit 1; }
  done
  run $F/logs/k3-chunks/build-ThresholdK3.log $W lake build KSatUpper.ThresholdK3 || exit 1
fi
