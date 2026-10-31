# Strict nonpositive-cone septic certificates need five frequencies and have only three five-node phase words

Owner **InfoSPR7-2**, slot info-2. Actual preceding `/bin/date`: **Wed Oct 28 18:20:05 PDT 2026**. **WRITTEN candidate, with the specifically identified finite abstract sign table checked in Python Eval; not reviewed or adopted.** This is a necessary condition on actual strict-negative certificate data, not an assertion that such data or a negative box exist.

## 1. Scope and results

Import the complete `frontier-20261028-five-frequency-single-endpoint-exclusion-v1.md`, SHA256 `e8aae88916a5275f0cbe4fe057dd6bcc2eea809f6ab1d3f8bb5a897d2db23f2a`, for its original independent septic box, strictly separated actual E/O root bands, phase labels and the universal phase ordering `q_i<=q_j+1` at distinct increasing positive frequencies. Also use the original compactified pairing definition in `frontier-20261028-positive-cone-rational-obstruction-v1.md`, SHA256 `2f5f6a87c24556efac981a5c4ee1ad7d2089a6b8e9113897b6944c3d01f761a8`. Both sources remain author-unreviewed; this is not parent adoption.

Let K be ANY original independent monic closed septic box, every member strictly Hurwitz, with possible degenerate intervals. Consider ANY finite positive weighted combination of actual compactified pairing vectors with **all eight** numerator-coefficient components strictly negative. Merge atoms at equal frequencies by actual coefficient averages, and write m for the number of distinct positive finite squared frequencies; zero and infinity atoms may be present or absent.

**Theorem.** Such a strict certificate has **m>=5**, independently of its endpoints. If m=5, then after choosing valid adjacent phase classes at a possible E/O zero, its five actual-member phase classes are necessarily one of exactly these three words:

`(2,1,3,2,4)`, `(2,1,3,5,4)`, `(2,4,3,5,4)`.

Here q=0,...,6 denotes the quadrant half-turn classes of the complete imported source. The first word forces nodes 1,2 into the common O1-root band and nodes 3,4 into E2; the second forces nodes 1,2 into O1 and nodes 4,5 into E3; the third forces nodes 2,3 into O2 and nodes 4,5 into E3. These are NECESSARY only. This result applies to strict negative vectors, not just exact zero-annihilators, and imposes no zero/infinity inclusion requirement on a strict certificate.

## 2. Strict negative coefficients force alternating moments

At merged positive squared frequencies `0<t_1<...<t_m`, write actual even/odd evaluations E_j,O_j and positive normalized weights `mu_j`. If zero is present, its contribution to F_0 is `eta0>0`; otherwise eta0=0. If infinity is present, its contribution to F_7 is `etaI>0`; otherwise etaI=0. Define

`M^E_k=sum_j mu_j t_j^k E_j`,
`M^O_k=sum_j mu_j t_j^(k+1) O_j`, `k=0,1,2,3`.

The even numerator coefficients have pairing signs `(+,-,+,-)`, and the odd coefficients also have signs `(+,-,+,-)` before the infinity term. Therefore F_j<0 for all eight j implies

`M^E_0<0`, `M^E_1>0`, `M^E_2<0`, `M^E_3>0`,
`M^O_0<0`, `M^O_1>0`, `M^O_2<0`, `M^O_3>0`.

At k=0 the nonnegative eta0 only strengthens `M^E_0<0`; at k=3, `F_7=-M^O_3+etaI<0` gives `M^O_3>etaI>=0`. Thus no hidden no-endpoints assumption is used. Same-frequency averaging is exact because V is affine in the denominator and the resulting average is an actual member of the SAME K.

## 3. Elementary sign-variation lemma

**Lemma.** Let `0<t_1<...<t_m` and real x_j, not all zero, have moments `M_k=sum_j x_j t_j^k` with signs `(-,+,-,+)` for k=0,1,2,3. After deleting zero x_j, their ordered sign sequence has at least THREE sign changes. If it has exactly three changes, its first nonzero sign is negative.

**Proof.** Suppose the nonzero sequence has s sign changes, and choose positive roots r_h strictly between the adjacent nodes at which these changes occur. The polynomial

`Q(t)=product_(h=1..s) (1-t/r_h)`

has coefficients with signs `(+,-,+,-,...)` and has alternating sign on the corresponding node runs. If the first nonzero x_j is positive and s<=3, x_j Q(t_j)>0 at each nonzero entry. But `sum x_j Q(t_j)` is a strictly negative linear combination of M_0,...,M_s, since the coefficient signs alternate against `(-,+,-,+)`. Contradiction.

If the first nonzero x_j is negative and s<=2, use `-t Q(t)`: its signs on positive nodes match those of x_j, so the sum is positive; its nonzero coefficients in degrees1,...,s+1 have signs `(-,+,-,...)`, each opposite the corresponding moment sign `(+,-,+)`, so the sum is strictly negative. Contradiction. These two cases prove s>=3 and, when s=3, negative first sign. No positivity of x_j or generic-node assumption beyond distinct positive t is used.

Apply the lemma to `x_j=mu_j E_j` and separately to `x_j=mu_j t_j O_j`. Positive mu_j and t_j mean their signs are the actual E_j and O_j signs. Neither can vanish simultaneously at a positive frequency because the actual denominator is Hurwitz.

## 4. Excluding at most four frequencies

For m<=3, neither sign sequence can have three changes, contradiction. For m=4 each sequence has exactly three changes, no zeros, and begins negative; both are `(-,+,-,+)`. The corresponding E/O pairs are `--,++,--,++`. Each consecutive pair reverses both signs. By the imported phase ordering each such reversal advances q by at least2. The first `--` has q>=2, so the fourth q is at least8, impossible because q<=6. This proves m>=5 for EVERY strict certificate, with arbitrary endpoint presence and arbitrary actual-member multiplicity before merging.

## 5. Exhaustive five-node phase boundary

For m=5, the variation lemma supplies a finite necessary sign test for E and O: after zeros are omitted each sign sequence has at least three changes, and if it has exactly three its first nonzero sign is negative. At any positive t the pair `(E,O)` cannot be `(0,0)`. A zero admits precisely the adjacent phase classes of the corresponding E- or O-root; a strictly signed pair admits the phase classes from the table in the imported source. Apply `q_i<=q_j+1` for every i<j.

The self-contained exact kernel `frontier-20261028-strict-cone-five-node-words-kernel-v1.py`, SHA256 `38301d6046663f85a323125127e03b8b75fe604627eb82fe05754d6a3cd0d1b8`, was loaded in the owner's Python Eval kernel. It enumerates only abstract `-1,0,+1` sign symbols and q in `{0,...,6}`. It found **21** surviving E/O sign profiles and **27** phase assignments: nine each of

`(2,1,3,2,4)`, `(2,1,3,5,4)`, `(2,4,3,5,4)`.

The table is a necessary over-approximation: satisfying the sign and phase conditions does not provide actual coefficients, positive weights or the eight strict sums. There is no floating-point or selected numerical box/frequency in this finite check.

The stated band placements follow directly. For instance, t1<t2 with `(q1,q2)=(2,1)` places BOTH in the globally ordered O1-root band; `(q3,q4)=(3,2)` places both in E2. Similarly `(4,3)` forces the O2 band, and `(5,4)` forces E3. Band boundary assignments are included.

## 6. Exact residual and assurance

The theorem is a new necessary barrier for the strict negative-cone rational/integer certificate route: it does NOT transfer the exact-zero five-node endpoint theorem to strict inequalities. The remaining five-frequency phase words and every m>=6 strict certificate still require the actual coefficient-interval, weights and Hurwitz coupling; no free phase word is a witness. An eight-distinct-frequency normal form remains valid because splitting/perturbing a strict certificate changes m and preserves strictness, rather than claiming m is an invariant.

The variation argument is a complete written proof; the 21-profile/27-assignment classification is exact same-harness finite symbolic arithmetic. Both the imported phase-order source and this paper need complete independent review before any adoption. No original counterexample, universal synthesis, numeric optimum, novelty, formal/kernel/human/configured-family acceptance or changed historical quarantine is claimed.

**END.**
