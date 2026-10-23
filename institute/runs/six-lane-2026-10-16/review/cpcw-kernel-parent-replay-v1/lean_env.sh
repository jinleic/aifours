#!/bin/sh
# Read-only Lean 4.34.1 + prebuilt Mathlib d13f23b environment (no lake, no writes to the cache).
# Same toolchain and cache as review/cdf-kernel-worker-v1/lean_env.sh (used read-only, not modified);
# the output directory is $CPCW_BUILD (default: ./build of this directory), so that a replay can
# compile into its own fresh directory.
set -eu
KDIR=$(CDPATH= cd -- "$(dirname -- "$0")" && pwd)
TOOLCHAIN=/Users/jinleic/.elan/toolchains/leanprover--lean4---v4.34.1
CACHE=/private/tmp/seymour-lean-20261014-68365/.lake/packages
CPCW_BUILD=${CPCW_BUILD:-$KDIR/build}
LEAN_PATH="$CPCW_BUILD"
for p in mathlib batteries aesop Qq proofwidgets plausible LeanSearchClient importGraph; do
  LEAN_PATH="$LEAN_PATH:$CACHE/$p/.lake/build/lib/lean"
done
export CPCW_BUILD LEAN_PATH
export PATH="$TOOLCHAIN/bin:$PATH"
export LEAN="$TOOLCHAIN/bin/lean"
export LEANCHECKER="$TOOLCHAIN/bin/leanchecker"
