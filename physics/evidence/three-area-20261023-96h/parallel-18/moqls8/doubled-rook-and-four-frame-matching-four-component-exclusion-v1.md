# ANY at-least-THREE-net — doubled-rook / four-frame-matching C4 stratum excluded

**PhysicsMOQLS8-2. NEW WRITTEN AUTHOR CANDIDATE**, no independent/parent/formal/executable/novelty acceptance. Actual precreation clock bound **2026-10-26T07:37:25-0700 PDT**. New per-stratum proof, not an expansion of an old C4NET or accepted C2 theorem.

## 1. Exact all-object stratum and applications

N is ANY actual order8 net with at least THREE classes. Q is arbitrary complex C8, ONB on EVERY actual N-line. Suppose one intrinsic dimension4 component V has EXACTLY SIXTEEN distinct rays, EACH of GLOBAL multiplicity2. Either of the following additional EXACT structural hypotheses is impossible:

**R (doubled-rook):** the rays can be indexed(i,j),1<=i,j<=4, with distinct rays orthogonal IFF they have the same i or the same j.

**F (four-frame matching):** the sixteen rays are partitioned into FOUR ONBs E_1,...,E_4 of V, and between EVERY two of these bases each ray is orthogonal to EXACTLY ONE ray of the other basis. The matchings need not initially be consistent, affine, real or standard.

We prove F reduces to R under the actual line conditions and then prove R impossible. These are ENTIRE explicitly named strata, not claims that every dimension4 component has this form. Additional orthogonalities, different multiplicities, overlapping frame partitions or a missing four-ONB partition remain OUTSIDE scope.

An original FOUR-family with TWO classical members supplies FOUR net classes; with ONE classical member it supplies THREE. The theorem therefore applies directly to the selected Q in either case, without using its other quantum companions. It also applies at the q1 FIVE-net interface. A standalone QLS with only its two row/column classes is NOT covered and need not satisfy the obstruction.

## 2. Physical component incidence — no abstract graph replaces the actual net

The component has32 actual cells, two copies of each ray. Every N-line contains EXACTLY FOUR component entries, an ONB of V. Different net classes share at most one component cell, since their full lines intersect once. We use these actual four-entry component subsets throughout.

Under R, each actual line's four rays form a4-clique in the4-by4 rook graph, hence are ALL of one ray row E_i OR ALL of one ray column F_j. Indeed if a clique uses two different row indices they must share a column; every additional clique vertex must share that same column. A4-clique confined to one row or column contains all its four distinct rays.

Call these row-type and column-type COMPONENT lines. Their full N-lines still have four other component-external cells, but any intersection of the component lines is at most one; no stronger unwritten full-board extension is assumed.

## 3. Each parallel class is pure-row, pure-column or mixed in a forced exact way

For one actual class alpha let r_i count its row-type lines in ray row i, and c_j its column-type lines in ray column j. At a ray(i,j), both of its actual cell copies are covered exactly once by the class partition. Each counted line contributes one occurrence there, so

    r_i+c_j=2       for EVERY i,j.

Therefore all r_i have one common value R_alpha and all c_j have value2-R_alpha. Only THREE types are possible:

- R_alpha2: two row-type lines in EACH of four ray rows, no column lines (pure-row);
- R_alpha0: two column-type lines in EACH ray column, no row lines (pure-column);
- R_alpha1: ONE row-type line in EACH ray row and ONE column-type line in EACH ray column (mixed).

This conclusion is forced by original coverage of the two cell copies, not assumed as a uniform line-type convention.

## 4. A pure class permits at most ONE other class

Suppose alpha is pure-row. In a fixed ray row its eight cells are partitioned by alpha's TWO four-cell component lines. Any row-type component line from another class beta has four cells in that same eight-cell set. Each intersection with either alpha line is at most ONE, so it could have at most TWO cells, a contradiction.

Thus EVERY other class beta must have NO row-type line, hence must be pure-column by §3. There cannot be TWO such pure-column classes: the identical argument in a fixed ray column rules out a column-type line against the two-line partition of the other class. Therefore the TOTAL number of classes is at most TWO. Pure-column as the initial class is symmetric.

No line intersection is silently assumed to be inside V; only the valid at-most-one component intersection is used.

## 5. THREE mixed classes contradict a complete binary distance count

If at least THREE classes exist and there is no pure class, choose three MIXED classes alpha,beta,gamma. Fix ONE ray row i. Its eight actual cells are two copies of each of four rays(i,j). Label those copies0/1 arbitrarily once. Each mixed class has ONE row-type component line there, selecting one copy at every j. Let the three resulting binary words of length4 be f_alpha,f_beta,f_gamma.

Two such actual lines from different classes meet in at most one cell, so their words agree in at most ONE position. Each pair has Hamming distance>=3. Hence the sum of their THREE pairwise distances is>=9.

At each binary position three bits contribute either ZERO pairwise disagreements (all equal) or EXACTLY TWO (not all equal). Four positions therefore contribute at most8. Contradiction.

This is the ENTIRE finite count, not an executed code enumeration or unproved maximum-code table. Together with §4 it proves that a doubled-rook component admits at most TWO such resolutions. Since the original net has at least THREE, hypothesis R is impossible.

## 6. ALL four-frame perfect matchings force the doubled-rook form

Now assume F, with four disjoint ONBs E_i of four rays. Within one E_i all rays are orthogonal; between two E_i,E_j the orthogonalities are exactly a perfect matching.

Any actual4-ONB line using TWO rays of one E_i cannot use ANY ray of a different E_j, since the latter is orthogonal to only ONE ray of E_i. It is therefore the whole E_i. Otherwise its four rays contain at most one from each group, hence EXACTLY one from EACH E_i; call it a transversal4-clique.

A vertex belongs to AT MOST ONE transversal4-clique, because its matched neighbor in every other group is unique. Suppose a ray v belongs to NO such transversal. Every actual net-line through either of its two cells would then use the SAME basis E_i. Fix one occurrence x and a second ray w in E_i. At least THREE different classes through x would each give one w occurrence, and those occurrences must be DISTINCT by actual net incidence. But w has only TWO global cells. Contradiction.

Therefore EVERY ray belongs to a transversal4-clique. Uniqueness makes these cliques a partition of all sixteen rays into FOUR disjoint alternate ONBs F_j. Each E_i meets each F_j in one ray. The original perfect-matchings condition ensures the ONLY orthogonalities between E groups are their shared F_j columns. Thus the whole orthogonality graph is EXACTLY the rook graph indexed by(E_i,F_j).

We have derived hypothesis R from F using original line multiplicities, without assuming an arbitrary abstract matching system is automatically realizable or that the bases were actual net classes in advance. Sections3–5 now exclude F as well.

## 7. New progress scope, remaining C4 gap and old C4NET distinction

The proof excludes an ENTIRE all-complex, all-net stratum with16 rays of multiplicity2 and the exact doubled-rook/four-frame matching structure. It may be useful at a sharp C4 ray/orthogonality-degree boundary, but NO theorem is proved here that all remaining q2 C4 components reach that boundary or possess the supplied four-frame partition. Dense/extra orthogonalities, different ray counts and actual phase-compatible higher-component configurations remain OPEN.

The retained parent source `RUN/wave-v16-written-frontiers-parent-v1.md` §§59–67 was actually freshly read. Its C4NET theorem requires THREE complex assignments on the four-net, ALL pair-product equations and original four unrestricted mates; its F>=7 consequence requires ALL THREE nonclassical. Those hypotheses belong to the old FIVE-family route, NOT the current q2 two-quantum four-family problem. It is NOT imported or weakened here. This new graph/copy/intersection/distance argument is self-contained and uses no C4NET heavy-support conclusion, degree3 classification, native/GB result or catalogue.

The unrestricted q2 higher4–8 coupled problem, q3/q4 outside this exact stratum, affine q1 r7/Fano-flag and8/no-fixed problems, nonaffine source bridges, numerical M(8), A10GB15/18/threeUNKNOWNs/A11 and finite-object/family/priority gates remain OPEN/unperformed. No maximum3, whole-family classicality or stronger numerical result follows.

## 8. Assurance and permanent process

All graph/cell/ray/intersection/binary identities are exact WRITTEN, not machine-checked. NO scientific interpreter/calculator/eval/CAS/program/enumeration/solver/replay/CLI/nestedagent/newGO/privatefloat/decimal gloss/numeric parameter trial. Only metadata date/hash/LF and readonly sources. Generic rook-clique/copy-count/Plotkin-type distance arguments are PRIOR mathematics; exact theorem priority/novelty remains UNCLEARED.

Fresh ENTIRE mathematical AND dependency/application reconstruction is required before promotion; old C4NET/C2/five-family verdicts are not transferred. No formal/kernel/human/configured-family/executable/mutation/replay/novelty acceptance or numerical-ledger change. All own currentv112/visiblev105/v107/v109 intake read-order PROCESS MAJOR and older findings remain; HELDv3 false ALL-eight-columns/global-light/staircase-only and rejected commutant shortcut remain WITHDRAWN/unused. No historical cure or clean-thought/runtime/trial-free cognition census.

Exclusive owner-root new writes, pinned/shared sources immutable, no git/deletion/publication. Same18/originalprimary/cutoff2026-10-27T11:05:38-07:00/deadline12:35:38/cadence<=30min; no early final-park or96-hour closeout. Original remaining exact written research continues.
