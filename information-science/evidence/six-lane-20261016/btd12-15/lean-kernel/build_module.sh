#!/bin/sh
# Compile one module of this directory to $BTD_BUILD/*.olean with the read-only Lean environment (lean_env.sh).
# Usage: sh build_module.sh BTDKernel/Foo.lean
#   log:      $BTD_LOGS/Foo.build.log   (default ./logs)       time/RSS: $BTD_LOGS/Foo.build.time (/usr/bin/time -l)
# One Lean process, $BTD_THREADS elaboration threads (default 1).  Exit status is Lean's.  Never deletes anything;
# an existing log for the same module is refused (use a fresh BTD_LOGS directory per build round).
KDIR=$(CDPATH= cd -- "$(dirname -- "$0")" && pwd)
. "$KDIR/lean_env.sh"
set +e
cd "$KDIR"
SRC="$1"
BASE=$(basename "$SRC" .lean)
REL=${SRC%.lean}
LOGS=${BTD_LOGS:-$KDIR/logs}
THREADS=${BTD_THREADS:-1}
mkdir -p "$BTD_BUILD/$(dirname "$REL")" "$LOGS"
if [ -e "$LOGS/$BASE.build.log" ]; then echo "refusing: $LOGS/$BASE.build.log exists"; exit 2; fi
/usr/bin/time -l "$LEAN" -j "$THREADS" -R . -o "$BTD_BUILD/$REL.olean" -i "$BTD_BUILD/$REL.ilean" "$SRC" \
  > "$LOGS/$BASE.build.log" 2> "$LOGS/$BASE.build.time"
STATUS=$?
echo "module=$SRC exit=$STATUS sha256=$(shasum -a 256 "$SRC" | cut -d' ' -f1)" >> "$LOGS/$BASE.build.time"
grep -E " real |maximum resident set size" "$LOGS/$BASE.build.time"
echo "exit=$STATUS"
exit $STATUS
