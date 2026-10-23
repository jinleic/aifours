# Review bundle list (rotation slice), natural stop after Theorem SH3+-

Written after host clock 2026-10-18T05:45:47-07:00 by OlsonRotationRigidity.  Lists the NEW unreviewed results since
results-v2.md, with sha256 and an import map.  Frozen predecessors are listed for provenance only.

## New results for review (all [W], unreviewed)

| file | sha256 | claim (exact scope) |
|---|---|---|
| proof-ELT0-v2.md | d17e81087e2a63bb8a3a54fb392349f81531d329e11710af1c544261fa4e9379 | Theorem ELT0: p >= 5, N <= 4p-2, RGR shape, all blocks odd, kappa = 0, generator with full GLOBAL subset sums (FULL), w avoids => N + E <= 4p-2; at N = 4p-2, w is rigid. Savchev-Chen remark purely conditional (no import). |
| proof-SH3-v4.md | 321978ffb3974c7a1770e91a7a8634c551ccf8653ea2f96b447bdd6fe712b06c | Theorem SH3+-: p >= 5, length 4p-2, RGR shape, rotations rho_c/rho_-c except ONE rho_(+-3c), H >= 1 (all-odd form) => identity 2p-subword. Any kappa, any number of odd blocks; self-contained (Lemma U incl. KB capped-case impossibility; Lemma FLEX without exceptions). |
| proof-EXP2-v1.md | b5287e761fc8efbb64c8a1c0a9b54a643b8cff042f68407268ce13bd32d6eb13 | Theorem EXP2: expansion with per-pattern side fullness (X1'), spare pairs (X2), and (X4) min(A,B) < kappa + E/2 => not an avoider unless rigid. KNOWN DEFECT: Sec. 1 weight convention for x = 0 is garbled (correct: b_x odd in {-(p-2),...,p-2} u {p}, x = 0 -> b = p); fix pending, do not review that sentence as written. |
| proof-SHROT-v1.md | d1c506c685913644b2752ef51604cf5a50bcb490595d1e23993d21b28ba9387e | Prop. SH-ROT (sharpness only): rho_-3 sigma_2^(2p-5) rho_1^(2p-1) sigma_0 is a non-rigid avoider of length 4p-4 for every p >= 5. |
| proof-EXP-v2.md | 4315e873b182eae8a6255dc45d801a95ad3b87b5900eee286be5308dfe57a2d9 | Theorem EXP (per-run fullness version; superseded in strength by EXP2/SH3 but kept). |

Frozen history (not for review): proof-SH3-v1.md 02968482..., v2 b81fe382... (KB use, (E*) exception), v3 d2c66677...
(not self-contained); proof-ELT0-v1.md 9c16c7e8...; proof-EXP-v1.md bbae26e4...
Already under review (unchanged): proof-ROT-o3-v3.md 9b0a37db..., proof-ROT-o4-v3.md db4eee8a...

## Import map

| file | imports |
|---|---|
| ELT0-v2 | GRX + PM* (accepted lowodd verdict 0853f4ac); RGR-LONG(p) (accepted RUNS verdict 82adbddd). |
| SH3-v4 | GRX, PM*, K1 (accepted lowodd); Corollary B'(b), C1 lemma composition, Theorem KBH, Theorem KB uncapped implication (accepted RUNS assembly v4; parent-confirmed scopes); Davenport-alpha (V) (reviewed, erratum m4); trivial cut. |
| EXP2-v1 | GRX (accepted); Corollary B'(b), C1 composition. |
| SHROT-v1 | GRX only. |
| EXP-v2 | GRX; Corollary B'(b), C1 composition. |

## Finite aids (not premises)

code/check_elt0_v1.py (6b730409...) with out/check_elt0_v1.jsonl (c9f7110a...): 3,750 kappa = 0 RGR-shape non-rigid avoiding
data at lengths 4p-4..4p-7 obey N + E <= 4p-2 (equality attained).  The C++ classifier code/kblock_exact_v2.cpp
(5a78a05f...) and the observation that non-rigid avoiders at 4p-4, 4p-5 have a single heavy +-3c motivated SH3.

## Still open for ROT(p) (RGR shape)

H = 0 with a heavy; two or more heavies outside ELT0 / EXP2; heavy values other than +-3c; and, for non-constant
reflection runs, everything beyond o <= 4 (these need the reflection slice's REFL).
