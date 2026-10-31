# f40 — anisotropic Bloch gap and spin-flip-overlap refinement

Reviewer **PhysicsMOQLS8-2**, author **PhysicsDepol4-2**. Actual native clock before writing: **Wed Oct 28 17:39:35 PDT 2026**. Same-harness WRITTEN reconstruction with independent exact finite checks; not formal/kernel,human,configured-family or novelty acceptance.

## 1. Inputs,exposure and exact verdict

Read COMPLETE assignment FIRST,then BOTH complete candidate bodies including endings. Live pins:

|Input|LF|SHA256|
|---|---:|---|
|assignment-v1.json|27|7c7d6ff99b981530334898c7d1e8500f44e582eeb892985097709df7f945a501|
|frontier-20261028-17-anisotropic-bloch-gap.md|54|c91882f9c8df87007ccb2b4227e96bf35eb27c2605807baedd3821dbc89c6712|
|frontier-20261028-20-spinflip-overlap-gap.md|43|dff388b2736d8cf0170fa8399a37a0950ab4f3173530fdceaf293c76c43947f3|

The registered target is ALL actual four-qubit densities and physical local-depolarizing parameters;the present results are scoped to the stated PURE/convex-hull subclasses. I previously read and reviewed the complete f5 and f23 source chains;prior exposure is disclosed,not blind. I reconstruct their needed channel/mirror/erasure/Schmidt claims again below. Historical quarantined episodes are not accepted premises;no author contact,external-model call or old held payload was used.

**Verdict: 0 FATAL / 0 MAJOR / 0 MINOR; NO_SUBSTANTIVE_DEFECT AT EXACT STATED SCOPE.**

- The anisotropic lower bound is supported for EVERY actual pure four-qubit input,EVERY complex rank3 orthogonal P and EVERY p∈[0,4/3],including negative lower bounds and endpoint/tie cases. The W illustration and the stated improvement over the coarse radius bound are correct.
- The spin-flip overlap bound is supported with the SAME rho,P in all terms,including c=0,1 and physical mirror. Its minimization is exact over the stated RELAXED scalar constraints,not a claim that every minimizer corresponds to a physical P.
- Both fixed-parameter closed-convex-hull extensions require componentwise caps as stated. Neither result covers arbitrary mixed local-marginal data or proves the global k3/all-index problem.

Section 8 gives a separately derived stronger **physical-P optimization** of the same spin-flip subproblem. It is an additional reviewer-authored candidate,not a defect or an unacknowledged author claim.

## 2. Physical same-pair channel and exact reference

For a four-qubit density rho and complex orthogonal rank3 P,let

    Φ_p(X)=(1−p)X+(p/2)Tr(X)I,  Λ_p=Φ_p^⊗4,
    E_i(X)=I_i/2⊗Tr_i X,  T_m=Σ_(|S|=m) E_S(rho),
    t_m=Tr(P T_m),  q=1−p.

Tensor positions are restored and erasures commute. For 0≤p≤1,

    Tr(PΛ_p(rho))=Σ_(m=0)^4 q^(4−m)p^m t_m,                  (E)

with NONNEGATIVE coefficients and the SAME actual rho,P in every term.

At `rho*=|0000><0000|` and fixed P* onto `|0000>,|1000>,|0100>`,the five erasure coefficients are exactly `(1,3,3,5/4,3/16)`,from `2^(−m)[binom(4,m)+2binom(3,m−1)]`. The product output has local eigenvalues `a=1−p/2,b=p/2`,so this SAME P* captures the largest three eigenvalues,including ties. Thus `R3=a⁴+2a³b`.

For the full physical interval use `s=min(p,2−p)`. The direct single-qubit identity `σ_y X^T σ_y=Tr(X)I−X=2E_i(X)−X`,tensorized,proves for EVERY complex operator X

    Λ_p(X)=Y Λ_(2−p)(X)^T Y,  Y=σ_y^⊗4.

For p∈[1,4/3],p'=2−p∈[2/3,1];P maps deterministically to `Y P^T Y`,an actual rank3 orthogonal projector. The SAME input rho/radii/spin-flip overlap remain. Product-reference spectrum is unchanged. No independent choice of layer projectors occurs.

## 3. Exact anisotropic layer bounds

Let rho=|ψ><ψ| be ANY pure four-qubit density. Order its actual one-qubit radii `0≤r1≤r2≤r3≤r4≤1` and put

    R=r1+r2+r3+r4,   L=r1+r2+3r3+3r4.

Schmidt decomposition across each cut i|bar i gives the four nonzero eigenvalues of E_i(rho) as `(1+r_i)/4` twice and `(1−r_i)/4` twice. For ANY complex rank3 P,its trace is bounded by their top-three sum `(3+r_i)/4`. Hence

    t1≤3+R/4.                                                       (1)

Meanwhile `T3=(1/8)Σ_i rho_i⊗I_(other sites)` is a sum of commuting operators. Its sixteen eigenvalues are `(4+Σ_i ε_i r_i)/16`. The all-plus eigenvalue and single flips of the two SMALLEST radii give the largest three,with ties allowed. Thus

    t3≤(12+L)/16.                                                   (2)

The crude predecessor bound follows from L≤3R. No chosen local ordering changes the original P or rho.

Put `x=t0=Tr(P rho)` and `y=Tr(P tilde-rho)`,where `tilde-rho=Y rho^T Y`. Both lie in[0,1]. Tensoring the exact spin-flip identity gives

    tilde-rho=T0−2T1+4T2−8T3+16T4,  T4=I16/16.

Tracing with the SAME P and using (1)–(2) yields

    4t2=y−x+2t1+8t3−3
        ≤10−x+(R+L)/2,
    t2≤5/2−x/4+(R+L)/8.                                           (3)

No independently optimized partial trace or spin-flipped projector is introduced.

## 4. Full anisotropic gap,threshold and W caller

Subtract the SAME-pair expression (E) from the fixed product reference,then apply (1)–(3) with nonnegative p,q weights:

    R3−Tr(PΛ_p(rho))
    ≥ q⁴(1−x) −(R/4)pq³
      +(1/2+x/4−(R+L)/8)p²q² +(8−L)p³q/16
    = pq[8p−(2−p)(2qR+pL)]/16
      + q⁴(1−x)+(p²q²/4)x.                                      (4)

The algebra uses p+q=1. Since 0≤x≤1,the last two terms are at least `h=min(q⁴,p²q²/4)`. Apply the mirror of §2 to obtain the candidate with p replaced by s=min(p,2−p),q=1−s.

The old coarse base is `sq[8s−R(4−s²)]/16`. Their exact difference is

    s²q(2−s)(3R−L)/16 = s²q(2−s)(r1+r2)/8 ≥0.

No strict improvement is claimed when the expression vanishes. If the resulting lower bound is≥0 it proves the k3 comparison;if positive it gives a strict gap. If negative it is still a valid inequality but inconclusive.

For W=(|1000>+|0100>+|0010>+|0001>)/2,each marginal has spectrum(3/4,1/4),so r_i=1/2,R=2,L=4. At s=2/3,the anisotropic BASE in (4) is0 and `h=1/81`,giving the claimed positive `1/81`. The coarse bound including h is `−1/81` there. At p=4/3 the same result follows by the exact physical mirror. This is a concrete actual-state illustration,not a general-state inference.

## 5. Spin-flip overlap,rank-two spectral bound and scalar minimum

For a pure input define `tildeψ=Y conjugate(ψ)`, `c=|<ψ,tildeψ>|`, `d=sqrt(1−c²)` and D=tilde-rho−rho. D is Hermitian,trace0,rank≤2,and

    Tr(D²)=2(1−c²)=2d².

Its only possible nonzero eigenvalues are ±d;when d=0 it is zero. For any actual orthogonal P,diagonalizing D gives `Tr(PD)≤d`. Also y≤1,so with `z=1−x∈[0,1]`,

    y−x = Tr(PD) ≤ min(d,z).                                         (5)

Using the exact spin-flip t2 identity BEFORE replacing y−x,and the SAME t1/t3 upper bounds,subtract from the product reference to get

    gap ≥ sq[8s−(2−s)(2qR+sL)]/16
          + A z + B(1−min(d,z)),
    A=q⁴,  B=s²q²/4.                                                  (6)

For z∈[0,d],the final expression is `B+(A−B)z`;for z∈[d,1] it is `A z+B(1−d)`. Its minimum over this ENTIRE RELAXED interval is B if A≥B,otherwise `B−d(B−A)`. Therefore it is exactly `B−d(B−A)_+`,as in the candidate. This scalar minimization includes d=0 and1 without division.

Relative to the previous minimum min(A,B),the improvement is exactly `(1−d)(B−A)_+≥0`. B>A iff `2/3<s<1` in the physical range,and d<1 iff c>0. Hence the candidate's stated strictness condition is correct. At s=0 and1 both refinements vanish;at s=2/3 A=B,including physical p=4/3.

The minimization in (6) is over the relaxed bounds z∈[0,1],y−x≤min(d,z). It is not an assertion that every corresponding endpoint z,y is realizable by a physical rank3 P. The author does not claim such sharpness;this is NOT a defect. Section 8 pays the stricter physical-P optimization separately.

## 6. Fixed-cap convex hull and remaining domain

Fix p and caps R0,L0,d0 for every generating PURE input. For the actual physical interval,sq≥0,(2−s)>0,q≥0,s≥0,so the base in (6) is nonincreasing in both R and L. The bonus `B−d(B−A)_+` is nonincreasing in d. Replacing these by upper caps therefore preserves a common lower bound for each pure input.

Apply that bound to each term of a finite mixture with the SAME original P,p;the trace is affine. Continuity then gives the closed convex hull. Empty generating classes are vacuous. The mixed input's own marginal radii or a fabricated mixed-state c do not by themselves imply an admissible decomposition with those componentwise caps.

Pure states for which the displayed RHS is negative remain undecided by this certificate;some may be covered by separately established scopes,but no such scope is inferred here. General mixed inputs outside the specified hull,global t1/t2 coefficient bounds and all-index majorization remain open in this review.

## 7. Independent exact algebra and actual-state checks

Wrote and ran ONCE:

    python3 -B frontier-review-f40-anisotropic-exact-check-v1.py \
      --output frontier-review-f40-anisotropic-exact-check-receipt-v1.json

Checker SHA256 **4fe9feebcf23952627460bd9b284d05d622b75429d44c4f3ce5547910302ebf4**;receipt SHA256 **a44e15dc81ae060ce73462a0d07e3f49221e1f6834bf3e6b160428e283bd4575**. It checks SHA-pinned reviewer-owned Gaussian-rational primitive files from f5/f23;NO author code is imported. Actual result `PASS_EXACT_ANISOTROPIC_SPINFLIP_SAMPLES_NOT_UNIVERSAL_PROOF`.

- Sparse polynomial dictionaries over exact Fractions checked the entire `(p,R,L,x)` identity (4) and the exact improvement over the coarse R-bound.
- Four EXACT pure inputs W,unequal complex GHZ,balanced complex GHZ,and a product input were checked with one genuine complex Hermitian idempotent trace3 P. Every actual local radius,c,d and layer trace was calculated exactly. Seven rational physical p values include0,2/3,1,7/6,4/3.
- W gives R=2,L=4,c=0,d=1 and anisotropic bound **1/81 at p=2/3 and4/3**. Unequal GHZ gives c=24/25,d=7/25;at p=5/6 the new author's spin-flip term improves its anisotropic bound by **7/2400**. Balanced complex GHZ exercises c=1,d=0;W/product exercise c=0,d=1.
- For each sampled p,d,actual piecewise scalar minimization was checked exactly at ALL breakpoints z=0,d,1. One explicitly specified convex mixture of two pure GHZ states was checked with common caps `(R0,L0,d0)=(28/25,56/25,7/25)` and the SAME complex P;its mixed marginals were not substituted for the component caps.

All calculations use Python standard-library exact rational pairs and polynomial dictionaries. The finite examples do not establish the universal statements. The all-operator mirror at two sampled p values had also been checked on512 matrix units in the independently authored f5 checker;the all-p result is the written proof above.

## 8. Additional independently derived physical-P optimization — NOT an author finding

This reviewer observation is a new WRITTEN candidate refinement of the same-pair subproblem,not required to validate either author claim. It shows why the relaxed z minimization is conservative.

Before replacing y−x by min(d,z),the exact spin-flip rearrangement and the SAME anisotropic t1/t3 bounds give

    gap ≥ base + A(1−x)+B(1−y+x),
    base=sq[8s−(2−s)(2qR+sL)]/16.

For FIXED pure rho and A,B≥0,the correction equals

    A+B−Tr(P H),  H=(A−B)rho+B tilde-rho.

If A≥B,H is PSD with trace A and rank≤2;an actual rank3 P can contain its support,so the minimum correction is B. If A<B,the nonzero eigenvalues of H on span{ψ,tildeψ} have sum A and product `(A−B)B(1−c²)=−B(B−A)d²`. They are

    λ_±=[A±sqrt(A²+4B(B−A)d²)]/2.

For d>0,λ+>0>λ−. An actual rank3 P can contain the positive eigenvector,exclude the negative one,and take its other two directions in the14-dimensional kernel. For d=0 the rank-one limit is immediate. Therefore the exact minimum over ALL actual rank3 P of THIS correction is

    Φ(A,B,d)=B + [A−sqrt(A²+4B(B−A)_+ d²)]/2.               (7)

It equals B for A≥B and is attained in both cases. For A<B,comparison with the author's relaxed bonus follows from

    [A+2d(B−A)]²−[A²+4B(B−A)d²]
      =4A(B−A)d(1−d) ≥0.

Thus Φ≥`B−d(B−A)`,strict if A>0,B>A and0<d<1. This yields an additional pure-state lower bound `gap≥base+Φ` at the same physical parameters/projector quantifiers,after applying the established mirror. It does NOT assert simultaneous equality in the earlier t1/t3 bounds,global majorization,or attainment of the actual-channel gap. It is a candidate requiring separate review.

**Actual exact physical check of (7):** `frontier-review-f40-physical-P-optimum-v1.py` SHA256 **3a4fcbed2850018ce030f0f669238dd404976a49024bc017581c754cdfc1f795**,receipt SHA256 **ccf7a7f47fd4c5ae0f890ced67de5509a5694037d12e6e3e6e44751ee96757a5**,executed once with exact Gaussian Fractions. For the ACTUAL state `(3|0000>+4i|1111>)/5`,s=25/32,c²=576/625,d=7/25,the program constructs the positive-eigenvector projector of H plus two orthogonal kernel basis vectors;it verifies Hermiticity,idempotence and trace3. Exact physical correction=Φ=**6713/1048576**,while the author's relaxed scalar bonus is **309239/52428800**,strict improvement **26411/52428800**. The actual-channel inequality was also checked at that P. This is one sample,not a computer proof of the universal spectral formula.

## 9. Final assurance

Both reviewed author bounds are mathematically supported at their stated scope with0F/0M/0m. Section 8 is an additional reviewer candidate and must not be attributed to,or automatically adopted with,the author papers. Parent must read BOTH complete sources and this complete return;any adoption must retain actual-pair,physical-parameter,pure/closed-hull and nonnegative-bound distinctions.

No full original k3/all-index proof,physical counterexample,global mixed-input result,novelty/priority,formal/kernel,human or configured-family review is asserted. Exact finite checks are reported only at their actual scopes;historical quarantined outcomes/process findings remain historical and unvalidated by this new review.
