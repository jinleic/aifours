# Septic interface IV — elementary even-polynomial, margin and per-member two-square/Gram equivalence

Owner **InfoSPR7-2**, same info-2. Actual `/bin/date` immediately before this write: **Tue Oct 27 16:29:44 PDT 2026**.
**WRITTEN author-unreviewed. No theorem is used as an external black box and no mathematical program was executed.**

## 1. Exact admission, order and input boundary

Main explicitly DENIED an external KYP/positive-real source and instead permitted this in-house complete elementary scalar proof: actual b/a positivity, an explicit even polynomial, and a per-member Gram/two-square certificate with margin, keeping the SAME b across the four actual vertices and NOT assuming a common quadratic matrix. That ruling was received while w45 was live and was held as NEXT duty. The ENTIRE w45 review was ACTUALLY RETURNED at the16:26:45 pin/send observation BEFORE this scalar derivation began; no SPR proof was interleaved with it.

The original frozen S1 definitions and the explicit current in-house ruling are the task inputs. The elementary four-member original-object interface is supplied in current `prerequisite-derivation-v3-four-member-interface.md`,108LF/12883B, SHA256 `9297cd6899346e9a80a187965065a3ca9c87f8e1a857040996679b0345a7eb04`. It remains an unreviewed current candidate, not an old adopted theorem. A combined original-box application must read its full proof as well as this one.

No external KYP source, state-space/companion identity, common-Lyapunov assertion, source-paper proof, old dual-lift/contact/phase-comparison body or ZERO consumer is an input. The stopped higher-contact route remains NONINPUT. Prior familiarity is not denied and no private-cognition/non-influence clearance is inferred. This proof uses only ordinary real/conjugate polynomial factorization, elementary algebra, nonnegativity and compactness; the special certificate consequences are proved below.

## 2. Actual scalar objects and explicit EVEN polynomial

Let a_i(s)=s^7+sum_(j=0..6)a_(i,j)s^j be any ACTUAL monic Hurwitz septic member, in particular one of the four coupled actual members of the original independent box. All its coefficients are real. Let b(s)=sum_(j=0..7)b_j s^j be the SAME real polynomial for every i; its degree is at most7 initially. Exact degree7 will either be a hypothesis of the original formulation or be forced by the certificate itself.

Set
`A_i^ev(t)=a_(i,0)-a_(i,2)t+a_(i,4)t^2-a_(i,6)t^3`,
`A_i^od(t)=a_(i,1)-a_(i,3)t+a_(i,5)t^2-t^3`,
`B^ev(t)=b_0-b_2t+b_4t^2-b_6t^3`,
`B^od(t)=b_1-b_3t+b_5t^2-b_7t^3`.
The explicit real polynomial of degree at most7 is
`P_i(t)=B^ev(t)A_i^ev(t)+t B^od(t)A_i^od(t)`.
Its constant is a_(i,0)b_0 and its coefficient of t^7 is b_7.

The requested explicit EVEN frequency polynomial is
`E_i(w)=P_i(w^2)=Re[b(iw) a_i(-iw)]`.
This identity follows by multiplying `b(iw)=B^ev(w^2)+iw B^od(w^2)` and the conjugate of the analogous a_i value. The cross terms are imaginary. Thus E_i is an even real polynomial of degree at most14; its top coefficient is b_7. There is no selected frequency substitution or numerical check in this universally quantified identity.

Since a_i is Hurwitz, its imaginary-axis denominator never vanishes and
`Re[b(iw)/a_i(iw)]=E_i(w)/|a_i(iw)|^2`.
Consequently strict ratio positivity at EVERY finite real w, including0, is exactly E_i(w)>0 there, which is exactly P_i(t)>0 for EVERY t>=0. This uses the ORIGINAL b/a direction directly; no reciprocal or numerator-stability theorem is invoked. Analyticity on the closed right half-plane is paid by the actual denominator a_i being Hurwitz.

## 3. Exact degree and the compactified strict margin

If b has EXACT degree7 and every finite-frequency ratio is positive, then b_7 is nonzero. A negative b_7 would make P_i(t) negative for sufficiently large positive t, so b_7>0. Therefore strict positivity at infinity for the normalized polynomial is AUTOMATIC in the original exact-degree problem.

Write x=t/(1+t) and define `R_i(x)=P_i(t)/(1+t)^7` for0<=x<1, extended by R_i(1)=b_7. Every term is a polynomial in x and1-x, so R_i is continuous on[0,1]. If P_i is positive on the half-line and b_7>0, it is positive at EVERY point of this compact interval. It has a positive attained minimum mu_i.

For finitely many actual members, choose ONE common epsilon>0 no larger than the minimum of their positive mu_i. Then
`Q_i(t):=P_i(t)-epsilon(1+t)^7>=0 for EVERY t>=0`
for every member. This is an existence argument for arbitrary data, NOT a computed margin or a selected plant/parameter test. The common margin costs no common-matrix hypothesis.

Conversely such a positive epsilon forces P_i>0 on the half-line and b_7>=epsilon>0 by its top coefficient once the nonnegative representation below is supplied. Thus the certificate itself enforces exact degree7 even if b was initially allowed degree at most7.

The positive leading condition cannot simply be omitted when discussing a seventh-degree weight: if the actual degree drops, P_i/(1+t)^7 tends to0 and a positive seventh-degree uniform margin need not exist. That is why exact degree/infinity is stated and paid rather than hidden in a noncompact strictness argument.

## 4. Elementary half-line factor lemma, INCLUDING all residual degeneracies

**Lemma.** For EVERY real polynomial Q of degree at most7,
`Q(t)>=0 for all t>=0`
IFF there are real polynomials F,G of degrees at most3 with
`Q(t)=F(t)^2+t G(t)^2`.
The zero polynomial and boundary/interior zeros of Q are included.

**Reverse direction:** both terms are nonnegative on t>=0.

**Forward direction, complete factor construction.** If Q is identically zero, take F=G=0. Otherwise its leading coefficient is positive, since a nonzero polynomial nonnegative for all sufficiently large positive t cannot have negative leading coefficient. Factor it over the reals into real linear factors and conjugate-pair irreducible quadratics. This ordinary finite-degree root factorization is the only factorization foundation used; no positivity/Gram theorem is imported.

Any positive real root must have EVEN multiplicity: after removing its root power, the remaining continuous nonzero factor has constant sign near that root, and an odd power would change Q's sign on two sides within the positive half-line. A root at0 may have ANY multiplicity. Negative real roots may have any multiplicity. Each irreducible real quadratic is a conjugate-pair factor `(t-u)^2+v^2` with v>0.

Every necessary elementary factor is already a norm of the required kind:

- A positive constant c is `(sqrt(c))^2+t*0^2`.
- The boundary-root factor t is `0^2+t*1^2`.
- A negative-root factor t+alpha, alpha>0, is `(sqrt(alpha))^2+t*1^2`.
- An even positive-root factor `(t-r)^2`, r>0, is `(t-r)^2+t*0^2`.
- For an irreducible quadratic put d=sqrt(u^2+v^2)>|u|. Then
  `(t-u)^2+v^2=(t-d)^2+t*(sqrt(2(d-u)))^2`.
  The equality follows by expansion; the square-root argument is positive because v>0. These are symbolic real factors, not roots computed for a chosen polynomial.

Finally the exact polynomial identity
`(F1^2+tG1^2)(F2^2+tG2^2)`
`=(F1F2-tG1G2)^2+t(F1G2+F2G1)^2`
closes this class under products. Applying it to the universally factored Q and repeated factors gives real F,G. No factor is dropped at a zero, no sign division or inverse of a vanishing quantity is used, and no finite root list is numerically enumerated.

It remains to pay the DEGREE bounds. If F/G are nonzero, the two summands have highest degrees2deg(F) and1+2deg(G), one even and the other odd. Their highest powers therefore cannot cancel. Their leading square coefficients are also positive. Since deg Q<=7, one gets deg F<=3 and deg G<=3. If either polynomial is zero omit that summand; the same bounds hold. This proves the whole lemma, including residual degree drop, boundary multiplicity, repeated roots and Q=0.

## 5. Exact scalar two-square certificate WITH margin

Combining §§2–4 gives, for an ACTUAL Hurwitz monic septic a_i and an exact-degree7 b, the equivalence of:

1. `Re[b(iw)/a_i(iw)]>0` for EVERY finite real w, including0.
2. `P_i(t)>0` for EVERY t>=0 and b_7>0.
3. There are epsilon_i>0 and real F_i,G_i of degrees at most3 with the polynomial identity
   `P_i(t)=epsilon_i(1+t)^7+F_i(t)^2+tG_i(t)^2`.

For several members, ALL epsilon_i can be replaced by ONE positive epsilon, by the finite compact minimum argument in §3 followed by the full residual lemma. The SAME b remains unchanged. The F_i/G_i are independent member certificates, not independently chosen numerators.

Equivalently the even frequency polynomial satisfies
`E_i(w)=epsilon(1+w^2)^7+F_i(w^2)^2+[w G_i(w^2)]^2`.
This is literally a sum of TWO ordinary real polynomial squares plus the explicit positive margin. The even square has degree at most6 in w and the odd square at most7. All real frequencies, positive/negative/zero, are included at once.

At0 this gives `a_(i,0)b_0=epsilon+F_i(0)^2>0`. Actual monic Hurwitz denominators have a_(i,0)>0, so b_0>0. At infinity its leading coefficient is `b_7=epsilon+(leading coefficient of G_i at degree3)^2>=epsilon>0`. No leading or zero-frequency condition has been supplied by a fabricated extra caller.

## 6. Explicit per-member Gram formulation and its LOSSLESS converse

Let `z(t)=(1,t,t^2,t^3)^T`. The scalar conditions are also equivalent to existence of ONE epsilon>0 and, for each actual member i, separate real symmetric PSD matrices M_i,N_i of size4 with
`P_i(t)=epsilon(1+t)^7+z(t)^T M_i z(t)+t z(t)^T N_i z(t)`.

The two-square certificate supplies such matrices directly: if f_i and g_i are the four coefficient vectors of F_i and G_i, choose M_i=f_i f_i^T and N_i=g_i g_i^T. They are PSD and each has rank at most1. Thus the necessary certificate is not asserted on the strength of an external semidefinite theorem.

Conversely ANY PSD M_i,N_i give nonnegative quadratic forms for EVERY real z(t), hence a nonnegative residual on t>=0. The positive margin proves scalar strictness. Its top coefficient is `epsilon+(N_i)_(3,3)>0`, where indices run0..3; the even quadratic form contributes no seventh-degree term. Thus exact degree/infinity is paid for general Gram matrices too. Applying the fully proved residual lemma to that SAME nonnegative residual can also produce alternate rank-at-most1 matrices at the SAME epsilon. No claim that the original matrices themselves had rank1 is made.

This proves that allowing general PSD member matrices is LOSSLESS for the original scalar positivity problem. It is not an unproved relaxation whose sufficiency was guessed, and not a common-quadratic-matrix condition.

## 7. Finite coefficient identities, SAME numerator and independent member certificates

Write `P_i(t)=sum_(k=0..7)c_(i,k)(b)t^k` using the explicit product in §2. Every c_(i,k) is real LINEAR in the shared eight b coefficients, because the actual a_i is fixed. The Gram identity is precisely the following coefficient equations, for k=0,...,7:

`c_(i,k)(b)=epsilon*binomial(7,k)`
` +sum_(r,s=0..3, r+s=k)(M_i)_(r,s)`
` +sum_(r,s=0..3, r+s=k-1)(N_i)_(r,s)`.

Empty sums are0. Both orders of an off-diagonal entry are counted by the displayed r,s sums, so no hidden factor2 is missing. These are explicit finite linear identities together with epsilon>0 and memberwise PSD constraints. They were NOT generated, solved, tested or optimized by a program.

Across the FOUR actual coupled members there is ONE b and ONE optional common epsilon; there are separate M_i,N_i for each i. Nothing assumes M_i=M_j, N_i=N_j, one common state-space P, or that four unrelated numerator choices can be assembled afterward. Conversely independently feasible certificates with different b would NOT supply this system or solve the original problem.

If desired, positive homogeneity permits b_7=1: divide b, epsilon and all Gram matrices by the positive b_7, preserving positivity and every coefficient identity. This loses no original witness. No boundedness, optimizer attainment, numerical solvability or uniformly chosen Gram formula across all boxes is inferred from normalization.

## 8. Exact original-box caller and what remains unpaid

For the four ACTUAL coefficient-coupled members constructed in v3, a shared b/positive-margin/per-member Gram solution is NECESSARY AND SUFFICIENT for the original all-member septic SPR property. The scalar equivalences here pay each member; the FULL elementary value-rectangle proof in v3 pays passage to/from every denominator of the same box. Degenerate coefficient intervals merely repeat some member constraints and do not require distinct matrices or positive widths.

The margin epsilon bounds a NORMALIZED PAIRING. It is not automatically the same numerical bound on the literal real ratio. For a fixed actual denominator its normalized modulus square is continuous/positive on the compactified half-line, and has a finite positive maximum. Dividing the pairing bound by that maximum gives a positive literal ratio margin. For the full compact original box the same elementary compactness argument supplies a common denominator bound. No actual value of either margin is computed.

The original remaining obligation is still: show that this shared-b system is feasible for EVERY actual robustly Hurwitz monic septic box, or provide ONE genuine eligible box for which it is infeasible with a sound original-object obstruction. Existence of a positive residual representation for each already-positive P_i does NOT prove a common b exists. A positive-real name, per-member certificates, or a finite encoding does not fill that quantifier.

This packet supplies the specifically requested complete scalar/certificate equivalence, with ALL strict/degree/endpoint/degenerate and same-numerator hypotheses. It is classical-content reconstruction/usable exact interface, not a claimed new universal theorem, actual negative box, solved original problem or novelty result. It must be fully reviewed with the v3 caller before any parent adoption.

## 9. Permanent limits and continuation boundary

External KYP/positive-real sources remain UNADMITTED. No source theorem is imported by name, no companion realization or common Lyapunov matrix is assumed, and no old higher-contact/phase-comparison/dual-lift body or ZERO consumer is reopened. The declared input chain is a conventional written one, not a private-cognition/non-influence certificate.

All original and new findings, including the checkpoint003 cadence gap, remain permanent. Same existing owner/new exclusive root; old round CLOSED/FROZEN; SPR78 outside current S1, the higher-contact STOP, HOLDv2, N4 UNKNOWN with historical child exit unestablished and auxiliary214 STOP persist. No scientific interpreter/calculator/Eval arithmetic/CAS/program/enumeration/solver/replay/build/test/typechecker, selected state/control/box/parameter/boundary/decimal probe, modelCLI/nested agent/newGO/Git/delete/contact/publication/infrastructure action occurred. Only metadata dates/hashes/counts were executed.

Research deadline remains2026-10-31T21:23:27.000Z. Same-harness WRITTEN does not imply formal/kernel/human/configured-family/executable, source-proof or novelty acceptance. The next scientific step must address the genuinely shared-b feasibility/coupling or a sound actual-box obstruction, not silently reintroduce an excluded method or treat this equivalence as existence.
