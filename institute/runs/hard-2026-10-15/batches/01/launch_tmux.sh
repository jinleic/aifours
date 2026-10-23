#!/bin/sh
set -eu
repo=/Users/jinleic/repos/aifours
run="$repo/institute/runs/hard-2026-10-15"
session=aifours-hard-20261015
if tmux has-session -t "$session" 2>/dev/null; then
  echo "refused: tmux session $session already exists" >&2
  exit 2
fi
if [ -e "$run/run.json" ]; then
  echo "refused: $run/run.json already exists; inspect it before any new launch" >&2
  exit 2
fi
python3 -B "$repo/institute/run_parallel.py" "$run/selection.json" --check
tmux new-session -d -s "$session" -c "$repo" /bin/sh -c '
  caffeinate -i python3 -B institute/run_parallel.py institute/runs/hard-2026-10-15/selection.json > institute/runs/hard-2026-10-15/supervisor.log 2>&1
  result=$?
  printf "%s\n" "$result" > institute/runs/hard-2026-10-15/supervisor.exit
  python3 -B institute/check_run.py institute/runs/hard-2026-10-15 > institute/runs/hard-2026-10-15/parent-check.log 2>&1
  printf "%s\n" "$?" > institute/runs/hard-2026-10-15/parent-check.exit
  tmux wait-for -S aifours-hard-20261015-finished
'
echo "started tmux session $session"
