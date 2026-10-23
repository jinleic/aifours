#!/bin/sh
# Compile one module of this directory to $BRD26_BUILD/*.olean with the read-only Lean environment.
# Same procedure as review/gcdcqs20-kernel-worker-v1/build_module.sh (read, not modified), with the
# variables renamed to BRD26_* and Lean's native memory limit `-M` (megabytes) added.
# Usage: sh build_module.sh Brd26/Foo.lean
#   log:       $BRD26_LOGS/Foo.build.log   (default ./logs)
#   time/RSS:  $BRD26_LOGS/Foo.build.time  (/usr/bin/time -l)
# One Lean process, one elaboration thread, memory limit $BRD26_MEM_MB (default 7168).
# Exit status is Lean's.
KDIR=$(CDPATH= cd -- "$(dirname -- "$0")" && pwd)
. "$KDIR/lean_env.sh"
set +e
cd "$KDIR"
SRC="$1"
BASE=$(basename "$SRC" .lean)
REL=${SRC%.lean}
LOGS=${BRD26_LOGS:-$KDIR/logs}
MEM=${BRD26_MEM_MB:-7168}
mkdir -p "$BRD26_BUILD/$(dirname "$REL")" "$LOGS"
/usr/bin/time -l "$LEAN" -j 1 -M "$MEM" -R . -o "$BRD26_BUILD/$REL.olean" -i "$BRD26_BUILD/$REL.ilean" "$SRC" \
  > "$LOGS/$BASE.build.log" 2> "$LOGS/$BASE.build.time"
STATUS=$?
echo "module=$SRC exit=$STATUS sha256=$(shasum -a 256 "$SRC" | cut -d' ' -f1)" >> "$LOGS/$BASE.build.time"
grep -E " real |maximum resident set size" "$LOGS/$BASE.build.time"
echo "exit=$STATUS"
exit $STATUS
