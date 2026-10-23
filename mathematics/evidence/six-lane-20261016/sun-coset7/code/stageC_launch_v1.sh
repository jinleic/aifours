#!/bin/bash
# stageC_launch_v1.sh -- Stage C launcher (lane sun-coset7). EXPLORATORY under the parent conditional GO.
# Both admissions are checked back-to-back before any launch; if either FAILs, nothing is launched and
# nothing is retried. Engines run directly (no wrapper) so the RSS watcher sees their own PIDs.
# The watcher samples each engine's RSS every 10 s and sends SIGTERM (cooperative; never SIGKILL) if it
# reaches 1 GiB. The engines self-enforce their time budget and the 12.0e9 in-flight disk floor.
set -o noclobber
LANE=/Users/jinleic/repos/aifours/mathematics/evidence/six-lane-20261016/sun-coset7
cd "$LANE" || exit 2
export TMPDIR="$LANE/tmp"
PY=/opt/homebrew/bin/python3
MON=/Users/jinleic/repos/aifours/institute/runs/six-lane-2026-10-16/review/disk-monitor-v1-20261018T0722-to-1810.jsonl
GROWTH=33554432          # 2 runs x 16 MiB output cap
BUDGET=3600              # self-budget per run (s)
RSSCAP_KB=1048576        # 1 GiB
LOG=evidence/stageC-watch.log
echo "start $(date '+%Y-%m-%dT%H:%M:%S%z')" > "$LOG"
$PY code/admission_v1.py "$MON" evidence/stageC-admission-K62.json $GROWTH; A1=$?
$PY code/admission_v1.py "$MON" evidence/stageC-admission-K63.json $GROWTH; A2=$?
echo "admission K62=$A1 K63=$A2 at $(date '+%H:%M:%S')" >> "$LOG"
if [ $A1 -ne 0 ] || [ $A2 -ne 0 ]; then
  echo "REFUSED: admission failed (K62 exit $A1, K63 exit $A2); no launch, no retry" | tee -a "$LOG"
  exit 0
fi
$PY code/core7_engine_v2.py K62 evidence/stageC-K62 $BUDGET > evidence/stageC-K62.stdout 2>&1 &
P1=$!
$PY code/core7_engine_v2.py K63 evidence/stageC-K63 $BUDGET > evidence/stageC-K63.stdout 2>&1 &
P2=$!
echo "launched K62 pid=$P1 K63 pid=$P2 at $(date '+%H:%M:%S')" >> "$LOG"
while kill -0 $P1 2>/dev/null || kill -0 $P2 2>/dev/null; do
  for P in $P1 $P2; do
    if kill -0 $P 2>/dev/null; then
      R=$(ps -o rss= -p $P | tr -d ' ')
      if [ -n "$R" ]; then
        echo "$(date '+%H:%M:%S') pid=$P rss_kb=$R" >> "$LOG"
        if [ "$R" -ge $RSSCAP_KB ]; then
          echo "$(date '+%H:%M:%S') RSS cap reached: SIGTERM pid=$P" >> "$LOG"
          kill -TERM $P
        fi
      fi
    fi
  done
  sleep 10
done
wait $P1; E1=$?
wait $P2; E2=$?
echo "exit K62=$E1 K63=$E2 at $(date '+%H:%M:%S')" >> "$LOG"
cat evidence/stageC-K62.stdout evidence/stageC-K63.stdout
