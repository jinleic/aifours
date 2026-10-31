# Septic interface VI — an all-half-line integral gauge makes the SHARED-b Gram problem compact, with an attained margin

Owner **InfoSPR7-2**, same info-2. Actual `/bin/date` immediately before this write: **Tue Oct 27 16:47:35 PDT 2026**.
**WRITTEN author-unreviewed. Complete elementary compactness/attainment theorem for a NEW explicit primal model, not a universal synthesis solution or a legacy contact-attainment claim.**

## 1. Inputs, exact purpose and scope

Continue only original S1 and Main's admitted IN-HOUSE scalar/Gram task. Correctness inputs are the original monic septic definitions, elementary polynomial/linear algebra/integration/compactness, and the complete CURRENT proofs:

- v3 four-actual-member original-object interface,108LF/12883B, SHA256 `9297cd6899346e9a80a187965065a3ca9c87f8e1a857040996679b0345a7eb04`;
- v4 scalar strict-margin/per-member Gram equivalence,138LF/15371B, SHA256 `1172b667e4b740fc0d005ee2bea46c394c9ba1cee7ec226bd2e131335e4317d5`.

They are current author candidates, not adopted inputs by filename. A full original-target gate must read their entire proofs AND this manuscript. Current v5 explains why monic/strict-margin normalization alone does not give bounded variables; it is context rather than a correctness premise here.

No external KYP/positive-real source, state-space theorem, common-quadratic P, old dual/contact/phase-comparison chart, higher-contact continuation or ZERO guide is used. No frequency is sampled, specialized or evaluated. The gauge below integrates over the ENTIRE half-line and is NOT a finite positivity test. The parent L1 quarantine remains binding/NONINPUT; no physics/L1 mathematical content is used.

Fix ANY actual original independent monic degree7 coefficient box K, closed nonempty intervals with degeneracies allowed, EVERY member Hurwitz. Let a_1,...,a_4 be the coupled actual parity-extremal members defined in v3, possibly repeated. Let b(s)=sum_(j=0..7)b_j s^j initially have degree at most7. Write P_i(t) for v4's explicit real pairing polynomial, so
`P_i(w^2)=Re[b(iw) a_i(-iw)]`.
The SAME b occurs in every i. All constants in the compactness proof may depend on this fixed actual K; there is no asserted uniform coefficient bound across the unbounded universe of all boxes.

## 2. A strictly positive linear functional on the nonnegative polynomial cone

For EVERY real polynomial P of degree at most7 define
`L(P)=integral_(0..infinity) P(t)/(1+t)^9 dt`.
It is absolutely finite: each monomial t^k/(1+t)^9 is integrable for0<=k<=7, and a finite coefficient sum bounds the absolute integrand.

This is an explicit continuous LINEAR coefficient functional. If P(t)=sum c_k t^k, then
`L(P)=sum_(k=0..7) c_k * k!*(7-k)!/8!`.
Here is the elementary integral proof, not a numerical integration. Substitute x=t/(1+t); the monomial integral becomes `integral_0^1 x^k(1-x)^(7-k) dx`. For nonnegative integers r,s, integration by parts gives
`I_(r,s)=r/(s+1) I_(r-1,s+1)` when r>0,
and `I_(0,s)=1/(s+1)`. Repetition yields `I_(r,s)=r!s!/(r+s+1)!`. This gives the stated rational coefficients with no computed table, selected parameter or external integral formula.

If P>=0 on the half-line and P is not the zero polynomial, then L(P)>0. A nonzero polynomial cannot vanish on an interval; continuity therefore makes it strictly positive on some open positive-t interval, whose integration weight is positive. This is a universal proof fact, not a chosen frequency test. Also, for psi(t)=(1+t)^7,
`L(psi)=integral_0^infinity (1+t)^-2 dt=1`.

**Cone-bound lemma.** The coefficient vectors of nonnegative degree-at-most7 polynomials with L(P)<=1 form a compact set.

**Proof.** Their nonnegative cone C is closed, being the intersection over all t>=0 of the closed coefficient half-spaces P(t)>=0. Use the Euclidean norm of the eight coefficient vector. On C intersected with the unit sphere, L is continuous and strictly positive. This is a compact set, so its minimum h is positive (if the slice were empty the bound would be trivial). Homogeneity gives `L(P)>=h||P||` for every P in C. Thus L(P)<=1 bounds every coefficient. The set is closed and bounded in finite dimension, hence compact. No unproved cone duality or closure of a projected semidefinite cone enters.

## 3. One ACTUAL stable denominator gives an injective coefficient map

For ANY fixed actual Hurwitz monic septic a, the linear map `T_a:b -> P_(a,b)` from real degree-at-most7 polynomials to real degree-at-most7 polynomials is invertible.

It suffices to prove injectivity. Suppose P_(a,b) is identically zero. The real polynomial
`H(s)=b(s)a(-s)+b(-s)a(s)`
has `H(iw)=2P_(a,b)(w^2)=0` for all real w, so H is identically zero. The polynomials a(s) and a(-s) have no common root: their roots lie in strict opposite half-planes. At each root of a, with its full multiplicity, H=0 therefore forces b to have that root with at least the same multiplicity, since a(-s) is nonzero there. Hence a divides b. Their degree bound gives b=c a for a real constant c, and then H=2c a(s)a(-s) forces c=0.

The two real coefficient spaces both have dimension8. The injective linear map is therefore bijective and has a continuous linear inverse. In particular, a coefficient bound on its pairing polynomial bounds b. Repeated roots of a cause no problem: the argument explicitly retained their multiplicities. No transfer-matrix, reciprocal or source-paper theorem is assumed.

This fact is only a coefficient-map statement. It does NOT say that a b selected for one denominator works for the other three.

## 4. The CLOSED auxiliary primal model — all member certificates retained

Choose ANY one reference member a_ref from the actual four; the theorem holds for EVERY such choice. Define F(K) as the finite-dimensional set of variables
`b in R^8`, `epsilon>=0`, and separate real symmetric PSD4x4 matrices M_i,N_i for i=1,...,4,
satisfying ALL polynomial coefficient identities
`P_i(t)=epsilon psi(t)+z(t)^T M_i z(t)+t z(t)^T N_i z(t)`,
`z(t)=(1,t,t^2,t^3)^T`,
and the ONE gauge inequality `L(P_ref)<=1`.

The identities are exactly v4's explicit linear coefficient equations, with the same b and epsilon across all members, but separate member matrices. NO common P or shared Gram matrix is imposed. The gauge is linear in b through the actual reference denominator.

This auxiliary set intentionally allows epsilon0 and degree loss at the boundary; it is not silently declared the original strict problem. The all-zero variables are feasible, so F(K) is NONEMPTY without assuming a nonzero weak common numerator or the original conjecture. Each feasible P_i is nonnegative on the ENTIRE half-line, because epsilon>=0 and the PSD forms are nonnegative there.

The model is CLOSED in its finite collection of real coefficients/matrix entries: polynomial identities are linear equalities, the gauge/epsilon constraints are closed linear inequalities, and PSD cones are closed (each is the intersection of quadratic-form half-spaces). The following proof, rather than the word “semidefinite”, pays boundedness.

## 5. Uniform bounds on b and epsilon for this fixed original box

For a feasible point, P_ref belongs to the nonnegative degree-at-most7 cone and L(P_ref)<=1. Section2 bounds its coefficients. Section3's actual-denominator inverse then bounds ALL b coefficients, with a finite bound depending on that fixed a_ref.

Every other P_i is a fixed linear coefficient map of the SAME b. Its coefficients, and thus L(P_i), are also bounded above by finite constants C_i depending on the actual members. Their nonnegativity gives L(P_i)>=0.

Applying L to the reference Gram identity gives
`L(P_ref)>=epsilon L(psi)=epsilon`.
Therefore EVERY feasible point satisfies `0<=epsilon<=1`. This uses the entire half-line positive functional, not the failed assumption that monic leading normalization alone bounds b or the matrices.

## 6. Uniform bounds on EVERY possible per-member Gram representation

Define the fixed real moment matrices, indexed r,s=0,...,3,
`H_(r,s)=integral_0^infinity t^(r+s)/(1+t)^9 dt`,
`J_(r,s)=integral_0^infinity t^(r+s+1)/(1+t)^9 dt`.
All entries are finite exact constants supplied by the formula in §2; no entry is numerically calculated. These matrices depend only on the fixed polynomial degree/gauge, not the box, a selected state or a chosen frequency.

Both are POSITIVE DEFINITE. For any nonzero real u in R^4, its coefficient polynomial q(t)=u dot z(t) is nonzero. Thus
`u^T H u=integral q(t)^2/(1+t)^9 dt>0`,
`u^T J u=integral t q(t)^2/(1+t)^9 dt>0`.
A nonzero polynomial has only finitely many zeros, and both weights are strictly positive on the positive half-line. Compactness of the unit sphere supplies positive constants h_H,h_J with H>=h_H I and J>=h_J I. Their values are not computed or asserted sharp.

For Q_i=P_i-epsilon psi, finite-sum integration of the Gram identity gives
`L(Q_i)=Tr(M_i H)+Tr(N_i J)`.
All quantities are finite since every polynomial degree is at most7. For PSD M and H>=h_H I, elementary real symmetric diagonalization of M yields
`Tr(MH)=sum lambda_r u_r^T H u_r>=h_H sum lambda_r=h_H Tr M`.
The analogous inequality holds for N,J. No source-specific representation theorem is used; these are ordinary finite-dimensional PSD trace inequalities.

Consequently
`h_H Tr M_i+h_J Tr N_i<=L(Q_i)=L(P_i)-epsilon<=C_i`.
Every trace is nonnegative, so BOTH traces are bounded individually. For a PSD matrix, its Frobenius norm is at most its trace, by its nonnegative eigenvalues. Thus every entry of EVERY allowed M_i,N_i is bounded. This applies to arbitrary PSD certificates, not only a specially chosen rank-one/two-square representation.

All variables of F(K) are therefore bounded. Combined with its proved closedness/nonemptiness, F(K) is a nonempty COMPACT set.

## 7. Attained objective and EXACT original-target equivalence

Define
`epsilon_star(K;a_ref)=max {epsilon : (b,epsilon,(M_i,N_i)) in F(K)}`.
The maximum EXISTS by compactness and continuity, and `0<=epsilon_star<=1`. This is a gauge-dependent certificate margin, not a computed value, intrinsic gain, optimal literal ratio, or uniform lower bound over all boxes.

**Theorem.** For the original actual K,
`there exists ONE unrestricted real exact-degree7 common SPR numerator`
IFF `epsilon_star(K;a_ref)>0`.

**Forward caller.** A genuine original numerator works against the four actual members by the proved v3 interface. V4 gives a SAME-b positive common margin and per-member PSD certificates. P_ref is strictly positive and nonzero, so L(P_ref)>0. Divide b, epsilon and all its member matrices by this positive scalar. Every identity and PSD condition is preserved, the gauge becomes1, and the margin stays positive. This is a point of F(K), so the attained maximum is positive.

**Converse caller.** If epsilon_star>0, an ACTUAL maximizer in F(K) has P_i>=epsilon_star psi>0 on the entire half-line. Its leading coefficient is
`b_7=epsilon_star+(N_i)_(3,3)>=epsilon_star>0`.
Thus b is EXACT degree7, not a lower-degree boundary artifact. The scalar proof in v4 gives the strict b/a_i condition at EVERY finite real w, including0, and the complete actual-four-member proof in v3 transfers it to EVERY member of K. This is the same b, not four separately realized numerators or a common-matrix approximation.

If epsilon_star=0, the auxiliary maximum may be attained at the zero variables or other weak/lower-degree boundary points. None is falsely promoted to an original strict witness. The theorem says only that no strict original witness exists IF that zero optimum were actually proved for this K. NO such actual box/value proof is supplied here.

At a positive optimum the gauge must equal1: its value is positive because it is at least epsilon, and if below1, positive rescaling to gauge1 would increase epsilon while preserving every member constraint. At zero optimum no such saturation or nonzero weak witness is assumed. This pays the otherwise troublesome empty/equality boundary cases.

## 8. Relation to the monic noncompactness barrier and scope of attainment

This does not contradict v5. That packet refutes boundedness of the MONIC section, even with a fixed positive margin. The present all-half-line gauge bounds a DIFFERENT homogeneous base. Its closed feasible set allows epsilon0 and degree loss only on a boundary explicitly rejected when extracting an original witness. It does not assert that the strict numerator set itself is closed.

The new theorem proves compactness and attainment for THIS explicitly defined primal margin problem at each FIXED actual original box. It supplies no uniform bounds over all possible boxes, no legacy critical-chart compactness/attainment, no higher-contact realization, and no retrospective payment of any older NR claim. It uses no stopped phase/comparison-polynomial or external KYP route.

All degenerate coefficient intervals and coincident reference/corner members are allowed: the inverse map uses only that the actual reference polynomial is Hurwitz, including repeated roots, and no distinctness of the four members. Infinity is handled by epsilon>0 forcing the leading degree; zero is handled by P_i(0)>=epsilon>0 and a_i(0)!=0. No endpoint assumption is silently lost under closure or rescaling.

## 9. Exact scientific delta and remaining original question

The delta beyond an encoding is a COMPLETE proof that an admissible common-b normalization exists with a NONEMPTY COMPACT joint coefficient/PSD feasible set and an ATTAINED optimum, with positivity of that optimum EXACTLY equivalent to the original strict septic target. This repairs one concrete failed compactness step without imposing a stronger common certificate or erasing the degree boundary.

The unresolved scientific question is STILL whether epsilon_star is positive for EVERY actual robustly Hurwitz original box, or whether ONE actual eligible K has epsilon_star=0 with a sound proof. Hurwitz stability alone has not been shown to force the sign. No solver, computation, selected box, numerical optimum, universal numerator, actual counterexample or original solution is claimed.

Ordinary foundations used: real/conjugate polynomial factorization and multiplicities, finite-dimensional linear algebra/PSD spectral decomposition, elementary integration by parts and continuity/compactness. Every special gauge/coercivity/injectivity/PSD-bound/original-caller step is supplied. No positive-real/SOS/KYP theorem is imported by name or an unread external proof used as a premise.

All results are author-WRITTEN/UNREVIEWED pending a complete frozen whole-scope review and parent source/return reads. No formal/kernel/human/configured-family/executable/novelty, intrinsic-gain or historical-source-equivalence acceptance. All old/new findings and ZERO consumers, parent L1 quarantine, SPR78 outside S1, accepted higher-contact STOP, HOLDv2, N4 UNKNOWN historical exit unestablished and auxiliary214 STOP persist.

No scientific interpreter/calculator/Eval arithmetic/CAS/program/enumeration/solver/replay/build/test/typechecker, sampled/selected numeric box/state/control/frequency/boundary/decimal probe, modelCLI/nested agent/newGO/Git/delete/contact/publication/infrastructure action occurred. Only metadata dates/hashes/counts were executed. Deadline2026-10-31T21:23:27.000Z unchanged.
