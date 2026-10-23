# Remaining residue types, round 2: (2,192), (4,160), (6,144)

**Result: no type is excluded.** This round proves new necessary conditions, sub-case classifications and exhaustive finite certificates. It refutes all three round-1 (2,192) witnesses and gives a precise stopping obstruction for each of the three types. The balanced nine-variable NL242 question remains open: seven residue types remain.

The proof is model-written and conditional on the reviewed lemmas listed at the top of [`PROOF.md`](PROOF.md). It is not Lean-verified, not peer reviewed, and has not yet had an independent proof review. Novelty is unestablished: the residue and paired-half tools are prior art (Wang–Lou–Wang, Lou–Xu–Wang), and the GL(6,2) cubic classification reproduces a classical result.

## Claims (details and proofs in PROOF.md)

| Type | New result | Stopping obstruction |
|---|---|---|
| all | Lemma 1.1: slice ternary structure. Uncertainty `Σ_u hat p_u(κ)^2 ≥ 64 max_u |hat p_u(κ)|`, uniform parity and an affine second bit. Lemma 1.2: the Λ residue is affine, so `W_{E_c} ≡ 12ℓ_c + 8(ε_c+κ·σ_c) mod 16`. Lemma 1.3: first moments. | — |
| (2,192) | Lemma 2.2: for six-variable cubics, `W ≡ 4·P6 mod 8`, and the next residue bit is affine. Exhaustive tables: 6 GL(6,2) cubic orbits; at `z = 8`, 6 Walsh classes of `x0x1x2+q`, each a single stabilizer orbit. Exact per-coset `(h,Λ)` realizability for `ℓ ≤ 4`. **All three round-1 witnesses are refuted.** | The strengthened `z = 8` count relaxation is still SAT. Its witness passes every per-coset test. Cross-coset κ-alignment and the exact S side remain unconstrained. |
| (4,160) | Lemma 3.1: affine slices make every coset function affine. `z = 8`: 715 zero flats, split 15 (8a, coset-affine) + 700 (8b, 6 non-affine cosets). **Theorem 3.4: pairwise distinct D1 characters force `c ≥ 12 + z/2`.** Case 8a has `c ≥ 4`; ℓ parity is uniform. | Slice witnesses at `c = 4` (with collisions) and at `c = 16` (distinct characters) satisfy every slice constraint, so collisions are not forced. |
| (6,144) | Lemma 4.1 (E structure) and a dichotomy: odd slices give `z ≥ 12`; otherwise E is coset-affine, and `RM(2,6)|D0` has minimum weight 4, so a non-K-invariant Z has `z ≥ 8`. **`z = 8` classification: K-invariant, or exactly 540 sets, each with D1 character fibers 12/24.** Theorem 4.4: K-invariant Z gives `c ≥ 14` (16 when `z ≡ 4 mod 8`). | With fibers ≤ 24, the projection energy is `≤ 3456 < 4096` even at `c = 0`. The single-character lever cannot see non-K-invariant Z. |

## Files

- `PROOF.md`: statements and proofs.
- `code/rank2_cubic_classes.py`: GL(6,2) orbits on cubic forms, completion Walsh tables and the Lemma 2.2 check. Output: `results/rank2-cubic-classes.json`.
- `code/rank2_coset_realizability.py`: stabilizer orbits and exhaustive ℓ = 2, 4 subsets. Output: `results/rank2-coset-realizability.json`.
- `code/rank2_witness_check.py`: refutes the round-1 witnesses. Output: `results/rank2-witness-check.json`.
- `code/rank2_probe2.py`: the exploratory strengthened relaxation (z3). Output: `results/rank2-probe2-z8.json` with a SAT witness. Its unsat/unknown verdicts would carry no claim.
- `code/rank4_160_structure.py`: z = 8 classification, lone slice and slice witnesses. Output: `results/rank4-160-structure.json`.
- `code/rank6_144_zero_sets.py`: restriction-code weights, odd slices, the 540 sets and the K-invariant minimum. Output: `results/rank6-144-zero-sets.json`.
- `code/audit.py`: independent audit. It imports no producer code and no z3, and every check raises `ValueError`.
- `code/final_verify.py`: runs the audit in place, normally and under `-O`, then runs seven corruption controls. Output: `results/final-verify.json`.
- `inputs/`: SHA-256-pinned round-1 witnesses (`round1-rank2-probe-*-aux.json`) and `round1-PROOF.txt`. `inputs/slice-screen.json.gz` is an unused copy of the root pin.

## Replay

```
python3 code/audit.py          # independent audit, about 6 s
python3 -O code/audit.py
python3 code/final_verify.py   # refuses to overwrite results/final-verify.json
```

The producers refuse to overwrite their outputs. Run them in a copy to regenerate. Resource use was one thread and less than 1 GiB. Elapsed producer times: cubic classes 6.1 s, realizability 1.9 s, (6,144) 0.5 s, (4,160) 1.8 s, z3 probe 38.2 s.

## Limitations

- The (2,192) analysis is complete only per coset, only for the R side, and only for `z = 8, ℓ ≤ 4`. The S side (any of four cubic classes, `a_c` up to 8) and cross-coset alignment are not enumerated.
- (4,160) Theorem 3.4 needs every D1 coset function to be affine. Case 8b, and larger z with non-affine slices, are outside it.
- (6,144): the dichotomy is complete for all z. The explicit classification covers only `z = 8`.
- The slice witnesses are aggregate energy assignments, not Boolean functions. A count or profile vector is not a Boolean function.

## FRONTIER

**PROOF-OBLIGATION.** Seven types remain open. The highest-value next steps are:

1. (2,192), `z = 8`: an aligned proof-producing search over the explicit orbit representatives, using the per-coset valid-subset lists as domains and adding the D0-coset form `h_00 = 8δ − 1_{Z^⊥} − hat G/4`.
2. (4,160), case 8a: combine Theorem 3.4 with the S-side uncertainty (`Σ_u hat S_u(κ)^2 ≥ 512 max_u |hat S_u(κ)|`) per slice.
3. (6,144): the same S-side coupling for the 540 non-invariant sets.

Do not repeat count relaxations without new spatial constraints.
