#!/bin/sh
# Replay every declaration of every KSatUpper module through the Lean kernel (lean4checker,
# starting from each module's imports). Usage: run_lean4checker.sh <formal-dir> [--fresh MODULE]
set -u
F=$1; shift
export PATH=$F/env/toolchains/lean-4.24.0-darwin_aarch64/bin:$PATH
export LEAN_NUM_THREADS=${LEAN_NUM_THREADS:-4}
CHK=$F/env/lean4checker/.lake/build/bin/lean4checker
cd $F/lean
if [ "${1:-}" = "--fresh" ]; then
  /usr/bin/time -p lake env $CHK --fresh "$2"; echo "EXIT $? fresh $2"; exit 0
fi
fails=0
for mod in $(find KSatUpper -name '*.lean' | sed 's#/#.#g; s#\.lean$##' | sort) KSatUpper; do
  out=$(lake env $CHK "$mod" 2>&1); rc=$?
  echo "MODULE $mod EXIT $rc $(echo "$out" | tail -1)"
  [ $rc -ne 0 ] && fails=$((fails+1))
done
echo "LEAN4CHECKER_FAILURES $fails"
