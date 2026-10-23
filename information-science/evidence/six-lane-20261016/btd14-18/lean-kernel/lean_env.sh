#!/bin/sh
# Read-only Lean 4.34.1 + prebuilt Mathlib environment (no lake, no writes to the cache), same logic as
# review/mcdsqs38-kernel-parent-replay-v1/lean_env.sh (read, not modified); the build output directory is $BTD_BUILD
# (default ./build of this directory) so that a replay can compile into its own fresh directory inside this lane.
set -eu
KDIR=$(CDPATH= cd -- "$(dirname -- "$0")" && pwd)
TOOLCHAIN=/Users/jinleic/.elan/toolchains/leanprover--lean4---v4.34.1
CACHE=/private/tmp/seymour-lean-20261014-68365/.lake/packages
BTD_BUILD=${BTD_BUILD:-$KDIR/build}
LEAN_PATH="$BTD_BUILD"
for p in mathlib batteries aesop Qq proofwidgets plausible LeanSearchClient importGraph; do
  LEAN_PATH="$LEAN_PATH:$CACHE/$p/.lake/build/lib/lean"
done
export BTD_BUILD LEAN_PATH
export PATH="$TOOLCHAIN/bin:$PATH"
export LEAN="$TOOLCHAIN/bin/lean"
export LEANCHECKER="$TOOLCHAIN/bin/leanchecker"
