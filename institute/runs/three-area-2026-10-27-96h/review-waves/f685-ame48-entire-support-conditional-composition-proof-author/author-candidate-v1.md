# Prospective author candidate: conditional entire support-48 exclusion

**Status.** This is a new, unadopted author proof of a conditional composition, not a parent disposition or an unconditional, source-free all-support-48 proof. Its explicit mathematical inputs are the adopted alphabet and entire fixed-profile results in S1, the t=28 theorem in S4, and the global maximal-count chain recorded in S6, with the exact premises and limitations stated below. The t=27 exclusion and the count reduction are independently reconstructed below from complex unitarity. The disposition may instead import the same full t=27 conclusion literally from S7. No scientific executable was run by this child.

## 1. One caller, quantities and assertion

Let `psi` be any normalized **complex** AME(4,6) pure state: every two-party reduced density matrix is `I_36/36`. Fix **one arbitrary product orthonormal basis** for its four parties, and write `psi_abcd` in that basis. Put `U=6 psi`. The three flattenings `AB|CD`, `AC|BD`, `AD|BC` of this **same** four-index array are unitary 36 by 36 matrices. Thus each `|U_abcd| <= 1`. Define

* `N = #{abcd: U_abcd != 0}`;
* `P = {abcd: |U_abcd|=1}`, `t=|P|`;
* `E = {abcd: 0<|U_abcd|<1}`, so `N=t+|E|`.

These definitions, the chosen basis, all pair projections, all three unitaries, and the single integer `t` refer to the very same `psi` and `U`. No local rechoice of basis between cuts or branches, phase convention, reality, or equal-modulus condition on `E` is used.

**Conditional theorem.** For every such `psi` and every such product basis, the exact mathematical imports I-A, I-P, I-28 and I-G below imply `N != 48`. In particular the imported global bound I-G is not proved from scratch here. At the separately stated f113/prior-`t<=30` and classical no-OLS provenance, and at the stated f296/f293 alphabet and six-profile provenance, this gives the desired entire-support-48 exclusion. It does not imply a support lower bound of 49.

A slightly more local version assumes only `t<=28` for the caller being contradicted, together with I-A, I-P and I-28; then the same argument excludes its `N=48`. This local hypothesis is a weakening of the global bound, not a replacement for the global provenance required to assert the result for **all** callers.

## 2. Literal imported statements and their boundaries

The following are inputs, not new proofs of the linked underlying source chains. Source identifiers, whole-file hashes and complete-body coverage are listed in Section 8. No referenced link, historical held output, or original author source was followed.

**I-A: conditional alphabet interface, S1 and S5.** S1 states, for the actual `N=48, t=24` tensor and `q_i` equal to the cardinality of the `i`th projection of its actual `E`: “The separately adopted [f296/f293 no-distance-one and no-six-symbol composition] gives `q_i∈{3,4,5}` under **no-OLS(6)**.” S5 specifies the AME-scoped imported conclusion as “noH and noZ at N48,t24, conditional on no-OLS(6),” where `H` means a distance-one pair in the actual `E` and `Z` means a residual party using all six symbols. This is not an unrestricted P2 selection lemma. We do not independently reauthenticate the classical source or the full f296/f293 original chains. `no-OLS(6)` means there do not exist two orthogonal Latin squares of order six: each square has every symbol once in each row and column, and all 36 ordered pairs formed by overlaying the squares would have to be distinct. It is a classical external import, not a consequence proved here.

**I-P: six entire fixed-profile exclusions, S1.** At `N=48,t=24`, with `P,E` from the same actual complex `U` as above, S1 states: “Each corresponding adopted theorem excludes its ENTIRE fixed profile for the same actual U/P/E and arbitrary nonzero complex residual amplitudes, up to physical party permutation where applicable.” The listed sorted residual alphabet-size profiles are exactly `3555, 4444, 4445, 4455, 4555, 5555`. These six full-profile conclusions are imported as universal assertions, not as sampled graphs or individually constructed tensors. S1 explicitly says the six profile theorems themselves do not require no-OLS; the exhaustive alphabet interface I-A still does. S1 also states the complete consequence literally: “Conditional on the named classical no-OLS(6) import and the adopted f296/f293 AME-scoped alphabet interface, there is no normalized complex AME(4,6) state in any product basis with exactly48 nonzero coefficients of which exactly24 have modulus1/6.” Section 5 independently checks the composition of I-A with the six imported whole-profile assertions; it does not reprove those six underlying assertions.

**I-28: entire `t=28` theorem, S4.** Its literal conclusion is: “No normalized complex AME(4,6) tensor in any product basis has exactly48 nonzero coefficients, exactly28 of modulus1/6.” S4 says this is a same-complex-tensor theorem for arbitrary residual complex amplitudes; it uses neither no-OLS nor f113/prior-maximal-count, the t=24/t=27 adoptions, a fixed phase, reality, nor an equal-residual-modulus assumption. We import this entire theorem, not a partial support graph or its local finite controls. We do not pretend to reconstruct its complete alphabet case proof in this composition. In particular, S9's q3 correction applies to any use of the supporting argument, as noted below.

**I-G: global maximal-count boundary, S6.** S6 item 3 states literally: “f113 gives `t≤29` and [the no-exactly-29 disposition] (self-contained) excludes `t=29` for any support; hence every normalized complex AME(4,6) state in every product basis has at most 28 coefficients of modulus `1/6`. Conditional on the f113 provenance only.” S6 declares that provenance as the classical `no-OLS(6)` theorem **and the prior global `t≤30` boundary**. Accordingly the input is the universal `t<=28` assertion at those retained premises, with the f113 `t<=29` step and the separately self-contained no-exactly-29 step both visible. Neither the earlier global `t<=30` bound nor the original f113 chain is independently reconstructed or source-authenticated here. The ordinary unitarity bound `t<=36` does not replace I-G.

For reference, S7 states the t=27 assertion literally: “No normalized complex AME(4,6) state in ANY product basis has exactly48 nonzero coefficients, of which exactly27 have modulus1/6. All amplitudes, choices of product basis and all three paired flattenings refer to the SAME tensor. No reality, equal-residual-modulus or phase restriction is imposed.” S7 explicitly says this standalone proof has no no-OLS mathematical prerequisite. Section 4 supplies an independent written reconstruction using only elementary unitary-support facts, so no max-count import is needed for that exact-branch proof either.

## 3. Singleton isolation and the excess lemmas

In any of the three unitary flattenings, an entry of modulus one exhausts both its row and column. Therefore the `t` members of `P` have distinct projections on **every** physical pair; no pair value used by `P` is used by `E`. Removing their singleton rows and columns gives a unitary residual matrix of order `n=36-t`, containing `m=N-t` nonzero entries. No residual row or column is a singleton: a singleton in a unitary row or column has modulus one and would belong to `P`. In the support-48 argument I-G gives `n>=8`, so all residual quotients below have nonzero denominators. There are exactly `n` residual values in each physical pair system, each with at least two `E` extensions. Thus

`N-t >= 2(36-t)`, i.e. `t >= 72-N`.

For `N=48` this gives `t>=24`; it is an elementary lower bound on **maximal-entry count**, not a lower bound on support.

For later use we prove the small-excess facts directly. The support of a square unitary decomposes into connected bipartite row/column components. Each component is square: orthonormal rows give `#rows <= #columns`, and orthonormal columns give the reverse. For a component of order `r` with `m_c` nonzeros, put `e=m_c-2r`. Its minimum line degree is at least two, hence `e>=0`.

Two distinct unitary rows cannot overlap in exactly one nonzero position, since the single nonzero summand in their inner product cannot vanish; the same is true of columns. In a positive-excess component, call a degree-two row low and another row high. Low-row supports are two-element column sets. Two such sets are disjoint or identical. If two low rows have the same pair, their complete 2-by-2 row submatrix is unitary; it exhausts both columns and forms its own isolated 2-by-2 component. Thus in a positive-excess component all low-row pairs are disjoint. Any high row that meets a low pair meets both its columns. Each low pair is met by at least two high rows: zero would leave its two columns with exactly one common nonzero; with exactly one, those two columns form a complete 2-by-2 unitary on the low and high rows, exhausting that supposedly high row. This proves the assertion without assuming real entries.

Now classify the excess needed here.

* `e=0`: every line has degree two. A low row and any row meeting it have the same two columns, and the columns have no further neighbors; each component is a full 2-by-2 block.
* `e=1`: there is one high row of degree three. No low pair can be met by two high rows, so there are no low rows; a one-row component cannot have degree three. Thus excess one is impossible.
* `e=2`: either there is one high row of degree four, impossible by the same argument, or there are two high rows of degree three. Each low pair must be met by both, and either degree-three row can meet at most one disjoint low pair. Consequently the component has at most three rows; its degree-three rows force order three. It is a 3-by-3 block with exactly one missing entry and eight nonzeros.
* `e=3`: with one high row it has degree five and there can be no low row; with two, their degrees are four and three and every low pair meets both, so the degree-three row permits at most one low pair and the order is at most three, incompatible with degree four. With three high rows all have degree three, each meets at most one low pair, and each low pair requires two high rows; hence there is at most one low row. If there is one, the order is four. Each high row must meet the low pair, because the other two columns alone cannot provide degree three. The three high rows then supply only three incidences to those two other columns, which require at least four. Hence there is no low row, the order is three, and the component is the full 3-by-3 block.

For `N=48`, total residual excess is

`e_total = (48-t)-2(36-t) = t-24`.

If `t=25`, total excess one is impossible. If `t=26`, total excess two consists of one eight-entry 3-by-3 component and zero-excess 2-by-2 components, so the residual order is odd, but `36-26=10` is even. If `t=27`, the only positive component has excess three and is a full 3-by-3, and the other six residual rows form three 2-by-2 blocks. This holds in every cut of the same `U`. Consequently the only values left between the independently established lower bound and imported `t<=28` are exactly

`t in {24,27,28}`.

This also checks the S5 count restriction at the same upper-bound boundary; it does not use that restriction to assume a state exists.

## 4. Written reconstruction of the entire t=27 exclusion

Assume `N=48,t=27`. In each pair system the nine residual pair values consist of three values with three `E` extensions and six values with two. Denote the three high values in physical pair `ij` by `H_ij`. The full 3-by-3 core in cut `ij|kl` is exactly the Cartesian set `H_ij x H_kl`; an `E` word is high on one of those complementary pairs if and only if it is high on the other.

For a symbol `a` at party `i`, let `p_i(a)` be the number of `P` words using it, `d_i^j(a)` the number of residual `ij` pair values containing it, and `s_i(a)` the number of `E` words using it. For each `j != i`, all six partner values are partitioned between the injective `P` projection and the residual projection, so `d_i^j(a)=6-p_i(a)`, independent of `j`; call it `d_i(a)`. Let `h_i^j(a)` be the number of `H_ij` values containing `a`. Counting `E` extensions gives

`s_i(a) = 2 d_i(a) + h_i^j(a)`.

Thus `h_i^j(a)=h_i(a)` is independent of `j`, nonnegative, and `sum_a h_i(a)=3` for each party.

For distinct parties `i,k`, choose a cut `ij|kl` in which they are on opposite sides. Its Cartesian high core contains `h_i(a) h_k(c)` different `E` words with fixed coordinates `(i,k)=(a,c)`. Every residual pair value has at most three extensions, so `h_i(a) h_k(c)<=3`. Hence two different parties cannot both have a symbol of high marginal at least two.

Suppose one party `A` has a symbol `a` with `h_A(a)>=2`. All three other parties then have only zero/one high marginals. Choose a high neighbor `b` of `a` in `H_AB`; `b` has a unique neighbor `d` in `H_BD`. Choose two distinct high neighbors `c1,c2` of `a` in `H_AC`. The full `AC|BD` core contains both `(a,b,c1,d)` and `(a,b,c2,d)`. Because `(a,b)` is high, the complementary `AB|CD` core makes both `(c1,d)` and `(c2,d)` high in `H_CD`. This contradicts `h_D(d)<=1`.

Therefore every high marginal is zero or one. Each party has exactly three high symbols, and every `H_ij` is a perfect matching on the respective high alphabets. Crossed full cores produce every one of the nine pairs of high symbols in any pair of parties. These are all nine residual pair values. Thus for every high symbol `a`, `d_i(a)=3`, and `p_i(a)=3`. The four parties have `4*3*3=36` incidences of high symbols among their `P` words. Yet no `P` word can use high symbols at two parties: that pair value is already residual. The 27 `P` words can therefore contribute at most 27 incidences, a contradiction. This argument is universal and uses no no-OLS or global bound.

## 5. Independent dispatch of the entire t=24 profile family

Assume `N=48,t=24`. Then `n=12,m=24` and total excess zero. In every cut the residual matrix is six full 2-by-2 blocks. Every residual pair value has exactly two `E` extensions; the 12 residual pair values and 24 injective `P` pair values partition all 36 possible values. Let `S_i=projection_i(E)`, `q_i=|S_i|`. I-A gives `q_i in {3,4,5}` for all four parties under the stated no-OLS/f296/f293 interface. No extra no-distance-one hypothesis is introduced into any fixed-profile theorem.

For a word `w in P`, let `k(w)` count its coordinates that lie in their corresponding `S_i`. Put

`C = sum_{w in P} k(w)`, and `M = sum_{w in P} binom(k(w),2)`.

For each party `i`, the number of `P` incidences in `S_i` is `6 q_i-12`: among the `6 q_i` pair values based at `S_i`, precisely 12 are residual and every other value belongs to one `P` word. Similarly, for each `i<j`, precisely `q_i q_j-12` `P` pair values lie in `S_i x S_j`. Hence

`C = 6 sum_i q_i - 48`,

`M = sum_{i<j} q_i q_j - 72`.

For `0<=k<=4`, both `binom(k,2)>=k-1` and `binom(k,2)>=2k-3`; consequently `M>=C-24` and `M>=2C-72`. Two `q_i=3` are impossible because their 3-by-3 box cannot contain the 12 distinct residual pair values. Sorting the remaining possibilities with one 3 gives:

| profile | C | M | violated condition |
|---|---:|---:|---|
| 3444 | 42 | 12 | `12 < 42-24` |
| 3445 | 48 | 23 | `23 < 48-24` |
| 3455 | 54 | 35 | `35 < 2*54-72` |
| 3555 | 60 | 48 | none of these inequalities |

The five sorted profiles without a 3 are `4444,4445,4455,4555,5555`. Thus one actual `E` determines exactly one of the six profiles in I-P, up to physical party permutation, and its corresponding whole-profile exclusion contradicts the same actual tensor. This establishes the entire conditional `t=24` branch from I-A and I-P, without using I-G, f113, or a separate six-word selection lemma.

## 6. t=28 import and compatibility checks

At `N=48,t=28`, I-28 applies directly to this caller and the same basis and excludes the entire branch. Its source's self-contained written proof is a distinct imported result, not reproduced by our simple counting. In particular it is **not** replaced by the existence or infeasibility of independent pair graphs. Its exact phase-general, simultaneous-unitary scope is essential.

The normalizations and residual counts at every relevant value are mutually consistent as arithmetic prerequisites, although consistency is not a construction or feasibility proof. Because `sum |U|^2=36` and each `P` entry contributes one, `sum_E |U|^2=36-t`. The table includes the two counts eliminated by Section 3 to make the division and parity boundaries explicit:

| t | residual order `36-t` | `|E|=48-t` | excess `t-24` | mean `|U|^2` on E | total E mass in `psi` |
|---:|---:|---:|---:|---:|---:|
| 24 | 12 | 24 | 0 | 1/2 | 1/3 |
| 25 | 11 | 23 | 1 | 11/23 | 11/36 |
| 26 | 10 | 22 | 2 | 5/11 | 5/18 |
| 27 | 9 | 21 | 3 | 3/7 | 1/4 |
| 28 | 8 | 20 | 4 | 2/5 | 2/9 |

The mean is an average only: it imposes no equality among residual moduli. In `psi`, every squared modulus and every average above for `U` is divided by 36, and the `P` contribution is `t/36`; the two masses sum to one. For t=24 the 12 pair multiplicities `2` sum to 24. For t=27, `3+3+3+2+2+2+2+2+2=21`. For t=28, each of the two S4 residual multiplicity types `D=(3,3,3,3,2,2,2,2)` and `Q=(4,4,2,2,2,2,2,2)` has eight values summing to 20, in agreement with the same tensor's `|E|`; this necessary arithmetic is not a classification proof.

S4's t=28 notation has, for each residual symbol `x` at party `i`, partner degree `d_i(x)`, occurrence count `s_i(x)`, and `h_i(x)=s_i(x)-2d_i(x)`. Its stated `sum d_i=8` and `sum h_i=4` agree with `sum s_i=20`. The t=24 alphabet `q_i in {3,4,5}` and the separately derived t=28 alphabet `q_i in {3,4}` concern different mutually exclusive values of the **same** `t`; they are not constraints to intersect on one branch. S9 corrects the t=28 supporting case argument: for a general q3 party, `sum d=8` and `d>=2` permit both `(2,3,3)` and `(2,2,4)`. The unique degree-two star is justified in the 3344 profile, not in general 3444; the latter needs only existence of a degree-two symbol. No contrary uniqueness premise is used here.

One quotient in the imported t=28 proof can be checked directly. Suppose two symbols at each party define a binary subarray such that **all four** values of every physical pair occur there and **all** their actual `E` extensions are inside the subarray. No `P` word can use those pair values. For each of the three cuts the four binary rows are therefore supported entirely on the four binary columns; their orthonormality makes that 4-by-4 block unitary. The same subarray in all three cuts, divided by 2, is normalized and would have every two-qubit marginal `I_4/4`. The divisor is 2, not 6: a 4-by-4 unitary has squared-entry sum 4. Such a four-qubit state is impossible. Indeed its three-qubit marginal has the Pauli expansion `rho=(I+M)/8` with `M` containing only weight-three Pauli strings, and its nonzero eigenvalues are `(1/2,1/2)`, so `rho^2=rho/2`, i.e. `M^2=3I+2M`. A pair of weight-three Pauli strings either anticommutes, agrees everywhere, or differs in exactly two positions and has product of weight two; hence the weight-three part of `M^2` is zero. Comparing weight-three parts forces `M=0`, contradicting `M^2=3I`. This checks a necessary block consumer only; pair occupancy without exhaustion in all six projections would not justify it and this check is not the complete I-28 proof.

## 7. Composition, historical wording and nonclaims

Suppose one caller has `N=48`. I-G gives `t<=28`; Section 3 gives `t in {24,27,28}`. Section 5 excludes 24 at I-A/I-P's stated classical and alphabet provenance; Section 4 excludes 27 by standalone complex-unitary reasoning; I-28 excludes 28 as an entire same-tensor theorem. These three alternatives exhaust one integer belonging to the one caller, giving the conditional contradiction. Since the caller and product basis were arbitrary, the quantified conditional theorem in Section 1 follows.

S1's `t=28`-only conclusion was a **necessary implication**, not an existence assertion, and its ending saying the branch was open was a historical statement before S4. S7's older wording that 24 and 28 had not then been excluded is likewise historical. S4 subsequently supplies the exact entire t=28 exclusion; neither later adoption retroactively changes those old documents or makes their historical statements logical contradictions.

No support-45 or support-46 exclusion follows from I-G, from the present no-48 conclusion, or from the separate conditional no-47 record. Therefore even combining no 47 with this no 48 does **not** establish `N>=49` or the minimum. No Boolean witness, explicit AME tensor, support-45/46 feasibility, global minimum, source identity, novelty, priority, human check, independent-model-family check, or formal/kernel verification is claimed. The no-OLS theorem, f296/f293 interface, six entire-profile theorems, f113 plus its prior global `t<=30` boundary, and S4's complete t=28 theorem remain the explicit imported proof obligations; the current composition does not launder them into a source-free proof.

S2 corrects S1's claim that the parent had read every source before its disposition: the parent read the previously omitted maximal-count source only afterwards. S3 retains **one parent PROCESS MAJOR**, not a backdated complete read and not by itself a mathematical refutation. S7 retains the f316 ACK fault: a file-write attempt was refused, and packet reading and derivation preceded the first successful direct message; it was not a timely ACK. S4/S8 retain **one f682 author source-provenance PROCESS MAJOR** for an in-place mathematical proof edit; the initial write was recovered later, not contemporaneously hashed. It is not recast as an additive edit and is not automatically a mathematical hold. S9's q3 correction is retained as above, not treated as an automatic mathematical hold. S4 reports a separate parent-run finite corroboration of local primitives only, not a global enumeration or child run. These qualifications neither authenticate uninspected source chains nor certify cognitive isolation.

## 8. Input bindings, chronology and assurance

The complete frozen packet, SHA-256 `1c6f94d350a4846ed47e33bb9ef347315c345d021d43431725720d310be9f7bc`, rendered the following complete bodies; all SHA values below are the frozen whole-source bindings, not claims that underlying linked records were opened:

| ID | Complete source basename | SHA-256 |
|---|---|---|
| S1 | `physics-6-ame48-conditional-entire-t24-exclusion-and-t28-only-residual-parent-v1.md` | `5a9e9128b964051bd667f04fc05ad8b289f1034992422a4666bc76e681fc9880` |
| S2 | `physics-6-ame48-conditional-entire-t24-exclusion-and-t28-only-residual-parent-v1-erratum-1.md` | `cb94f545d8497bff4cabfe8454decacd68c95534c4270820d0628fc10ca03ade` |
| S3 | `physics-6-ame48-conditional-entire-t24-exclusion-and-t28-only-residual-parent-v1-erratum-2.md` | `fcd489d9c04a5c9520159519d7f3c0cae14830e8d356a077ddfcb13f0bb9a918` |
| S4 | `physics-6-ame48-t28-entire-same-complex-tensor-exclusion-parent-v1.md` | `25c34705825561d501701a26b50c08a7b734bf2282f72f3283568c8cb459f968` |
| S5 | `physics-6-support48-maximal-count-24-27-28-and-distance-interface-parent-v1.md` | `2af4fde719fbee23fa740160792e152945bd6e352e9006a77f7817c1949fe9aa` |
| S6 | `physics-6-ame46-support-47-excluded-and-at-most-28-maximal-coefficients-composition-parent-v1.md` | `4101ae2cdb08aa2c9238b680359dc2793bcccfc3af672fbb92be9dd460a41003` |
| S7 | `physics-6-ame46-support48-t27-universal-exclusion-parent-v1.md` | `fa3e4f124b17621ec7e9be91df0c6f1073f47fd91151be2e9b146c9ed577a4a2` |
| S8 | `parent-native-write-edit-provenance-verification-v1.json` | `f6b3afbd63d6771a2483fbc8b83bdfc2c5913f6d5e475b9511ea88146ca0687d` |
| S9 | `parent-q3-degree-qualification-for-f683-f684-v1.md` | `e1c391362ad0d0493f1189753279706f61590fc52adacca803bd754960763ab2` |

Before packet body access this child read the manifest, freeze receipt, prepared parent metadata, actual dispatch receipt, and all 20 listed controls through their endings; native SHA-256 checks matched the assigned manifest and freeze hashes. It sent Main a direct prebody acknowledgement, then read packet LF 1–251 in order, in raw slices of at most 20 LF; the packet SHA was subsequently checked natively. The general memory summary and written-math protocol were read as administrative context, not as scientific premises. Written reasoning followed the complete packet. No linked source, old author code, sibling proof, held episode or its consumers was used. These observable steps are not an independence or clean-cognition certificate.

The packet-hash/native-clock observation was `2026-10-30T16:22:59-0700 PDT`; a further native clock before this final write was `2026-10-30T16:24:49-0700 PDT`. Apart from ordinary metadata hashing/counts and clock observations, no scientific program, local experiment, test, build, lint, solver, external CLI, package installation, or remote/paid job was run by this child. The algebra above is written proof, not numerical evidence; there is no calculation code or experimental result to report. This new file is created with its final bytes in one write. Any parent mathematical review, independent verification, corrections and adoption are separate future acts.
