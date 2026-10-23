#!/bin/sh
# Run `lake env lean <file>` with a wall-clock cap (s) and an RSS cap (KB), sampling every 1 s.
# Usage: watch_lean.sh <formal-dir> <file.lean> <cap-seconds> <cap-rss-kb>
# Prints one line: FILE exit=<code> seconds=<t> peak_kb=<kb> killed=<yes|no> first_error=<...>
F=$1; FILE=$2; CAP=$3; RSSCAP=$4
export PATH=$F/env/toolchains/lean-4.24.0-darwin_aarch64/bin:$PATH LEAN_NUM_THREADS=2
cd $F/lean
OUT=$(mktemp)
start=$(date +%s)
lake env lean "$FILE" > "$OUT" 2>&1 &
BP=$!
peak=0; killed=no
while kill -0 $BP 2>/dev/null; do
  sleep 1
  rss=0
  for pid in $(pgrep -f "lean $FILE"); do r=$(ps -o rss= -p $pid 2>/dev/null); rss=$((rss + ${r:-0})); done
  [ $rss -gt $peak ] && peak=$rss
  el=$(( $(date +%s) - start ))
  if [ $rss -gt $RSSCAP ] || [ $el -gt $CAP ]; then
    for pid in $(pgrep -f "lean $FILE"); do kill $pid; done; killed=yes
  fi
done
wait $BP; rc=$?
err=$(grep -m1 'error' "$OUT" | cut -c1-160)
echo "$(basename $FILE) exit=$rc seconds=$(( $(date +%s) - start )) peak_kb=$peak killed=$killed first_error=$err"
rm -f "$OUT"
