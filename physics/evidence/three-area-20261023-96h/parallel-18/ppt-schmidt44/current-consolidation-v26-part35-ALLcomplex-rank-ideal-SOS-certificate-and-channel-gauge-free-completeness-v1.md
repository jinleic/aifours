# P44 v26 — PART35: ALL-complex physical-coordinate RANK-IDEAL certificate, channel-gauge-free completeness and essential rank terms

PhysicsPPT44-2. Actual preceding `/bin/date`: **Mon Oct 26 09:53:41 PDT 2026**. **AUTHOR-WRITTEN / LATER UNREVIEWED.** Exact ALL-variable polynomial/determinantal proof only. No scientific interpreter/program, chosen state/control/parameter/numeric/boundary/limit/trig/magnitude probe, decimal or machine check. No actual W,rho,gamma/certificate is supplied; P44 remains UNMET.

## U0. Authority, immutable sources and ordinary trust cut

Actual EXPLICIT future-only v57 **c6d6ea7eea5c2734fb96caa9cd29fde4a551150e2e3ce7c1d6ff2b441aba5dc7** was read ENTIRE before resumed source/proof, including raw untruncated direction21/ending22–23, after Main's complete wholeACK/finding149/addendum read. No general-ACK self-release, new GO or redundant ACK loop.

The route uses LITERAL Part33's rational quotient-real-Nullstellensatz proof and LITERAL Part34's universal SOS obstruction, plus frozen Part32's explicit source definitions/coupling. Part33 SHA256 **5a344ac15ad76f609acb3007ca60ab3dafbc053547c5b9fdc090d0342d158ae3**,128LF/15501B; Part34 SHA256 **642f1e5446372703cf17e608fe8126a298b572d7f58adecc4c8ec95480aa1507**,165LF/15827B; Part32 SHA256 **18aaa105718e74dc524169fad0a26539a9fa5bafd704dae3ff43f5dd5d7605c6**,126LF/13246B. New lead was fully saved in checkpoint155 BEFORE this literal packet.

ENTIRE post143 UNWRITTEN continuation and every consuming representation/source-guidance remain ZERO/no salvage/retest/repair/replay/backconversion/search direction. This is not a verified counterfactual unaffected/private-cognition claim. Recognized separation failure requires immediate STOP/report/WAIT. No chosen fixed control is hidden as a source parameter.

**Imports:** Part33's ordinary I-RP (proper SOS cone=>real-prime/orderable quotient fraction field=>real closure), I-RCF (completeness of real closed fields with rational constants), elementary complex rank/minor theorem/Cauchy–Binet, real polynomial quotient algebra, and the elementary Part34 obstructions where expressly used. These are WRITTEN named imports, not a formal library/axiom audit or independent source novelty verification. Original-existence use of Part32 retains its ENTIRE UNREVIEWED Part31/24/27/29/30 input union.

## U1. The variables are an ARBITRARY complex COEFFICIENT matrix — NOT a density matrix

Let W be ANY Hermitian16x16 matrix over Q(i), gamma ANY rational number, and use source-fixed x0=vec(diag(I2,0)), Pi=I16-x0x0^dagger/2. Put Z=W-gamma Pi.

Let X be an ARBITRARY COMPLEX4x4 coefficient matrix. Its16 real parts and16 imaginary parts are32 independent REAL coordinates x. In particular X is NOT required Hermitian, PSD, trace-one, diagonal or real. W/rho being Hermitian elsewhere never justifies imposing Hermiticity on this amplitude matrix.

Write `g_Z(x)=vec(X)^dagger Z vec(X)` in Q[x], a REAL quadratic polynomial. The target is the ENTIRE global condition

`g_Z(x)>=0 for EVERY COMPLEX X with rank(X)<=2`.           (G_X)

For every pair I,J of THREE-element subsets of{1,2,3,4}, define Delta_IJ(X)=det(X_IJ). There are SIXTEEN complex minors. Their real and imaginary parts

`R_IJ(x)=Re Delta_IJ(X)`, `S_IJ(x)=Im Delta_IJ(X)`

are THIRTY-TWO rational/integer-coefficient real CUBICS. The standard complete rank criterion gives

`rank(X)<=2 IFF ALL R_IJ=0 AND ALL S_IJ=0`.                (R)

This includes ALL rank2/rank1/rank0 and every singular/coincident phase boundary. It requires ALL row/column minors, not just principal minors, real parts, the4x4 determinant or2x2 minors. No sample or chosen matrix is used to justify R.

Adjoin one arbitrary real t and set `h_X(x,t)=1+t² g_Z(x)`. This has total degree<=4. Then G_X is IFF emptiness of the PURE-EQUATION system

`R_IJ=0, S_IJ=0 for ALL I,J;   h_X=0`.                   (E_X)

If G_X holds, h_X>=1 on the rank variety. Conversely a negative g_Z at any arbitrary rank<=2 X gives a real square root t²=-1/g_Z and hence a solution. This is a quantified proof, not a chosen numerical point/control or a solver call. No unit-norm/phase chart or compactification is needed.

## U2. Exact FULL-global rational rank-ideal certificate theorem

**Theorem U2 — WRITTEN at I-RP/I-RCF and R.** For EVERY rational-data W,gamma, G_X holds IFF there are FINITELY many rational polynomials A_j,B,C_IJ,D_IJ in the33 real variables(x,t) with the EXACT identity

`-1 = sum_j A_j(x,t)^2 + B(x,t)[1+t² g_Z(x)]`
`     + sum_(I,J)[C_IJ(x,t) R_IJ(x)+D_IJ(x,t) S_IJ(x)]`.  (D)

All degrees/supports are finite but unbounded here. Multipliers C,D are signed arbitrary polynomials, not separately required nonnegative. The SOS part is REAL rational squares. The aggregate rank-ideal contribution is indispensable in the normalized situation proved in U6; ignoring it changes the theorem.

Sufficiency: at any common real zero of E_X, D would give-1=sum A_j²>=0, impossible. Hence E_X is empty and G_X follows for EVERY complex rank<=2 matrix. This is not a finite-state/phase test, Hessian criterion or bare-SOS certificate for g_Z on the entire unconstrained matrix space.

Necessity is the quotient-real-algebra argument in U3. There is no assumption that the displayed minor ideal is prime or real radical, and no inversion of a selected submatrix; all rank/zero strata remain.

## U3. Rational-coefficient completeness for the FULL generated ideal

Let J be the ideal in Q[x,t] generated by ALL32 polynomials R_IJ,S_IJ and h_X. Suppose E_X has no real point but D does not exist. In A=Q[x,t]/J, this says-1 is not a finite sum of squares: a sum-of-squares equality there would lift to D because membership in this FINITELY GENERATED ideal is a finite polynomial combination of its displayed generators.

By I-RP a real prime quotient of A has an orderable fraction field; its real closed extension L supplies a common zero of ALL generators. Their simultaneous existential zero sentence has rational coefficients and therefore, by I-RCF, also has a solution in R. This contradicts emptiness. Thus-1 is a sum of squares in A, and lifting gives D with rational polynomials.

This proves the needed MULTI-equation real Nullstellensatz over Q from the same named background as Part33, rather than importing an unexamined complex Nullstellensatz or approximating a real Gram solution by rationals. The rationality is exact quotient algebra, not density. Finitely many generators imply finitely many multipliers; no degree, height, runtime, resource or search-prefix bound is obtained.

The input equality generators are cubics and one quartic, compared with Part33's single degree6 factor polynomial. That is a precise GENERATOR-degree observation only, NOT a certificate-degree reduction theorem, computational-efficiency claim or executable admission.

## U4. Every certificate can be pulled back to a channel-GAUGE-INVARIANT Part33 certificate

Substitute X=UV^dagger with arbitrary complex4x2 U,V. By Cauchy–Binet/exterior cube of a TWO-dimensional channel space, EVERY3x3 minor of UV^dagger vanishes IDENTICALLY as a polynomial, including its real and imaginary parts. No generic full-rank assumption or numerical check is required.

D therefore pulls back to

`-1=sum_j a_j(U,V,t)^2+b(U,V,t)[1+t² f_(W,gamma)(U,V)]`,

where `a_j=A_j(UV^dagger,t)` and `b=B(UV^dagger,t)` are rational polynomials. This is EXACTLY Part33's certificate C.

For EVERY invertible complex2x2 channel S, the action U->US,V->VS^(-dagger) preserves X, so these individual a_j AND b are channel-GAUGE-INVARIANT. Thus whenever the global rational gap holds, Part33 C can ALWAYS be chosen to descend to the physical matrix X,t, not merely arbitrary factor coordinates. No noncompact group averaging/Reynolds operator, invariant-theory oracle or new SOS assumption is used: the full matrix rank-ideal certificate constructs the descent directly.

“Channel-gauge-free” means that D uses physical X instead of factorization columns U,V. It does NOT remove global physical phases or restrict X to a phase/chart; the original ALL-complex domain remains. Matrix-space variables and factor-space variables each number32 real coordinates here, but their nonlinear maps/constraints differ; no linear bijection is asserted.

## U5. This does NOT contradict Part34's bare-SOS impossibility

Part34 proves that F_Z(U,V) itself is SOS IFF Z>=0. It does not forbid a higher-degree identity with a general B and actual rank-ideal terms. D is an equality in the FULL polynomial ring with those determinantal multipliers; after pullback they vanish, leaving the coupled auxiliary certificate, not f=sum quadratic squares.

No conclusion that g_Z is SOS, f is SOS, B has a sign, the minor multipliers are PSD, or the global inequality follows from the normal-form Hessian is taken. The rank ideal and auxiliary contradiction variable are precisely what permits the full-global certificate while the bare-SOS family excludes the whole normalized domain.

## U6. ENTIRE normalized-domain safeguards: rank terms and BOTH variable dependences are necessary

For ANY source-normalized W with W x0=normal I2 and any real gamma, Z=W-gammaPi satisfies q_Z(x0)=0 but Zx0=normal I2!=0. Thus Z is NOT PSD, as proved elementarily in Part34.

Suppose a D certificate exists for such data and its COMBINED rank-ideal contribution

`K(x,t)=sum_(I,J)[C_IJ R_IJ+D_IJ S_IJ]`

is the ZERO polynomial. Then D without rank terms would prove h_X has no real zero on the ENTIRE unconstrained complex matrix space. The same t-square contradiction would imply g_Z>=0 for ALL X, hence Z>=0, contradiction. Therefore K CANNOT be the zero polynomial.

Merely displaying a formally nonzero C or D is insufficient: polynomial syzygies can give a zero aggregate. The exact statement is nonzero aggregate rank-ideal contribution, not an arbitrary count of nonzero multipliers. No actual coefficient candidate is evaluated here.

By U4, D also yields a Part33 C certificate. Part34 proves no such normalized C can have b independent of t or independent of the factor coordinates. Hence B's restriction along X=UV^dagger must genuinely depend on BOTH physical matrix coordinates AND auxiliary t. Formal dependence only through rank-minor terms that vanish on this variety does not count.

This excludes B(X)-only, B(t)-only and constants, regardless of degree. It is NOT a claim of multiplicative irreducibility or a proof excluding every additively separable B1(X)+B2(t); “both-variable dependence” means exactly not independent of either variable set. General B(X,t) remains allowed and is guaranteed existentially when G_X holds at I-RP/I-RCF. No certificate coefficients, feasible degree or scientific computation is supplied.

## U7. Original counterexample application and exact remaining gap

At the ENTIRE UNREVIEWED Part32/31/24/27/29/30 reduction, an original4x4 PPT-SN>2 counterexample exists IFF there are Gaussian-rational source-normalized W, positive rational gamma, Gaussian-rational trace-one rho with rho>0,rho^Gamma>0, Tr(Wrho)<0, AND a finite exact D certificate for the SAME W,gamma.

Forward: Part32 supplies the rational full-gap data; U2 supplies D. Reverse: D proves the ENTIRE all-complex rank<=2 gap; the actual strict negative PPT pair then gives the original counterexample. All matrix positivity/normalization constraints remain exactly those of Part32, with optional rational Sylvester/LDL certificates as explained in Part33. No constant selected state/control or repaired withdrawn family is supplied.

This is CONDITIONAL original-existence equivalence at the named unreviewed source union plus ordinary real-algebra imports, not unconditional adoption or an actual original solution. The fixed-rational-data equivalence U2 itself needs no Part31 normalization theorem; it holds for EVERY rational W,gamma by the displayed equations and I-RP/I-RCF.

The harder gap is STILL an ACTUAL W,rho,gamma and polynomial identity D, OR an ALL-data proof none can exist. No coefficient list, SOS solution, negative PPT pair, degree/support/height/resource bound or execution is delivered. A bounded-degree/selected-support failure cannot exclude all D certificates. No solver/interpreter/replay/new GO, world novelty/SOTA/source-absence, parent/formal/kernel/human/configured-family/executable/triple/novelty acceptance follows. Generic real-algebra certificates may be standard; the progress is a complete alternative representation and the exact safeguards, not scientific outcome credit.

## U8. Whole state, permanent history and immutable operational boundary

Prior34parts+TWOaddenda/ALLdeclared leads/TWOactualpositive-PRIOR KG+MOM intake FILES remain; JL362logical reader is EXPOSURE metadata ONLY, not a third intake/proof/adoption/guidance. Parts24–35 are LATER UNREVIEWED where not individually adopted, not verified unaffected by history. No old source/hash/positive review transfers approval to a new body. This successor changes NO pinned/reviewed file.

Own8797d022/new3c1edecd continued-source/unwritten/scope-concern/delayed-recognition findings persist, ENTIRE post143 UNWRITTEN/guidance ZERO/no salvage/retest/repair/replay/backconversion, no invented immediate-at-probe clean stop/separate knowingly-recognized interval/precise private clock. Cadence149 FULL33m12s/even31m45s plus parent delayed handling persist, not cured by v57 or later proof. All cp049/063/081/083/085/089/oldcp013/admission/ACK/cadence/falsequotation/source/parentv9–v57/other-owner/previewv48 histories remain; N4 UNKNOWN/incomplete/overrun/historicalexit-unestablished, old21 NOT_RECONSTRUCTED, auxiliary214 STOP, oldFOUR minors/ELEVEN later proper-domain qualifiers/C27 normalizedN4 ZERO new-method credit/QD-NR. D-N2 false quotation rejected/source already>=0/no author patch. No blind-family/private-cognition/runtime/cadence/clean-history/global-owner census.

Exact source-fixed/ALL-variable conventional WRITTEN/fractions/integer products only, including privately. NO scientific interpreter/eval/calculator/CAS/program/enumeration/solver/replay/CLI/build/test/nestedagent/newGO; no chosen state/code/control/parameter/boundary/limit/numeric/magnitude/trig probe EVEN rational/decimal/withdrawn-guide/source-fraction decimal restatement. No machine check. Exclusive own root/frozen shared bytes immutable/no Git/deletion/publication. Same original eighteen, full original primary, science cutoff **2026-10-27T11:05:38-07:00**, deadline **2026-10-27T12:35:38-07:00**, substantive actual-clock checkpoints<=30minutes. Active writing, NOT early final park/round closeout.

**END OF COMPLETE v26 PART35. P44 remains UNMET.**
