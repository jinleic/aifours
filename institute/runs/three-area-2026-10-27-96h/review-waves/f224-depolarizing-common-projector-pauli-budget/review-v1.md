# f224 review: common-projector Pauli budget for four-qubit depolarization

Reviewer: ReviewF224DepolBudget, same harness. Native `/bin/date` observed before writing this review: `2026-10-29T13:54:00-0700 PDT`; it is not an assertion of file-creation time. The target is candidate 186, not its author's checker. The review's SHA-256 is supplied separately after this file is written; a file cannot in general include its own final full hash.

## Verdict and claim-by-claim accounting

**Scope-supported:** the written, same-actual-density/same-actual-complex-rank-three-projector inequality (1), its optimizer and state-dependent criterion, for every physical `p in [0,4/3]`; the stated exact example, the strict all-`Q` conclusions at both `p=2/3` and `p=4/3`, and exclusion from the corrected *named* fixed-`p` `P ∪ U ∪ D_p ∪ H` finite hull. This is not an unrestricted all-density `k3` theorem: the bound can be negative. This is same-harness written review, not human, independent-model-family, formal/kernel, novelty or priority verification.

Finding counts: **0 FATAL / 0 MAJOR / 1 MINOR / 3 INCONCLUSIVE**, with counts attributed to the individual claims below. The three inconclusives concern undefined or unpinned historical labels, not the independently reconstructed main inequality or named-hull exclusion.

| Claim | Disposition | F/M/m/I | Reason |
|---|---|---:|---|
| C1. Physical interval, product reference, and arbitrary complex densities/projectors | SUPPORTED | 0/0/0/0 | Choi eigenvalues and product spectrum below; no reality assumption on the state or projector. |
| C2. Exact shared projector budget and `0 ≤ x(Q) ≤ 20` | SUPPORTED | 0/0/0/0 | Parseval plus a hypersimplex/three-binary-strings argument; 20 is attainable. |
| C3. One-body bound `min(L,√(Sx))` and signed higher-weight bound | SUPPORTED | 0/0/0/0 | Both bounds use that very same `ρ,Q,p`; the proof below retains `s^j`, including negative `s`. |
| C4. Claimed gap (1) and the fact its right side may be negative | SUPPORTED | 0/0/0/0 | Explicit derivation and an actual physical GHZ/same-`Q` negative-right-side example below. |
| C5. Scalar optimizer and all boundary cases, including `S=0`, `H_t=0`, `t=0`, and the `x0=u` transition | SUPPORTED | 0/0/0/0 | Full case analysis below; this is a relaxation, not an assertion that a maximizing `x` is attained by a projector. |
| C6. Uniform-in-`Q` `K3` upper bound and precise sufficient criterion, pure or mixed | SUPPORTED | 0/0/0/0 | The pointwise bound holds uniformly for the same fixed input, then take the Ky Fan maximum. Strictness requires `t>0`. |
| C7. Implication from the corrected pure-state `D_p` test | SUPPORTED | 0/0/0/0 | Reconstructed from Parseval, `0≤t≤1`, and the adopted `D_p` hypothesis; no extension of the original class definition is imported. |
| C8. Example moments, `H_t`, scalar optimizer, and all-`Q` strict certificate at both endpoints | SUPPORTED | 0/0/0/0 | Exact fractions and a separate construction from reduced purities are given below. |
| C9. Stated same-`Q` traces and positive weaker same-`Q` certificate | SUPPORTED | 0/0/0/0 | Independent direct transition-probability calculation and exact control, without assuming this `Q` is optimal. |
| C10. Genuine four-party entanglement and exclusion from the corrected named fixed-`p` hull | SUPPORTED | 0/0/0/0 | Seven explicit coefficient minors; strict failures of U, D and the mandatory H moment condition; rank-one extremality. |
| C11. Algebraic full-output-purity-style comparison | SUPPORTED | 0/0/0/0 | Direct global Pauli/Cauchy derivation gives the displayed test and difference `680/2187>0`. |
| C12. Attribution of that test to the historical packet 39 | INCONCLUSIVE | 0/0/0/1 | Packet 39 is not a declared input. Its identification and historical attribution cannot be checked in this freeze; the algebraic comparison itself is verified independently. |
| C13. Near-product `G≥124/125` comparison and phrase “any product overlap … at most 5/6” | MINOR + INCONCLUSIVE | 0/0/1/1 | The target does not define `G`, and no listed input supplies its exact definition. The **squared** product overlap is at most `5/6`; the unsquared amplitude can exceed `5/6`, e.g. `|<0000|ψ>|=√3/2`. Both of these common conventions still give a value below `124/125`, but attribution to the exact historical `G` is unproved. Repair wording to “squared product overlap” and define `G` in a permitted correction. |
| C14. Public-source/Zhang historical attribution | INCONCLUSIVE | 0/0/0/1 | The cited public source is not a declared input and was not sought. No priority or novelty claim is accepted. |

These are finding counts, not a claim that source-review/process assertions in the input were independently replayed. The linked author checker and its PASS, unlisted source bodies, held materials, solver results and other reviews are not premises.

## 1. Independent reconstruction: physical interval and common budgets

For the normalized Bell vector `Ω=(|00>+|11>)/√2`, the one-qubit channel's normalized Choi operator is

`(Φ_p ⊗ id)(|Ω><Ω|) = (1-p)|Ω><Ω| + (p/4) I_4`.

Its eigenvalues are `1-3p/4` and `p/4` three times, so complete positivity holds exactly for `0≤p≤4/3`. Write `s=1-p`, `t=|s|`; throughout this physical interval `0≤t≤1`. For a pure product input each one-qubit output has eigenvalues `a=(1+t)/2`, `b=(1-t)/2`, regardless of the sign of `s`. Its three largest four-fold product eigenvalues are `a^4,a^3b,a^3b`, including ties at the endpoints. Thus

`R3=a^4+2a^3b=(3+8t+6t^2-t^4)/16`.

Take the 256 Hermitian phase-free Pauli strings `P` with `Tr(PP')=16δ_PP'`. Define the *actual* coefficients `a_P=Tr(ρP)`, `b_P=Tr(QP)` and weight sums `A_j=Σ_wt(P)=j a_P²`. They are real for all Hermitian `ρ,Q`, including complex matrices. Parseval gives

`Σ_P a_P²=16 Tr(ρ²)≤16`, `A_0=1`, and `S=A_1=Σ_i r_i²`;

`Σ_P b_P²=16 Tr(Q²)=48`, `b_I=Tr(Q)=3`.

Consequently, for the very same `Q`,

`x=Σ_wt(P)=1 b_P²`, `Σ_wt(P)≥2 b_P²=39-x`.                                      (R1)

No second projector or density enters either term. In fact `0≤x≤20`: rotate each one-site coefficient vector of `Q` to a local Z direction, preserving `x`. In the product basis let `q_z=<z|Q|z>`; then `0≤q_z≤1`, `Σ_z q_z=3`, and `x=Σ_i(Σ_z q_z(-1)^{z_i})²`. This convex function is maximized over the hypersimplex at a vertex, namely three distinct basis strings `z,z',z''`. The value there is

`36-4[d(z,z')+d(z,z'')+d(z',z'')]`.

At least two coordinate positions vary among three distinct binary strings, and each varying coordinate contributes two to the distance sum. Hence `x≤36-4·4=20`. `Q=|0000><0000|+|0001><0001|+|0010><0010|` attains 20. This is a maximization over possible diagonals, not a replacement of the actual complex `Q` in (R1).

The channel sends a weight-`j` Pauli to `s^j P`, and therefore

`16 Tr(Q Λ_p(ρ)) = 3 + Σ_{j=1}^4 s^j Σ_wt(P)=j a_P b_P`.                        (R2)

Let the actual local Bloch vectors be `r_i n_i` and sort their lengths as `r_1≤r_2≤r_3≤r_4`; set `L=r_1+r_2+3r_3+3r_4`. Cauchy gives `|Σ_wt1 a_Pb_P|≤√(Sx)`. The same sum is `Tr(Q H_1)` for the commuting Hermitian operator `H_1=Σ_i r_i n_i·σ_i`. Its three greatest eigenvalues are `Σr_i`, `Σr_i-2r_1`, `Σr_i-2r_2` (ties allowed), with sum `L`. Its spectrum is symmetric about zero, so its three smallest sum to `-L`. The Ky Fan variational principle therefore gives the simultaneous bound

`|Σ_wt1 a_Pb_P|≤min(L,√(Sx))`.                                                 (R3)

Define `H_t=A_2+t²A_3+t⁴A_4`. For `t>0`, Cauchy on all weights 2–4 at once, with the **signed** factors `s^j/t²` retained, gives

`|Σ_{j=2}^4 s^j Σ_wt=j a_Pb_P| ≤ t² √[H_t(39-x)]`.                           (R4)

At `t=0` the higher term is identically zero; (R4) still holds. Combining (R2)–(R4) with the reference polynomial yields exactly

`16[R3(t)-Tr(QΛ_p(ρ))] ≥ t[8+6t-t³-min(L,√(Sx))-t√(H_t(39-x))]`.

This is true for every actual density and projector on the full physical interval. It does not require reflection, and the signed odd powers have not been replaced by positive ones.

Reflection, if used separately, is `Λ_{1+t}(ρ)=Y^{⊗4} Λ_{1-t}(ρ)^T Y^{⊗4}`, since `Yσ_j^TY=-σ_j` for each nonidentity single-qubit Pauli. Thus the corresponding positive-shrinkage projector is `Q'=Y^{⊗4}Q^T Y^{⊗4}`; it is an actual rank-three projector, but in general **not** the original `Q`. The endpoint `p=4/3` has `t=1/3` and Choi eigenvalues `(0,1/3,1/3,1/3)`.

## 2. Complete scalar optimization, boundaries, and criteria

For `S>0`, put `u=L²/S`. By Cauchy against `(1,1,3,3)`, `0<u≤20<39`. On the relaxed domain `0≤x≤39` define

`F(x)=min(L,√(Sx))+t√(H_t(39-x))`.

For `x≤u`, its first term is `√(Sx)`; for `x≥u`, it is `L`. When `t>0` and `H_t>0`, the derivative on the first branch is

`F'(x)=√S/(2√x) - t√H_t/(2√(39-x))`,

which changes sign only at `x0=39S/(S+t²H_t)`. On the second branch the derivative is negative. Therefore:

* If `x0<u`, the unique relaxed optimizer is `x*=x0`.
* If `x0=u`, the unique relaxed optimizer is the transition `x*=u`.
* If `x0>u`, the unique relaxed optimizer is `x*=u`.

When `S>0` and either `t=0` or `H_t=0`, `x0=39`; every `x∈[u,39]` is an optimizer, and choosing `x*=u` is valid. Restricting the relaxation to the necessary actual bound `x≤20` leaves the possible plateau `[u,20]`; it does **not** establish that each scalar value comes from a projector.

When `S=0`, all local radii and `L` vanish. If `t>0,H_t>0`, `F(x)=t√(H_t(39-x))` has the unique relaxed optimizer `x=0`; if `t=0` or `H_t=0`, it is the constant zero function and every relaxed `x` is an optimizer. Thus the candidate's formula is correct in every boundary case:

`B_t(ρ)=√(Sx*)+t√(H_t(39-x*))`, `x*=min(u,x0)` for `S>0`,

and `B_t(ρ)=t√(39H_t)` for `S=0`. At `t=0`, `Λ_p(ρ)=I/16` and both sides of the gap inequality are zero, regardless of the optimizer's nonuniqueness. No division by `S` is used in that branch.

Since the bound applies for **every** rank-three `Q` with the same fixed `ρ,p`, the finite-dimensional Ky Fan maximum gives

`K3(Λ_p(ρ)) ≤ [3+t B_t(ρ)]/16`,

`16[R3(t)-K3(Λ_p(ρ))] ≥ t[8+6t-t³-B_t(ρ)]`.

Thus for `t>0`, `B_t(ρ)≤8+6t-t³` is a sufficient condition for the original `k3` inequality; strict inequality gives a strict gap. For a pure state this is exactly the same criterion using its own `A_1,…,A_4`; for a mixed state its moments are computed directly, not from a chosen pure decomposition. Neither criterion is necessary, and a negative lower bound is informative only as an inequality, not as a nonnegative-gap certificate.

Further, physical `t≤1` and density Parseval give `H_t≤A_2+A_3+A_4≤15-S`, so `B_t≤L+t√[39(15-S)]`. If a pure input meets the adopted `D_p` condition `8-L≥t(√[39(15-S)]-5)`, then `B_t≤8+5t≤8+6t-t³`, the last inequality following from `t(1-t²)≥0`. This checks the claimed implication, without importing any larger D class.

## 3. Exact state, moments, and both actual projector traces

Use the target's normalized state `ψ=(3|0000>+|0011>+|0101>+|1110>)/√12`. No two support strings differ in exactly one bit, so its one-site reduced states are diagonal. Their radii in site order are `(5/6,2/3,2/3,2/3)`, and

`S=73/36`, `L=35/6`, `C=|<ψ,Y^{⊗4}\bar ψ>|²=0`.

The last equality also follows because the support contains no bitwise-complementary pair. A separate reduced-purity reconstruction of the higher moments is as follows. With site indices `0,1,2,3`,

`Tr ρ_01²=Tr ρ_23²=Tr ρ_02²=Tr ρ_13²=17/24`,

`Tr ρ_03²=Tr ρ_12²=43/72`.

The first value, for example, follows from reduced eigenvalues `(10,1,1,0)/12`; the second from `(9,2,1,0)/12`. Summing `4 Tr ρ_ij²` over pairs gives `6+3S+A_2`, hence `A_2=145/36`. Purity across complementary bipartitions gives `Σ_{|T|=3} 8 Tr ρ_T²=16+4S`, while its Pauli expansion is `4+3S+2A_2+A_3`; hence `A_3=215/36`. Since the state is pure, `Σ_j A_j=16`, giving `A_4=107/36`. Therefore

`(A_0,A_1,A_2,A_3,A_4)=(1,73/36,145/36,215/36,107/36)`.

At `t=1/3`—both physical `p=2/3` and `p=4/3`—the exact values are

`H_t=13787/2916`, `u=1225/73`, `x0=2075463/67004>u`,

`H_t(39-u)=11181257/106434<121`.

It follows that `B_t=35/6+(1/3)√[H_t(39-u)]<19/2<269/27=8+6t-t³`. The bound is uniform in the *actual* projector, so

`K3(Λ_p(ρ)) < (3+(1/3)(19/2))/16=37/96`

for **every** rank-three `Q` at each of these two `p`. The reference is `R3=32/81`, so the actual `K3` gap is strictly greater than `25/2592`. This is a claim for this input only, not every input at either parameter.

For the explicitly displayed `Q=|0000><0000|+|0011><0011|+|0101><0101|`, the full weight-norm vector is `(9,12,6,12,9)`, so `x=12`. Directly, let `c=1-p/2` be the probability of preserving an input bit and `d=p/2` the probability of flipping it. The four input populations are `9,1,1,1` divided by 12, and their distances to the three `Q` strings yield

`Tr(QΛ_p(ρ)) = (11/12)(c⁴+2c²d²) + (1/4) c d³`.

This is `5/18` at `p=2/3` and `41/324` at `p=4/3`; against `32/81` the respective gaps are `19/162` and `29/108`. For this same actual `ρ,Q`, `Sx=73/3<25` and `H_t(39-x)=13787/108<144`. Hence the square-bracket expression is strictly greater than `269/27-5-4=26/27`, giving the weaker positive gap `>13/648` at each parameter without diagonalizing the output. The different fixed-`Q` traces also show why one may not silently substitute `t` for signed channel powers or keep `Q` unchanged under reflection.

## 4. Genuinely entangled and outside exactly the named hull

For a pure state, a bipartition is product only if its coefficient matrix has rank one. The following seven representatives cover all nontrivial four-party bipartitions up to complement. Sites, rows and columns are numbered from zero and binary tuples are packed in increasing site order. Each selected unnormalized coefficient minor has determinant `+3`, and the normalized determinant is `+1/4`.

| Cut | rows | columns | unnormalized determinant |
|---|---:|---:|---:|
| `{0}` | `(0,1)` | `(0,6)` | 3 |
| `{1}` | `(0,1)` | `(0,1)` | 3 |
| `{2}` | `(0,1)` | `(0,1)` | 3 |
| `{3}` | `(0,1)` | `(0,1)` | 3 |
| `{0,1}` | `(0,1)` | `(0,1)` | 3 |
| `{0,2}` | `(0,1)` | `(0,1)` | 3 |
| `{0,3}` | `(0,1)` | `(0,1)` | 3 |

Thus every bipartition has rank at least two and the state is genuinely four-party entangled. In the corrected adopted scope, `P,U,D_p,H` are pure-input classes at fixed `p`:

* It is not in `P`, and it is not in `U` because its single-site radii are nonzero.
* The mandatory H moment hypothesis fails: `4S+8C=73/9>64/9`. No spin-flip criterion alone can restore membership in H.
* For `t=1/3`, `δ=8-L=13/6`; both quantities being compared are nonnegative and
  `39(15-S)-(5+δ/t)²=1121/3>0`.
  Hence `δ<t(√[39(15-S)]-5)` and the `D_p` condition fails strictly at both named parameters.

If a rank-one density is a finite convex combination of positive trace-one densities, every positive-weight summand has support in its one-dimensional range and is the same density. Therefore this `ρ` cannot lie in the finite convex hull of the named classes at either fixed parameter. This is not a proof of exclusion from every other earlier region or method.

Separately, the elementary whole-nonidentity-Pauli Cauchy bound is

`16 Tr(QΛ_p(ρ))≤3+t√[39(S+t²H_t)]`.

At `t>0`, its sufficient test for the `k3` reference is `39(S+t²H_t)≤(8+6t-t³)²`; here the left minus right equals `680/2187>0`. This verifies the arithmetic and failure of that test, **not** its attribution to an unlisted historical packet.

For near-product wording, using any site with radius `2/3` gives the rigorous bound `|<a b c d|ψ>|²≤λ_max(ρ_i)=5/6`. In particular the squared product fidelity is below `124/125`; also an unsquared product amplitude is at most `√(5/6)<124/125`. However, the target does not define `G`, so the exact old condition cannot be imported as an identified premise. Moreover `|<0000|ψ>|=√3/2>5/6`; the target's phrase “any product overlap … at most 5/6” is false if “overlap” means unsquared amplitude, and should explicitly say “squared overlap.” This wording issue does not affect the main theorem or the named-hull exclusion.

## 5. Bounded reviewer-owned controls and intended-reason negatives

One reviewer-owned standard-library integer/Fraction/Gaussian-rational program was executed, not the author checker. Source: `reviewer-controls-v1.py`, SHA-256 `a91c950538e58614671396288de74d7727f2d04af15f467ccfd3099315b82717` both before and after execution. Receipt: `reviewer-controls-v1.receipt.json`, SHA-256 `dd4b318c3489029b492a9a1d8bfeec992586134ac1309c867c7d4fe87355abbc`. Captured output: `reviewer-controls-v1.output.txt`, SHA-256 `fb72ea76192958ce66784dc5bb1ab57abe1728f75b02246adad2afd728c9cb71`. Actual process exit **0**, native `/bin/date` observations `2026-10-29T13:53:14-0700 PDT` at start and end, monotonic elapsed `0.530147 s`, timeout `120 s`. No timeout/incomplete result is treated as success. Rational lower/upper square-root enclosures were used, not floating acceptance thresholds.

* 100 exact cases: five physical densities (including a complex pure state and a mixed state), four actual projectors (including a complex projector), and `p=0,1/3,2/3,1,4/3`. Matrix-unit tensor channel evaluation was compared to the signed 256-Pauli expansion and the actual same-`Q` bounds. These finite cases are controls, not the all-variable proof.
* Scalar controls hit interior `x*=39/11`, cap `x*=4`, equality transition `x*=9`, `H=0`, `t=0`, `S=0` with nonconstant and constant cases. These are scalar relaxation examples, not asserted realizable density/projector moment tuples.
* Intended physical-parameter negatives: the normalized Choi operator has eigenvalue `-1/12` at `p=-1/3` and `-1/8` at `p=3/2`; endpoint `p=4/3` has nonnegative Choi eigenvalues. These negatives demonstrate the reason the CP interval cannot be enlarged.
* Intended same-`Q` negative: at `p=2/3`, `ρ=|0000><0000|` and the real top-three `Q` with `x=20` attain the reference, so their actual gap is zero. Substituting `x=0` from a **different physical rank-three GHZ projector** into that gap formula falsely predicts a positive gap. Likewise, substituting the maximally mixed state's `S=H=0` for this product input falsely bounds its actual trace by `3/16`. Neither substitution is permitted.
* Intended sign/reflection negative: the displayed actual `ρ,Q` give `41/324` at `p=4/3`, not the `5/18` value at `p=2/3`. The program also checks the correctly transformed projector for both a diagonal and a complex `Q`.
* Intended negative right side: for the physical GHZ input `(|0000>+|1111>)/√2`, an actual rank-three GHZ projector containing it has `x=0`. At `p=0`, the actual gap is zero, but the proposed lower-bound right side is `13-√585<0`. Thus the inequality is not itself a global `k3` proof.

## 6. Frozen inputs, exact display order, imports, and residuals

The assigned manifest was hashed before its body was displayed: SHA-256 `55820cc8fca90ef93c861bb8894f2c68d73b4c65b2959876e21d7979f9d9e960`. It was displayed in raw windows `1–15,16–30,31–44`. Before displaying **any** declared input body, all four full files were measured against all three manifest pins; all matched. Then all declared bodies were displayed completely in the exact manifest order, raw windows no larger than 15 lines, including their last lines:

1. Mandatory H scope correction, SHA-256 `c9b5632e8285298a6b8438842498fc5a35695a889efcee0245836c2cbf038db2`, 2444 bytes, 27 LF: windows `1–15,16–27`.
2. Corrected f172 regional disposition, SHA-256 `774cbb0f053c2b5c6400320a6c3bfdb919ec1e3df09ddf5884508e54cccb3f6c`, 7514 bytes, 22 LF: windows `1–15,16–22`.
3. f200 all-density-window disposition, SHA-256 `bb16e861cedad17fc2a9eb9520dba4cb7bdbd69ad3cd510df2e7bd59060f8b54`, 4873 bytes, 17 LF: windows `1–15,16–17`.
4. Target candidate 186, SHA-256 `36aa530048387e244b27815e25fb93f38ad98366af37d839f047732dd9cba922`, 11016 bytes, 167 LF: windows `1–15,16–30,31–45,46–60,61–75,76–90,91–105,106–120,121–135,136–150,151–165,166–167`.

All displays were completed before mathematical reasoning and before the reviewer control was prepared. No declared-input or ordering deviation occurred. The only mathematical imports from adopted dispositions are their expressly stated channel/reference and the corrected fixed-`p` pure class definitions and scopes, including the mandatory conjunction for H; the f200 `|1-p|≤1/142` all-density theorem is background only and not needed for the proof. The separate `|1-p|≤1/200` f172 all-density result is likewise not substituted for any all-physical-`p` step. Named source/review links in those dispositions were not opened or promoted to premises. No R-positivity, one-erasure, equality-183, held f161/f162, author PASS, external literature, external model/API, author contact, author code, Git operation, or unrelated build/lint/test/formatter was used.

Residuals: the example does not settle all-density `k3` outside adopted windows, every other sufficient class, other spectral prefixes, full majorization, or novelty/priority. Historical packet-39 and public-source attributions and the undefined `G` label remain unverified under the frozen evidence boundary. The mathematical bounds here do not equate the relaxed optimizer to a realizable actual projector.
