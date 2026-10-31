# Septic interface VII — compact functional dual, equality of attained margins, and an exact actual-box matrix obstruction

Owner **InfoSPR7-2**, same info-2. Actual `/bin/date` immediately before this write: **Tue Oct 27 17:26:09 PDT 2026**.
**WRITTEN author-unreviewed. In-house coefficient-cone/Gram continuation only; no external optimization theorem, frequency instance or old profile/contact method is imported.**

## 1. Current authority, corrected dependency and original objects

Main directed that after the ONE short additive v4 wording erratum I continue admitted S1 work. That erratum was written and reported BEFORE this continuation: `prerequisite-derivation-v4-degree-factor-erratum-v1.md`,9LF/850B, SHA256 `ebfbe087bacc6d91353e0cb60a28eb9fd674ba45137cf4fa149c9091af3110b8`. The factors have frequency degrees6/7; their squared terms have bounds12/14. Frozen v4 bytes are unchanged.

This is a genuinely coefficient-functional/PSD proof on the admitted in-house model, NOT the HELD post-v6 fixed-parity/profile construction or its selection/representation/confidence consumers. The parent provenance MAJOR and all quarantines remain. No historical same-parity construction, higher-contact/phase-comparison, atom-pattern classification, external KYP or source-paper proof is used. The declared proof chain is not an independent cognitive-noninfluence certificate.

Use the COMPLETE current elementary proofs: v3 actual-four-member equivalence (SHA256 `9297cd6899346e9a80a187965065a3ca9c87f8e1a857040996679b0345a7eb04`); v4 scalar/half-line/two-square/Gram equivalence (SHA256 `1172b667e4b740fc0d005ee2bea46c394c9ba1cee7ec226bd2e131335e4317d5`) WITH the erratum; v6 compact integral-gauge primal (SHA256 `8520af8b1f91c0e8274d3846c3a702e0f32b6e70c710cadac15e5a2753048fd7`). These are author candidates at their own current review/adoption states, not automatically adopted research imports. Every new duality step is proved below.

Fix ANY actual original independent monic Hurwitz septic box K and its four coefficient-coupled actual members a_i, with degeneracies/repetitions allowed. Keep the SAME real coefficient vector b in R^8. Let V be the real vector space of polynomials in t of degree at most7. Let T_i:b->P_i be the explicit linear pairing map of v4. Choose ANY actual reference member a_ref and write T_ref for its map. It is invertible by v6's full Hurwitz/opposite-root argument, including repeated roots.

Let C={P in V:P(t)>=0 for EVERY t>=0}, psi(t)=(1+t)^7, and L(P)=integral_0^infinity P(t)/(1+t)^9 dt. V6 proves C closed, positivity/coercivity of L on C, L(psi)=1 and the compact attained primal maximum epsilon_star in[0,1]. This is the NEW gauge-dependent certificate margin, not an intrinsic gain or a legacy contact optimum.

## 2. Exact finite PSD form of the polynomial functional cone

Define C*={y in V*:y(P)>=0 for EVERY P in C}. Write y_k=y(t^k), k=0,...,7. Set, for r,s=0,...,3,
`H_y(r,s)=y_(r+s)`, `J_y(r,s)=y_(r+s+1)`.

**Lemma 1.** y belongs to C* IFF BOTH real symmetric4x4 matrices H_y,J_y are PSD.

If y is positive on C, apply it to EVERY cubic square F(t)^2 and to EVERY tG(t)^2. Their values are f^T H_y f and g^T J_y g for arbitrary real coefficient vectors f,g, so the two matrices are PSD. Conversely the COMPLETE elementary half-line factor lemma in v4 writes EVERY Q in C as F^2+tG^2 with cubic-or-lower F,G, including Q0 and all root/degree degeneracies. The two PSD inequalities then give y(Q)>=0. This proves both directions, not merely a necessary truncated-moment condition.

H_y and J_y are NOT two independently chosen PSD matrices: their overlapping entries arise from the SAME eight y coordinates. There is no claim here that y has a selected atomic/frequency representation, and no such representation is needed or used.

## 3. Compact normalization of the positive functionals

The polynomial psi is an interior point of C. Indeed for a coefficient perturbation R(t)=sum r_k t^k,
`|R(t)|<=(sum |r_k|)psi(t)<=sqrt(8)||r|| psi(t)`
for EVERY t>=0, because each monomial t^k,0<=k<=7, is bounded by psi there. Choose ANY fixed positive delta with delta*sqrt(8)<1. For every coefficient-unit vector u, both psi+delta u and psi-delta u belong to C.

Therefore for y in C*, positivity of those perturbed polynomials gives
`delta ||y||<=y(psi)`.
In particular a nonzero y in C* has y(psi)>0. This is a universal coefficient-norm argument, not a polynomial/frequency test instance.

The base B*={y in C*:y(psi)=1} is consequently closed and bounded, hence compact. It is nonempty because L belongs to it. More generally the tuple set
`Y={ (y_1,...,y_4):y_i in C*, sum_i y_i(psi)=1 }`
is compact, convex and nonempty: each summand is nonnegative and bounds its own functional norm. Zero member functionals are allowed, but not all four zero. No strict positivity of each individual member or independent-copy hypothesis is inserted.

We also need the full cone test: P belongs to C IFF y(P)>=0 for EVERY y in C*, equivalently for every y in B*. Here is its elementary separation proof. If P is outside the nonempty closed convex cone C, choose a nearest Q in C; it exists by restricting the distance minimization to a finite ball. Put v=Q-P. Segment minimality gives `v dot (R-Q)>=0` for all R in C. Choosing R0 and R=2Q gives v dot Q=0; then v is in C*, while `v dot P=-||v||^2<0`. Normalizing by v(psi)>0 gives the required B* witness. The converse is positivity by definition. No unproved bipolar/source theorem is used.

## 4. Explicit compact dual candidate and weak inequality

For a functional y, define `T_i* y` as the coefficient functional `b -> y(T_i b)`. Let F_ref=T_ref*L; it is nonzero because T_ref is invertible and L(psi)=1.

Define the following finite-dimensional set D(K):
`lambda>=0`, `y_i in C*`,
`sum_i y_i(psi)=1`,
`sum_i T_i* y_i=lambda F_ref`.
These are explicit linear coefficient equations, one normalization and the PSD constraints of Lemma1. They retain the SAME b through the last functional identity. Arbitrary separate positive member data without that cancellation identity would NOT be an original obstruction.

D(K) is nonempty: y_ref=L, the other y_i0, lambda1 works. Its y tuples lie in compact Y. The last equation bounds lambda as well, since F_ref is fixed and nonzero. All constraints are closed. Thus D(K) is COMPACT and lambda_min=min_D lambda is attained, with0<=lambda_min<=1.

For ANY feasible primal point and ANY dual point, apply y_i to EACH residual `T_i b-epsilon psi` in C and sum:
`lambda L(T_ref b)-epsilon>=0`.
The primal gauge is at most1 and lambda>=0, so epsilon<=lambda. In particular
`epsilon_star<=lambda_min`.
This weak inequality is valid without a strictly feasible original numerator or a common Gram matrix.

## 5. A complete elementary compact bilinear interchange

The exact reverse inequality will use the following fact, whose proof is included to avoid importing an optimization theorem.

For ANY nonempty compact convex finite-dimensional sets X,Y and real continuous bilinear f,
`max_(x in X) min_(y in Y) f(x,y)=min_(y in Y) max_(x in X) f(x,y)`.

The left side never exceeds the right. Let v denote the left side and take ANY alpha>v. For every x choose some y with f(x,y)<alpha. Continuity gives a relative open cover of X by these inequalities; compactness supplies finitely many y_1,...,y_m. The compact convex image
`S={ (f(x,y_1),...,f(x,y_m)):x in X }`
is disjoint from the closed orthant O=[alpha,infinity)^m.

Choose a closest pair s0 in S,t0 in O. It exists because S is compact and the distance minimization in O may be restricted to a bounded set; the distance is strictly positive. Set p=t0-s0. Segment minimality in the two convex sets gives
`p dot s<=p dot s0<p dot t0<=p dot t` for every s in S,t in O.
Because O contains each positive coordinate ray from t0, every p_j is nonnegative. Since p is nonzero, its sum is positive. The minimum of p dot t over O is alpha times that sum. Normalize p to sum1 and put y_bar=sum p_j y_j, which belongs to Y. The displayed strict separation gives `max_x f(x,y_bar)<alpha`.

Hence the right side is at most EVERY alpha>v and therefore at most v. Both maxima/minima are attained by compactness; their value functions are continuous because the opposing set is compact/bounded and f is bilinear. This proves the interchange, including all degenerate set/boundary cases, using only finite-dimensional compactness and squared-distance segment inequalities.

No x,y,alpha here is an instantiated physical state, polynomial box, group, parameter or frequency; this is a proof for arbitrary abstract compact coefficient sets. No selected-case diagnostic is involved.

## 6. Apply the interchange to the ACTUAL shared-numerator problem

Use
`X={b:T_ref b in C, L(T_ref b)<=1}`.
It is compact and convex: v6's polynomial-cone coercivity bounds T_ref b, and its actual-Hurwitz inverse bounds b. It is nonempty because it contains0. For Y from §3 define
`f(b,(y_i))=sum_i y_i(T_i b)`.

For fixed b, the minimum over Y equals `min_(i,y in B*) y(T_i b)`. Indeed every tuple is a convex combination of normalized nonzero member functionals with weights y_i(psi), and tuples supported on one member are allowed. The cone test in §3 shows that this minimum is at least epsilon IFF all `T_i b-epsilon psi` belong to C.

Its maximum over X is nonnegative because b0 is allowed. Any maximizer with nonnegative value has all those residuals in C at that value; v4's FULL residual factor lemma supplies per-member PSD Gram certificates, including at epsilon0. Conversely every v6 primal feasible point lies in X and has no greater epsilon than that minimum. Thus
`epsilon_star=max_X min_Y f`.
This does not discard the other three constraints merely because X is bounded using the reference: they are present in the minimum over ALL member functionals.

The proved compact interchange gives
`epsilon_star=min_(y tuple in Y) max_(b in X) sum_i y_i(T_i b)`.
Choose an attained minimizing tuple y. Put F=sum T_i* y_i and h=max_X F(b)=epsilon_star>=0. On polynomial coefficients define `q(P)=F(T_ref^-1 P)`.

For every nonzero P in C, L(P)>0 and P/L(P) lies in the normalized reference base. Hence `q(P)<=h L(P)`. Thus z=hL-q belongs to C*. This is an actual coefficient-functional consequence of the attained support maximum, not a guessed common certificate.

Add z to the reference functional: y'_ref=y_ref+z, others unchanged. Then
`sum T_i* y'_i=h F_ref`,
and `r:=sum y'_i(psi)=1+z(psi)>=1`.
Normalize all y'_i and h by r. This gives an ACTUAL point of D(K) with lambda=h/r<=h=epsilon_star. Section4's weak inequality gives the opposite bound epsilon_star<=h/r. Consequently equality holds and
`lambda_min=epsilon_star`.

This includes epsilon_star0: r is still finite and at least1, normalized functionals remain nonzero collectively, and lambda0 is valid. At a positive optimum the inequalities force r1, but no such assertion is needed at the zero boundary. No primal interior/strict-feasibility assumption or external strong-duality theorem is hidden in the proof.

## 7. Exact actual-box matrix obstruction, with BOTH directions paid

Combining §§4–6 gives a finite dual minimum that is attained and equals the attained primal maximum. Together with v3/v4/v6:

- The ORIGINAL box has one unrestricted exact-degree7 common SPR numerator IFF epsilon_star=lambda_min>0.
- It has NO such numerator IFF there exist four eight-coordinate real functionals y_i with BOTH linked matrices H_(y_i),J_(y_i) PSD, total normalization `sum y_i(psi)=1`, and the exact SHARED-b coefficient cancellation
  `sum_i T_i* y_i=0`.

**Forward obstruction caller.** If such actual coefficient data exist and b were an original common numerator, v4 gives a positive common margin epsilon. Each positive functional is nonnegative on its member residual; summing forces `sum y_i(T_i b)>=epsilon>0`. The exact coefficient cancellation instead makes that sum0. Contradiction.

**Converse caller.** If the actual K has no original numerator, v6 gives epsilon_star0. The proved attained dual equality gives a minimizing point with lambda0, hence precisely those normalized nonzero functionals and cancellation. No unprovided frequency-atom realization, free critical tuple, positivity of a single matrix, or partial-case argument supplies the converse.

The actual a_i must be the coefficient-coupled four members of ONE registered K and the original all-member Hurwitz hypothesis remains. V3 pays whole-box equivalence; individual stability of an arbitrary unrelated four-tuple is not substituted for it. Degenerate intervals, repeated corners and repeated stable denominator roots remain covered.

This is an exact certificate in the polynomial FUNCTIONAL cone, not a physical density/operator or a selected finite-group model. It does not assert a contact/phase/atomic decomposition, and no such continuation is undertaken. The linked-matrix and shared-b equations are essential; dropping them would admit an invalid independent-data relaxation.

## 8. Scientific delta, remaining original sign and controls

The new result is a COMPLETE elementary equality of two COMPACT ATTAINED coefficient-cone optimizations, plus a finite PSD functional obstruction NECESSARY AND SUFFICIENT for original failure at any actual eligible box. It pays zero-boundary and shared-numerator callers, rather than relying on an unproved generic semidefinite duality/closure claim. It is not merely a renamed old contact chart or an assertion that arbitrary PSD blocks are realizable.

The ORIGINAL open question remains the SIGN for all actual boxes: prove lambda_min(K)>0 for EVERY robustly Hurwitz registered K, or supply ONE actual eligible K with the normalized zero-cancellation certificate. No such universal sign proof, actual zero-optimum box, numeric value, scientific computation, universal numerator or original counterexample is provided. The numerical margin is gauge/reference dependent, not an intrinsic optimal SPR ratio. Novelty/SOTA/priority are unestablished.

All dependencies and mathematical steps are in the supplied original definitions and CURRENT complete v3/v4(with its additive wording correction)/v6 proofs plus elementary coefficient/PSD/compactness facts, with separation/interchange proved here. No external KYP/positive-real/SOS/optimization theorem is imported by name or source proof accessed. No w82 return was opened; Main's reported0F/0M/1MINOR and this erratum do not constitute Main adoption or process absolution.

The conservative post-v6 provenance PROCESS MAJOR, entire fixed-parity/profile branch/ALL consumers HELD/ZERO/NONINPUT, the higher-contact STOP, externalKYP denial, parentL1 quarantine and all earlier findings persist. This resumed in-house coefficient-functional branch neither repairs nor consumes that quarantined construction; no independent/non-influence certification is inferred.

No scientific interpreter/calculator/Eval arithmetic/CAS/program/enumeration/solver/replay/build/test/typechecker, selected numeric box/state/control/group/frequency/boundary/decimal probe, modelCLI/nested agent/newGO/Git/delete/contact/publication/infrastructure action occurred. Only metadata dates/hashes/counts were executed. Same owner/new exclusive root/old round frozen/HOLDv2/N4 UNKNOWN historical exit unestablished/aux214 STOP; same-harness WRITTEN, not formal/kernel/human/configured-family/executable/novelty/adoption. Deadline2026-10-31T21:23:27.000Z unchanged.
