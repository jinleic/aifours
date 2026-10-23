#!/bin/bash
# run_chunk4.sh T E MAX_SECONDS [extra engine args...]: one guarded engine-v4 chunk. Lane ame46-support.
# Starts code/large_t_joint4.py for (T, E) with the given extra arguments, attaches code/disk_floor_watch.sh (floor
# 12,000,000,000 B) and enforces a wall-clock limit of MAX_SECONDS. At the limit the engine and its children get
# SIGTERM, with a bounded wait of 30 s and never SIGKILL. A killed engine writes no report, so the case is UNKNOWN.
# Chunk log: evidence/chunks.log.
T="$1"; E="$2"; MAX="$3"; shift 3
HERE="$(cd "$(dirname "$0")" && pwd)"; LANE="$(dirname "$HERE")"
LOG="$LANE/evidence/chunks.log"
OUTTXT="$LANE/explore/large_t_joint4/run_t${T}_e${E}$( [[ " $* " == *" --proof "* ]] || echo _explore ).stdout.txt"
mkdir -p "$LANE/explore/large_t_joint4"
cd "$HERE" || exit 2
echo "$(date '+%H:%M:%S') start t=$T e=$E max=${MAX}s args: $*" >> "$LOG"
OMP_NUM_THREADS=1 ../../depolarizing/env/bin/python -B large_t_joint4.py --t "$T" --e "$E" "$@" > "$OUTTXT" 2>&1 &
PID=$!
"$HERE/disk_floor_watch.sh" "$PID" 12000000000 "$LOG" &
WPID=$!
SECS=0
while kill -0 "$PID" 2>/dev/null; do
  if [ "$SECS" -ge "$MAX" ]; then
    echo "$(date '+%H:%M:%S') wall limit ${MAX}s reached: SIGTERM to children of $PID and to $PID (UNKNOWN)" >> "$LOG"
    for c in $(pgrep -P "$PID"); do kill -TERM "$c" 2>/dev/null; done
    kill -TERM "$PID" 2>/dev/null
    for i in $(seq 1 30); do kill -0 "$PID" 2>/dev/null || break; sleep 1; done
    break
  fi
  sleep 5; SECS=$((SECS + 5))
done
wait "$PID" 2>/dev/null; RC=$?
wait "$WPID" 2>/dev/null
echo "$(date '+%H:%M:%S') end t=$T e=$E rc=$RC $(tail -1 "$OUTTXT")" >> "$LOG"
echo "t=$T e=$E rc=$RC $(tail -1 "$OUTTXT")"
