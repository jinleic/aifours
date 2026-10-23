#!/bin/sh
# Read-only Lean 4.34.1 + prebuilt Mathlib environment (no lake, no writes to the cache).
# The originally named cache scratch/rh-quasi-lean-2026-10-07/lean no longer exists on this
# machine (searched the whole filesystem on 2026-10-16); this is the only Lean 4.34.1
# project with a fully built Mathlib that was found.
set -eu
KDIR=$(CDPATH= cd -- "$(dirname -- "$0")" && pwd)
TOOLCHAIN=/Users/jinleic/.elan/toolchains/leanprover--lean4---v4.34.1
CACHE=/private/tmp/seymour-lean-20261014-68365/.lake/packages
LEAN_PATH="$KDIR/build"
for p in mathlib batteries aesop Qq proofwidgets plausible LeanSearchClient importGraph; do
  LEAN_PATH="$LEAN_PATH:$CACHE/$p/.lake/build/lib/lean"
done
export LEAN_PATH
export PATH="$TOOLCHAIN/bin:$PATH"
export LEAN="$TOOLCHAIN/bin/lean"
export LEANCHECKER="$TOOLCHAIN/bin/leanchecker"
