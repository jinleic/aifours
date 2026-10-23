#!/bin/sh
set -eu
repo=/Users/jinleic/repos/aifours
run="$repo/institute/runs/hard-2026-10-15"
session=aifours-hard-20261015
case "${1:-}" in
  "") restart=no ;;
  --restart) restart=yes ;;
  *) echo "usage: institute/launch_tmux.sh [--restart]" >&2; exit 2 ;;
esac
if tmux has-session -t "$session" 2>/dev/null; then
  echo "refused: tmux session $session already exists" >&2
  exit 2
fi
if [ -e "$run/run.json" ]; then
  if [ "$restart" != yes ]; then
    echo "refused: $run/run.json already exists; explicit --restart and preserved receipts are required" >&2
    exit 2
  fi
  preserved=no
  for snapshot in "$run"/batches/*/run.json; do
    if [ -f "$snapshot" ] && cmp -s "$run/run.json" "$snapshot"; then
      preserved=yes
      break
    fi
  done
  if [ "$preserved" != yes ]; then
    echo "refused: preserve the current run receipt before restarting" >&2
    exit 2
  fi
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
