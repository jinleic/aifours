#!/bin/sh
# Compile one module of this directory to $PC100_BUILD/*.olean with the read-only Lean environment.
# Same procedure as review/rdsqs-kernel-worker-v1/build_module.sh (used read-only, not modified), with the
# variables renamed to PC100_*.
# Usage: sh build_module.sh PC100Kernel/Foo.lean
#   log:       $PC100_LOGS/Foo.build.log   (default ./logs)
#   time/RSS:  $PC100_LOGS/Foo.build.time  (/usr/bin/time -l)
# One Lean process, $PC100_THREADS elaboration threads (default 1).  Exit status is Lean's.
KDIR=$(CDPATH= cd -- "$(dirname -- "$0")" && pwd)
. "$KDIR/lean_env.sh"
set +e
cd "$KDIR"
SRC="$1"
BASE=$(basename "$SRC" .lean)
REL=${SRC%.lean}
LOGS=${PC100_LOGS:-$KDIR/logs}
THREADS=${PC100_THREADS:-1}
mkdir -p "$PC100_BUILD/$(dirname "$REL")" "$LOGS"
/usr/bin/time -l "$LEAN" -j "$THREADS" -R . -o "$PC100_BUILD/$REL.olean" -i "$PC100_BUILD/$REL.ilean" "$SRC" \
  > "$LOGS/$BASE.build.log" 2> "$LOGS/$BASE.build.time"
STATUS=$?
echo "module=$SRC exit=$STATUS sha256=$(shasum -a 256 "$SRC" | cut -d' ' -f1)" >> "$LOGS/$BASE.build.time"
grep -E " real |maximum resident set size" "$LOGS/$BASE.build.time"
echo "exit=$STATUS"
exit $STATUS
