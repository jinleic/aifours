# Uniform QLS(10): global gauge rigidity closes every two-prime phase class except 12/20 families

**NEW WRITTEN AUTHOR CANDIDATE, unreviewed.** Native `/bin/date` before writing: **Wed Oct 28 17:54:13 PDT 2026**. This is an ALL-resolution theorem on the physical uniform M_* branch under a fixed finite root-of-unity coordinate-phase hypothesis. It does NOT assume that general QLS10 are uniform or have root-of-unity coordinates; the unrestricted target remains open. The result requires independent review and novelty assessment.

## 1. Exact statement

Suppose a physical uniform-overlap 1-resolvable QLS(10) exists. Choose any reference row as coordinate ONB. Assume that, after arbitrary per-cell phases and an arbitrary COMMON coordinate-diagonal phase gauge, every nonzero coordinate of every nonreference vector is a q-th root of unity times `1/sqrt(8)`.

**Theorem.** If q has at most TWO distinct prime factors, the only orders not excluded by the arguments here are

`q=2^a 3^b` or `q=2^a 5^b`, with `a>=2, b>=1`.

In particular q must be divisible by12 or20 within that two-prime universe. This includes EVERY choice of L and ALL phase exponents and gauges. It does not claim that the remaining12/20 families work, or exclude q with three or more distinct prime factors, arbitrary non-root phases, or nonuniform arrays.

New ingredient: whenever `q=p^a 7^b`, p!=7, all p-power coordinate phases can be REMOVED GLOBALLY by legal coordinate/cell gauges. The remaining 7-power alphabet is impossible by the previously written and independently checkable seven-term overlap theorem. This closes the factor7/two-prime cases not settled by a bare zero-sum length argument.

## 2. Fixed original-object support and zero-sum identities

As established directly in `frontier-20261028-uniform-phase-obstructions-v1.md` SHA **11ae022040c391e2d4151446a6a88e47ab5feefcb27e5d38815d85e54c4dd945**, choose the reference row basis e_0,...,e_9, indexed by its columns. EVERY nonreference vector has exactly two zero coordinates: its column i and the index j of the reference-row cell in its transversal, i!=j. It has modulus1/sqrt(8) in its other8 coordinates. For EVERY ordered pair i!=j there is exactly one such cell x_ij: the intersection of column i and the transversal through e_j, necessarily outside the reference row.

Any two nonreference cells in a given column share exactly7 nonzero coordinates, because they have the column zero in common and distinct other zeros. They are orthogonal, so the seven relative phases there sum to0. The same holds for any two nonreference cells in a given transversal. These are the SAME physical vectors/partitions for every L; the identification x_ij is by the ACTUAL unique column/transversal intersection, not a free independent phase table.

Separately, the preceding all-L incidence proof shows a nonsharing pair with exactly7 common nonzero coordinates; uniformity requires that seven-term sum to have squared modulus8. This latter condition is used only at the end through the independently written prime-power theorem.

## 3. Seven-term zeros for q=p^a 7^b force one p-component

Use the complete two-prime vanishing-sum decomposition proved in `frontier-20261028-uniform-composite-phase-obstruction-v1.md`, SHA **b69c642590aa1aee9ffe35bf26b9d7cb65768c0f26021bec873e9d02fd50a9bd**; its decisive argument is repeated here.

Let alpha and beta be primitive p^a- and 7^b-th roots, and group a seven-term zero sum by the residues below the respective powers `p^(a−1)` and `7^(b−1)`. In each group form the nonnegative p×7 multiplicity matrix N_ij. The product of the two prime-power cyclotomic power bases is a Q-basis of Q(zeta_q). After eliminating the final alpha and beta powers, the coefficients vanish only if

`N_ij=N_(i,6)+N_(p−1,j)-N_(p−1,6)`.

Choosing a row of minimum last-column multiplicity expresses N_ij as `a_i+b_j` with all a_i,b_j nonnegative integers. Hence the whole seven-term length is `7 A+p B`, where A,B are nonnegative integer sums. Because p!=7, reducing `7=7A+pB` modulo7 gives B≡0 mod7; but pB<=7 and p>=2 imply B<7. Thus B=0 and A=1.

Therefore EXACTLY ONE residue group contributes, its multiplicity matrix has exactly one nonzero row and that row contains each of its seven 7-components once. In particular **all seven summands have the SAME p^a component**. No classification of longer vanishing sums is imported. This statement applies with repetition and all boundary cases included; the length equation itself excludes any other multiplicity pattern.

## 4. Punctured-matrix lemma over ANY abelian group

Let m>=4, and let s_(t,j) take values in an arbitrary additive abelian group for all ordered t!=j. Suppose for every pair of columns j,k, the difference `s_(t,j)-s_(t,k)` is independent of t for all t outside {j,k}. Then there exist row potentials a_t and column potentials b_j with

`s_(t,j)=a_t+b_j` for every t!=j.                                   (4.1)

**Proof.** Fix a reference column j0. For j!=j0 define b_j as the constant difference `s_(t,j)-s_(t,j0)` for t outside {j,j0}, and set b_j0=0. For t!=j0 set a_t=s_(t,j0); then (4.1) holds whenever t,j differ and t!=j0. For t=j0 choose j1!=j0 and set `a_j0=s_(j0,j1)-b_j1`. For any j different from both j0,j1, compare columns j,j1 at t=j0 and at another row outside {j0,j1,j}; m>=4 supplies that row. Their column difference is constant, giving `s_(j0,j)-b_j=a_j0`. All entries are covered. No division, ordering or field characteristic is used. □

## 5. Complete global phase-gauge theorem

Write the p-power exponent at coordinate t of x_ij as `s_(t,i,j)` in the additive cyclic group Z/p^a, for pairwise distinct t,i,j. Per-cell and common-coordinate arbitrary phases from the hypothesis factor out of each block inner product and do not affect this root-component argument.

For fixed column i, any two vectors x_ij and x_ik (j!=k) are orthogonal and have seven common coordinates t outside {i,j,k}. §3 says the p-component of each of the seven relative phase products is the SAME. Therefore the difference `s_(t,i,j)-s_(t,i,k)` is constant in t. Applying §4 to the 9×9 punctured coordinate/zero matrix gives

`s_(t,i,j)=A_i(t)+B_(i,j)` for all distinct t,i,j.                 (5.1)

For fixed transversal j the identical argument gives

`s_(t,i,j)=C_j(t)+D_(i,j)`.                                        (5.2)

Subtract at two coordinates t,u. For any i,j outside {t,u}, i!=j,

`A_i(t)-A_i(u)=C_j(t)-C_j(u)`.                                    (5.3)

There are8 available indices. For any two admissible i, choose an admissible j different from both; (5.3) shows their differences agree. Similarly all admissible j agree. Thus the difference is one common Delta_tu. Choosing an index outside any three distinct t,u,v shows `Delta_tu+Delta_uv=Delta_tv`. Consequently there are global coordinate potentials h(t) with `Delta_tu=h(t)-h(u)`.

For each i, (5.3) then makes `A_i(t)-h(t)` independent of t!=i; write it a_i. Hence

`s_(t,i,j)=h(t)+a_i+B_(i,j)`.                                    (5.4)

Multiplying coordinate t by the inverse p-power phase h(t) and each cell x_ij by the inverse p-power phase `a_i+B_ij` eliminates the p^a component of EVERY nonzero entry simultaneously. These are exactly the permitted common-coordinate and per-cell gauges; they preserve every actual inner product magnitude. The reference basis rays can be rephased back to standard form. All remaining phase factors are 7^b-th roots, not independently chosen replacements.

The prior prime-power theorem, fully proved in `frontier-20261028-uniform-prime-power-phase-obstruction-v1.md` SHA **2b9ac43797a5720e01746dda9f3343c3ea9227f7dcae36f2f1d7c9ddcd7c8467**, says that seven 7^b-th roots cannot have squared sum modulus8. The actual nonsharing pair of §2 demands exactly that. Contradiction. Thus **EVERY** q=p^a7^b, p!=7, is excluded. The argument is over the actual SAME phases/blocks and any cyclic p^a group; finite-field rank alone is not used to infer the group theorem.

## 6. Full two-prime classification and exact checks

- If q is a prime power, the prior seven-term norm lemma excludes it (including every7^b).
- If q has two distinct prime factors and one is7, §5 excludes it.
- If neither is7, the two-prime length theorem excludes all pairs except `{2,3}` and `{2,5}` because7 can then only be `2+2+3` or `2+5`.
- For the remaining q=2*3^b or2*5^b (2-adic exponent1), the exact two-adic norm lemma in the cited composite report excludes them. Indeed `2^(3^(b−1))≡−1 mod3^b` and `2^(2*5^(b−1))≡−1 mod5^b`; each follows by induction from 2≡−1 mod3 or 2²≡−1 mod5 and raising `−1+p^b t` to the p-th power. Its modulo2 reduced-cyclotomic-ring proof then rules out the required squared norm8.

Thus only `2^a3^b` or `2^a5^b` with a>=2,b>=1 survive within at-most-two-prime q. A common multiplier of root order q may be nonminimal, but the theorem still excludes it if that q satisfies an excluded condition.

**Independent finite-rank corroboration of the gauge lemma.** `frontier-20261028-phase-gauge-linear-v1.py` SHA **ef9c4b7d36be9435371323a64a4e23b87a0f7e793529b54980cfbe6b6f9c2f77** builds ALL4320 integer difference constraints on the720 variables s_(t,i,j), and `frontier-20261028-phase-gauge-constraints-v1.txt` has SHA **4bcd1bebf4ab8dfeeccb26474e3ad9cd5921dae90f3df2b0584e0ae715eaa74d**. Independent sparse rank code `frontier-20261028-sparse-modrank-v1.py` SHA **d71202329a1a580edcdf0b68c036bb802d9c22c0b99178bda6112768e72c38f2** reports rank621/kernel99 over EACH of F2,F3,F7. The predicted gauge kernel has10 coordinate plus90 cell potentials minus one common redundancy =99. These finite-field checks corroborate the structure but do NOT replace §§4–5, which work over every cyclic p^a group, including composite modulus/torsion.

The bounded exact single-pair search `frontier-20261028-composite-phase-scan-v1.py` SHA **56a2181f1be221be96fcb57855286ac105929613201c6c25f0c6404bef56e5af**, output `frontier-20261028-composite-phase-scan-result-v1.json` SHA **2d4885897db3ed0da84232fdeb9366475a468290e7c763676ba686867bd40aad**, is NOT used as a proof. For q14 it found separate zero and norm8 seven-root multisets; this is consistent with the theorem: the obstruction is the GLOBAL simultaneous column/transversal gauge compatibility, not either isolated pair condition. The allowed q12 and q20 similarly admit separate single-pair examples; none is a globally glued QLS witness.

## 7. Scope and artifacts

All historical/cross-slot held material remains unvalidated and is not a premise. The two independent earlier written proofs named above are re-used only at their exact current candidate scope; no prior nonuniform/no-go claim is imported. No external model/secret/deletion/publication/infrastructure action. Main must obtain independent scientific review of the two-prime sum lemma, abelian gauge argument and prime-power caller before adoption. The actual 100-ray order-10 target and the unrestricted uniform branch remain OPEN.

**END — only 12/20-type alphabets survive among at-most-two-prime root orders; no unrestricted QLS10 conclusion.**
