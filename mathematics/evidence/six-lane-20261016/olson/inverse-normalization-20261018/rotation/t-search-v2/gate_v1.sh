#!/bin/bash
# t-search-v2/gate_v1.sh - admission + exactly one launch + in-flight watcher (parent conditional GO, 13:17 PDT).
# Never uses SIGKILL, ulimit, timeout or gtimeout.  Stops only the one owned PID, with SIGTERM and a bounded wait.
# Usage (from anywhere): t-search-v2/gate_v1.sh
set -u
set -o noclobber
cd "$(dirname "$0")" || exit 99
MON=/Users/jinleic/repos/aifours/institute/runs/six-lane-2026-10-16/review/disk-monitor-v1-20261018T0722-to-1810.jsonl
PROJ=1300000000                       # max(projection 5e7, 1.3e9): A4 then enforces free >= 13.5e9
FLOOR=12000000000                     # in-flight floor 12.0e9 B
RSS_MAX_KB=3145728                    # 3 GiB
STOP_EPOCH=$(date -j -f '%Y-%m-%d %H:%M:%S' "$(date '+%Y-%m-%d') 17:29:00" '+%s')
export TMPDIR="$PWD/tmp" PYTHONDONTWRITEBYTECODE=1
LOG=out/wrapper-run1.log
: > "$LOG" || { echo "wrapper log exists or cannot be created; refusing"; exit 98; }
log() { local m; m="$(date '+%Y-%m-%dT%H:%M:%S%z') $*"; echo "$m" >> "$LOG"; echo "$m"; }

log "WRAPPER START sha256(self)=$(shasum -a 256 "$0" | cut -c1-64) stop_epoch=$STOP_EPOCH"
python3 -B code/admission_v1.py "$MON" "$PROJ" > out/admission-run1.json
ADM=$?
log "ADMISSION exit=$ADM json=$(cat out/admission-run1.json)"
if [ "$ADM" -ne 0 ]; then
  log "ADMISSION FAIL: no launch"
  exit 97
fi

python3 -B code/t_search_v2.py out/run1.jsonl > out/run1.stdout.txt 2> out/run1.stderr.txt &
PID=$!
log "LAUNCH pid=$PID cmd='python3 -B code/t_search_v2.py out/run1.jsonl' TMPDIR=$TMPDIR"

REASON=""
while kill -0 "$PID" 2>/dev/null; do
  sleep 20
  kill -0 "$PID" 2>/dev/null || break
  FREE_KB=$(/bin/df -k . | tail -n 1 | tr -s ' ' | cut -d ' ' -f 4)
  FREE=$((FREE_KB * 1024))
  RSS_KB=$(/bin/ps -o rss= -p "$PID" | tr -d ' ')
  NOW=$(date '+%s')
  log "WATCH pid=$PID free=$FREE rss_kb=${RSS_KB:-NA}"
  if [ "$FREE" -lt "$FLOOR" ]; then REASON="free $FREE < 12.0e9"; fi
  if [ -n "$RSS_KB" ] && [ "$RSS_KB" -gt "$RSS_MAX_KB" ]; then REASON="rss_kb $RSS_KB > 3 GiB"; fi
  if [ "$NOW" -ge "$STOP_EPOCH" ]; then REASON="clock reached 17:29 PDT"; fi
  if [ -n "$REASON" ]; then
    log "STOP reason=[$REASON]: kill -TERM $PID"
    kill -TERM "$PID"
    i=0
    while kill -0 "$PID" 2>/dev/null && [ "$i" -lt 120 ]; do sleep 1; i=$((i + 1)); done
    if kill -0 "$PID" 2>/dev/null; then
      log "STILL ALIVE after 120 s bounded wait; no further signal; RESULT UNKNOWN ($REASON)"
      log "END exit=unknown (process alive)"
      exit 96
    fi
    log "exited ${i} s after SIGTERM; RESULT UNKNOWN ($REASON)"
    break
  fi
done
wait "$PID"
EC=$?
log "END exit=$EC"
exit 0
