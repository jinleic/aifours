# Erratum 1 to B3-AZ-CORNER-PURITY-CANDIDATE-v1.md

Issued at 2026-10-19T17:55:47-0700. Target: `/Users/jinleic/repos/aifours/physics/evidence/six-lane-20261018-96h/moqls8/continuations/b3-az-corner/B3-AZ-CORNER-PURITY-CANDIDATE-v1.md`, SHA256 `52c6b59b39ffd1348e412947ac7c301329d70f645205c0b42adcb656eb36b03d`. The target file is immutable and unchanged. This erratum routes the three MINOR findings of the Codex review [CX] (`/Users/jinleic/repos/aifours/institute/runs/six-lane-2026-10-18-96h/review/moqls8-B3-AZpurity-codex-v1.prompt.stdout.txt`, SHA256 `89e839570c05d6b4b6a088665c3c9a36fd1cfd6da1f98ab9df536209119a109c`; 0 FATAL / 0 MAJOR / 3 MINOR) and corrects the amplitude gloss. Status: the candidate remains CANDIDATE, not accepted. This erratum adds no new claim.

## E1 (MINOR 1): index sets and own-basis bridge, L15, L29, L51-52

Add to section 1, after L15: A := {1,2,3} (coordinates) and O := {1,6,7} (own indices).

Insert before the coefficient assertion at L51:

> Column-0 orthonormality and H4 make q_1^1, q_1^6, q_1^7 three orthonormal vectors in the three-dimensional space V_A. So they form an orthonormal basis of V_A. For a = P_A Q_1(i,c), its coefficients in this basis are <q_1^r,a> = <q_1^r,Q_1(i,c)> for r ∈ O. The equality holds because q_1^r ∈ V_A.

With this bridge, the step at L52 reads as follows. If a != 0 had a single nonzero own coefficient, then a ∝ q_1^r with c ∉ supp q_1^r, contradicting a ⊥ e_c. Each of q_1^1, q_1^6, q_1^7 has nonzero coordinates 2 and 3, and c ∈ {2,3}. So each nonzero A-part has at least two nonzero own coefficients.

The own-slot exclusivity used in Theorem U' shares the own index r, not a basis. By H1 at the cells (i,c) and (r,0), <Q_s(i,c),q_s^r><Q_t(i,c),q_t^r> = 0 for s != t, where q_s^r and q_t^r are different vectors in different squares.

## E2 (MINOR 2): amplitude gloss at L73 (also the Theorem L remark)

The sentence "It requires the three corner lines to carry a tight frame of the plane P_r, which constrains the amplitudes of q_1^r" is WITHDRAWN. The weighted tight-frame requirement imposes no extra amplitude restriction on a unit q = (a,b,c) of full support. The columns of

    B = [[0, −conj c, conj b], [conj c, 0, −conj a], [−conj b, conj a, 0]]

lie in the respective corner lines and satisfy B B^* = I − q q^*. This is only a projected-plane identity. It is NOT a realization of Σ or of any configuration.

Replacement for L73:

> Σ itself is not proved to hold or fail. Under Σ, the three nonzero A-projections must resolve the projector onto P_r. Compatibility with the remaining whole-vector constraints is unresolved here.

**Theorem L is conditional only.** Its conclusions hold under Σ. Nothing in the candidate, or in this erratum, asserts or implies that any configuration satisfies Σ, or that Theorem L has realizations.

A later, separate CANDIDATE [SIG] claims that Σ is impossible. It is unreviewed and not accepted, and it is not used or relied on here.

## E3 (MINOR 3): excess terminology at L86

Replace "the at-most-4 excess vectors of Theorems U and U'" with:

> the support excess in each application of Theorems U and U', bounded by four, together with the guaranteed pure pairs

The proved quantity is a bound on support-incidence excess. Equivalently, at most four pairs per application are nonpure. It does NOT bound the number of nonpure whole vectors by four: a pair spread over two cells contributes only one unit of excess.

## E4 (clarifications from [CX]; no change of claims)

- The A-pairs are a subset of the U-pairs, so their purity totals must not be added.
- A common-pure pair and an own-pure pair can describe the same whole cell vector.
- Row and column totals do not determine how many pure entries fall in the corner intersections.
- Section 5's union bound of four is valid, but supplies no placement or incompatibility theorem.
- The sentence "These statements are not in the prior notes" is a statement of the worker's knowledge only. Novelty is not certified, and no novelty is claimed.

## Sources

- [CX] `/Users/jinleic/repos/aifours/institute/runs/six-lane-2026-10-18-96h/review/moqls8-B3-AZpurity-codex-v1.prompt.stdout.txt`, SHA256 `89e839570c05d6b4b6a088665c3c9a36fd1cfd6da1f98ab9df536209119a109c`.
- [SIG] `/Users/jinleic/repos/aifours/physics/evidence/six-lane-20261018-96h/moqls8/continuations/b3-sigma-closure/B3-SIGMA-MIXED-CORNER-EXCLUSION-CANDIDATE-v1.md`, SHA256 `adad9baeb814f85a370a5b1c62cb9fb883b6166d366556a121d4f7ed0771ddd3` (CANDIDATE, not used).
