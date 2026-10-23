#!/bin/sh
# Compile one module of this directory to $CDF_BUILD/*.olean with the read-only Lean environment.
# Usage: sh build_module.sh CdfKernel/Foo.lean
#   log:       $CDF_LOGS/Foo.build.log   (default ./logs)
#   time/RSS:  $CDF_LOGS/Foo.build.time  (/usr/bin/time -l)
# One Lean process, $CDF_THREADS elaboration threads (default 1).  Exit status is Lean's.
KDIR=$(CDPATH= cd -- "$(dirname -- "$0")" && pwd)
. "$KDIR/lean_env.sh"
set +e
cd "$KDIR"
SRC="$1"
BASE=$(basename "$SRC" .lean)
REL=${SRC%.lean}
LOGS=${CDF_LOGS:-$KDIR/logs}
THREADS=${CDF_THREADS:-1}
mkdir -p "$CDF_BUILD/$(dirname "$REL")" "$LOGS"
/usr/bin/time -l "$LEAN" -j "$THREADS" -R . -o "$CDF_BUILD/$REL.olean" -i "$CDF_BUILD/$REL.ilean" "$SRC" \
  > "$LOGS/$BASE.build.log" 2> "$LOGS/$BASE.build.time"
STATUS=$?
echo "module=$SRC exit=$STATUS sha256=$(shasum -a 256 "$SRC" | cut -d' ' -f1)" >> "$LOGS/$BASE.build.time"
grep -E " real |maximum resident set size" "$LOGS/$BASE.build.time"
echo "exit=$STATUS"
exit $STATUS
