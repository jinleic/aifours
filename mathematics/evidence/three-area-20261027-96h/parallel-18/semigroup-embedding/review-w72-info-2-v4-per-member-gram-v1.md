# Review w72 — septic scalar margin and per-member Gram equivalence

**Reviewer:** MathSemigroup-2, math-4. **Author:** InfoSPR7-2, info-2.

Actual first review wake: **Tue Oct 27 16:40:42 PDT 2026**. Actual pre-body ACK observation: **16:41:06**. Actual native observation immediately before writing this review: **Tue Oct 27 16:43:21 PDT 2026**.

## 1. Verdict and exact scope

**NO_SUBSTANTIVE_DEFECT AT EXACT SCOPE** in the complete v4 candidate S5.

- FATAL mathematical findings: **0**.
- MAJOR mathematical findings: **0**.
- MINOR mathematical findings: **0**.

The scalar half-line factor proof is complete, including zero residuals, all real-root multiplicities, irreducible factors and degree drops. It proves the claimed per-member two-square and separate4x4 PSD Gram equivalences with a **positive normalized-pairing margin**. A finite four-member family admits one common epsilon by compactness, without any common state-space or common quadratic matrix premise.

The used v3 actual-box/four-corner interface is independently reconstructed below. The same exact-degree-seven b must satisfy all member identities. The result is an exact feasibility interface, **not** a proof that every robustly Hurwitz septic box has such b, an actual counterexample box, a KYP theorem, a solved original conjecture or novelty acceptance.

## 2. Required order, actual coverage and exposure

I read all of S0 in raw1–16/17–31, then the complete frozen manifest, SHA `32a5736cfe2d5c3744023a558b3d9dfbf8efb88bf32df7452efafbb21840ecd2`. Before any packet opening or mathematical reasoning I wrote the designated pre-body ACK, SHA `df57d91e4936e102e2117267cf1d5b7073116acc36e825ee8144399535a6dc6a`, at actual16:41:06.

I then read every line and ending of the **575-LF / 72047-byte** exact packet, SHA `562b804ba256d3379a1ba2f8b576e699640ac84ea6e8a326532ad085aec10a95`, in raw ranges1–60,61–120,121–180,181–240,241–300,301–360,361–420,421–480,481–540,541–575. All windows were at most60LF; no long line or ending was omitted.

| Source / role | Complete LF | SHA-256 |
|---|---:|---|
| S1, literal original model | 63 | `9df2b558c03b2aac8cefb786be5a2a0802de822724bcd6ee60b47d0205fc61f6` |
| S2, v3 dependency | 108 | `9297cd6899346e9a80a187965065a3ca9c87f8e1a857040996679b0345a7eb04` |
| S3, v1 dependency | 117 | `2c50f876efc528ec5f276ea52694fa7175516da830d176b842e535ecc1bef677` |
| S4, v2 dependency | 129 | `76306a285eecdc20a390b6eaf45a5aec5bc20d723e20543d4bff898f535abaa4` |
| S5, full v4 candidate | 138 | `1172b667e4b740fc0d005ee2bea46c394c9ba1cee7ec226bd2e131335e4317d5` |

Prior closed-round SPR even-Euler review and incoming SPR107/112/v153-A semigroup contacts remain disclosed, not treated as blind work. No old body, guide or verdict was used. The named w46 review of v3 is not my verdict or a proof premise; the used v3 steps are paid from this literal packet. S3's finite dual/interpolation and S4's root-band/higher-frequency theorems are not required by v4 and are not re-adopted simply because their full files were read.

Own semigroup method STOP, QOA public-source display MINOR, prior one-window reading deviation, every historical finding and the new **parent L1 PROCESS MAJOR / entire L1 and consumers HELD/ZERO** remain. L1 itself/payload was not opened or reconstructed. No selected small polynomial, box, plant, matrix, spectrum, root configuration or frequency instance was checked even privately. No scientific interpreter, calculator/Eval/CAS, enumeration, solver, test, replay, CLI, nested agent, external source or author contact. Only the ACK and this review were written.

## 3. Claim-by-claim dispositions

| Claim / source references | Verdict / exact condition |
|---|---|
| Actual even polynomial, S5:16–33 | CORRECT in original b/a direction, for real coefficients and each actual Hurwitz monic denominator. No numerator-stability or reciprocal theorem required. |
| Exact degree and compact margin, S5:35–47 | CORRECT: finite-frequency strictness plus exact degree forces b7>0; compactified normalized pairing has a positive minimum. Dropped numerator degree is explicitly not covered by that automatic margin. |
| Half-line lemma, S5:51–78 | CORRECT for every real Q of degree at most7, including Q=0, root0, positive even multiplicities, arbitrary negative roots, complex conjugate factors and residual degree drops. |
| Two-square margin, S5:82–95 | CORRECT; one epsilon across finitely many members, all real w and the actual zero/infinity coefficients retained. |
| General PSD Gram equivalence, S5:99–106 | CORRECT and lossless; rank-at-most1 alternatives exist at the same epsilon, without asserting the originally supplied PSD matrices have rank1. |
| Coefficient identities, S5:110–120 | CORRECT, linear in the shared b and each independent Gram pair; both off-diagonal orders counted, empty sums0, positive homogeneity valid. |
| Full original-box caller, S5:124–130 using S2 | CORRECT for the same actual coefficient-coupled four members, the same b, strict inequalities and possibly degenerate intervals. |
| Ratio-margin and unsolved existence boundary, S5:126–138 | ACCURATE: epsilon is not numerically the literal ratio margin; common-b feasibility for every eligible box remains unproved. |

## 4. Used v3 four-member interface: direct reconstruction

The registered specialization is a compact nonempty monic coefficient box

K={s^7+sum_(j=0..6)a_j s^j : a_j in[l_j,u_j]},

with every actual member strictly Hurwitz, finite closed possibly degenerate intervals, and one unrestricted real exact-degree-seven numerator. Uncertain leading coefficients and all-order conjectures are not silently added.

At t=w²>=0,

a(iw)=E_a(t)+iw O_a(t),
E_a=a0-a2t+a4t²-a6t³,
O_a=a1-a3t+a5t²-t³.

The signs of these nonnegative powers fix their extrema at the literal alternating coefficient choices U-/U+ and V-/V+ printed in S2:20–26. Those four choices are actual coefficient vertices and do not change with t. They are Hurwitz because the entire original box is, not by an unprovided vertex-stability theorem.

At each fixed t, the even and odd coefficient groups are independent. Their linear images are the full intervals[E-,E+] and[O-,O+]. Given an actual a, interpolate each value with alpha,beta in[0,1]. Combining the two interval choices gives the four nonnegative weights(1-alpha)(1-beta),(1-alpha)beta,alpha(1-beta),alpha beta and hence a convex representation of its **complex value** a(iw). The weights may depend on a,t. This is not a claim that the full coefficient box is the coefficient hull of four points.

For fixed b, Re[b(iw)conjugate(a(iw))] is real linear in the actual denominator value. It is thus a convex combination of the four positive corner pairings. Every actual denominator is nonzero on the imaginary axis, so dividing by its positive modulus square gives strict positivity of b/a. Necessity is immediate from actual membership. This pays the same-b, all-frequency, all-member reduction directly; the ratio itself was not falsely treated as affine in a.

At w=0 the imaginary component vanishes and the same argument remains valid. If either interval collapses choose its interpolation parameter0; no zero-width division occurs. Negative w follows by real-coefficient conjugation. Coincident corners are repetitions, not a loss of strictness.

Exact degree gives the normalized pairing's common infinity value b7>0, as detailed below. Four compact positive curves have a common positive minimum. Their pointwise convex representation transfers it to the actual box at the same t. Finally the normalized denominator modulus square is continuous/positive on compact K times the compactified half-line, with infinity value1; its finite maximum converts the pairing margin to a literal ratio margin. No numerical value is computed.

This is the only v3 scientific reduction needed by v4. The v1/v2 finite dual, root-band or interpolation-obstruction claims are not silently prerequisites of the scalar certificate.

## 5. Explicit even polynomial, strictness and endpoints

Write b(iw)=B_ev(t)+iw B_od(t), and similarly for a_i using the printed real polynomials. Direct multiplication gives

Re[b(iw)a_i(-iw)]=B_ev(t)A_i_ev(t)+t B_od(t)A_i_od(t)=P_i(t).

The mixed terms are imaginary. Therefore E_i(w)=P_i(w²) is even, with degree at most14, constant a_i0 b0 and top coefficient b7. The a_i odd cubic has leading coefficient-1 and the b odd cubic-b7, so the t^7 coefficient of their t-weighted product is b7; the even product has degree at most6.

Hurwitz a_i has no imaginary-axis zero. Thus every finite-real-w ratio inequality is exactly E_i(w)>0, equivalently P_i(t)>0 on t>=0. No root on that axis is divided out and no a/b orientation is substituted.

If b is exact degree7, b7 is nonzero. Negative b7 contradicts positivity for all sufficiently large positive t, so b7>0. With x=t/(1+t), the normalized function P_i(t)/(1+t)^7 is a polynomial in x and1-x and extends continuously at x=1 with value b7. Strictness on the half-line and b7>0 make it positive on all of[0,1], giving a positive minimum mu_i.

For finitely many members take any epsilon>0 at most min_i mu_i. Then Q_i=P_i-epsilon(1+t)^7 is nonnegative on the half-line. This common epsilon does not require common Gram matrices. Conversely the representation below makes P_i positive and forces b7>=epsilon>0, even if b was initially allowed degree at most7.

If degree drops below7, normalized infinity value is0 and this positive seventh-degree margin cannot be inferred. This is a genuine exact-degree boundary, correctly retained rather than hidden behind noncompact pointwise strictness. For actual monic Hurwitz a_i, the constant is positive by real negative-root/conjugate-pair factorization; the final constant identity therefore gives b0>0.

## 6. Half-line two-square lemma: all factor and degree cases

For real Q of degree at most7, the reverse implication Q=F²+tG² => Q>=0 on t>=0 is immediate.

For the forward implication:

- **Zero polynomial:** choose F=G=0.
- **Nonzero leading constant:** it is positive because Q is eventually nonnegative. Its real positive square root supplies the constant norm factor.
- **Positive real root:** multiplicity is even; an odd power would reverse sign on two nearby positive t sides, while the remaining nonzero continuous factor retains sign. Thus use repeated(t-r)² norms.
- **Root0:** arbitrary multiplicity is permitted, using repeated t=0²+t·1².
- **Negative real root:** arbitrary multiplicity is permitted, using repeated t+alpha=(sqrt(alpha))²+t·1².
- **Irreducible real quadratic:** with v>0 and delta=sqrt(u²+v²)>|u|,

(t-u)²+v²=(t-delta)²+t·(sqrt(2(delta-u)))².

Expansion gives t²-2u t+delta² on both sides. All square roots are of positive real quantities; no selected roots or numeric polynomial is computed.

These cases cover the complete ordinary real factorization with positive leading coefficient. Products stay in the class because

(F1²+tG1²)(F2²+tG2²)
 =(F1F2-tG1G2)²+t(F1G2+F2G1)².

The two mixed cross terms cancel exactly. Repeated factors, zeros and all multiplicities are retained.

Finally the highest degrees of nonzero F² and tG² are respectively even and odd; no highest-power cancellation can occur. Since the final Q has degree at most7, deg F<=3 and deg G<=3. If either polynomial is zero, omit its term. This pays degree drops too: no factor-construction overestimate is left as an implicit assumption.

Thus the lemma is complete and elementary; no Markov/Lukacs, KYP or semidefinite black box is imported.

## 7. Margin and literal frequency two-square certificate

Apply the lemma to each Q_i at the single chosen epsilon. It gives

P_i(t)=epsilon(1+t)^7+F_i(t)²+tG_i(t)²,

with degrees at most3. Conversely such an identity immediately gives strict half-line positivity. Substitution t=w² gives the printed even-frequency certificate: one even square F_i(w²) of degree at most6 and one odd square wG_i(w²) of degree at most7, plus positive margin. All positive/negative/zero real w are included, not sampled.

The endpoint coefficients are exactly

a_i0 b0=epsilon+F_i(0)²>0,
b7=epsilon+(degree3 coefficient of G_i)²>=epsilon>0.

The latter uses coefficient0 when G_i has lower degree. Zero residual is allowed; interior zeros of Q_i have even multiplicity and a boundary zero can have arbitrary multiplicity, already covered by §6. No division by a vanished residual, root or coordinate occurs.

## 8. General PSD Grams, every coefficient identity and exact converse

Let z(t)=(1,t,t²,t³)^T. From the coefficient vectors f_i,g_i of F_i,G_i, take M_i=f_i f_i^T and N_i=g_i g_i^T. These are real PSD of rank at most1, and reproduce both squares exactly. The zero-vector case gives rank0.

Conversely for **any** real symmetric PSD M_i,N_i, z^T M_i z and t z^T N_i z are nonnegative on the half-line. Thus the positive margin gives strictness without a rank assumption. Their leading coefficient is b7=epsilon+(N_i)33>0; the first Gram term has degree at most6 and contributes nothing at t^7. Their constant is epsilon+(M_i)00>0. Applying §6 to the same residual can produce alternative rank-at-most1 Grams at the **same epsilon**; it does not make the initially supplied Grams rank1.

For every k=0,...,7, expanding z^T M_i z+t z^T N_i z yields exactly

c_i,k(b)=epsilon binomial(7,k)
        +sum_(r+s=k) (M_i)rs
        +sum_(r+s=k-1) (N_i)rs,

with indices0..3 and empty sums0. Ordered off-diagonal pairs appear twice, correctly implementing the symmetric quadratic form. The k=0 and k=7 endpoint formulas above follow directly; no omitted factor2 or extra highest-degree term occurs. c_i,k is linear in the same eight b coefficients because a_i is fixed.

All four members share **b and epsilon**. Their Gram pairs and square factors may differ. Independent feasibility with different b does not solve this system. Nor is any common companion/state-space matrix P assumed; these are coefficient-Gram matrices in a four-component monomial vector.

Positive homogeneity allows b7=1 by dividing b, epsilon and both Grams by the original positive b7. PSD and all coefficient identities are preserved. This proves only lossless normalization, not boundedness, numerical solvability or optimizer attainment.

## 9. Original-box caller, margins and unproved obligation

Combining §§4–8 gives both original callers:

- a common-b, positive-epsilon, per-member Gram certificate for the four actual coefficient-coupled corners proves original b/a positivity for every actual denominator and finite frequency;
- any original exact-degree common numerator gives the four compact margins, a common epsilon and member Grams.

Degenerate intervals and coincident members merely repeat constraints. The pairing margin is not automatically the same number as a ratio margin: divide its lower bound by the positive finite maximum of the normalized denominator modulus. Compactness supplies that maximum jointly on the original box; no actual margin is computed.

What remains unproved is feasibility of this common-b system for **every** robustly Hurwitz monic septic box, or an actual eligible box with a sound infeasibility certificate. Factoring an already-positive P_i does not establish existence of a shared b. Four individually synthesized numerators, sampled positivity, a common-Lyapunov assertion or an unread classical source cannot fill that quantifier.

## 10. Imports, NR boundaries and assurance

All load-bearing v4 steps and the used v3 four-member passage were reconstructed in this review. No required non-elementary mathematical premise remained NOT_RECONSTRUCTED for those exact claims. Named foundations are ordinary real polynomial factorization, elementary root/sign reasoning, finite-dimensional polynomial algebra, PSD quadratic forms, linear images/convex combinations of intervals and compactness/continuity; their specialized applications were paid above.

The supplied model is a registered canonical-dossier transcription, not a fresh book-image/source-equivalence certification. Uncertain leading coefficients, all-order conjectures, primary theorem ancestry and current literature/novelty remain outside the reviewed scope. The v1/v2 dependency files' separate finite-dual/higher-frequency theorems are not newly reviewed/adopted by their inclusion here.

SPR78 outside S1, the stopped higher-contact/phase-comparison route, every ZERO consumer, own method STOP/QOA MINOR, the parent L1 major/quarantine, HOLDv2, N4 UNKNOWN/historical child exit unestablished and auxiliary214 STOP remain. No private selected check, scientific execution, external KYP/positive-real source, old proof or author contact occurred.

This is same-harness WRITTEN review only—not parent adoption, formal/kernel/human/configured-family/executable/independent-model or novelty acceptance. Main must itself read complete operative sources and this actual return before any adoption. Original universal synthesis remains OPEN.
