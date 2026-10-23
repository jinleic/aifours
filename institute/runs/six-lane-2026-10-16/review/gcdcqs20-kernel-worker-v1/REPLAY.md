# gcDCQS(20^4 : 0) certificate A and mcDSQS(80): Lean-kernel replay

What is kernel-checked (Lean 4.34.1 with the prebuilt Mathlib d13f23b; axioms only `propext`,
`Classical.choice`, `Quot.sound`):

* `Mcd.Audit.root_gc80 : Mcd.TargetGc80`: a gcDCQS(20^4 : 0) exists on `Fin 80`. The groups
  are `{0..19}, {20..39}, {40..59}, {60..79}` and the stem is empty. Every derived design is a
  gcSTS(79, 19) with `r = χ′(79)` and `s = χ′(79) - (79 - 19) / 2`.
  `root_gc80_counts` adds `|A| = 19400` and 970 derived blocks at every point.
  `root_gc80_numerals` and `root_gc80_unfolded` give the same root with numerals: 40 classes,
  exactly 10 of which avoid `G(x) \ {x}`.
* `Mcd.Audit.root_mc80 : Mcd.TargetMc 80`: an mcDSQS(80) exists. `witness_mc80` adds the
  counts: 20540 blocks, 1027 derived triples at every point, 40-class colourings.
* `Mcd.Audit.root_chi79 : Mcd.chiPrime 79 = 40`. The `≥` direction is
  `root_lower79 : Mcd.ColourLowerBound 79 40`, which covers every colouring of every STS on
  every 79-element type. The `≤` direction is the raw mcDSQS(80) `POINT 79` section, read on
  `Fin 79`.
* The witnesses are the raw certificates themselves, pinned by SHA-256:
  `review/gcdcqs20-parent-inputs-v1/gcdcqs20-e1s1_p10.txt` (`58b51b50…a0ca`) and
  `review/mcdsqs80-parent-inputs-v1/mcdsqs80_c21_A.txt` (`49f500c5…44a3`). Every BLOCKS line,
  GROUPS line and POINT/CLASS triple is copied verbatim, in order (`gen_lean80.py`).
  `audit_binding80.py` re-parses both raw files and the Lean literals independently and
  compares them.

Not formalized: the Tan–Zhou constructions (Construction 2.1, Corollary 2.6, the infinite
family). Only the two finite witnesses and `χ′(79) = 40` are kernel-checked.

## Files

* `McdKernel/{Target,Check,Counts}.lean`, `lean_env.sh`, `build_module.sh`: byte-identical copies
  of the reviewed `review/mcdsqs38-kernel-parent-replay-v1` machinery. The SHA-256 values are
  pinned in `manifest.json` `reused_byte_identical`.
* `Gc80/GcTarget.lean`: the gcDCQS target definitions (no proofs, no data).
* `Gc80/Derived.lean`: data-independent lemmas: SQS, CQS and incomplete STS from derived
  designs, and the four groups.
* `Gc80/Check80.lean`: per-point Boolean checkers and their soundness theorems.
* `Gc80/Counts79.lean`: `ColourLowerBound 79 40`.
* `Gc80/Data*.lean`: 20 generated literal modules.
* `Gc80/Cert{Mc,Gc}Pts{0..3}.lean`: one `decide +kernel` declaration per point, 160 in total.
* `Gc80/CertMc.lean`, `Gc80/CertGc.lean`: assembly.
* `Gc80/Audit80.lean`: the roots, their unfolded forms, `#print` of every definition, and
  `#print axioms`.
* `Gc80/Controls80.lean`: 17 kernel and semantic controls. This module must build.
* `Gc80/PosTwin.lean`: the positive twin. It must build.
* Statement-mutation controls (each must fail):
  * `Gc80/NegPointCount81.lean`: wrong point count;
  * `Gc80/NegBlockSize5.lean`: wrong block size;
  * `Gc80/NegColours39.lean`: 39 colours;
  * `Gc80/NegHoleFree9.lean`: 9 hole-free classes.
* `Gc80/NegKernelSwap.lean`: the kernel must reject `decide +kernel` on corrupted data. Must
  fail.
* `gen_lean80.py`, `audit_binding80.py`, `lean_source_scan.py` (a byte-identical copy of the
  reviewed scanner) and `replay80.py` (the driver).
* `manifest.json` pins all of the above.
* `progress.md`: the host-clock log. `scratch/` holds development builds only and is not part
  of the pinned deliverable.

## Replay in place

```sh
cd /Users/jinleic/repos/aifours/institute/runs/six-lane-2026-10-16/review/gcdcqs20-kernel-worker-v1
python3 -B replay80.py /ABSOLUTE/OR/RELATIVE/NEW_OUT_DIR      # --jobs N optional, N <= 4, default 2
```

`NEW_OUT_DIR` must not exist. The driver creates it and writes only inside it: `build/`,
`logs/`, `regenerated/`, `binding-audit.json` and `result.json`. Success is
`"status": "REBUILD_AND_FRESH_KERNEL_REPLAY_PASS"` in `NEW_OUT_DIR/result.json`. The driver
runs steps 1–8 listed in its docstring: pins, regeneration, binding audit, source scan,
rebuild, negative controls, and `leanchecker --fresh` of `Gc80.Audit80` and `Gc80.Controls80`.
It uses one elaboration thread per Lean process and at most N Lean processes at once.

Resources measured on the worker replay are recorded in `result.json`: wall time per step,
`/usr/bin/time -l` peak RSS and peak memory footprint.

## Replay from a fresh copy

Copy only the pinned files plus the manifest, then point the driver at the review directory
that holds the raw certificates:

```sh
SRC=/Users/jinleic/repos/aifours/institute/runs/six-lane-2026-10-16/review/gcdcqs20-kernel-worker-v1
DST=/path/to/fresh-copy          # must not exist
python3 - "$SRC" "$DST" <<'EOF'
import json, shutil, sys
from pathlib import Path
src, dst = Path(sys.argv[1]), Path(sys.argv[2])
dst.mkdir()
files = list(json.loads((src / 'manifest.json').read_text())['files']) + ['manifest.json']
for rel in files:
    (dst / rel).parent.mkdir(parents=True, exist_ok=True)
    shutil.copy2(src / rel, dst / rel)
print(len(files), 'files copied')
EOF
GC80_REVIEW=/Users/jinleic/repos/aifours/institute/runs/six-lane-2026-10-16/review \
  python3 -B "$DST/replay80.py" /path/to/fresh-out   # must not exist
```

Without `GC80_REVIEW`, the driver reads the raw certificates from the copy's parent
directory.

## Trust limits

* `lean` and `leanchecker` come from one toolchain. They share one kernel implementation; this
  is not Comparator and not an independent kernel.
* The prebuilt Mathlib oleans are trusted for elaboration. `leanchecker --fresh` re-checks every
  declaration in the import closure, Mathlib included.
* `decide +kernel` reduces Bool-valued checkers in the kernel, using GMP-accelerated Nat
  literals. There is no `native_decide` and no `Lean.ofReduceBool`.
* The meaning of the roots rests on two files, `McdKernel/Target.lean` and
  `Gc80/GcTarget.lean`. Their definitions and the root types are printed in the Audit80 log,
  which is included in `result.json` as `printed_audit_output`.
