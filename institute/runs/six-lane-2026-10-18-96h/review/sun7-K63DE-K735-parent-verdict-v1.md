# Sun k7: K63-D, K63-E and K7-35 written exclusions

Recorded at 2026-10-19T02:08:23-0700.

**CORRECTNESS-ACCEPTED SCOPED PARTIALS**, with all mandatory errata listed below. These are written proofs; no exploratory search, LP optimum or leaf census is a premise.

## Exact conclusions

- **K63-D:** no class-K6.3 configuration has f_d=1 (d carries no 3-marker), with arbitrary marker sharing in C and arbitrary exponents.
- **K63-E:** no class-K6.3 configuration has f_d≥2 and no 2-marker in C, with any allowed 5-marker placement and arbitrary exponents.
- **K7-35:** no class-K7 configuration has no 2-marker and has its 3- and 5-markers on distinct vertices, with arbitrary exponents.

R0 extends all three finite-group arguments to arbitrary groups with finite-index subgroups.

## Frozen evidence

- **K63-D**: [K63-D-v1.md](/Users/jinleic/repos/aifours/mathematics/evidence/six-lane-20261018-96h/sun-coset7/K63-D-v1.md) `f4027779f19a4733614f543d56a4cf596af9383f04510fbc725a5a7a3ebed255`; [K63-D-erratum-v1.md](/Users/jinleic/repos/aifours/mathematics/evidence/six-lane-20261018-96h/sun-coset7/K63-D-erratum-v1.md) `75478241f060873f3911b897ad65a41cb46a3637dd8d15bfe8e09f3e7f3dae90`; [K63-D-erratum-v2.md](/Users/jinleic/repos/aifours/mathematics/evidence/six-lane-20261018-96h/sun-coset7/K63-D-erratum-v2.md) `891567ee25fae8e109fca702eeac616e26243ede0e535e8c0e30c798d8da147a`
- **K63-E**: [K63-E-v1.md](/Users/jinleic/repos/aifours/mathematics/evidence/six-lane-20261018-96h/sun-coset7/K63-E-v1.md) `73bcde10f4197ffc06c65107b5786ec9a03426c8ba86b7308343bfddac2d4de8`; [K63-E-erratum-v1.md](/Users/jinleic/repos/aifours/mathematics/evidence/six-lane-20261018-96h/sun-coset7/K63-E-erratum-v1.md) `b5d07d06f50f44262985553ece0101268f523a0c53edf18fdaca924e52968480`; [K63-E-erratum-v2.md](/Users/jinleic/repos/aifours/mathematics/evidence/six-lane-20261018-96h/sun-coset7/K63-E-erratum-v2.md) `20fb0b0a68a3996d41f9991e9a28eeaeb77c24097d1c82290165c2870c6f601c`; [K63-E-erratum-v3.md](/Users/jinleic/repos/aifours/mathematics/evidence/six-lane-20261018-96h/sun-coset7/K63-E-erratum-v3.md) `159def412deaa4a4a2dbba1f416418414daa1e2d869592a02d724c9f57bcb356`
- **K7-35**: [K7-35-v1.md](/Users/jinleic/repos/aifours/mathematics/evidence/six-lane-20261018-96h/sun-coset7/K7-35-v1.md) `5624d9783f5fb0236283a870109ce45c3655123949fd0e6dfcb0546ad517fc5a`; [K7-35-erratum-v1.md](/Users/jinleic/repos/aifours/mathematics/evidence/six-lane-20261018-96h/sun-coset7/K7-35-erratum-v1.md) `b13e1cf28dd55cd0983c5cc8259520e6723206d556dbcad27389ac6aaec66e32`; [K7-35-erratum-v2.md](/Users/jinleic/repos/aifours/mathematics/evidence/six-lane-20261018-96h/sun-coset7/K7-35-erratum-v2.md) `93f99707c5700ec2f7f1c9f9f088ce00866e02b073c8e38c052650dd1bd20d44`

- [Codex](sun7-three-written-codex-v1.prompt.stdout.txt) `e562a13e36449b30f6171d23a9687242992135b7f13372ec00c96480bbae92d4`: K63-E and K7-35 ACCEPT, no findings; K63-D correct conclusion after one required MAJOR repair (shared 2/3-marker in D5's inverse-row certificate). Actual CLI model gpt-6.1-sol.
- [Claude](sun7-three-written-claude-v1.prompt.note.md) `907f566364f5886f67b82af5df359f7c47f557e7343c4e0c25a6c00a796f10c5`: all three CORRECT, 0 FATAL/0 MAJOR/3 MINOR each. Its D-1 is the same mathematical defect as Codex's MAJOR D1; severity labels do not alter the required repair. Actual CLI model claude-opus-5-5.

The parent read every candidate and every mandatory erratum in full. The final K63-D repair was explicitly checked by both reviewers in their reports and by the parent: for marked neighbour m_x=2^E3^F and inverse d-entry2, the only compatible pair is x,d with gcd2, so half-weights give objective4+1/2+2=13/2>6. No new statement or unreviewed mathematical idea is introduced by the errata.

## Parent verification and defect dispositions

**K63-D.** At a C-apex, assuming alpha_vd=1, the d-label contributes2 units. If d is unmarked, choose an apex with at leastfour unmarked C-neighbours or, when markers occupy three distinct C-vertices, the 5-marked apex. Explicit class-weight tables give at least4 C-units. Parent found the omitted 5–5 compatibility in D0; H1 repairs it with half-weights. If d carries only5, all five C-entries must be5; inversion gives five1s, and H2 handles both pure2 and joint2/3 marker products by evenness, not by assuming a pure prime power. The same apex is chosen from indices in both orientations, forcing alpha_vd=alpha*_vd=2 against INV's sum≤3. H3–H5 fix marker wording and cite the accepted subset-form class bound.

**K63-E.** LFC at d restricts the number of alpha_dc=2 entries to3..5 in each orientation. INV makes their supports disjoint, hence complementary triples. At each C-apex, explicit weights show alpha_vd=1 needs at leastthree C-threes (apart from an all-five alternative killed by inversion), while alpha_vd=2 forbids threes. Parent found and the worker repaired the double-four weight13/12 and the marked-three/unmarked-five overlap. J1 lowers the marked-four weight to1/4; J2 first eliminates every C-five using its coprimeness with d when h_d=0; J3 explicitly supplies the separate h_d>0 certificate with y_d=0. The three-neighbour closure forces at leastfour vertices inside a three-element support, impossible. J4/J5 cover the marked apex and subset-form imports.

**K7-35.** ROW-2's four-unmarked/two-marked local tables imply 5-closure and 3-closure restrictions. The 3-marked vertex's row in both orientations partitions its neighbours into complementary triples of4s. No5 edge among the five unmarked vertices survives. If a3 edge exists, its support is a triple; the other unmarked vertex has three incident values≤2, regardless of their mixture, so its three4s must hit the other outside vertex and both markers. The 5-marked vertex then has both a3 and a4 among its unmarked neighbours, contradicting ROW-1. Parent identified the original omitted mixed1/2 case; erratumK1 is the split-free repair. Finally all rows have at leastthree4s in both orientations, and INV forces a3-regular graph on7vertices, impossible. K2–K4 fix the contribution arithmetic, inversion transfer and alpha-range import.

## Current mathematical frontier

- K5.3 excluded by the [computation-free X1 proof](x1-written-parent-verdict-v1.md); old StageA/F-1 history retained.
- K7 remains open only with **both a 2-marker and a 3-marker**, on the same or different vertices, with the5-marker anywhere.
- K6.3 remains open only with **a 3-marker on d and a 2-marker i* in C**.
- K6.2* remains open; K62-A is a separate unreviewed candidate, not an accepted partial exclusion.
- K63-CLIQUE/TG is a separate unreviewed candidate after a mandatory full-clique hypothesis correction; not promoted here.

This supersedes any earlier shorthand “K6.2* partly” as an accepted frontier: no K62 result has yet been accepted in this continuation.

## Limits and bookkeeping

These results inherit the accepted Sun(t),t≤6, applications through LFC and the existing class definitions/finite-core/INV facts. No Lean, human review, priority or significance assessment. The generic erratum source headers mentioning “Codex MAJOR D1” in the E/35 files refer to the review packet, not defects in those two claims; only K63-D had that Codex finding. Erroneous approximate IRC time labels remain withdrawn by the lane timing addendum.
