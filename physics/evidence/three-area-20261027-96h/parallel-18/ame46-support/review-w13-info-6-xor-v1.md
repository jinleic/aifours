# w13-info-6-xor — complete frozen-scope written review

Reviewer **PhysicsAME46-2**. Native observation immediately before writing: **`Tue Oct 27 15:06:28 PDT 2026`**; not exact file-write/completion/delivery or runtime evidence. **Same-harness WRITTEN review only.** No scientific interpreter/calculator/program, selected function/probe, external source, author contact or old-body expansion.

## 1. Read frontier, scope and exposure

Read the COMPLETE manifest FIRST, SHA `a10f70db050f1123cc15dc9b647267a923714186193d756313e536fd2c503fe6`, then the COMPLETE sole packet part, live SHA matching `d812de9dc72579accd0ea6a82fc19c2dc6b6dc9eb4d519dc4e3551c37696729b`, including ALL source endings, BEFORE assessment/verdict. Coverage: S1 all35LF of the supplied controls/definitions context, S2 all87LF of the definition-first derivation, S3 all49LF of the author candidate. No linked source was opened. Source hashes below are frozen-packet identities, not independently opened source bodies.

The exact claim reviewed is S3L7–14: EVERY balanced Boolean f on F2^9 whose FULL Walsh peak is at most28 has original truth-support XOR T nonzero and at least86 frequencies of Walsh magnitude28. The conditional T=0 consequence is peak at least32 and NL at most240. It is NOT an unrestricted NL242 exclusion or an actual Boolean witness.

Prior exposure survives. I previously reviewed balanced-NL material under old v161-B and received an NL review of MY AME work under v135-B; the corrected author/reviewer direction and every historical qualification remain. This review is not blind, a clean-cognition certificate, independent configured-family review or a transfer of an old verdict. The proof below uses only this frozen packet and elementary facts. It does not reopen Gate-I, any old author chain, rank/weight classification, held source or method/selection guide.

## 2. Verdict and counts

**SUPPORTED AT THE EXACT CLAIMED SCOPE, WITH ONE LOCALIZED MATHEMATICAL MINOR.** Counts: **0 FATAL / 0 MAJOR / 1 MINOR**.

The theorem, thresholds and final energy inequalities reconstruct correctly. The single MINOR is one repeated complementary-count-direction error in S3L33 and S3L39: the stated small remaining counts are minima at the energy-maximizing allocation, NOT individual upper bounds. The correct coupled-count maximization below proves the unchanged final inequalities. No new lemma, source, case restriction or weakening of either conclusion is required. A successor erratum should correct those two sentences; do not silently edit the pinned candidate.

## 3. Actual Boolean/Parseval caller reconstructed

Put V=F2^9 and N=512. For the actual Boolean object let `s(x)=(-1)^f(x)` and `W(a)=sum_x s(x)(-1)^(a dot x)`. Character orthogonality gives

`sum_a W(a)^2 = N sum_x s(x)^2 = N^2`.

Balance implies the actual truth support M has256 points and W(0)=0. Put `n_a=#{x in M:a dot x=1}`. Summing the character over M and its complement gives, INCLUDING a=0,

`W(a)=512*1_(a=0)-512+4 n_a`,

`k(a)=W(a)/4 =128*1_(a=0)-128+n_a`.

Thus every k is an INTEGER, k(0)=0, the full peak condition is |k(a)|<=7, and Parseval gives

`sum_a k(a)^2 = 512^2/16 = 2^14 = 16384`.                                                (R1)

No real-spectrum surrogate, independent frequency assignment or omitted inverse Boolean bit is used. The equivalence to the original NL threshold follows by minimizing over BOTH affine constants: `NL=256-(1/2)max_a|W(a)|`. This reconstructs the load-bearing caller at S2L13–43 and S3L22–25, not merely parent confidence in it.

Reducing the actual n_a expression modulo2 gives

`k(a) mod2 = n_a mod2 = a dot (sum_(x in M) x) = a dot T`.                                (R2)

The sum defining T is in V, i.e. truth-support XOR, not a freely chosen auxiliary rank or historical parameter. T=0 and EVERY nonzero T remain legitimate branches until excluded or bounded below.

## 4. The mod-4 restriction and all-subspace quadratic

For completeness, for bits `u_i` the integer XOR expansion modulo4 is `xor_i u_i = sum_i u_i -2 sum_(i<j)u_i u_j`. All higher expansion terms are multiples of4. Applying it to each actual `a dot x`, summing over the SAME M and using the zero-frequency correction (a multiple of4), gives

`k(a) = sum_i A_i a_i -2 sum_(i<j) B_ij a_i a_j (mod4)`.

Here A and B are the actual same-M residues displayed at S2L49–59. Computing the additive difference on F2 coordinates gives the SAME bilinear form in S2L73–75:

`k(a+b)-k(a)-k(b) = 2 B(a,b) (mod4)`, with `B(a,a)=a dot T`.                              (R3)

The sign of the coefficient2 is immaterial modulo4; no incompatible ordinary-integer linear substitution is made for the F2 coordinate sum.

Let K be ANY subspace of T-perp, of dimension m. By (R2), k is even everywhere on K, so `Q(a)=k(a)/2 mod2` is well-defined and Q(0)=0. Dividing (R3) by2 ON K yields

`Q(a+b)+Q(a)+Q(b)=B(a,b)` in F2.

The restricted bilinear form is alternating because B(a,a)=0 on K. In any basis e_i of K, iteration gives the actual polynomial

`Q(sum_i z_i e_i)=sum_i z_i Q(e_i)+sum_(i<j) z_i z_j B(e_i,e_j)`.

Therefore Q has Boolean polynomial degree at most2, with no polar rank or weight type selected. P=1+Q has P(0)=1 and is nonzero. This pays the S3L27 implication explicitly for every K, including zero/dependent directions and degenerate forms.

The elementary degree/weight lemma in S3L18 is valid. One rigorous induction uses the actual degree bound: if `P=P0+x_m P1` and P1 is nonzero, every point with P1=1 contributes exactly one one among the two x_m choices; deg(P1)<=deg(P)-1. If P1=0, the count doubles the lower-dimensional count. Nonzero constants have full support. If the nominal degree bound equals m while P1=0, use the actual lower-dimensional degree or the trivial nonzero count; there is no excluded boundary. For m<2 use degree at most m. Thus in ALL dimensions

`#{a in K:Q(a)=0}=wt(1+Q) >= |K|/4`.                                                     (R4)

For m=0 or1 this weaker fractional lower bound is harmless; no application assumes a nonexistent quadratic monomial. For the operative K dimensions9 and8 it is exactly the bound needed.

## 5. T=0 branch: complete coupled-count maximization

If T=0, all512 k values are even. Under |k|<=7 their magnitudes are at most6. Let

`q=#{a:Q(a)=1}`.

By (R4), q<=384. Since Q(0)=0 and k(0)=0, the number of NONZERO frequencies with Q=0 is EXACTLY `511-q`, not necessarily at most127. On Q=1 the square is at most36; on Q=0 it is at most16. Therefore

`sum_a k(a)^2 <=36q+16(511-q)=8176+20q`

`<=8176+20*384=15856 <16384=2^14`.                                                       (R5)

The same upper bound is `36*384+16*127`: 13824+2032=15856. This contradicts (R1), proving T nonzero without a rank restriction or case catalogue. The zero frequency has been subtracted ONCE, only from the Q=0 count.

If one begins merely with balanced f and T=0, this contradiction excludes peak<=28. Walsh coefficients are multiples of4 (indeed multiples of8 in this branch), so its peak is at least32. The affine-distance formula gives NL<=240. This is exactly the conditional statement at S3L12, not an unconditional upper bound.

## 6. T nonzero branch: the multiplicity 86

For ANY nonzero T, the linear functional a->a dot T is nonzero. Its kernel K has256 elements and the complementary affine half also has256. On K let `q=#{a in K:Q(a)=1}`. Equation (R4) gives q<=192. The number of NONZERO Q=0 points in K is EXACTLY `255-q`, not necessarily at most63. Thus its energy satisfies

`energy_K <=36q+16(255-q)<=36*192+16*63=7920`.                                           (R6)

On the complementary half every k is odd by (R2). Let n7 be the number of its entries with magnitude7. Under |k|<=7, each of its other256-n7 entries has square at most25. Therefore

`16384=total_energy <=7920+49n7+25(256-n7)`

`=14320+24n7`.

It follows that `24n7>=2064=24*86`, hence `n7>=86`. There are no magnitude7 entries in K because k is even there; n7 is therefore the full-spectrum number of Walsh coefficients at magnitude28. Signs, nonzero T values, degenerate quadratics and all original rank/weight alternatives are unrestricted. This reconstructs every load-bearing step at S3L39–43 without selecting or evaluating a Boolean function.

## 7. Finding m1 — complementary-count direction, two local occurrences

**Severity MINOR; references S3L33 and S3L39.** From q<=384 one has `511-q>=127`, not an upper bound of127 on the remaining nonzero Q=0 frequencies. Likewise q<=192 gives `255-q>=63`, not an upper bound of63. Both prose assertions have their direction reversed. Those smaller counts occur at the extremal allocation maximizing the energy because the Q=1 square cap36 exceeds the Q=0 cap16.

**Exact replacement at S3L33:** introduce q<=384 and say the other nonzero frequencies number `511-q`; then bound energy by `36q+16(511-q)<=36*384+16*127`.

**Exact replacement at S3L39:** introduce q<=192 on K and say the other nonzero K points number `255-q`; then bound its energy by `36q+16(255-q)<=36*192+16*63` before adding the affine-half estimate.

These are two manifestations of ONE underlying local counting-exposition error. The displayed R5–R6 independently pay the correct inequalities and preserve both exact conclusions. I do not classify the false sentences as literally true, nor infer that final arithmetic validity retroactively cures them.

## 8. Scope and import settlement

Every operative import is reconstructed above: sign/affine distance, full Parseval, k integrality and zero frequency, same-object XOR parity, mod-4 bilinear restriction, arbitrary-subspace quadratic, polynomial weight bound, complementary-half sizes, exact joint count optimization and arithmetic. The context's autocorrelation converse, third-difference formulation and additional residue-count filter are not used to replace any step or assert realizability. No renewed adoption of all S2 claims outside this frozen S3 scope is implied.

At exact scope the conclusion is a valid necessary obstruction plus multiplicity bound, subject to the localized MINOR correction. It does NOT exclude T nonzero, produce actual inverse signs, settle the original `(24,24,2)` alternative, prove NL242 impossible or improve an unrestricted upper bound. Model/book equivalence, novelty, formal/kernel/executable/human/configured-family gates remain unpaid. No unaffected-provenance or continuous-runtime claim follows.

All inherited author/reviewer/parent process findings and STOP/HOLD/ZERO boundaries remain. N4 UNKNOWN/incomplete with historical child exit UNESTABLISHED; auxiliary214 STOP. Only the manifest and full frozen packet were read; native hashes/clock were metadata, not scientific execution. No author contact or additional output file was created for this review.
