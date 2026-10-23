#!/bin/bash
# Lane launcher v1: fresh per-launch disk gate, pre-execution receipt (script hashes BEFORE running),
# owned TMPDIR, native CPU cap (ulimit -t), /usr/bin/time -l for max RSS, post receipt with output hashes.
# Usage: code/run_v1.sh RUN_NAME CPU_SECONDS PROJECTED_GROWTH_BYTES SCRIPT [ARGS...]
# Never deletes or overwrites: run dir is created with plain mkdir, files with noclobber.
set -u
set -o noclobber
LANE=/Users/jinleic/repos/aifours/mathematics/evidence/six-lane-20261016/phase-type-complex3
export TMPDIR="$LANE/tmp/"
export PYTHONDONTWRITEBYTECODE=1
PY=/Users/jinleic/repos/aifours/information-science/evidence/six-lane-20261016/robust-spr/code/venv/bin/python
NAME="$1"; CPU="$2"; GROWTH="$3"; SCRIPT="$4"; shift 4
cd "$LANE" || exit 90
FREE_KB=$(df -k / | awk 'NR==2 {print $4}')
FREE_B=$((FREE_KB * 1024))
NEED_B=$((12200000000 + GROWTH))
if [ "$FREE_B" -lt "$NEED_B" ]; then
  echo "GATE FAIL: free=$FREE_B < need=$NEED_B; not launching $NAME"
  exit 91
fi
RUN="runs/$NAME"
mkdir "$RUN" || { echo "run dir exists: $RUN"; exit 92; }
START=$(date '+%Y-%m-%dT%H:%M:%S%z')
{
  echo "{"
  echo " \"run\": \"$NAME\","
  echo " \"stage\": \"pre-execution\","
  echo " \"written_at\": \"$START\","
  echo " \"gate\": {\"free_bytes\": $FREE_B, \"required_bytes\": $NEED_B, \"projected_growth_bytes\": $GROWTH},"
  echo " \"interpreter\": \"$PY\","
  echo " \"interpreter_version\": \"$("$PY" -B -c 'import sys,flint,sympy,mpmath; print(sys.version.split()[0], "flint", flint.__version__, "sympy", sympy.__version__, "mpmath", mpmath.__version__)')\","
  echo " \"cpu_cap_seconds\": $CPU,"
  echo " \"tmpdir\": \"$LANE/tmp/\","
  echo " \"argv\": \"$SCRIPT $*\","
  echo " \"code_sha256\": {"
  first=1
  for f in code/*.py code/*.sh; do
    [ -f "$f" ] || continue
    h=$(shasum -a 256 "$f" | cut -d' ' -f1)
    if [ $first -eq 1 ]; then first=0; else echo ","; fi
    printf '  "%s": "%s"' "$f" "$h"
  done
  echo ""
  echo " }"
  echo "}"
} > "receipts/$NAME-pre.json"
T0=$(python3 -c 'import time; print(time.time())')
(
  export TMPDIR="$LANE/tmp/"
  export PYTHONDONTWRITEBYTECODE=1
  ulimit -t "$CPU"
  /usr/bin/time -l "$PY" -B "$SCRIPT" "$RUN" "$@" > "$RUN/stdout.txt" 2> "$RUN/stderr_time.txt"
)
RC=$?
T1=$(python3 -c 'import time; print(time.time())')
END=$(date '+%Y-%m-%dT%H:%M:%S%z')
RSS=$(awk '/maximum resident set size/ {print $1}' "$RUN/stderr_time.txt")
{
  echo "{"
  echo " \"run\": \"$NAME\","
  echo " \"stage\": \"post-execution\","
  echo " \"started_at\": \"$START\","
  echo " \"ended_at\": \"$END\","
  echo " \"exit_code\": $RC,"
  echo " \"wall_seconds\": $(python3 -c "print(round($T1-$T0,3))"),"
  echo " \"max_rss_bytes\": ${RSS:-null},"
  echo " \"pre_receipt_sha256\": \"$(shasum -a 256 "receipts/$NAME-pre.json" | cut -d' ' -f1)\","
  echo " \"outputs_sha256\": {"
  first=1
  for f in "$RUN"/*; do
    [ -f "$f" ] || continue
    h=$(shasum -a 256 "$f" | cut -d' ' -f1)
    b=$(wc -c < "$f" | tr -d ' ')
    if [ $first -eq 1 ]; then first=0; else echo ","; fi
    printf '  "%s": {"sha256": "%s", "bytes": %s}' "$f" "$h" "$b"
  done
  echo ""
  echo " }"
  echo "}"
} > "receipts/$NAME-post.json"
echo "run $NAME exit=$RC rss=${RSS:-?} start=$START end=$END"
exit $RC
