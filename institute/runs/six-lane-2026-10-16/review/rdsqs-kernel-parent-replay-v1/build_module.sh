#!/bin/sh
# Compile one module of this directory to $RDSQS_BUILD/*.olean with the read-only Lean environment.
# Same procedure as review/point-cyclic88-kernel-worker-v1/build_module.sh (used read-only, not
# modified), with the variables renamed to RDSQS_*.
# Usage: sh build_module.sh RdsqsKernel/Foo.lean
#   log:       $RDSQS_LOGS/Foo.build.log   (default ./logs)
#   time/RSS:  $RDSQS_LOGS/Foo.build.time  (/usr/bin/time -l)
# One Lean process, $RDSQS_THREADS elaboration threads (default 1).  Exit status is Lean's.
KDIR=$(CDPATH= cd -- "$(dirname -- "$0")" && pwd)
. "$KDIR/lean_env.sh"
set +e
cd "$KDIR"
SRC="$1"
BASE=$(basename "$SRC" .lean)
REL=${SRC%.lean}
LOGS=${RDSQS_LOGS:-$KDIR/logs}
THREADS=${RDSQS_THREADS:-1}
mkdir -p "$RDSQS_BUILD/$(dirname "$REL")" "$LOGS"
/usr/bin/time -l "$LEAN" -j "$THREADS" -R . -o "$RDSQS_BUILD/$REL.olean" -i "$RDSQS_BUILD/$REL.ilean" "$SRC" \
  > "$LOGS/$BASE.build.log" 2> "$LOGS/$BASE.build.time"
STATUS=$?
echo "module=$SRC exit=$STATUS sha256=$(shasum -a 256 "$SRC" | cut -d' ' -f1)" >> "$LOGS/$BASE.build.time"
grep -E " real |maximum resident set size" "$LOGS/$BASE.build.time"
echo "exit=$STATUS"
exit $STATUS
