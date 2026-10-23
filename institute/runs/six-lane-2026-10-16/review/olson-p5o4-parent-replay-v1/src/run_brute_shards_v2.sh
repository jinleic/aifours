#!/bin/bash
# Full no-filter brute force of layers H = 0..3 with bin/replay_v2 (H = 4..7 were run as single shards).
# Each shard is a separate process under ulimit -t 1800; at most 2 shards run at once (xargs -P 2).
# Logs and outputs are created exclusively (noclobber, mkdir without -p inside the program).
set -u
cd "$(dirname "$0")/.." || exit 1
export TMPDIR="$PWD/tmp"
job() {
  set -o noclobber
  H=$1 S=$2 N=$3
  name=brute-H$H-s${S}of$N-v2
  { date; echo "cmd: ./bin/replay_v2 brute out/$name $H $S $N"; } > "out/$name.log" || exit 1
  ( ulimit -t 1800; /usr/bin/time -l ./bin/replay_v2 brute "out/$name" "$H" "$S" "$N" ) >> "out/$name.log" 2>&1
  echo "exit=$?" >> "out/$name.log"
  date >> "out/$name.log"
}
export -f job
{
  for s in 0 1 2 3 4 5; do echo "0 $s 6"; done
  for s in 0 1 2 3; do echo "1 $s 4"; done
  for s in 0 1; do echo "2 $s 2"; done
  echo "3 0 1"
} | xargs -P 2 -L 1 bash -c 'job "$@"' _
date
