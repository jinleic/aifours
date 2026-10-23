#!/bin/bash
# run.sh NAME CPU_CAP_SECONDS CMD [ARGS...]  (moqls7-ls147-parent-v1)
# Runs CMD from the run directory with TMPDIR=<dir>/tmp, a native CPU cap (ulimit -t) and /usr/bin/time -l.
# Writes runs/NAME.out, runs/NAME.err, runs/NAME.time.txt, runs/NAME.meta.json; refuses to overwrite (noclobber +
# pre-check; meta via open(...,'x')). A CPU-cap stop (SIGXCPU) is recorded as its exit status and means UNKNOWN.
set -u
set -o noclobber
D="$(cd "$(dirname "$0")/.." && pwd)"
NAME="$1"; CAP="$2"; shift 2
cd "$D" || exit 90
for ext in out err time.txt meta.json; do
  if [ -e "runs/$NAME.$ext" ]; then echo "refuse: runs/$NAME.$ext exists" >&2; exit 91; fi
done
export TMPDIR="$D/tmp"
START=$(date '+%Y-%m-%dT%H:%M:%S%z')
( ulimit -t "$CAP"; exec /usr/bin/time -l -o "runs/$NAME.time.txt" "$@" ) > "runs/$NAME.out" 2> "runs/$NAME.err"
RC=$?
END=$(date '+%Y-%m-%dT%H:%M:%S%z')
/usr/bin/python3 -B - "$NAME" "$RC" "$START" "$END" "$CAP" "$@" <<'PY'
import json, sys
name, rc, start, end, cap = sys.argv[1:6]
with open("runs/%s.meta.json" % name, "x") as f:
    json.dump({"name": name, "argv": sys.argv[6:], "cwd": "<run dir>", "TMPDIR": "<run dir>/tmp",
               "cpu_cap_s": int(cap), "exit": int(rc), "start": start, "end": end}, f, indent=1)
    f.write("\n")
PY
echo "$NAME exit=$RC start=$START end=$END"
