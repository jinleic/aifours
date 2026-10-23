#!/bin/bash
# ADDENDUM-v1 provenance (review m6): toolchain metadata, file times, code signature / LC_UUID of the frozen binaries,
# the v1 -> v2 source diff, and a reproducibility rebuild of replay_v1 / replay_v2 from the pinned sources with the
# recorded build commands.  The rebuilt binaries go to out/addendum-v1/rebuild/ with the SAME basenames as bin/ (the
# linker's ad-hoc signature identifier is the output basename).  Existing desk files are only read; out/addendum-v1/ is
# created exclusively (mkdir without -p), every output file with noclobber.  The frozen bin/ binaries are not touched
# and remain the only binaries used by any run.
set -u
cd "$(dirname "$0")/.." || exit 1
export TMPDIR="$PWD/tmp"
set -o noclobber
mkdir out/addendum-v1 || exit 1
mkdir out/addendum-v1/provenance out/addendum-v1/rebuild || exit 1
P=out/addendum-v1/provenance
{
  echo "== date"; date
  echo "== cwd"; pwd
  echo "== TMPDIR"; echo "$TMPDIR"
  echo "== type -a clang++"; type -a clang++
  echo "== xcrun --find clang++"; xcrun --find clang++
  echo "== xcode-select -p"; xcode-select -p
  echo "== clang++ --version"; clang++ --version
  echo "== xcrun --show-sdk-path"; xcrun --show-sdk-path
  echo "== xcrun --show-sdk-version"; xcrun --show-sdk-version
  echo "== ld -v"; ld -v 2>&1
  echo "== sw_vers"; sw_vers
  echo "== uname -a"; uname -a
  echo "== python"; /opt/homebrew/opt/python@3.14/bin/python3.14 --version
  echo "== /usr/bin/time"; ls -l /usr/bin/time
} > "$P/toolchain.txt" 2>&1
{
  for f in src/olson_p5o4_replay_v1.cpp src/olson_p5o4_replay_v2.cpp bin/replay_v1 bin/replay_v2; do
    stat -f "%N birth=%SB mtime=%Sm ctime=%Sc size=%z" -t "%Y-%m-%dT%H:%M:%S%z" "$f"
  done
  shasum -a 256 src/olson_p5o4_replay_v1.cpp src/olson_p5o4_replay_v2.cpp bin/replay_v1 bin/replay_v2
} > "$P/frozen_files.txt" 2>&1
for b in replay_v1 replay_v2; do
  { echo "== codesign -d -vvv bin/$b"; codesign -d -vvv "bin/$b" 2>&1
    echo "== dwarfdump --uuid bin/$b"; xcrun dwarfdump --uuid "bin/$b"; } > "$P/sig_$b.txt" 2>&1
done
diff -u src/olson_p5o4_replay_v1.cpp src/olson_p5o4_replay_v2.cpp > "$P/src_v1_to_v2.diff"
echo "diff_rc=$?" > "$P/src_v1_to_v2.diff.rc"
for v in 1 2; do
  b=replay_v$v
  s=src/olson_p5o4_replay_v$v.cpp
  o=out/addendum-v1/rebuild/$b
  log=out/addendum-v1/rebuild/build-$b.log
  { date; echo "cmd: clang++ -O2 -std=c++17 -Wall -Wextra -o $o $s"; echo "cwd: $PWD"; echo "TMPDIR: $TMPDIR"
    echo "== compiler output (warnings/errors) begin"; } > "$log"
  clang++ -O2 -std=c++17 -Wall -Wextra -o "$o" "$s" >> "$log" 2>&1
  echo "exit=$?" >> "$log"
  { echo "== compiler output end"; date; shasum -a 256 "$s" "$o" "bin/$b"
    echo "== codesign -d -vvv $o"; codesign -d -vvv "$o" 2>&1
    echo "== dwarfdump --uuid $o"; xcrun dwarfdump --uuid "$o"; } >> "$log" 2>&1
done
date
