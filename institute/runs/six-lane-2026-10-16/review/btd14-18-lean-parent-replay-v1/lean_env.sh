#!/bin/sh
# Parent-owned read-only Lean 4.34.1 + prebuilt Mathlib environment (no lake, no writes to the cache).
# Same toolchain/cache logic as review/mcdsqs38-kernel-parent-replay-v1/lean_env.sh (read, not modified);
# build output goes to $PBTD_BUILD (default ./build of this directory).
set -eu
KDIR=$(CDPATH= cd -- "$(dirname -- "$0")" && pwd)
TOOLCHAIN=/Users/jinleic/.elan/toolchains/leanprover--lean4---v4.34.1
CACHE=/private/tmp/seymour-lean-20261014-68365/.lake/packages
PBTD_BUILD=${PBTD_BUILD:-$KDIR/build}
LEAN_PATH="$PBTD_BUILD"
for p in mathlib batteries aesop Qq proofwidgets plausible LeanSearchClient importGraph; do
  LEAN_PATH="$LEAN_PATH:$CACHE/$p/.lake/build/lib/lean"
done
export PBTD_BUILD LEAN_PATH
export PATH="$TOOLCHAIN/bin:$PATH"
export LEAN="$TOOLCHAIN/bin/lean"
export LEANCHECKER="$TOOLCHAIN/bin/leanchecker"
