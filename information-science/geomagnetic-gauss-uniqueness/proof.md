# Classical certification of geomagnetic Gauss uniqueness

Date: 2026-10-14. **Certification, not Discovery.** These are conventional written proofs, not Lean/kernel-certified results. References and the exact book quotations are in README.md and sources/references.md. All potentials and fields below are real. The sign convention is B = −∇V. A change of the historical sign convention changes no uniqueness conclusion.

## 1. Contract and topology

Let D be a bounded connected domain in R³ with connected compact embedded C² boundary S, connected exterior, and 0 in D. Let K be a compact subset of D, with connected exterior R³\K, containing a neighborhood of 0. Let O be a connected open set containing the closure of D. Require Ω = O\K to be connected. Assume

- V_i is harmonic on R³\K and V_i(x) = O(1/|x|) at infinity;
- V_e is harmonic on O;
- V = V_i + V_e on Ω, and the observations are B = −∇V on S.

The compact inclusions give a source-free two-sided neighborhood of S. “Regular at infinity” is fixed here to **vanishing at infinity**, not merely boundedness: otherwise a constant could be exchanged freely between V_i and V_e and the assertion that V_i itself is unique would be false. For geomagnetism impose additionally zero total magnetic flux, equivalently no degree-zero internal monopole. Constants of V_e are a gauge. The proofs of separation also work with a monopole, but the geomagnetic coefficients in question have degree n ≥ 1.

No genus-zero assumption on S is needed because a single-valued scalar potential is explicitly assumed. Curl-free on an arbitrary multiply connected region alone does not imply that assumption. No currents or jump sheets are permitted on S. Source separation is a separation of *fields*, not identification of the underlying currents or magnetization.

Choose a fixed real spherical-harmonic basis Y_nm orthonormal for dω on the unit sphere, m = 1,…,2n+1 (a basis index, not the usual signed order). For the stated individual conversion to conventional Gauss coefficients, take the conventional real cosine/sine harmonics with orthonormal normalization. With any other specified orthonormal basis the conversion instead includes the known invertible degree-by-degree basis change. Set h_nm(x)=r^nY_nm(ω), k_nm(x)=r^(−n−1)Y_nm(ω). Write

V_i = Σ A_nm k_nm,   V_e = C_00Y_00 + Σ C_nm h_nm.

The exterior expansion converges outside a ball containing K, and the interior expansion inside a ball centered at 0 contained in O. If there exist a < b with K ⊂ {|x|<a} and {|x|≤b} ⊂ O, the two series converge together for a < r < b. General nonspherical K and O need not admit a common spherical convergence shell containing S; the boundary formulas below do not require one. Each coefficient remains unambiguously defined by its own expansion. The usual g,h,q,s are fixed nonzero normalization/radius rescalings of A,C. The book prints j,k for the external coefficients; q,s is the standard renaming used here.

## 2. R1: full vector data on one closed surface

### Theorem 1 (Cauchy recovery and separation)

Under §1 the data B|S determine V on Ω up to one additive constant, V_i on R³\K uniquely, V_e on O up to that same constant, and every A_nm,C_nm for n≥1 uniquely. There is no need for a new fourth boundary condition.

**Proof and explicit reconstruction.** Write n for the outward unit normal of D, B_T=B−(B·n)n, f=V|S and g=∂_nV|S=−B·n. The tangential data give

∇_S f=−B_T,

so, for any path γ on S from p to q,

f(q)−f(p)=−∫_γ B_T·dℓ.                                      (1)

The integral is independent of path because the data come from a single-valued potential. In particular all periods vanish, including on a surface of positive genus. Connectedness of S leaves exactly one constant. Fix it by ∫_S f dS=0, which fixes the gauge of the recovered total and external potentials, not that of the original physical convention. Inconsistent arbitrary vector data need not admit any harmonic solution; this is a uniqueness theorem on the admissible data set, not an existence assertion for arbitrary noisy observations.

Let G(x,y)=1/(4π|x−y|), so −Δ_yG=δ_x. Define

H(x)=∫_S [G(x,y)g(y)−f(y)∂_{n_y}G(x,y)] dS_y.               (2)

Then the reconstruction is

V_e(x)=H(x) for x∈D,      V_i(x)=−H(x) for x∉closure(D).      (3)

To prove (3), apply Green's second identity. If w is harmonic inside D and through its boundary, its contribution H_w is w inside D and zero outside closure(D). If w is harmonic outside D and decays O(1/r), apply Green's identity between S and a large sphere, recalling that the inner boundary's normal is −n. The contribution H_w is zero inside D and −w outside D. The large-sphere term tends to zero: w=O(r^−1), ∇w=O(r^−2), G=O(r^−1), ∇G=O(r^−2), so its absolute integral is O(r^−1). The gradient decay follows either from exterior harmonic expansion or from the interior gradient estimate on balls of radius comparable to r. Adding w=V_e,V_i proves (3), with the same chosen gauge as f.

Adding c to f changes H by −c∫_S∂_nG: this is c inside D and zero outside. Thus V_i is unaffected and V_e changes by c. The reconstructed functions continue uniquely to their stated connected harmonic domains. For completeness, the unique-continuation lemma used for that assertion is proved in §5. If two decompositions produce the same observations, they give the same f modulo c and the same g, hence by (3) the same V_i on the open exterior of D, and external potentials differing by c inside D. Unique continuation finishes the claim on R³\K and O, respectively. □

### Theorem 2 (direct coefficient moments on nonspherical S)

With the above normalization, for every n≥1,

A_nm = (2n+1)^−1 ∫_S [f∂_n h_nm−g h_nm] dS,                (4)
C_nm = (2n+1)^−1 ∫_S [g k_nm−f∂_n k_nm] dS.                (5)

**Proof.** The addition formula for the Newton kernel is

G(x,y)=Σ_{n,m} (2n+1)^−1 |x|^(−n−1)Y_nm(x/|x|)h_nm(y)

when |x|>max_S|y|. Insert this normally convergent series into −H in (3) and identify coefficients. For |x|<min_S|y| exchange the interior and exterior variables, insert into H, and identify the regular coefficients. Derivatives may be interchanged because these inequalities are strict. This proves (4),(5). Constants in f do not affect (4), since ∫_S∂_n h=∫_DΔh=0, or (5) for n≥1, since ∫_S∂_n k=0 by applying the divergence theorem after removing a small origin-centered sphere and using ∫Y_nm dω=0. □

### Theorem 3 (Gauss's spherical 2n+1 separation)

On S={r=R} in a common source-free spherical shell, put I_nm=A_nmR^(−n−1), E_nm=C_nmR^n, v_nm=∫fY_nm dω and b_nm=∫B_rY_nm dω. Then

v_nm=I_nm+E_nm,    Rb_nm=(n+1)I_nm−nE_nm,

I_nm=(nv_nm+Rb_nm)/(2n+1),
E_nm=((n+1)v_nm−Rb_nm)/(2n+1).                              (6)

**Proof.** Differentiate the radial powers; invert the displayed 2×2 system, whose determinant is −(2n+1)≠0. Tangential observations recover v_nm using (1). This is Gauss's 1839 §40 argument, also reproduced in Sabaka–Hulot–Olsen (2010), §6.1, pp.525–526. □

The 2014 English translation of Gauss, printed p.40, visibly omits factors 2 and 3 before Π″ and Π‴ in the internal-coefficient rows of its last display. This is not just PDF extraction loss: sources/gauss-section40-30.png shows it. The preceding equations Π=P+p and Q=(n+1)P−np give (2n+1)P=nΠ+Q, which is (6). We use that explicitly derived identity, not the erroneous printed rows. No claim is made about whether the error was present in the 1839 German original.

### Corollary (what fewer components do and do not supply)

For a purely internal field, the whole-sphere potential determines each I_nm=v_nm, and the whole-sphere radial field determines I_nm=Rb_nm/(n+1). In the mixed internal/external class, one component on one sphere does not in general separate the sources: for any n≥1 choose I_nm=nE_nm/(n+1), obtaining B_r=0 but a nonzero field. Similarly I_nm=−E_nm gives zero tangential field but nonzero radial field. Full vector data contain both potential trace (modulo constant) and normal derivative: they are **Cauchy data**, not a missing boundary-condition species.

## 3. R1 stability: the output norm matters

### Theorem 4 (Lipschitz coefficient recovery on the observed surface)

Let differences be between two admissible data sets. Fix the zero-mean gauge for δf. Surface Poincaré gives

||δf||_{H¹(S)} ≤ C_S ||δB_T||_{L²(S)},   ||δg||_{L²(S)}≤||δB||_{L²(S)}. (7)

Consequently each coefficient in (4),(5), and each fixed finite vector of coefficients, depends Lipschitz continuously on B in L²(S). In particular,

|δA_nm| ≤ [C_S||∂_nh_nm||₂+||h_nm||₂] ||δB||₂/(2n+1),       (8)

and the analogous bound with k_nm holds for δC_nm.

**Proof.** The mean-zero surface Poincaré inequality bounds ||δf||₂ by its tangential gradient. This gradient is −δB_T. Apply Cauchy–Schwarz to (4),(5); all test functions and their normal derivatives are bounded on compact S, since 0∉S. □

On a sphere, in the no-monopole geomagnetic class, a sharper all-degree identity holds (if the optional internal monopole is admitted, add |δI_00|² to the right-hand side):

||δB||²_{L²(S_R)} = Σ_{n≥1,m} [(n+1)(2n+1)|δI_nm|²+n(2n+1)|δE_nm|²]. (9)

Thus the full-vector map to the weighted coefficient Hilbert space in (9) is an isometry. To verify the identity, the radial part for one harmonic is R^−1[(n+1)I−nE]Y, and the tangential part is −R^−1(I+E)∇_{S²}Y. Orthogonality and ∫|∇_{S²}Y_nm|²=n(n+1) cancel the cross term exactly. The surface element is R²dω. First do this for finite sums; convergence in the harmonic collar implies smooth boundary convergence and permits the limit.

For a general S, pick R_+>max_S|x| and 0<R_-<min_S|x|. Differentiation of (2), with kernels bounded away from their singularity, and (7) give

||∇δV_i||_{L²(S_{R_+})}+||∇δV_e||_{L²(S_{R_-})}≤C||δB||_{L²(S)}. (10)

Applying the internal/external specializations of (9) yields a bounded map into the infinite weighted coefficient space with I_nm=A_nmR_+^(−n−1) and E_nm=C_nmR_-^n. This is a genuine all-degree continuity statement, not merely continuity of a finite truncation.

**No contrary claim about downward continuation.** If 0<r₀<R, a purely internal degree-n field has

||B||_{L²(S_{r₀})}/||B||_{L²(S_R)}=(R/r₀)^(n+1).             (11)

Normalize the numerator to one; then the data norm tends to zero. Hence continuation towards internal sources is unbounded between those L² norms without extra a priori restrictions. Likewise outward continuation of regular degree-n external fields has norm ratio (r₁/R)^n for r₁>R. The sequence uses potentials harmonic off the fixed origin (or entire external polynomials), so every member satisfies a common source-free collar assumption. Coefficients at a reference radius different from the observation radius can inherit these exponential weights. A statement “all Gauss coefficients are stable” without a coefficient norm and reference radius would therefore be misleading.

## 4. Vertical versus normal on nonspherical surfaces

### Theorem 5 (oblique measurements)

Suppose the observations are the two components B_T tangent to S and the radial scalar b_r=B·e_r, where e_r=x/|x|. On every point with n·e_r≠0,

B·n=(b_r−B_T·e_r)/(n·e_r).                                (12)

If S={R(ω)ω:ω∈S²}, with positive C² R, then

n·e_r=[1+|∇_{S²}log R|²]^−1/2 ≥ c>0.

Thus the measurements are equivalent to full-vector data, with a bounded pointwise/L² conversion, and all R1 conclusions hold. If “horizontal” instead means the geocentric e_θ,e_φ directions, those and e_r form an orthonormal frame directly, regardless of S's normal (using nonsingular local frames at the poles).

Even for a non-star-shaped S satisfying §1, uniqueness still follows from these tangential-plus-radial data. At a maximum of |x| on S, the radial vector is normal to S; hence |n·e_r|=1 there and remains nonzero on an open patch. Formula (12) determines the full vector on that patch, and Theorem 6 below supplies uniqueness. This last argument asserts uniqueness, not a global uniform bound from division by n·e_r. Radial data *alone* in the mixed-source class fail already on a sphere, as the corollary to Theorem 3 shows. □

## 5. R2: exact continuum data on an open patch

### Lemma (harmonic Cauchy unique continuation)

Let u be harmonic in a connected open set containing a C² surface patch Γ. If u=0 and ∂_nu=0 on Γ, then u=0 throughout the connected open set.

**Proof.** Take a small ball cut into two sides by a relatively compact subpatch. Define w=u on one side and w=0 on the other. For any smooth test function compactly supported in this ball, integration by parts twice yields

∫wΔφ=∫_{one side}uΔφ=∫_{patch}(u∂_νφ−φ∂_νu)=0.

There is no other boundary term, and both traces vanish. Thus w is distributionally harmonic. Weyl's lemma makes w smooth and harmonic; harmonic functions are real analytic (for example the Poisson formula in each ball gives locally convergent Taylor series by differentiating its analytic kernel on a smaller concentric ball). Since w vanishes on an open half-ball, its power series and hence w vanish on the ball. Therefore u vanishes on an open subset of its original domain. Propagate the analytic identity along a finite chain of overlapping balls covering any path in the connected domain. An open connected subset of R³ is path connected, and a compact path has a finite such cover. This gives u=0 everywhere. □

This is the Laplace-specialized Holmgren/analytic-continuation argument. Hörmander (1993), introduction pp.1223–1224, explicitly states the general noncharacteristic uniqueness theorem and its C¹-surface extension. Our argument needs no analyticity of S. **Analyticity of V alone, without the zero normal derivative, is not a valid argument for a general two-dimensional observation surface**: e.g. u=z vanishes on a plane but is nonzero elsewhere.

### Theorem 6 (patch uniqueness)

For any nonempty relatively open patch Γ⊂S, full-vector B|Γ uniquely determines V on Ω up to a constant and, under §1, the two source fields and all coefficients as in Theorem 1.

**Proof.** For two candidates, ∇u=0 on Γ. On a connected subpatch, tangential integration gives u=c and the normal derivative is zero. Apply the lemma to u−c. Their full-vector data consequently agree on all S; Theorem 1 then separates their fields. □

### Theorem 7 (explicit patch instability with fixed source region)

Let the observation patch on the unit sphere avoid a nonempty open cap about a point p. After rotation take p=(0,0,1), and assume z≤1−ε on the closure of Γ, ε>0. Define, for integers N≥1 and r=|x|,

u_N(x)=1/(Nr) {Re[((1+(z+ix)/r²)/2)^N]−2^(−N)}.             (13)

Here x inside z+ix denotes the first Cartesian coordinate and i²=−1. Each u_N is a real, purely internal, finite multipole potential with degrees 1,…,N and no monopole, harmonic on R³\{0}, vanishing at infinity. If B_N=−∇u_N, then

||B_N||_{C^k(closure Γ)} → 0 for each fixed k,
|B_N(p)|=1/2+(1−2^(−N))/N ≥ 1/2.                           (14)

In particular the inverse from patch C⁰ vector data to whole-sphere C⁰ vector field is not continuous at zero. The same discontinuity holds when a fixed finite number of derivatives is included in the input norm. It also holds with L² patch input and C⁰ whole-sphere output. This is an ill-posed inverse, not exact non-uniqueness.

**Proof.** The polynomial P_N(X)=Re[(1+Z+iX)^N]−1 is harmonic: the complex vector (i,0,1) has its bilinear square i²+1=0, so Δ(1+Z+iX)^N=0. Its constant term vanishes. Its Kelvin transform r^−1P_N(x/r²), scaled by 1/(N2^N), is (13). Alternatively expand the binomial: each homogeneous term Re(z+ix)^l is harmonic and its Kelvin transform is a decaying solid harmonic of degree l≥1. This proves all domain and monopole claims without invoking singularities near the observed sphere.

On r=1 set t=(1+z+ix)/2. Since x²≤1−z²,

|t|²=[(1+z)²+x²]/4≤(1+z)/2≤1−ε/2=:q²<1.

The gradient is explicitly

∇u_N=−x_vec/(Nr³)(Re(t^N)−2^(−N)) + r^−1 Re[t^(N−1)∇t],
∇t= (i,0,1)/(2r²)−(z+ix)x_vec/r⁴.                         (15)

On Γ,

|B_N|≤(q^N+2^(−N))/N+(1+1/√2)q^(N−1).                    (16)

Any fixed number k of tangential derivatives contributes only a fixed polynomial in N and bounded smooth factors, so the exponential decay remains. At p, t=1, and its radial derivative is −1/2; direct differentiation of (13) gives (14). □

The nonempty-unobserved-cap hypothesis matters: a proper open set can be dense or have complement of measure zero. One must not claim this instability theorem for *every* proper open patch without checking the observation/output norms. The numerical example uses Γ={z≤−1/4}, so ε=5/4 and q=√(3/8).

### Theorem 7A (rival local U-only or Z-only reading)

The sentence preceding the book's “local region” clause discusses **U or vertical Z**, not necessarily the full vector. This ambiguity must be kept separate from Theorem 6.

**With a two-sided source-free collar and a spherical observing surface**, an internal-only decaying potential is uniquely determined by either its exact potential trace or its radial field trace on any nonempty open patch. Indeed, the potential is real analytic near the entire sphere, and its restriction and radial derivative are real analytic on that connected analytic surface. The difference of either trace for two candidates vanishes on an open patch, so the real-analytic identity theorem on the sphere gives zero on the whole sphere. In the internal-only expansion the potential trace coefficients are I_nm and the radial coefficients are (n+1)I_nm/R, so either determines all coefficients. This continuation need not be stable.

**Without that collar**, suppose only that the potential is harmonic for r>1, smooth up to r=1, decays at infinity and has no monopole. If the complement of the observed patch Γ contains an open set, neither U|Γ nor B_r|Γ alone is injective in this larger class.

To prove this exactly, choose two nonzero nonnegative smooth bumps with disjoint supports in the unobserved open set, scale them to have equal surface integral, and let f be their difference. Then f is nonzero, smooth, zero on Γ and has zero spherical mean. Let f_nm be its orthonormal spherical-harmonic coefficients. Repeated integration by parts with the spherical Laplacian shows they decay faster than any fixed inverse power of n: apply Δ_{S²}^k to f and divide by [n(n+1)]^k. Define

U_D(r,ω)=Σ_{n≥1,m} f_nm r^(−n−1)Y_nm(ω),
U_Z(r,ω)=Σ_{n≥1,m} f_nm r^(−n−1)Y_nm(ω)/(n+1).

Rapid coefficient decay, polynomial bounds for derivatives of the spherical harmonics, and multiplicity2n+1 imply convergence of every fixed derivative uniformly up to r=1. The sums are nonzero harmonic functions for r>1 and decay at infinity. They have no monopole, and satisfy U_D|S=f and −∂_rU_Z|S=f. Thus each gives the same relevant one-component patch data as the zero field, yet is not the zero field. Neither can have a harmonic collar around the *entire* sphere, since that would make its nonzero compactly supported boundary datum f real analytic, a contradiction. This is a boundary-source/no-clearance class, not the compactly separated K⊂D class of R1. □

**Reconciliation with the book.** The full-vector exact-patch reading is uniquely solvable, so non-uniqueness is false under that reading. The one-component internal-only reading is also unique on a sphere **if** a two-sided collar is assumed, but genuinely nonunique in the exterior-only smooth-boundary class just constructed. The book does not explicitly fix this clearance/regularity distinction in its local-data sentence; it should therefore not be declared universally false. Finite samples are not continuum patches, finite-error observations allow widely different fields, and the practical warning remains sound. Mixed internal/external one-component observations fail even on the complete sphere, by the corollary to Theorem3.

## 6. R3: any finite set of vector samples is non-injective

### Theorem 8

For any M finite observation locations x_j∈Ω (in particular x_j∈S), exact values of B(x_j), j=1,…,M, do not determine all internal Gauss coefficients in the untruncated class. Non-uniqueness already occurs among finite multipole potentials of a sufficiently high degree. The kernel construction itself works at any x_j≠0, but perturbing an arbitrary admissible V requires samples inside its domain Ω.

**Proof.** Let H_N be the real vector space spanned by k_nm, 1≤n≤N. Its dimension is Σ(2n+1)=N(N+2). Pointwise gradient evaluation is a linear map H_N→R^(3M). Choose N(N+2)>3M. Rank-nullity gives a nonzero u in its kernel, exactly, with no numerical conditioning assumption. This u is harmonic away from 0 and decays at infinity. Its field cannot vanish identically: ∇u=0 on the connected punctured space would make u constant, and decay would make it zero, contrary to its nonzero independent coefficients. Given any admissible field V, the distinct fields V+tu, t∈R, have precisely the same samples. The origin lies inside fixed K, so all perturbations obey the source-region assumption. □

If one *a priori* fixes a finite degree N and chooses a full-column-rank sampling matrix, sufficiently many suitable observations can determine that finite model. Such a statement does not determine every coefficient of an untruncated field and does not contradict Theorem 8. Unknown physical sources remain even less identifiable.

## 7. R4: intensity on a complete sphere

All internal-only statements in this section refer to potentials harmonic outside a ball of radius a<1, decaying at infinity, and without a monopole. They are not statements about a mixed-source class. Scale the unit radius to any R if desired.

### Theorem 9 (Backus finite-expansion uniqueness, fully certified here)

Suppose V₁,V₂ are finite sums of decaying solid harmonics. If |∇V₁|=|∇V₂| on the unit sphere, then V₂=V₁ or V₂=−V₁. Degrees need not be equal. Thus the global sign is the only ambiguity **within the finite-expansion class**.

**Proof.** Set U=(V₁+V₂)/2 and W=(V₁−V₂)/2. Intensity equality gives ∇U·∇W=0 on the sphere. Assume both potentials nonzero, and let their largest degrees be p,q≥1, with nonzero real homogeneous harmonic polynomials H_p,K_q. On r=1,

∇(H_p/r^(2p+1))=∇H_p−(2p+1)H_p x_vec.

Using Euler's identity x_vec·∇H_p=pH_p, the dot product for these top terms is

∇H_p·∇K_q+(p+q+1)H_pK_q.                                 (17)

The first summand has homogeneous degree p+q−2. All other pairs of degrees in U,W have total degree below p+q and so no spherical harmonic component of degree p+q. Thus the top spherical-harmonic projection of the complete dot product equals (p+q+1) times the degree-(p+q) harmonic part of H_pK_q.

That harmonic part is nonzero. Here is the algebraic justification, including nongeneric coefficients. On real homogeneous polynomials define the positive definite Fischer inner product by <x^α,x^β>=α!δ_{αβ}. Multiplication by r² is adjoint to Δ, so

P_d = ker(Δ|P_d) ⊕ r²P_{d−2}

as an orthogonal direct sum: the orthogonal complement of the image of multiplication by r² is exactly kerΔ. Hence a homogeneous polynomial has zero top harmonic part iff it is divisible by r². No nonzero harmonic polynomial is divisible by r², because if H=r²Q then ||H||²=<H,r²Q>=<ΔH,Q>=0. Finally r²=x²+y²+z² is irreducible over R: a factorization of its quadratic homogeneous form would require real linear factors, but a linear zero plane contains nonzero points whereas r² vanishes only at zero. The polynomial ring over R is a UFD, so this irreducible is prime. If r² divided H_pK_q it would divide one factor, impossible. This proves the claimed nonzero projection.

Equation (17) therefore cannot be identically zero on the sphere, a contradiction. At least one of U,W is zero, giving the two alternatives. The zero-potential case is included. □

This is a different complete certification argument for Backus's known theorem, not a claim of a new theorem. Alberto–Oliveira–Pais (2004), §3.1, pp.550–551, supplies a primary rederivation via Clebsch–Gordan coefficients; their introduction explicitly attributes the theorem to Backus (1968). Our polynomial argument avoids assuming any particular highest-order coefficient is nonzero in a fixed coordinate frame.

### Theorem 10 (non-sign intensity ambiguity: a convergent Backus series)

There exist two internal-only potentials V₊,V₋, harmonic on a common neighborhood of the unit sphere and throughout its exterior, whose fields have identical intensity on the entire sphere but are neither equal nor globally opposite.

**Construction and proof.** Let μ=cosθ, use the ordinary associated Legendre functions with Condon–Shortley convention, and set D=r^−2μ (an axial dipole). Define

U=Σ_{l=1,3,5,…} a_l r^(−l−1)P_l¹(μ)cosφ,
a₁=1,
a_{l+2}=−[(l+2)l(2l+5)]/[3(l+3)²(2l+1)] a_l.              (18)

All coefficients are real, nonzero rational numbers. Their two-step absolute ratio tends to 1/3. For every η>1/√3 there is a constant C_η with |a_l|≤C_η η^l. The functions P_l¹cosφ have at most polynomial sup-norm growth: P_l¹=−√(1−μ²)P_l′ and the polynomial Markov bound |P_l′|≤l² on [−1,1] suffices. Thus the series converges uniformly on every compact subset of r>1/√3, by choosing η below the smallest radius of that compact set. Each term is harmonic, so its sum is harmonic; interior harmonic derivative estimates give termwise convergence of every derivative on smaller compact subsets. This supplies the necessary collar and field convergence, not just a formal recurrence. At infinity the leading dipole decays; there is no monopole.

On r=1 the dot product of ∇D with the gradient of the l-th basis potential equals

[2(l+1)μP_l¹+(1−μ²)(P_l¹)′]cosφ
= [A_lP_{l+1}¹+B_lP_{l−1}¹]cosφ,
A_l=(l+2)l/(2l+1),    B_l=3(l+1)²/(2l+1).                 (19)

For clarity, use the standard polynomial identities

(1−μ²)(P_l^m)′=−lμP_l^m+(l+m)P_{l−1}^m,
(2l+1)μP_l^m=(l−m+1)P_{l+1}^m+(l+m)P_{l−1}^m.

These follow by differentiating the Legendre recurrence (or Rodrigues' formula); substituting m=1 gives (19). Equation (18) is exactly A_la_l+B_{l+2}a_{l+2}=0. The lowest leftover P_0¹ is zero. Absolute convergence of the differentiated series legitimizes all cancellations. Therefore ∇D·∇U=0 on S².

Take V₊=D+U and V₋=D−U. Then |∇V₊|²−|∇V₋|²=4∇D·∇U=0. They cannot be equal or opposite because U≠0 and D≠0 (their nonzero degree-one terms also have different orders). This is ambiguity beyond global sign. The ratio limit gives a common allowed source ball with any radius a∈(1/√3,1), so the construction satisfies the same strict source-free collar assumption as the other theorems. □

Alberto–Oliveira–Pais (2004), §3.2, Eq.(22), pp.551–552, gives the same recurrence in normalized harmonics and identifies it as Backus's 1970 series. To compare exactly, let N_lm=[(2l+1)(l−m)!/(4π(l+m)!)]^(1/2), omitting a fixed real cos/sin normalization. Our normalized coefficient is a_l/N_l1. Multiplying the ratio in (18) by N_l1/N_(l+2),1 gives their Eq.(22) at m=1. This verifies the primary formula, rather than treating its attribution as a new discovery. We do not use the stronger informal statement that every finite field has a convergent orthogonal partner: that paper explicitly warns in §3.3 that convergence for general combinations depends on parameters.

### Corollary (finite mixed sources do not satisfy Theorem 9)

External degree-one potentials V₁=x and V₂=y have constant unit intensities everywhere and nonparallel fields. Both are finite Gauss expansions but not internal-only decaying fields. Thus even finite-degree scalar uniqueness modulo sign fails in the full R1 mixed-source class. Similarly the universal sign ambiguity V↦−V is unavoidable in every nonzero intensity-only model unless signed orientation information is added.

## 8. What is fully answered, and what is not claimed

For the book's stated full tangential-plus-vertical measurements on a closed surface in a harmonic source-free region, uniqueness and internal/external separation are classical and completely answered above; the spherical argument is explicitly in Gauss (1839) and the 2010 review. Exact patch full-vector data also give uniqueness, but not stable continuation; finite-point data and unrestricted intensity data do not. The apparently conflicting statements concern different observation operators and function classes.

We have **not** classified all pairs of infinite internal fields with a given intensity, solved noisy-data regularization optimally, identified arbitrary source current distributions, or included currents crossing the observing surface. None of these stronger rival readings is silently advertised as solved. The theorem that unrestricted intensity is non-injective needs one convergent counterexample, supplied by Theorem 10; it does not require a complete classification of its fibers. Numerical experiments in work/sanity.py are only Empirical evidence and play no role in any proof.
