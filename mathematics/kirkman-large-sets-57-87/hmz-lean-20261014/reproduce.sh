#!/bin/sh
# Frozen acceptance commands; neither exit0 in partial mode nor UNKNOWN solves the goal.
set -u
TASK_REPO=$(CDPATH= cd -- "$(dirname -- "$0")" && pwd)
cd "$TASK_REPO"
case "${1:-}" in
  lean)
    cd /Users/jinleic/jinleic-workspace/scratch/rh-quasi-lean-2026-10-07/lean
    exec /Users/jinleic/.elan/bin/lake env lean "$TASK_REPO/Formal.lean"
    ;;
  partial) exec python3 verify.py --partial ;;
  full) exec python3 verify.py ;;
  audit-joint)
    exec env PYTHONDONTWRITEBYTECODE=1 UV_CACHE_DIR=/tmp/lkts-uv-cache uv run --offline --with ortools==9.15.6755 python audit_joint.py
    ;;
  *)
    echo 'usage: sh reproduce.sh {lean|partial|full|audit-joint}' >&2
    echo 'Search is intentionally excluded; joint_search.py refuses to overwrite its saved attempt.' >&2
    exit 2
    ;;
esac
