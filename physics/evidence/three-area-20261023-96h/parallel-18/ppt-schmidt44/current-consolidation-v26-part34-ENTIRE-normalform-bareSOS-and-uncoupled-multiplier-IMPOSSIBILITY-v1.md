# P44 v26 — PART34: ENTIRE normal-form domain excludes bare factor-SOS and EVERY uncoupled Part33 multiplier

PhysicsPPT44-2. Actual preceding `/bin/date`: **Mon Oct 26 09:46:00 PDT 2026**. **AUTHOR-WRITTEN / LATER UNREVIEWED.** ALL-variable polynomial/linear-algebra proof; no chosen state/control/code/parameter/numeric/magnitude/boundary/limit/trig probe, decimal, scientific interpreter/program or machine check.

## T0. Authority, frozen inputs and exact non-outcome

EXPLICIT future-only v57 **c6d6ea7eea5c2734fb96caa9cd29fde4a551150e2e3ce7c1d6ff2b441aba5dc7** was ACTUALLY read ENTIRE, including raw untruncated direction21/ending22–23, before resumed proof/source work. Main had actually read wholeACK56943a09/finding149b1d254fd/addendumc8230d63. This is no self-release/new GO or redundant ACK loop.

The NEW route is from LITERAL Part33's universal rank factorization and polynomial identity, and frozen Part32's SOURCE-FIXED zero/normal coupling ONLY. Part33,128LF/15501B, SHA256 **5a344ac15ad76f609acb3007ca60ab3dafbc053547c5b9fdc090d0342d158ae3**. Part32,126LF/13246B, SHA256 **18aaa105718e74dc524169fad0a26539a9fa5bafd704dae3ff43f5dd5d7605c6**. No post143 unwritten/withdrawn source/representation/scout guidance is used; ENTIRE post143 UNWRITTEN and all consuming guidance remain ZERO/no salvage/retest/repair/replay/backconversion/search direction. This is not a verified counterfactual unaffected/private-cognition certificate. Any recognized separation failure requires immediate STOP/report/WAIT.

This proof is independent of Part33's real-prime/RCF theorem imports: it is elementary polynomial and Hermitian linear algebra. It does NOT certify Part32's global existence normal-form reduction. Where applied to original counterexample EXISTENCE that Part31/24/27/29/30/32 union remains UNREVIEWED and conditional. The obstruction below itself holds for EVERY matrix satisfying the explicitly stated coupling, regardless of whether any negative PPT pair exists.

This is a FULL-domain certificate-strategy obstruction, NOT a P44 solution: normalized K2 witnesses, including decomposable witnesses, need not be PSD. Failure of the excluded SOS forms is therefore NO evidence for a PPT-SN>2 counterexample OR the original universal SN<=2 claim.

## T1. Unconditional rank-factor quartic theorem for EVERY Hermitian Z

Let Z be ANY Hermitian16x16 matrix, with arbitrary real/complex entries, and U,V ANY complex4x2 matrices. In ALL32 real/imaginary coordinates define

`F_Z(U,V)=vec(UV^dagger)^dagger Z vec(UV^dagger)`.

This is a homogeneous real quartic, of real bidegree(2,2) in(U,V).

**Theorem T1 — WRITTEN, elementary.** F_Z is a sum of squares of REAL polynomials in those32 coordinates IFF Z is PSD.

This is stronger than saying “a particular fixed-degree ansatz did not find a certificate.” It excludes EVERY polynomial SOS representation if Z is not PSD, because homogeneity will force degree2 summands automatically. Rational SOS is also excluded, since rational coefficients are real. No special Z, state, parameter value, gauge normalization, finite test or isolated instance is used.

## T2. Any real SOS of F_Z has only MIXED quadratic summands

Suppose `F_Z=sum_j p_j(U,V)^2`, with finitely many REAL polynomials p_j of arbitrary degrees.

Highest-degree terms cannot cancel in a real sum of squares: if maxdeg p_j>2, the sum of squares of the leading homogeneous parts at that degree would be the zero polynomial, forcing each leading part0, a contradiction. Thus all p_j have degree<=2. At the origin the constant coefficient is a sum of constant squares and F_Z(0)=0, so every constant part is0. The degree2 homogeneous part is then a sum of the linear parts' squares and must be0, so every linear part is0. Therefore each nonzero p_j is homogeneous QUADRATIC.

Now F_Z(U,0)=0 for ALL U, and F_Z(0,V)=0 for ALL V. Nonnegativity of each square gives p_j(U,0)=p_j(0,V)=0 identically. Hence no summand contains U-U or V-V quadratic terms: EVERY p_j is real-bilinear, one U coordinate and one V coordinate. This is an identity proof on whole variable spaces, not evaluation of a selected state/control or input sample.

## T3. Noncompact channel unipotents force EACH square separately invariant

For arbitrary complex2x2 invertible S, the channel action

`U->U S`, `V->V S^(-dagger)`

preserves UV^dagger EXACTLY. We only need the upper/lower unipotents

`S_+(z)=I2+zE12`, `S_-(z)=I2+zE21`

for ALL z=r and z=ir, with r an arbitrary REAL variable. Their inverses are I2-zE12 or I2-zE21; all transformed REAL coordinates are polynomials in r. These are symbolic channel identities, not choosing/testing a new physical control or parameter value.

For arbitrary fixed symbolic U,V and either such one-parameter action g_r,

`sum_j [p_j(g_r(U,V))]^2=F_Z(U,V)` for EVERY real r.

Each p_j(g_r(U,V)) is a real polynomial in r bounded by the same finite square-sum constant for ALL r. A real polynomial bounded on the entire real line is constant. At r=0 that constant is p_j(U,V). Thus EVERY individual p_j is invariant under ALL real/imaginary upper/lower unipotents.

Only the positivity of REAL squares is used; cancellation between complex squares would not justify this inference. There is no group-representation compactness assumption, general invariant-theory oracle or numerical orbit test.

## T4. Complete elementary classification of the remaining mixed quadratics

Write row a of U as u_a∈C^(1x2) and row b of V as v_b∈C^(1x2). Every real mixed-bilinear polynomial has a unique representation

`p(U,V)=Re sum_(a,b)[u_a C_ab v_b^T+u_a D_ab bar(v_b)^T]`,

with complex2x2 coefficient matrices C_ab,D_ab. Uniqueness follows by varying arbitrary real/imaginary row coordinates, equivalently by independence of the uv and u bar(v) monomials; conjugate terms are absorbed by Re. Different row pairs cannot cancel an identity on all independent coordinates.

The invariance established in T3 therefore gives, for EVERY one of its S,

`S C_ab bar(S)^(-1)=C_ab`, `S D_ab S^(-1)=D_ab`.

For ALL real upper/lower unipotents, both coefficients commute with E12 and E21. Direct2x2 coefficient comparison makes each a scalar matrix: C_ab=c_ab I2,D_ab=d_ab I2. Invariance under ALL imaginary upper unipotents then gives

`c_ab[S_+(ir)-bar(S_+(ir))]=2ir c_ab E12=0` for EVERY real r,

hence c_ab=0. There is no restriction on d_ab. The conclusion is

`p(U,V)=Re sum_(a,b) d_ab (UV^dagger)_ab = L(UV^dagger)`

for a REAL-linear functional L on the COMPLEX4x4 matrix space considered as a real vector space. This is the complete mixed-quadratic classification needed here; it does not assume an inverse-positive gauge, diagonal/real Z or selected U/V ranks.

## T5. Rank<=2 polarization finishes the iff, WITHOUT a determinantal-ideal shortcut

The assumed SOS now reads `q_Z(X)=sum_j L_j(X)^2` for EVERY complex rank<=2 matrix X. Let

`R(X)=q_Z(X)-sum_j L_j(X)^2`.

R is a REAL homogeneous quadratic form on M4(C), vanishing for ALL rank<=2 X. For arbitrary rank1 A,B, rank(A+B)<=2, so its real polarization satisfies

`B_R(A,B)=[R(A+B)-R(A)-R(B)]/2=0`.

Rank1 complex matrices span M4(C) AS A REAL vector space: simple tensors span the matrix tensor product, including all real/imaginary multiples. Bilinearity therefore gives B_R=0 on the ENTIRE matrix space and R identically0. No finite set of chosen product states was used as a positivity test; this is universal symbolic polarization.

Consequently q_Z is a sum of squares of real-linear functions for EVERY X, hence Z>=0. Conversely, if Z>=0, any ordinary Hermitian square-root/spectral factorization gives q_Z as a sum of complex-linear modulus-squares, or real/imaginary linear squares. Pulling them back through X=UV^dagger gives real quadratic SOS. This is an existence proof of a linear-algebra factorization, not computing a matrix/state example. T1 is proved.

The width-TWO channel is load-bearing: the noncompact upper/lower mixing in T3 is available. Nothing here asserts the same PSD-only conclusion for rank-one factorization, where partial-transpose/decomposable SOS mechanisms need not be eliminated.

## T6. EVERY source-normalized Part32 candidate is OUTSIDE bare SOS

Let W be ANY Hermitian matrix satisfying the SOURCE-FIXED equations

`x0=vec(diag(I2,0))`, `Pi=I16-x0x0^dagger/2`, `W x0=normal I2`.

Let gamma be ANY REAL number and put Z=W-gamma Pi. Then

`q_Z(x0)=0`, but `Z x0=normal I2 !=0`.

For PSD Z, q_Z(x0)=0 implies Zx0=0, by its nonnegative spectral/square-root factorization. Contradiction. Hence Z is NOT PSD, so T1 proves

`f_(W,gamma)(U,V)=q_(W-gammaPi)(UV^dagger) is NOT SOS over R`.

This applies to the ENTIRE normalized domain, not a chosen state, class, diagonal-triplet value, numeric gap or proper parameter range. In particular it applies to EVERY potential Part32 global-gap/negative-PPT-pair candidate IF one exists. It does not use existence or positivity of that candidate, and does not infer W outside DEC merely from W not PSD.

Thus a future search demanding bare factor-quartic SOS would reject ALL normalized candidates, even if their global inequality is valid. Failure of that wrong certificate family cannot establish original feasibility/emptiness or be counted as scientific evidence. Part33's general coupled-multiplier certificate is NOT bare SOS and is not refuted.

## T7. No multiplier positive at the homogeneous origin can repair bare SOS

Let f be ANY real homogeneous quartic that is NOT SOS. Suppose a real polynomial s satisfies s(0)>0 and sf=sum_j d_j(u)^2. Since sf has no degrees below4, the constant and linear homogeneous parts of every d_j vanish, by the same sum-of-squares argument as T2. Its degree4 component is therefore

`s(0) f=sum_j [d_j,2(u)]^2`.

Dividing the quadratic summands by sqrt(s(0)) would make f SOS, contradiction. Thus NO such s exists, even without assuming s nonnegative elsewhere.

In particular a strictly positive-at-origin SOS multiplier or common rational-SOS denominator nonvanishing there is impossible. This is an all-variable leading-form obstruction, not a failure of one selected degree/multiplier. If a rational-functions SOS exists by a separate theorem, any common denominator must vanish at this origin; no denominator that is regular there can work. This is not a claim that all rational certificates or all multipliers are impossible.

## T8. Part33's multiplier cannot depend ONLY on u — at ANY degree

Take the exact Part33 certificate

`-1=sum_j a_j(u,t)^2+b(u,t)[1+t² f(u)]`.                 (C)

Assume b=b(u). The square-sum has degree<=2 in t, so every a_j has degree<=1 in t: otherwise highest t-degree square terms could not cancel. Write a_j=c_j(u)+t d_j(u). Coefficients of t0,t2 give

`-b(u)=1+sum_j c_j(u)^2=:s(u)`, `s(u) f(u)=sum_j d_j(u)^2`.

The t1 coefficient supplies an additional equality but cannot remove this consequence. Since s(0)>0, T7 contradicts f not SOS. Hence for EVERY normalized f in T6, no u-only multiplier b can certify C, regardless of degrees/supports or rational versus real coefficients.

## T9. Part33's multiplier cannot depend ONLY on t — at ANY degree

Now assume b=b(t). At u=0, C gives

`b(t)=-1-sum_j a_j(0,t)^2<=-1` for EVERY real t.

The square-sum in C has u-degree<=4, so each a_j has u-degree<=2, again because highest-u-degree squares cannot cancel as a real polynomial identity. Compare homogeneous u-degree4:

`sum_j [a_j,2(u,t)]^2=-b(t)t² f(u)`.

For EVERY nonzero SYMBOLIC real tau, -b(tau)tau²>0. Specializing the polynomial identity at that arbitrary tau and dividing each quadratic summand by the positive square root would make f SOS over R. That contradicts T6. No numeric tau, sample, boundary or limiting parameter is chosen/evaluated; the proof is quantified over the entire nonzero real line.

Therefore no t-only multiplier works either. Constants are included in both exclusions.

**Conclusion T9:** EVERY actual Part33 identity for a normalized global-gap candidate MUST have genuine dependence of b on BOTH the32 factor coordinates AND the auxiliary t. This is necessity of coupled dependence, not sufficiency of any particular coupled ansatz, degree bound, support enumeration, solver permission or actual certificate.

## T10. What is new here, and the unchanged full original gap

At the explicit source definitions this is an UNCONDITIONAL elementary iff for all Hermitian Z, and a uniform obstruction for the ENTIRE source-normalized domain: direct factor-SOS, positive-origin multipliers, u-only and t-only C multipliers all fail, at ANY degree. Part33's rational weak-real-Nullstellensatz criterion therefore cannot be replaced by these apparently simpler SOS conditions. This records a genuinely different full-domain representation obstruction, not another instance enumeration or a timeout.

No original quantum counterexample or ALL-state SN<=2 theorem follows. Decomposable witnesses may also be nonPSD; nonnegative nonSOS factor quartics are not themselves evidence of indecomposability. No actual W,rho,gamma, h-identity or coefficient list is delivered. New coupling-dependence necessity does not supply a successful general b(u,t) or a finite resource/degree/height bound. The harder remaining task is STILL an ACTUAL full-global K2 nonDEC W plus eligible PPT negative pair/full exact certificate, OR an ALL-data impossibility proof.

All fixed-data statements are distinguished from the conditional original-existence application at UNREVIEWED Part32/31/24/27/29/30. No source absence/SOTA/world-novelty claim: elementary polynomial/invariant reasoning may be standard. No parent, formal/kernel, human, configured-family, executable/triple or novelty acceptance is conferred.

## T11. Whole state, permanent history and operational nonclaims

Prior33parts+TWOaddenda/ALLdeclared leads/TWOactualKG+MOM positive-PRIOR intake FILES remain; JL362logical reader EXPOSURE metadata ONLY, NOT third intake/proof/adoption/guidance. Parts24–34 remain LATER UNREVIEWED where not individually adopted, not verified unaffected by process history. New lead was saved in checkpoint153 BEFORE this literal packet; no future rediscovery claim.

Own8797d022/new3c1edecd continued-source/unwritten/scope-concern/delayed-recognition findings remain, ENTIRE post143 UNWRITTEN/guidance ZERO/no salvage/retest/repair/replay/backconversion, no invented immediate-at-probe clean stop/separate knowingly-recognized interval/private clock. New cadence149 FULL33m12s/even31m45s and parent delayed handling remain, not cured by v57 or correct new math. All oldcp049/063/081/083/085/089/oldcp013/admission/ACK/cadence/falsequotation/source/parentv9–v57/other-owner/previewv48 histories remain; N4 UNKNOWN/incomplete/overrun/historicalexit-unestablished, old21 NOT_RECONSTRUCTED, auxiliary214 STOP, oldFOUR minors/ELEVEN later proper-domain qualifiers/C27 normalizedN4 ZERO new-method credit/QD-NR. D-N2 false quotation rejected/source already>=0/no author patch. No blind-family/private-cognition/runtime/cadence/clean-history/global-owner census.

Exact source-fixed/ALL-variable conventional WRITTEN/fractions/integer products only, including privately. No scientific interpreter/eval/calculator/CAS/program/enumeration/solver/replay/build/test/CLI/nestedagent/newGO; no chosen state/code/control/parameter/boundary/limit/numeric/magnitude/trig probe EVEN rational/decimal/withdrawn guide/source-fraction decimal restatement. No coefficient evaluation or machine check. Exclusive own-root outputs, frozen/shared immutable, no Git/deletion/publication. Same original eighteen, full original primary, science cutoff **2026-10-27T11:05:38-07:00**, deadline **2026-10-27T12:35:38-07:00**, substantive actual-clock checkpoints<=30minutes. Active primary writing, NOT early final park/round closeout.

**END OF COMPLETE v26 PART34. P44 remains UNMET.**
