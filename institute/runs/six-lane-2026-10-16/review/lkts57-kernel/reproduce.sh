#!/bin/sh
# Reproduce the kernel certificates from the pinned raw files (sequential, <= 4 Lean threads).
# Usage: sh reproduce.sh {gen|57|87|controls|replay57|replay87|all}
#   gen       regenerate every generated Lean module from the raw files (SHA-256 checked)
#   57 / 87   compile PriorFormal, Generic, Data<v>, Cert<v> (logs/ get time + peak RSS)
#   controls  compile the two altered-certificate controls (Cert57Swap/Cert57Dup must FAIL,
#             Diag57Swap/Diag57Dup must succeed); writes logs/controls.summary
#   replay57 / replay87  leanchecker (toolchain lean4checker) replay of the compiled modules
set -u
KDIR=$(CDPATH= cd -- "$(dirname -- "$0")" && pwd)
cd "$KDIR"
REVIEW=$(CDPATH= cd -- "$KDIR/.." && pwd)
RAW57="$REVIEW/lkts57-construction-snapshot-v1/lkts57_g513.txt"
RAW87="$REVIEW/lkts87-parent-inputs-v1/lkts87_g903.txt"
SHA57=09a9d8ca0602ed28541e170ada7f096871311c29fd4515b6fea3e25f72b05f09
SHA87=65ab29ae6d24545c4ed41c3a4ea027becdf497b6810384b728379cfd0cae273e
SHAPRIOR=a39613c93506390e52b75b4fb355d6a0d69160ea2f8a3bfe5e0ebd30ff3f2dee
export PYTHONDONTWRITEBYTECODE=1

check_prior() {
  got=$(shasum -a 256 LktsKernel/PriorFormal.lean | cut -d' ' -f1)
  [ "$got" = "$SHAPRIOR" ] || { echo "PriorFormal.lean hash mismatch: $got" >&2; exit 2; }
}

gen() {
  check_prior
  python3 gen_data.py "$RAW57" LktsKernel/Data57.lean --v 57 --name data57 --expect-sha256 $SHA57 \
    --label "review/lkts57-construction-snapshot-v1/lkts57_g513.txt" || exit 2
  python3 gen_cert.py "$RAW57" LktsKernel/Cert57.lean --v 57 --name data57 --module LktsKernel.Data57 \
    --expect-sha256 $SHA57 --group 11 --theorem-prefix lkts57 \
    --label "review/lkts57-construction-snapshot-v1/lkts57_g513.txt" || exit 2
  python3 gen_data.py "$RAW87" LktsKernel/Data87.lean --v 87 --name data87 --expect-sha256 $SHA87 \
    --label "review/lkts87-parent-inputs-v1/lkts87_g903.txt" || exit 2
  python3 gen_cert.py "$RAW87" LktsKernel/Cert87.lean --v 87 --name data87 --module LktsKernel.Data87 \
    --expect-sha256 $SHA87 --group 8 --theorem-prefix lkts87 \
    --label "review/lkts87-parent-inputs-v1/lkts87_g903.txt" || exit 2
  python3 make_controls.py "$RAW57" controls || exit 2
  python3 gen_data.py controls/lkts57_control_swap.txt LktsKernel/Control/Data57Swap.lean --v 57 \
    --name data57swap --expect-sha256 c9d9c0d28b667da7e93b3e6c860312d728bf3af73035172d76036644c72852a2 \
    --label "controls/lkts57_control_swap.txt (ALTERED CONTROL)" || exit 2
  python3 gen_cert.py controls/lkts57_control_swap.txt LktsKernel/Control/Cert57Swap.lean --v 57 \
    --name data57swap --module LktsKernel.Control.Data57Swap \
    --expect-sha256 c9d9c0d28b667da7e93b3e6c860312d728bf3af73035172d76036644c72852a2 --group 11 \
    --theorem-prefix lkts57swap --label "controls/lkts57_control_swap.txt (ALTERED CONTROL)" || exit 2
  python3 gen_data.py controls/lkts57_control_dupsys.txt LktsKernel/Control/Data57Dup.lean --v 57 \
    --name data57dup --expect-sha256 afe7e17cb2d025c1d7c6bd052572a4c4c04cf6f6f90c51945c7acf27db9f2b35 \
    --label "controls/lkts57_control_dupsys.txt (ALTERED CONTROL)" || exit 2
  python3 gen_cert.py controls/lkts57_control_dupsys.txt LktsKernel/Control/Cert57Dup.lean --v 57 \
    --name data57dup --module LktsKernel.Control.Data57Dup \
    --expect-sha256 afe7e17cb2d025c1d7c6bd052572a4c4c04cf6f6f90c51945c7acf27db9f2b35 --group 11 \
    --theorem-prefix lkts57dup --label "controls/lkts57_control_dupsys.txt (ALTERED CONTROL)" || exit 2
}

build() {  # build modules in order, stopping at the first failure
  for m in "$@"; do sh build_module.sh "$m" || exit 1; done
}

case "${1:-}" in
  gen) gen ;;
  57) check_prior; build LktsKernel/PriorFormal.lean LktsKernel/Generic.lean LktsKernel/Data57.lean \
        LktsKernel/Cert57.lean ;;
  87) check_prior; build LktsKernel/PriorFormal.lean LktsKernel/Generic.lean LktsKernel/Data87.lean \
        LktsKernel/Cert87.lean ;;
  controls)
    build LktsKernel/Control/Data57Swap.lean LktsKernel/Control/Data57Dup.lean
    : > logs/controls.summary
    for m in Cert57Swap Cert57Dup; do
      sh build_module.sh LktsKernel/Control/$m.lean
      echo "$m exit=$? (expected nonzero)" >> logs/controls.summary
    done
    for m in Diag57Swap Diag57Dup; do
      sh build_module.sh LktsKernel/Control/$m.lean
      echo "$m exit=$? (expected 0)" >> logs/controls.summary
    done
    cat logs/controls.summary ;;
  replay57|replay87)
    v=${1#replay}
    . ./lean_env.sh
    set +e
    for m in LktsKernel.PriorFormal LktsKernel.Generic LktsKernel.Data$v LktsKernel.Cert$v; do
      /usr/bin/time -l "$LEANCHECKER" -v "$m" > "logs/replay.$m.log" 2> "logs/replay.$m.time"
      echo "leanchecker -v $m exit=$? $(grep -E ' real ' "logs/replay.$m.time" | awk '{print $1"s"}')" \
        "rss=$(grep 'maximum resident' "logs/replay.$m.time" | awk '{printf "%.2fGB", $1/1e9}')"
    done ;;
  all) "$0" gen && "$0" 57 && "$0" 87 && "$0" controls && "$0" replay57 && "$0" replay87 ;;
  *) echo "usage: sh reproduce.sh {gen|57|87|controls|replay57|replay87|all}" >&2; exit 2 ;;
esac
