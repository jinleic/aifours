#!/bin/bash
# ME3 parent desk (ME3ParentPrimal) launcher v1.
# Usage: code/launch_v1.sh RUN_NAME PROJECTED_GROWTH_BYTES SCRIPT [ARGS...]   (SCRIPT relative to the desk)
# Fresh disk gate (free >= 12.2e9 + projected growth) before launch; exclusive run dir and receipts (noclobber);
# desk-owned TMPDIR; pre-execution receipt pins every desk code/snapshot/receipt file BEFORE the run; one python
# process under /usr/bin/time -l (not setuid); post receipt with exit code, wall time, max RSS and output hashes.
# No signals are ever sent by this launcher; the python process carries its own disk/RSS/clock guards.
set -u
set -o noclobber
DESK=/Users/jinleic/repos/aifours/institute/runs/six-lane-2026-10-16/review/me3-parent-primal-reductions-v1
PY=/Users/jinleic/repos/aifours/information-science/evidence/six-lane-20261016/robust-spr/code/venv/bin/python
NAME="$1"; GROWTH="$2"; SCRIPT="$3"; shift 3
cd "$DESK" || exit 90
FREE_KB=$(df -k / | awk 'NR==2 {print $4}')
FREE_B=$((FREE_KB * 1024))
NEED_B=$((12200000000 + GROWTH))
if [ "$FREE_B" -lt "$NEED_B" ]; then
  echo "GATE FAIL: free=$FREE_B < need=$NEED_B; not launching $NAME"
  exit 91
fi
RUN="runs/$NAME"
mkdir "$RUN" || { echo "run dir exists: $RUN"; exit 92; }
mkdir "tmp/$NAME" || { echo "tmp dir exists: tmp/$NAME"; exit 92; }
export TMPDIR="$DESK/tmp/$NAME/"
export PYTHONDONTWRITEBYTECODE=1
export MPLCONFIGDIR="$DESK/tmp/$NAME/"
START=$(date '+%Y-%m-%dT%H:%M:%S%z')
{
  echo "{"
  echo " \"run\": \"$NAME\","
  echo " \"stage\": \"pre-execution\","
  echo " \"written_at_host_clock\": \"$START\","
  echo " \"gate\": {\"free_bytes\": $FREE_B, \"required_bytes\": $NEED_B, \"projected_growth_bytes\": $GROWTH},"
  echo " \"interpreter\": \"$PY\","
  echo " \"interpreter_version\": \"$("$PY" -B -c 'import sys,flint,sympy,mpmath; print(sys.version.split()[0], "flint", flint.__version__, "sympy", sympy.__version__, "mpmath", mpmath.__version__)')\","
  echo " \"tmpdir\": \"$TMPDIR\","
  echo " \"argv\": \"$SCRIPT $*\","
  echo " \"desk_file_sha256\": {"
  first=1
  for f in code/* snapshot/* receipts/input-pins-*.txt; do
    [ -f "$f" ] || continue
    h=$(shasum -a 256 "$f" | cut -d' ' -f1)
    if [ $first -eq 1 ]; then first=0; else echo ","; fi
    printf '  "%s": "%s"' "$f" "$h"
  done
  echo ""
  echo " }"
  echo "}"
} > "receipts/$NAME-pre.json"
T0=$(date +%s)
/usr/bin/time -l "$PY" -B "$SCRIPT" "$RUN" "$@" > "$RUN/stdout.txt" 2> "$RUN/stderr_time.txt"
RC=$?
T1=$(date +%s)
END=$(date '+%Y-%m-%dT%H:%M:%S%z')
RSS=$(awk '/maximum resident set size/ {print $1}' "$RUN/stderr_time.txt")
FREE_END=$(( $(df -k / | awk 'NR==2 {print $4}') * 1024 ))
{
  echo "{"
  echo " \"run\": \"$NAME\","
  echo " \"stage\": \"post-execution\","
  echo " \"started_at_host_clock\": \"$START\","
  echo " \"ended_at_host_clock\": \"$END\","
  echo " \"exit_code\": $RC,"
  echo " \"wall_seconds\": $((T1 - T0)),"
  echo " \"max_rss_bytes\": ${RSS:-null},"
  echo " \"free_bytes_end\": $FREE_END,"
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
