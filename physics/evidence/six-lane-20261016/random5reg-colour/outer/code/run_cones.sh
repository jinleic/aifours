#!/bin/bash
# Sequential driver: produce (resumable chunks of <= 25 min) and check the listed cones.
# Usage (from the lane root): outer/code/run_cones.sh "01 02 10 11"
# One process at a time per driver; run at most two drivers concurrently.
cd "$(dirname "$0")/../.." || exit 1
PY=.venv/bin/python
EV=outer/evidence
mkdir -p "$EV/resources"
start=$(date +%s)
for c in $1; do
  fi=${c:0:1}; fj=${c:1:1}
  if [ $(( $(date +%s) - start )) -gt 1500 ]; then
    echo "$(date '+%F %T %Z') driver budget reached before cone $c"; exit 3
  fi
  k=1
  while [ ! -f "$EV/cone$c.json" ]; do
    while [ -f "$EV/resources/produce_cone${c}_chunk$k.time" ]; do k=$((k + 1)); done
    echo "$(date '+%F %T %Z') produce cone $c chunk $k"
    /usr/bin/time -l -o "$EV/resources/produce_cone${c}_chunk$k.time" \
      $PY outer/code/bnb_produce.py "$fi" "$fj" 1/10000 "$EV/cone$c.json" --workdir "$EV/cone$c.work" \
      --top-depth 5 --time-limit 1500 --save-every 240 --progress-every 30 --log "$EV/cone$c.log" > /dev/null 2>&1
    rc=$?
    echo "$(date '+%F %T %Z') produce cone $c chunk $k exit $rc"
    if [ $rc -ne 0 ] && [ $rc -ne 3 ]; then exit $rc; fi
    if [ $(( $(date +%s) - start )) -gt 3000 ] && [ ! -f "$EV/cone$c.json" ]; then
      echo "$(date '+%F %T %Z') driver stopping; cone $c resumable"; exit 3
    fi
  done
  if [ ! -f "$EV/cone$c.check.json" ]; then
    echo "$(date '+%F %T %Z') check cone $c"
    /usr/bin/time -l -o "$EV/resources/check_cone$c.time" \
      $PY outer/code/cert_cells.py "$EV/cone$c.json" "$EV/cone$c.check.json" --require-r0 1/10000 \
      > "$EV/cone$c.check.stdout" 2> "$EV/cone$c.check.stderr"
    echo "$(date '+%F %T %Z') check cone $c exit $?"
  fi
done
echo "$(date '+%F %T %Z') driver done: $1"
