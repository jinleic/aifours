# K3 text errata r1 (lane moqls7-maximum)

Written 2026-10-18 00:52 PDT in response to the parent K3 cover disposition
(`moqls7-k3-cover-parent-disposition-v1.md`, fbfc0e10…f369) and the desk RESULT (0f80460c…ef84). These errata
correct wording in frozen files without rewriting them. No proof object, CNF, receipt or mathematical step changes,
and nothing here is a K3 or M(7) claim. Provenance bindings are in `K3-Q4-SIDECAR.r1.json`.

## E1. B-map runtime claim (Q2), `AMENDMENT-2.r1.md:43-45`
The frozen text says the wrapper "reads each encoder's actual g-variable order" and "must confirm those orders
agree", and that B's construction "is replayed independently". That overstates what ran.
- For encoder A the wrapper asserts at run time that `gram_enc.build`'s map equals its own independently written
  map (`k3_cubes.py` A branch).
- For encoder B the wrapper checks only that the header has at least 2646 variables (`k3_cubes.py:126`). Index
  equality for B rested on a static reading of `gram_encB.py:113-118`.
- Byte-identical A and B appended cube blocks are tautological: both are generated from the same map. They are not
  evidence that B attaches the same pairs to those indices.

**Correction.** The runtime evidence is now `evidence/k3cubes/bmap_oracle_r1.json` (sha256
6e2bd95ee38c615ab2a1a6282531da730b2bf0cc45e104e95b850102e0b1952c), produced by the pinned
`code/bmap_oracle_r1.py` (13f4a5e6…cd8e, pinned in `K3-BMAP-ORACLE.r1.json` before execution). Encoder B's own
`--fix-json` branch was driven by 12 binary designs plus two sign controls, with the K3 production arguments.
Every B variable 1..2646 decodes to its own A index: 0 mismatches. A's map equals the wrapper's map, and the B base
bytes equal the base hash in both B cube metadata files. No B-route K3 result before this oracle is relied on;
the only earlier B attempt (B/C321, `cert_B_r4`) was UNKNOWN in any case.

## E2. Lex invariance statement (Q3), `AMENDMENT-3.r1.md:10` and `:20`
The text says every generator fixes "the cube's full 18-literal assignment" and preserves "cube units" and the
G1–G5 implications, which can be read as invariance of the base CNF and of the cube unit set separately.

**Correction.** Each generator preserves the g-projection of the conjunction base ∧ cube: the base --sym units
together with the cube's 18 signed units, and all G1–G5/G4 constraints. It need not preserve the base --sym units on
their own. Example: C411's column (3,4) swap (`k3_lex.py:33`) sends the --sym unit g_1(p,(0,3)) (variable 109) to
g_1(p,(0,4)) (variable 145). Variable 145 is a positive C411 cube unit, not a base unit. The coverage argument
uses only invariance of the satisfying g-patterns of base ∧ cube, so it is unaffected. The finite control
`evidence/k3cubes/lex_controls_r1.json` checked that each generator is a predicate bijection preserving the
18 signed cube units; the --sym units are a subset of the positive cube units in all three cubes.

## E3. Definition of T(X) (Q3), `AMENDMENT-3.r1.md:25-28`
**Correction.** For a generator, let σ be the induced permutation of the 2646 predicate indices: σ(v) is the index
of the pair obtained by applying the generator's row, column and square relabelling to the pair of v. Define
T(X)_v = X_{σ(v)}, so the appended constraint is X ≤lex X∘σ. This is what the code compares: `k3_lex.image`
returns σ as `perm[v]`, and `lex_clauses` pairs X_v with X_{perm[v]}. X∘σ is the Gram pattern of the transformed
configuration, so the lex-minimal member of each H-orbit satisfies every comparator. Neither involution nor
invariance of X is assumed.

## E4. Zero (0,0) coefficient (Q1), `AMENDMENT-2.r1.md:10` and `:31`
**Correction.** S_a ⊆ {1,…,6} because p = (1,0) and (0,0) share column 0, so g_a(p,(0,0)) = 0 by G1. S_a is nonempty
because row 0 is an ONB and ψ_{a,p} is a unit vector; at the Boolean level this is G3. At `:31`, "exactly one
nonzero coefficient in the ONB of row 0" uses the same G1 zero at (0,0).

## E5. G6 derivation wording, `G6-G2-DERIVATION.r1.md:5-6`, `:8`, `:12`
**Corrections.**
- `:5-6` and `:8`: the cube fixes g(p,(0,k)) for k = 1..6 only. The coefficient at (0,0) is absent by G1, not
  fixed by the cube.
- `:12`: when p and t are collinear, g(p,t) is the constant false. Read: "G1 and G2 forbid a common-neighbour count
  of 1, so g(q,t) = 0." The equality g(p,t) = g(q,t) then holds in that case too.

## E6. Gram citation, `AMENDMENT-2.r1.md:5`
**Correction.** Read `GRAM-ENCODING.r2.md` (c6c506a7…d7c6) §2 G4 (lines 52-65) and `LEMMAS.md` (lines 69-78) in
place of `GRAM-ENCODING.r1.md`. The r1 text pointed G4 at K1 §8, which is insufficient for K3.

## E7. Exclusion status wording, `GRAM-ENCODING.r2.md:136-138`
The text says C321/C411 "are not exclusions until certified", which suggests a producer certificate alone makes an
exclusion.

**Correction.** Producer certificates are evidence. An exclusion of a cube is accepted only by a parent verdict that
names the exact CNF hash: C321 d598507d…8388, C411 2b92f5b1…ddf2. As of this erratum both have producer A-route
certificates only. Parent replay is in progress, and the B routes run after the oracle.

## E8. K2 prerequisite (Q4)
**Correction.** Every K3 statement in AMENDMENT-2, AMENDMENT-3, the cube receipts and any AMENDMENT-4 successor is
conditional on K1 accepted and K2 parent-accepted. That condition makes every K3 triple minimal, so G4 holds on all
14 own row/column lines. The K2 parent verdict (25ecb6ba…1242, 2026-10-18 00:42:18 PDT) meets the condition. See
`K3-Q4-SIDECAR.r1.json` binding 3.
