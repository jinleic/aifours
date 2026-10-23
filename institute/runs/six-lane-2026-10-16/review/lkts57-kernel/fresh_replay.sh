#!/bin/sh
# leanchecker --fresh MODULE: replay every constant the module depends on (Init, the Mathlib
# closure, PriorFormal, Generic, data, certificate) into an empty environment.
# A watchdog stops the run if resident memory exceeds 7.5 GiB or wall time exceeds LIMIT seconds.
# Usage: sh fresh_replay.sh LktsKernel.Cert57 [LIMIT_SECONDS]   (summary: logs/replay-fresh.<module>.summary)
KDIR=$(CDPATH= cd -- "$(dirname -- "$0")" && pwd)
cd "$KDIR"
. ./lean_env.sh
set +e
MOD="$1"
LIMIT="${2:-3600}"
OUT="logs/replay-fresh.$MOD"
START=$(date +%s)
/usr/bin/time -l "$LEANCHECKER" --fresh -v "$MOD" > "$OUT.log" 2> "$OUT.time" &
TPID=$!
PEAK=0
REASON=finished
while kill -0 "$TPID" 2>/dev/null; do
  CPID=$(pgrep -P "$TPID" | head -1)
  if [ -n "$CPID" ]; then
    RSS=$(ps -o rss= -p "$CPID" 2>/dev/null | tr -d ' ')
    [ -n "$RSS" ] && [ "$RSS" -gt "$PEAK" ] && PEAK=$RSS
    if [ -n "$RSS" ] && [ "$RSS" -gt 7864320 ]; then REASON=killed-rss; kill "$CPID"; fi
  fi
  NOW=$(date +%s)
  if [ $((NOW - START)) -gt "$LIMIT" ]; then REASON=killed-time; [ -n "$CPID" ] && kill "$CPID"; fi
  sleep 5
done
wait "$TPID"
STATUS=$?
END=$(date +%s)
echo "module=$MOD exit=$STATUS reason=$REASON wall_s=$((END - START)) sampled_peak_rss_kib=$PEAK limit_s=$LIMIT" \
  | tee "$OUT.summary"
