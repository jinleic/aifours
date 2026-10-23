#!/bin/bash
# disk_floor_watch.sh PID [FLOOR_BYTES] [LOG]: run-wide free-space floor for a running engine job. Lane ame46-support.
# Every 5 s it reads the free bytes of the lane's filesystem (df -k). If they drop below FLOOR_BYTES (default
# 12,000,000,000), it sends SIGTERM to the children of PID and then to PID, with a bounded wait of 30 s, and never
# SIGKILL. The job outcome is then UNKNOWN. The watchdog exits when PID exits.
PID="$1"; FLOOR="${2:-12000000000}"; LOG="${3:-/dev/stdout}"
LANE="$(cd "$(dirname "$0")/.." && pwd)"
while kill -0 "$PID" 2>/dev/null; do
  FREE=$(( $(df -k "$LANE" | awk 'NR==2 {print $4}') * 1024 ))
  if [ "$FREE" -lt "$FLOOR" ]; then
    echo "$(date '+%H:%M:%S') free $FREE B < floor $FLOOR B: SIGTERM to children of $PID and to $PID" >> "$LOG"
    for c in $(pgrep -P "$PID"); do kill -TERM "$c" 2>/dev/null; done
    kill -TERM "$PID" 2>/dev/null
    for i in $(seq 1 30); do kill -0 "$PID" 2>/dev/null || break; sleep 1; done
    echo "$(date '+%H:%M:%S') stopped (outcome UNKNOWN)" >> "$LOG"
    exit 3
  fi
  sleep 5
done
echo "$(date '+%H:%M:%S') job $PID ended; last free $FREE B (floor $FLOOR B never crossed)" >> "$LOG"
exit 0
