#!/bin/sh
# Compile one module of this directory to build/*.olean with the read-only Lean environment.
# Usage: sh build_module.sh LktsKernel/Foo.lean   (log: logs/Foo.build.log, time/RSS: logs/Foo.build.time)
# Exit status is Lean's exit status.
KDIR=$(CDPATH= cd -- "$(dirname -- "$0")" && pwd)
. "$KDIR/lean_env.sh"
set +e
cd "$KDIR"
SRC="$1"
BASE=$(basename "$SRC" .lean)
REL=${SRC%.lean}
mkdir -p "build/$(dirname "$REL")" logs
/usr/bin/time -l "$LEAN" -j 4 -R . -o "build/$REL.olean" -i "build/$REL.ilean" "$SRC" \
  > "logs/$BASE.build.log" 2> "logs/$BASE.build.time"
STATUS=$?
echo "module=$SRC exit=$STATUS sha256=$(shasum -a 256 "$SRC" | cut -d' ' -f1)" >> "logs/$BASE.build.time"
grep -E " real |maximum resident set size" "logs/$BASE.build.time"
echo "exit=$STATUS"
exit $STATUS
