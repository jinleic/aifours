#!/bin/sh
# Build one module with a wall-clock cap (seconds) and an RSS cap (KB) on its lean process.
# Usage: watch_build.sh <formal-dir> <module> <cap-seconds> <cap-rss-kb> <log> [interval-seconds]
F=$1; MOD=$2; CAP=$3; RSSCAP=$4; LOG=$5; IV=${6:-2}
export PATH=$F/env/toolchains/lean-4.24.0-darwin_aarch64/bin:$PATH LEAN_NUM_THREADS=2 MATHLIB_CACHE_DIR=$F/env/mathlib-cache
cd $F/lean
start=$(date +%s)
( /usr/bin/time -l lake build "$MOD" > "$LOG.build" 2>&1; echo "BUILD_EXIT $?" >> "$LOG.build" ) &
BP=$!
peak=0
while kill -0 $BP 2>/dev/null; do
  sleep $IV
  rss=0
  for pid in $(pgrep -f "lean.*$(echo $MOD | tr . /)"); do r=$(ps -o rss= -p $pid 2>/dev/null); rss=$((rss + ${r:-0})); done
  [ $rss -gt $peak ] && peak=$rss
  el=$(( $(date +%s) - start ))
  echo "t=$el rss_kb=$rss peak_kb=$peak" >> "$LOG"
  if [ $rss -gt $RSSCAP ] || [ $el -gt $CAP ]; then
    for pid in $(pgrep -f "lean.*$(echo $MOD | tr . /)"); do kill $pid; done
    echo "KILLED t=$el rss_kb=$rss" >> "$LOG"
  fi
done
echo "DONE t=$(( $(date +%s) - start )) peak_kb=$peak" >> "$LOG"
