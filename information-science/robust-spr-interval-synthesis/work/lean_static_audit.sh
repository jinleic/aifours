#!/usr/bin/env bash
# Static (no-build) audit of the public n=5 and n=6 Lean developments at pinned commits.
# Usage: bash work/lean_static_audit.sh > evidence/lean-static-audit.txt
# Clones into the scratch directory if absent; never builds (Lean 4.30.0 + Mathlib would need ~11 GB).
set -euo pipefail
S=/Users/jinleic/jinleic-workspace/scratch/ai4s-robust-spr-interval-synthesis
pin() { case "$1" in
  quintic-spr-proof) echo 866e2b53774e8f614b6b01a393301da47ac887b2 ;;
  sextic-spr-proof) echo 2b94aa79e472288d6044eae4382ac4abad535bb9 ;;
esac; }
for r in quintic-spr-proof sextic-spr-proof; do
  [ -d "$S/$r" ] || git clone -q "https://github.com/dgjszy/$r.git" "$S/$r"
  head=$(git -C "$S/$r" rev-parse HEAD)
  p=$(pin "$r")
  echo "=== $r HEAD=$head (pinned $p) $( [ "$head" = "$p" ] && echo MATCH || echo MISMATCH)"
  echo "toolchain: $(cat "$S/$r/lean-toolchain"); mathlib rev: $(jq -r '.packages[]|select(.name=="mathlib")|.rev' "$S/$r/lake-manifest.json")"
  echo "lean files: $(find "$S/$r/Lean" -name '*.lean' | wc -l | tr -d ' ')"
  for pat in '\bsorry\b' '\badmit\b' '^\s*(private\s+|protected\s+)?axiom\b' 'native_decide' '\bunsafe\b' \
             'implemented_by' '@\[extern' '^\s*opaque\b' 'ofReduceBool' 'debug\.skipKernelTC' \
             '^\s*(local\s+|scoped\s+)?(notation|infix|macro|syntax|elab)\b' 'attribute \[-'; do
    c=$( { grep -rEn --include='*.lean' "$pat" "$S/$r/Lean" || true; } | wc -l | tr -d ' ')
    echo "  count[$pat] = $c"
  done
  echo "  definitions of RobustSPRStatement:"
  grep -rEn --include='*.lean' 'def RobustSPRStatement' "$S/$r/Lean" | sed "s|$S/||"
  echo "  public theorem line:"
  grep -En 'theorem robustSPR\b' "$S/$r/Lean/Main.lean" | sed "s|$S/||"
  echo "  axiom audit allow-list (Audit.lean):"
  grep -En 'allowed|throwError|checked <' "$S/$r/Lean/Audit.lean" | sed 's/^/    /'
done
echo "=== GitHub CI evidence (gh api)"
for r in quintic-spr-proof sextic-spr-proof; do
  echo "$r workflow runs: $(gh api repos/dgjszy/$r/actions/runs -q .total_count 2>&1)  check-runs on main: $(gh api repos/dgjszy/$r/commits/main/check-runs -q .total_count 2>&1)"
done
