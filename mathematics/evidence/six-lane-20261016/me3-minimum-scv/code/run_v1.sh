#!/bin/bash
# ME3 lane launcher v1: fresh per-launch disk gate, pre-execution receipt (code hashes BEFORE running),
# owned TMPDIR, native CPU cap (ulimit -t), /usr/bin/time -l for max RSS, post receipt with output hashes.
# Usage: code/run_v1.sh SUBTREE RUN_NAME CPU_SECONDS PROJECTED_GROWTH_BYTES SCRIPT [ARGS...]
#   SUBTREE = "." (lane owner) or an owned subdirectory such as "reductions" (it needs runs/ and receipts/ inside).
# Never deletes or overwrites: the run dir is created with plain mkdir, receipts with noclobber.
set -u
set -o noclobber
LANE=/Users/jinleic/repos/aifours/mathematics/evidence/six-lane-20261016/me3-minimum-scv
export TMPDIR="$LANE/tmp/"
export PYTHONDONTWRITEBYTECODE=1
PY=/Users/jinleic/repos/aifours/information-science/evidence/six-lane-20261016/robust-spr/code/venv/bin/python
SUB="$1"; NAME="$2"; CPU="$3"; GROWTH="$4"; SCRIPT="$5"; shift 5
cd "$LANE" || exit 90
[ -d "$SUB/runs" ] && [ -d "$SUB/receipts" ] || { echo "subtree $SUB lacks runs/ or receipts/"; exit 93; }
FREE_KB=$(df -k / | awk 'NR==2 {print $4}')
FREE_B=$((FREE_KB * 1024))
NEED_B=$((12200000000 + GROWTH))
if [ "$FREE_B" -lt "$NEED_B" ]; then
  echo "GATE FAIL: free=$FREE_B < need=$NEED_B; not launching $NAME"
  exit 91
fi
RUN="$SUB/runs/$NAME"
REC="$SUB/receipts"
mkdir "$RUN" || { echo "run dir exists: $RUN"; exit 92; }
START=$(date '+%Y-%m-%dT%H:%M:%S%z')
{
  echo "{"
  echo " \"run\": \"$NAME\","
  echo " \"subtree\": \"$SUB\","
  echo " \"stage\": \"pre-execution\","
  echo " \"written_at_host_clock\": \"$START\","
  echo " \"gate\": {\"free_bytes\": $FREE_B, \"required_bytes\": $NEED_B, \"projected_growth_bytes\": $GROWTH},"
  echo " \"interpreter\": \"$PY\","
  echo " \"interpreter_version\": \"$("$PY" -B -c 'import sys,flint,sympy,mpmath; print(sys.version.split()[0], "flint", flint.__version__, "sympy", sympy.__version__, "mpmath", mpmath.__version__)')\","
  echo " \"cpu_cap_seconds\": $CPU,"
  echo " \"tmpdir\": \"$TMPDIR\","
  echo " \"argv\": \"$SCRIPT $*\","
  echo " \"code_sha256\": {"
  first=1
  for f in code/*.py code/*.sh "$SUB"/code/*.py; do
    [ -f "$f" ] || continue
    h=$(shasum -a 256 "$f" | cut -d' ' -f1)
    if [ $first -eq 1 ]; then first=0; else echo ","; fi
    printf '  "%s": "%s"' "$f" "$h"
  done
  echo ""
  echo " }"
  echo "}"
} > "$REC/$NAME-pre.json"
T0=$(python3 -c 'import time; print(time.time())')
(
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
  echo " \"subtree\": \"$SUB\","
  echo " \"stage\": \"post-execution\","
  echo " \"started_at_host_clock\": \"$START\","
  echo " \"ended_at_host_clock\": \"$END\","
  echo " \"exit_code\": $RC,"
  echo " \"wall_seconds\": $(python3 -c "print(round($T1-$T0,3))"),"
  echo " \"max_rss_bytes\": ${RSS:-null},"
  echo " \"pre_receipt_sha256\": \"$(shasum -a 256 "$REC/$NAME-pre.json" | cut -d' ' -f1)\","
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
} > "$REC/$NAME-post.json"
echo "run $NAME exit=$RC rss=${RSS:-?} start=$START end=$END"
exit $RC
