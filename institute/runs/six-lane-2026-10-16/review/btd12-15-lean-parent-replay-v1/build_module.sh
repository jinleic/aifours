#!/bin/sh
# Compile one module of this directory to $PBTD_BUILD/*.olean with the parent read-only Lean environment.
# Usage: sh build_module.sh BTDKernel/Foo.lean   (log: $PBTD_LOGS/Foo.build.log, time/RSS: Foo.build.time)
# One Lean process, one elaboration thread. Exit status is Lean's.
KDIR=$(CDPATH= cd -- "$(dirname -- "$0")" && pwd)
. "$KDIR/lean_env.sh"
set +e
cd "$KDIR"
SRC="$1"
BASE=$(basename "$SRC" .lean)
REL=${SRC%.lean}
LOGS=${PBTD_LOGS:-$KDIR/logs}
mkdir -p "$PBTD_BUILD/$(dirname "$REL")" "$LOGS"
/usr/bin/time -l "$LEAN" -j 1 -R . -o "$PBTD_BUILD/$REL.olean" -i "$PBTD_BUILD/$REL.ilean" "$SRC" \
  > "$LOGS/$BASE.build.log" 2> "$LOGS/$BASE.build.time"
STATUS=$?
echo "module=$SRC exit=$STATUS sha256=$(shasum -a 256 "$SRC" | cut -d' ' -f1)" >> "$LOGS/$BASE.build.time"
echo "exit=$STATUS"
exit $STATUS
