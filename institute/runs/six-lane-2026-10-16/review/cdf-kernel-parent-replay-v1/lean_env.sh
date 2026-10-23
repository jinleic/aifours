#!/bin/sh
# Read-only Lean 4.34.1 + prebuilt Mathlib d13f23b environment (no lake, no writes to the cache).
# Same procedure as review/lkts-kernel-parent-replay-v1/lean_env.sh (used read-only, not modified),
# except that the output directory is $CDF_BUILD (default: ./build of this directory), so that a
# replay can compile into its own fresh directory.
set -eu
KDIR=$(CDPATH= cd -- "$(dirname -- "$0")" && pwd)
TOOLCHAIN=/Users/jinleic/.elan/toolchains/leanprover--lean4---v4.34.1
CACHE=/private/tmp/seymour-lean-20261014-68365/.lake/packages
CDF_BUILD=${CDF_BUILD:-$KDIR/build}
LEAN_PATH="$CDF_BUILD"
for p in mathlib batteries aesop Qq proofwidgets plausible LeanSearchClient importGraph; do
  LEAN_PATH="$LEAN_PATH:$CACHE/$p/.lake/build/lib/lean"
done
export CDF_BUILD LEAN_PATH
export PATH="$TOOLCHAIN/bin:$PATH"
export LEAN="$TOOLCHAIN/bin/lean"
export LEANCHECKER="$TOOLCHAIN/bin/leanchecker"
