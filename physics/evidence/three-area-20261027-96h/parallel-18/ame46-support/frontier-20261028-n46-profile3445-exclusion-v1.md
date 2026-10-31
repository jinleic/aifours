# Candidate exclusion of residual alphabet profile (3,4,4,5) at support 46

Owner **PhysicsAME46-2**. Native clock immediately before writing: `Wed Oct 28 19:31:53 PDT 2026`; not an exact completion time. **WRITTEN plus exact finite-enumeration candidate**, not independently accepted, formally verified, or a novelty claim. This is one profile of the open N=46 case, not a global ≥47 result.

The reduction to `N=46,t=26,n=10,|E|=20` and the residual notation depend on `frontier-20261028-n46-residual-alphabet-exclusions-v1.md`, SHA-256 `966f125ed180bb48b2848b0900ca37a5f4ee53fab44d5c937050a529cba6e2fc`, and its pinned unreviewed prerequisites. In particular P denotes the 26 saturated coefficients, E the other 20 entries, and every coordinate-pair projection of E has exactly 10 values, each with exactly two E extensions. The named classical no-OLS(6) import is inherited from the prerequisites.

## 1. Claim and required normal form

Assume, for contradiction, that a 46-support AME(4,6) has residual alphabet sizes `(5,3,4,4)` at parties `(A,B,C,D)` in that order. The following deductions force a finite, complete normal form.

For any pair of parties, the P and E pair projections partition all 36 possible pairs: P pair values are injective and do not meet E. Counting P active coordinates gives

`Σ_x k(x)=56`, `Σ_x C(k(x),2)=35`, `|P|=26`,

where k(x) is the number of coordinates of P word x inside their corresponding E alphabets. Hence `n_0+n_3+3n_4=5`, with n_j the number of P words of active count j.

Every A fiber has at least four E entries and there are five A values; therefore each fiber has exactly four. Because each occurring pair has exactly two E extensions, every other coordinate takes exactly two values, each twice, in each A fiber. In particular each A symbol has residual partner degree 2 toward any other party and occurs in exactly four P words. Summed over the five A symbols, there are 20 A-active P words. The active/active P pair counts involving A are 5 for AB, 10 for AC and 10 for AD, totaling 25. If `s_A,T_A,Q_A` denote respectively the numbers of P singleton-, triple-, and quadruple-active words containing A, then

`T_A+2Q_A=s_A+5`.

But `T_A≤n_3`, `Q_A≤n_4`, and `n_3+2n_4≤n_0+n_3+3n_4=5`. Equality throughout gives `n_0=n_4=0`, `n_3=5`, every triple contains A, and no singleton contains A. The original counts then give `n_1=1`, `n_2=20`.

For an active symbol a at any party i, let `d_i(a)` be its number of E-partner values at another party. This is independent of which partner is chosen: P occupies exactly the other `6−d_i(a)` pair values, and P words using a are pair-injective. Each degree is at least two, as a one-degree E fiber could vary in no other coordinate. Degrees at party i sum to n=10.

At B, partner alphabets C,D have size 4, so its three degrees are either `(2,4,4)` or `(3,3,4)`. At each of C,D, the partner B has only three values, so its four degrees are necessarily `(2,2,3,3)`. For an active symbol at B, the number of singleton-active P words using it minus the number of triple-active P words using it is

`(6−d)−[(5−d)+(4−d)+(4−d)] = 2d−7`.

There is only one singleton-active P word overall. The degree sequence `(2,4,4)` would require at least one singleton on each of two distinct degree-4 symbols, so it is impossible. Thus B has degrees `(3,3,4)`.

Relabel B's degree-3 symbols as 0,1 and its degree-4 symbol as 2. Its five A-fiber two-sets are exactly `{0,1}` once, `{0,2}` twice, `{1,2}` twice. Relabel A's five symbols to put them in the order

`B = (01,02,02,12,12)`.                                            (3)

Relabel the degree-2 C symbols as 0,1 and the degree-3 C symbols as 2,3, and similarly for D. The residual BC and BD projections each have ten of the twelve possible pairs. Their two missing pairs form a perfect matching between B's two degree-3 symbols and the other coordinate's two degree-2 symbols. Independently swap C's and D's two low labels so that both missing matchings are

`{(0,0),(1,1)}`.                                                    (4)

The C and D alphabets and degree patterns are identical. A party swap preserves the problem and the normalization above, so their five-row incidence patterns may be ordered `C≤D` lexicographically without loss of generality.

## 2. Exhaustive balanced-fiber enumeration

Under this normal form, each of C and D has one of 310 sequences of five 2-element row sets with symbol occurrence counts `(2,2,3,3)`. There are `310·311/2=48,205` ordered choices with C≤D. For each A fiber, E is a four-point subset of its B×C×D binary cube, with every local value occurring twice. There are exactly eight such subsets: two parity subsets, and two cylinders for each of the three possible correlated coordinate pairs. Equivalently, the direct checker enumerates all four-element cube subsets and filters the exact balance condition.

The independent source programs below exhaust these finite choices, discard any fiber containing one of the forced missing BC or BD pairs (4), require all six pair projections to have exactly ten values of multiplicity two, and then check the necessary unitary condition that no two distinct rows or columns in any cut intersect in exactly one nonzero position.

- The **direct set/count implementation** constructs 2,827,560 balanced support combinations from 10,116 incidence-pattern pairs with allowed fibers. Exactly 76 satisfy all six projection/multiplicity conditions. Its executed final assertion requires zero survivors of the no-unique-overlap test. Its JSON lists the 76 count and a surviving support with an explicit unique-overlap witness; its Counter serialization does not separately emit a zero-valued survivor key.
- The **independent parity/cylinder implementation** first computes F₂ rectangle-parity-compatible masks, then generates balanced fibers using explicit binary parity and cylinder formulas rather than four-subset enumeration. It finds 12 parity forms with allowed fibers, constructs 324 supports, and finds the same 76 projection-valid supports. For **every one** it detects a unique row overlap in each of the AC|BD and AD|BC cuts. Its receipt explicitly records `both_AC_and_AD_unique_overlap=76`. Of the 76, 72 have full-fiber count pattern `(5,5,0)` and four have `(3,3,4)`.

A unitary cannot contain two rows with exactly one common nonzero column, since their inner product would have precisely one nonzero summand. Hence every one of the complete normal-form supports is impossible, excluding the `(3,4,4,5)` profile conditional on the exact enumeration and its normal-form proof. The possible free-coordinate cases are included in both programs; they are not discarded by an unverified completion argument.

## 3. Pinned checker evidence and exact remaining scope

Direct checker `frontier-20261028-n46-profile3445-direct-v1.py`, SHA-256 `f0045977266a8da6d0ce8eb37d1f9065350a074752357c41b64dca7cda52f7cb`; receipt `frontier-20261028-n46-profile3445-direct-v1.json`, SHA-256 `eb9e8ea9f843f29d37ed169c0d06ac6abad6ff3ee2bf2a2976b5ce6cf792498a`.

Independent parity checker `frontier-20261028-n46-profile3445-parity-v1.py`, SHA-256 `84465e5888969decddb32ec97ddadebbc3d44909f80170bfa4f025d3cc254f94`; receipt `frontier-20261028-n46-profile3445-parity-v1.json`, SHA-256 `687ee6360186d59a405d388847057151d19755525a6c8c1daf617de1b21ba0d1`.

Both are same-harness implementations. Review should reconstruct the degree/phase-free normal form, both forced matching relabelings, C/D swap symmetry, enumeration completeness, and the independently checked unique-overlap witnesses. No probability, finite-field, or numerical threshold is used. These finite checks are not a formal proof or a substitute for independent scientific review.

Combined with the four other candidate profile exclusions in the pinned N=46 partial packet, this would leave `(3,4,5,5)`, `(4,4,4,4)`, `(4,4,4,5)`, `(4,4,5,5)`, `(4,5,5,5)` unresolved. No claim is made about their feasibility, a 46-term AME witness, or a global lower bound 47.
