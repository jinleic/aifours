#!/bin/bash
# v3 provenance-bound reruns (frozen code: ../code_snapshot_v3, numpy DD path only; no C kernel)
cd "$(dirname "$0")/../code_snapshot_v3"
PY=../../../env/bin/python
run() {  # $1 = witness, $2 = tag, $3.. = ranges
  w=$1; tag=$2; shift 2
  for r in "$@"; do
    OMP_NUM_THREADS=1 $PY cert.py $w --out ../v3/${tag}_part_${r/:/_}.json --ptail 1e-13 --pitail 1e-40 --sectors $r > ../v3/${tag}_part_${r/:/_}.log 2>&1 &
  done
  wait
  $PY combine.py $w ../v3/${tag}_part_*.json.sectors.jsonl --ptail 1e-13 --pitail 1e-40 --out ../v3/${tag}_TOTAL.json > ../v3/${tag}_combine.log 2>&1
  echo "combine_exit=$?" >> ../v3/${tag}_combine.log
  $PY replay.py $w ../v3/${tag}_part_*.json.sectors.jsonl --ptail 1e-13 --pitail 1e-40 --random 4 --seed 20261016 > ../v3/${tag}_replay.log 2>&1
  echo "replay_exit=$?" >> ../v3/${tag}_replay.log
}
date > ../v3/run_v3.started
run ../witness_g3_M2000_p1_5.json p1_5 1236:1344 1346:1454 1456:1564 1566:1674
run ../witness_g3_M2000_p201_1000.json p201_1000 1234:1342 1344:1452 1454:1562 1564:1672
date > ../v3/run_v3.finished
