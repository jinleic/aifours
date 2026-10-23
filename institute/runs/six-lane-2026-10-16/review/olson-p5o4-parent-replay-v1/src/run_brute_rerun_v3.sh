#!/bin/bash
# Rerun, under new labels (-v2r2), of the brute strata H = 2 (2 shards) and H = 3 (1 shard) with bin/replay_v2.
# Reason: the v2 launcher (run_brute_shards_v2.sh, xargs) received an external SIGTERM at 09:25:51 PDT; the shard
# brute-H2-s1of2-v2 was stopped by it and brute-H2-s0of2-v2 was stopped by this desk's SIGTERM at 09:28:03 (exit=143);
# both are UNKNOWN and kept; brute-H3 had not started.  This launcher is started in its own session (setsid), runs at
# most 2 shards at once, each a separate process under ulimit -t 1800, and creates out/brute-rerun-v3.done at the end.
set -u
cd "$(dirname "$0")/.." || exit 1
export TMPDIR="$PWD/tmp"
job() {
  set -o noclobber
  H=$1 S=$2 N=$3
  name=brute-H$H-s${S}of$N-v2r2
  { date; echo "cmd: ./bin/replay_v2 brute out/$name $H $S $N"; } > "out/$name.log" || exit 1
  ( ulimit -t 1800; /usr/bin/time -l ./bin/replay_v2 brute "out/$name" "$H" "$S" "$N" ) >> "out/$name.log" 2>&1
  echo "exit=$?" >> "out/$name.log"
  date >> "out/$name.log"
}
export -f job
{ echo "2 0 2"; echo "3 0 1"; echo "2 1 2"; } | xargs -P 2 -L 1 bash -c 'job "$@"' _
rc=$?
set -o noclobber
{ date; echo "xargs_rc=$rc"; } > out/brute-rerun-v3.done
