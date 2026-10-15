# Results and proofs

Snapshot: 2026-10-14 (PT). **Verdict: PARTIAL.** The stated model problems below are settled, but the original unrestricted book goal remains **OPEN-BLOCKED / PROOF-OBLIGATION in this project**. Its current literature-open status was not verified, and its selection as “not too hard” was not justified; see `STATUS.md`. **FRONTIER state: NOVELTY-UNCLEAR** for the optical synthesis, with established mathematical ingredients and no priority claim. C2 is a **stronger-invariance-requirement partial lemma**, not a replacement for the original Fresnel/Maxwell target. C6 explicitly refutes a naive transfer of its necessity to Fresnel-only propagation.

**Approved scoped target C8: SOLVED / DELIVERY-READY for correctness; NOVELTY-UNCLEAR for publication priority.** Its complete finite-mode Fresnel classification is given below and independently reviewed. This does not change the book-level PARTIAL verdict.


## Contract and evidence

- **Claim:** classify local spectral degree-of-polarization invariance for all scalar probes of a finite-spatial-mode source; distinguish deterministic probes from arbitrary incoherent mixtures; give the corresponding observable far-zone spectral condition and counterexamples to implication.
- **Baseline:** Wolf's sufficient far-zone condition; factorized GSM invariance (Zhao et al., 2009); nonuniform all-distance pseudo-Schell invariance (Martínez-Herrero et al., 2022); standard qubit-channel geometry (Ruskai, Szarek and Werner, 2002); and joint numerical-range convexity (Au-Yeung and Poon, 1979, as explicitly stated by Lau et al., 2020). See `STATUS.md` for scopes and access limits.
- **Missing ingredient for the book's full problem:** the actual Fresnel probe family is smaller than all linear probes. C6 proves that C2's necessity does not transfer, so the missing bridge cannot simply be assumed or filled in for all sources. A different characterization of the restricted Fresnel family is needed; full Maxwell propagation also is not scalar on polarization.
- **Decision value:** separates an explicit exceptional deterministic family from universal random-medium robustness. It rules out inferring robust polarization invariance merely from successful deterministic propagation, or inferring either invariant from the other.
- **Protocol:** exact rational/symbolic controls first; fixed Gaussian/Hermite-Gaussian and Gaussian Schell-model examples; independent modal/FFT and source-CSD/Fresnel-integral propagation; no fitted parameters, no searches, no performance or AI-advantage claim. CPU threads capped at one in the reproduction command.

Every numerical check is reproduced with:

```sh
OPENBLAS_NUM_THREADS=1 OMP_NUM_THREADS=1 /Users/jinleic/jinleic-workspace/scratch/ai4s-venv/bin/python code/verify.py && \
OPENBLAS_NUM_THREADS=1 OMP_NUM_THREADS=1 /Users/jinleic/jinleic-workspace/scratch/ai4s-venv/bin/python code/fresnel_only.py && \
OPENBLAS_NUM_THREADS=1 OMP_NUM_THREADS=1 /Users/jinleic/jinleic-workspace/scratch/ai4s-venv/bin/python code/lg_fresnel_classification.py
```

The script's exact identities are **Certification** of those identities, not formal verification of the complete handwritten proofs. Finite-grid propagation is **Empirical evidence** and does not establish universal quantifiers.

## Definitions and conventions

At a fixed angular frequency, let the two transverse components of a stationary source have cross-spectral density

\[
W_{ij}(r_1,r_2)=\mathbb E[E_i(r_1)E_j(r_2)^*].
\]

This convention is the complex conjugate/transposed convention of some optics references; observables are unchanged. A physically realizable source has a positive-semidefinite matrix kernel. A polarization-independent deterministic scalar kernel produces

\[
J_{ij}(x)=\iint K(x,r_1)W_{ij}(r_1,r_2)K(x,r_2)^*\,dr_1dr_2.
\]

Define intensity \(I=\operatorname{tr}J\), and, **only where \(I>0\)**,

\[
P(J)=\sqrt{1-4\det J/(\operatorname{tr}J)^2}
     =|\boldsymbol s|/s_0,\qquad
J=(s_0I_2+\boldsymbol s\cdot\boldsymbol\sigma)/2.
\]

`P` is the **local, ensemble-averaged, two-component spectral** degree of polarization. It is not the polarization of an instantaneous deterministic field, a spatially integrated Stokes vector, or a three-dimensional Maxwell polarization measure. A zero-intensity observation has no defined normalized spectrum or degree of polarization and is excluded, not assigned zero.

Normalized-spectrum invariance over an observation set means \(I(x,\omega)=A(x)B(\omega)\), with nonnegative factors and a finite, nonzero integral of \(B\). This is equivalent to \(I(x,\omega)/\int I(x,\nu)d\nu\) being independent of every illuminated \(x\). It does not automatically mean equality to each point's source-plane spectrum.

## C1. Source-domain spectral criterion without a Schell assumption

**Evidence: Certification. Novelty: no priority claim; a Fourier reformulation/generalization of the standard far-field scaling argument, not an improvement over an already known physical law.**

Work in two transverse dimensions, in the ideal scalar/paraxial Fraunhofer model, at a common propagation distance. Suppress the frequency-independent factor \((2\pi z)^{-2}\). The transverse angular coordinate \(s=x/z\) ranges over **all of \(\mathbb R^2\)** in this mathematical model. Put \(k=\omega/c>0\),

\[
G(v;k)=\int_{\mathbb R^2}\operatorname{tr}W(u+v/2,u-v/2;k)\,du,
\quad
\widehat G(q;k)=\int G(v;k)e^{-iq\cdot v}\,dv.
\]

Assume these functions and their Fourier transforms are integrable so that Fourier inversion and the displayed exchanges of integrals apply. Assume a nonzero source and nonzero finite total power. Then

\[
I(s;k)=k^2\widehat G(ks;k).
\]

For a specified nonnegative spectral factor \(B(k)\), the following are equivalent:

1. \(I(s;k)=A(s)B(k)\) for all \(s,k\) (up to the usual almost-everywhere interpretation).
2. There is one function \(g\), independent of \(k\), such that
   \[
   G(v;k)=B(k)g(kv).
   \]

**Proof.** Substitute \(r_1=u+v/2,r_2=u-v/2\) in the Fraunhofer double integral; its Jacobian is one and the phase is \(-ik s\cdot v\), proving the intensity formula. If (2) holds, the change of variable \(t=kv\) gives \(\widehat G(q;k)=B(k)k^{-2}\widehat g(q/k)\), hence (1) with \(A=\widehat g\). Conversely, (1) gives \(\widehat G(q;k)=B(k)k^{-2}A(q/k)\). Fourier inversion and \(q=kt\) give (2), with \(g(v)=(2\pi)^{-2}\int A(t)e^{it\cdot v}dt\). This proves both directions. Since \(G(0;k)\) is the source's spatially integrated spectral power, \(B(k)\) is proportional to that power when \(g(0)>0\). It need not equal the local source spectrum. ∎

**Limits.** Only the midpoint-integrated trace is observable in far-zone intensity; no necessity for the *entire* source coherence function follows. In a nonparaxial physical hemisphere, only \(|q|\leq k\) is sampled; an inverse-Fourier necessity on all \(q\) is then invalid without an additional support/analyticity hypothesis. Obliquity factors and vector projections must also be included in a full-Maxwell theorem. No such theorem is asserted here.

## C2. Complete finite-mode classification for every deterministic scalar probe

**Evidence: Certification (complete proof below). Novelty: NOVELTY-UNCLEAR; closely related to standard constant-output-purity quantum-channel geometry.**

Let \(\phi_1,\ldots,\phi_n\) be linearly independent square-integrable scalar source modes and

\[
E_i(r)=\sum_a c_{ai}\phi_a(r),\qquad
\Gamma_{ai,bj}=\mathbb E[c_{ai}c_{bj}^*],\qquad \Gamma\succeq0.
\]

Let \(\Gamma_{ab}\) be its \(2\times2\) polarization blocks. A deterministic scalar probe with amplitudes \(f_a=\int K(r)\phi_a(r)dr\) gives

\[
J(f)=\Phi(ff^\dagger),\qquad
\Phi(X)=\sum_{a,b}X_{ab}\Gamma_{ab}.
\]

The block matrix \(\Gamma\) is the Choi matrix of \(\Phi\); thus \(\Phi\) is completely positive. This also follows directly by decomposing \(\Gamma\) into nonnegative outer products: each term gives \(A X A^\dagger\). Let \(T=\Phi^*(I_2)\succeq0\), so \(\operatorname{tr}\Phi(X)=\operatorname{tr}(TX)\). The trace support dimension is \(r=\operatorname{rank}T\), **not** the rank of \(\Gamma\). The zero source \(r=0\) is excluded.

For a vector in \(\ker T\), the positive matrix \(\Phi(ff^\dagger)\) has zero trace and is zero. In a Kraus representation this implies every \(A f=0\); consequently all mixed terms involving that kernel vanish too. Restrict to the support and define the trace-preserving completely positive map

\[
\Psi(X)=\Phi(T^{-1/2}XT^{-1/2}).
\]

For \(0\leq p\leq1\), \(P[J(f)]=p\) for **every** \(f\) with \(f^\dagger T f>0\) if and only if the whitened map is one of:

**A. Replacement / factorized family, any \(r\):**
\[
\Psi(X)=\operatorname{tr}(X)C,\quad C\succeq0,\quad\operatorname{tr}C=1,\quad P(C)=p.
\]

**B. Two-mode orientation-preserving family, \(r=2\):**
\[
\Psi(X)=p U X U^\dagger+(1-p)\operatorname{tr}(X)I_2/2,
\quad U\text{ unitary},\quad0\leq p\leq1.
\]

**C. Two-mode orientation-reversing family, \(r=2\):**
\[
\Psi(X)=p U X^{\mathsf T} U^\dagger+(1-p)\operatorname{tr}(X)I_2/2,
\quad U\text{ unitary},\quad0\leq p\leq1/3.
\]

For \(r=1\), only A occurs. For \(r\geq3\), only A occurs. At \(p=0\) the families overlap. The transpose is in a fixed orthonormal basis of the whitened two-mode input space. These conditions preserve the **degree**, not necessarily the polarization ellipse/orientation.

### Proof, including the higher-dimensional exclusion

For a unit input vector \(f\), the normalized output is a density matrix. Write its Bloch vector as \(b(f)\in\mathbb R^3\). A general qubit-input trace-preserving Hermiticity-preserving map is affine on Bloch vectors:

\[
b=a+M x,\qquad |x|=1,
\]

with real \(a\) and real \(3\times3\) matrix \(M\). Constant output degree \(p\) gives

\[
|a|^2+2a^{\mathsf T}Mx+x^{\mathsf T}M^{\mathsf T}Mx=p^2\quad (|x|=1).
\]

Replacing \(x\) by \(-x\) yields \(M^{\mathsf T}a=0\). A real symmetric matrix whose quadratic form is constant on the unit sphere is a scalar multiple of identity (evaluate on coordinate vectors and their pairwise sums), so \(M^{\mathsf T}M=\lambda I_3\). If \(\lambda=0\), \(M=0\), \(|a|=p\), giving A. Otherwise \(M\) is invertible, \(a=0\), and \(M=p O\), where \(O\in O(3)\). Every rotation in \(SO(3)\) is induced by a unitary conjugation on qubit matrices; reflection \((x,y,z)\mapsto(x,-y,z)\) is transposition. Thus these two components of \(O(3)\) give B and C.

Complete positivity supplies the stated ranges rather than being assumed from mere output positivity. With \(|\Omega\rangle=|00\rangle+|11\rangle\) and swap \(F\), the Choi matrices before unitary conjugation are

\[
\Gamma_B=(1-p)I_4/2+p|\Omega\rangle\langle\Omega|,
\qquad
\Gamma_C=(1-p)I_4/2+pF.
\]

Their eigenvalues are respectively \((1+3p)/2\) once and \((1-p)/2\) three times; and \((1+p)/2\) three times and \((1-3p)/2\) once. Positive semidefiniteness gives \(p\leq1\) and \(p\leq1/3\). A's Choi matrix is \(I_r\otimes C\), which is positive. Each displayed map has output Bloch length \(p\) for unit pure inputs, proving sufficiency in dimensions one and two.

Now suppose \(r\geq3\), \(p>0\), and the map is not replacement. Every two-dimensional input compression is a trace-preserving completely positive qubit map with the same constant output degree, so by the preceding argument it is either constant or maps its input sphere onto the sphere of radius \(p\). Nonreplacement means two pure inputs have different outputs: otherwise the polarization identity would make the entire linear map replacement. Their span is a nonconstant two-dimensional compression. Choose orthonormal \(e_1,e_2\) in that span and output coordinates so their Bloch vectors are \(+p\hat z,-p\hat z\). Pick \(e_3\) orthogonal to that span. The two-dimensional classification applied to \(\operatorname{span}(e_1,e_3)\) implies that the output for \(e_3\) is either \(+p\hat z\) (constant compression) or \(-p\hat z\) (nonconstant compression maps orthogonal input states to antipodes). Exchanging \(e_1,e_2\) if needed, take it to be \(-p\hat z\).

The compression to \(V=\operatorname{span}(e_2,e_3)\) must be constant: a nonconstant compression maps orthogonal inputs to different antipodes, whereas both these outputs are \(-p\hat z\). Hence every unit \(w\in V\) has output \(-p\hat z\). Define the Hermitian observable \(B_x=\Psi^*(\sigma_x)/p\). For every such \(w\), the compression to \(\operatorname{span}(e_1,w)\) is nonconstant and maps its north/south poles to \(\pm p\hat z\). Its Bloch action divided by \(p\) is orthogonal and fixes those poles; consequently its \(x\)-row has unit length in the input equatorial plane. In matrix form this says

\[
|\langle e_1,B_x w\rangle|=1\qquad\text{for every unit }w\in V.
\]

But \(w\mapsto\langle e_1,B_x w\rangle\) is a complex linear functional on the two-dimensional complex space \(V\), and has a nonzero kernel. Choosing a unit vector in that kernel is a contradiction. Thus the map is replacement. If \(p=0\), every pure input has output \(I_2/2\); linearity/polarization again gives replacement. This covers all cases. ∎

**Established alternative derivation / prior-art correction.** The independent referee identified an additional baseline: for three Hermitian matrices on a complex space of dimension at least three, their joint numerical range is convex. The primary research paper by Lau, Li, Poon and Sze, *Joint matricial range and joint congruence matricial range of operators* (2020), [DOI 10.1007/s43036-019-00009-w](https://doi.org/10.1007/s43036-019-00009-w), explicitly states this in its introduction and attributes it to Au-Yeung and Poon (1979). We checked the [author-hosted paper](https://faculty.sites.iastate.edu/ytpoon/files/inline-files/AOT_1.pdf); the original 1979 proof was not inspected. Apply that theorem to \(\Psi^*(\sigma_x),\Psi^*(\sigma_y),\Psi^*(\sigma_z)\). Their joint numerical range is exactly the set of pure-input output Bloch vectors. A convex set on a fixed-radius sphere must be a singleton, by the midpoint identity in C3. Thus the dimension-at-least-three conclusion is also an immediate corollary of established mathematics. The elementary proof above is retained for self-contained certification, not as a novelty argument.


**Source meaning.** Family A before whitening is \(\Phi(X)=\operatorname{tr}(TX)C\), equivalently \(\Gamma_{ab}=T_{ba}C\), so
\(W(r_1,r_2)=g(r_1,r_2)C\).
Families B/C are valid positive sources with nonzero cross-polarization correlations and generally varying local polarization direction. They need not be Schell-model sources. Any scalar Fresnel, scalar angular-spectrum, scalar ABCD, aperture or deterministic phase-screen probe is covered by sufficiency; necessity concerns **all** probes, not Fresnel propagation alone. Independent source modes make arbitrary amplitude vectors realizable by some scalar linear functional, but not necessarily by free-space point sampling alone.

## C3. Universal random-kernel robustness forces factorization

**Evidence: Certification. Novelty: elementary convexity consequence, not claimed new.**

Under the finite-mode assumptions, replace a deterministic probe by an arbitrary incoherent mixture of scalar probes. Its modal response is any positive semidefinite matrix \(R=\mathbb E[ff^\dagger]\), and its local coherency matrix is \(\Phi(R)\). This presupposes a scalar medium statistically independent of the source. Fix \(p\). Then

\[
P[\Phi(R)]=p\text{ for every }R\succeq0\text{ with }\operatorname{tr}(TR)>0
\]

**if and only if** \(\Phi(X)=\operatorname{tr}(TX)C\), with \(P(C)=p\).

**Proof.** Whiten as in C2. For any two pure inputs, let their output Bloch vectors be \(b_1,b_2\), each of length \(p\). The equal mixture has vector \((b_1+b_2)/2\), which must also have length \(p\). The identity
\[
|(b_1+b_2)/2|^2=p^2-|b_1-b_2|^2/4
\]
forces \(b_1=b_2\). For \(p=0\) this is automatic. All pure inputs therefore have the same output; their projectors span the Hermitian matrices, so linearity gives the replacement map. Its sufficiency is immediate. ∎

For either exceptional two-mode family B/C,

\[
P[\Psi(R)]=p\sqrt{1-4\det R/(\operatorname{tr}R)^2}=p\,P(R).
\]

Here \(R\) is a response **in the whitened input space**. For an original modal response \(R_0\), put \(S=T^{1/2}R_0T^{1/2}\); the general formula is \(P[\Phi(R_0)]=pP(S)\), not \(pP(R_0)\). For example \(T=\operatorname{diag}(4,1)\), \(R_0=I_2/2\), and \(p=1/2\) give degree \(3/10\), not zero.


This follows from the same Bloch action \(b\mapsto pO b\). For \(p>0\), equality to \(p\) occurs exactly when \(R\) has rank one. The exact example \(R=(|0\rangle\langle0|+|1\rangle\langle1|)/2\) reduces degree \(p\) to zero although each realization has degree \(p\). It is a source/modal counterexample to deterministic-to-ensemble inference, **not** a claim that every atmospheric turbulence model realizes every \(R\).

For any continuous positive kernel of factorized form \(W=gC\), scalar deterministic and scalar extended-Huygens–Fresnel ensemble propagation both give \(J=hC\), directly by pulling \(C\) outside the integral. This sufficiency needs neither finite rank nor a particular turbulence law. Necessity above remains a finite-mode, all-mixtures statement.

## C4. Neither invariant implies the other

**Evidence: Certification of analytic constructions; numerical propagation is Empirical evidence. Novelty: no priority claim.**

### Polarization invariance does not imply spectral invariance

Take the finite-energy two-dimensional coherent scalar source profile
\(u_0(r)=\exp(-|r|^2/(2w^2))\), frequency-independent waist \(w\), source spectrum \(B(k)\), and constant polarization matrix \(C=\operatorname{diag}(3/4,1/4)\). Set
\(W(r_1,r_2;k)=B(k)u_0(r_1)u_0(r_2)^* C\).
C3 gives \(P=1/2\) at every illuminated point under any scalar channel. Fresnel propagation gives on-axis spectral intensity, relative to its initial value,

\[
I(0,z;k)/B(k)=\frac{1}{1+(z/(kw^2))^2}.
\]

It depends on \(k\); the off-axis Gaussian width is also frequency dependent. At \(z=w=1\), equal-weight spectral lines at \(k=1,2\) have on-axis weights \(1/2,4/5\), so normalized weights change from \((1/2,1/2)\) to \((5/13,8/13)\). These are rational identities, not floating-point evidence. The same failure holds for a continuous integrable spectrum positive near both frequencies. Already in the far zone, the angular spectrum is proportional to \(B(k)k^2e^{-w^2k^2|s|^2}\), which is not separable in \(s,k\).

### Far-zone spectral invariance does not imply polarization invariance

Take two statistically independent, orthogonally polarized coherent source modes in two dimensions,

\[
u_a(r;k)=\frac{k}{a^2}\exp[-k^2|r|^2/(2a^2)],\quad
u_b(r;k)=\frac{k}{b^2}\exp[-k^2|r|^2/(2b^2)],\quad a=1,b=2.
\]

Their powers are finite; set \(W_{xx}=B(k)u_a(r_1;k)u_a(r_2;k)^*\), \(W_{yy}=B(k)u_b(r_1;k)u_b(r_2;k)^*\), \(W_{xy}=0\). Direct Fourier integration yields
\(\widehat u_a(ks;k)=2\pi k^{-1}e^{-a^2|s|^2/2}\). After the common Fraunhofer factor,

\[
J(s;k)\propto B(k)\begin{pmatrix}e^{-|s|^2}&0\\0&e^{-4|s|^2}\end{pmatrix}.
\]

The normalized spectrum is independent of \(s\), but
\[
P(s;k)=\frac{|e^{-|s|^2}-e^{-4|s|^2}|}{e^{-|s|^2}+e^{-4|s|^2}}
\]
is zero at \(s=0\) and \(1/3\) at \(|s|^2=\log 2/3\). Thus it is not invariant across the far zone. This construction asserts **far-zone spectrum invariance**, not equality to every source-plane local spectrum. Both implication counterexamples apply to the same far-zone observation set.

## C5. Joint invariance and the chromaticity boundary

**Evidence: Certification. Novelty: elementary operator criterion, not claimed new.**

Consider a family \(\Phi_\omega\) in the **same finite-dimensional input basis** and the same achromatic probe vector \(f\) at every frequency. Let \(T_\omega=\Phi_\omega^*(I_2)\). For positive spectral factor \(B(\omega)\), spectral invariance for every probe is equivalent to

\[
T_\omega=B(\omega)T
\]

for one positive matrix \(T\). **Proof:** the intensity is \(f^\dagger T_\omega f\). Subtract \(B(\omega)/B(\omega_0)\) times the equation at a reference frequency; vanishing of every quadratic form implies vanishing of the Hermitian matrix, by polarization. The converse is substitution. ∎

Joint deterministic invariance is therefore precisely this trace condition plus one of C2's whitened families at each frequency. The spatially constant degree may be \(p(\omega)\); requiring a degree constant in frequency is the additional condition \(p(\omega)=p\).

Joint invariance for every incoherent mixture of the same probes is precisely

\[
\Phi_\omega(X)=B(\omega)\operatorname{tr}(TX)C_\omega,
\quad\operatorname{tr}C_\omega=1,
\]

with the prescribed degree \(P(C_\omega)\), by C3. This is an actual source condition, not an assumption that trace and determinant are independent for arbitrary positive kernels.

In physical Fresnel/ABCD systems, \(f=f(x,\omega)\) is generally chromatic. Then a common \(T\) alone does **not** give spectral invariance: the additional scalar response \(f(x,\omega)^\dagger T f(x,\omega)\) must itself separate into spatial and spectral factors. C1 gives the appropriate far-zone condition. C4 is an explicit negative control against dropping this caveat.

## C6. Physical counterexample: Fresnel invariance is weaker than all-probe invariance

**Evidence: Certification of the explicit source and symmetry argument; Empirical evidence for sampled propagation. Novelty: no claim; an elementary instance of the established opposite-azimuthal-order mechanism, consistent with the structured-source baseline in STATUS.md. Verdict for the proposed necessity transfer: COUNTEREXAMPLE.**

On the two-dimensional source plane set \(r^2=x^2+y^2\), and define four scalar modes

\[
\psi_{0,\pm}(x,y)=\frac{x\pm iy}{\sqrt\pi}e^{-r^2/2},\qquad
\psi_{1,\pm}(x,y)=\frac{(x\pm iy)(2-r^2)}{\sqrt{2\pi}}e^{-r^2/2}.
\]

They are orthonormal. The angular integral separates azimuthal orders \(+1,-1\); within either order substitute \(t=r^2\). The radial Gram matrix is the identity because
\(\int_0^\infty t e^{-t}dt=1\),
\(\int_0^\infty t(2-t)e^{-t}dt=0\), and
\(\int_0^\infty t(2-t)^2e^{-t}dt=2\).
Let \(w_0=1,w_1=1/2\), and take four independent random coefficients to generate

\[
W_{xx}(r_1,r_2)=\frac34\sum_{\ell=0}^1 w_\ell
\psi_{\ell,+}(r_1)\psi_{\ell,+}(r_2)^*,\quad
W_{yy}(r_1,r_2)=\frac14\sum_{\ell=0}^1 w_\ell
\psi_{\ell,-}(r_1)\psi_{\ell,-}(r_2)^*,\quad W_{xy}=W_{yx}=0.
\]

This is a positive-semidefinite, finite-energy source kernel, being a nonnegative sum of polarized coherent-mode outer products. In scalar-mode order \((0+,0-,1+,1-)\), its trace matrix is
\(T=\operatorname{diag}(3/4,1/4,3/8,1/8)\), of rank four.
It is not factorized \(gC\): at equal spatial points the diagonal polarization ratio is \(3\), whereas for equal nonzero radii and angular separation \(\pi/4\) the ratio of the two diagonal kernel entries is \(3i\). The common radial factor there is nonzero.

For fixed \(k>0\), let \(U_z\) be full-plane scalar Fresnel propagation. On fields \(h(r)e^{im\theta}\), the transverse Laplacian acts by

\[
\Delta_\perp[h(r)e^{im\theta}]
=e^{im\theta}\left(h''+h'/r-m^2h/r^2\right).
\]

Therefore \(m=+1\) and \(m=-1\) have identical propagated radial envelopes at every distance. Equivalently the angular Fresnel integral uses
\(\int_0^{2\pi}e^{-ia\cos(\theta-\Theta)}e^{im\theta}d\theta
=2\pi(-i)^mJ_m(a)e^{im\Theta}\);
\(J_{-1}=-J_1\) makes the two radial transfer factors equal.
The modes are smooth Gaussian-polynomial functions, so these propagations and integrals are well defined, and
\(|U_z\psi_{\ell,+}|^2=|U_z\psi_{\ell,-}|^2\) for every transverse point and every \(z\geq0\).
Writing \(H=\sum_\ell w_\ell|U_z\psi_{\ell,+}|^2\), the local matrix is exactly

\[
J(r,z)=H(r,z)\operatorname{diag}(3/4,1/4).
\]

Thus both its normalized matrix and degree \(P=1/2\) are invariant under **all free-space Fresnel distances**, wherever \(H>0\). At dark points, including the axis, the degree is undefined, not zero.

In contrast, the scalar functional
\(L(E)=\int\psi_{0,+}(r)^*E(r)\,d^2r\)
selects just the \(0+\) mode by orthonormality. Its local matrix is
\(\operatorname{diag}(3/4,0)\), of degree **one**.
Consequently this source satisfies physical Fresnel invariance but fails the all-probe hypothesis of C2. The attempted necessity transfer is **false**, not merely unproved. This does not contradict Wolf's sufficiency theorem and does not classify every Fresnel-invariant source. ∎

The same symmetry reasoning applies to rotationally symmetric scalar ABCD propagation; it does **not** apply to every astigmatic ABCD system. `code/fresnel_only.py` uses independent two-dimensional FFT and radial Hankel–Fresnel quadrature, and includes an astigmatic lens as a negative control. The script verifies exact radial orthogonality and trace rank symbolically; its continuum theorem remains the preceding written argument.

## C7. What is and is not settled

The C2 all-probe finite-mode problem and C3 all-mixture problem are fully settled by the proofs above. This does not fully solve Zhao's open-ended 2009 problem. Remaining precise gaps are:

1. Classify general positive kernels invariant under **only** the actual point-evaluation Fresnel family, allowing arbitrary or infinite spatial rank. C8 now settles the approved sector-diagonal four-LG-mode class, but no arbitrary-source necessity transfer is asserted.
2. Treat longitudinal electric-field components, transversality projections and non-scalar Jones kernels in full Maxwell propagation with a specified three-dimensional polarization observable.
3. For any particular random environment, characterize its attainable response cone \(\{\mathbb E[f f^\dagger]\}\), rather than replacing it by all positive matrices without proof.
4. Complete the prior-art positioning of the *optical formulation*. The mathematical dimension exclusion already follows from established joint numerical-range convexity, and the two-mode cases specialize established qubit-channel geometry. Correctness is not novelty.

**Current next action:** the approved C8 proof obligation is closed. Before claiming a publishable discovery, resolve the exact prior-art comparison, including Li's 2015 full text. A distinct future mathematical target is to allow cross-azimuthal-sector covariance in the same four modes; angular interference then prevents the single-SUM reduction. Neither task is silently included in the solved C8 scope.

## Verification results and independent-review dispositions

### Executed reproduction and claim-to-evidence map

In the first phase, the two-script command `verify.py && fresnel_only.py` (with the displayed Python path and environment on each invocation) was run successfully after that phase's final code changes. It exited **0** and printed six `PASS` groups from `code/verify.py`, three `PASS` groups from `code/fresnel_only.py`, and the two output paths. The scripts report Python **3.13.9**, NumPy **2.5.4**, SciPy **1.18.1**, SymPy **1.14.0**, seed **20261014**, and effective `OPENBLAS_NUM_THREADS=1`, `OMP_NUM_THREADS=1`. The later C8 script has its own executed command and evidence below; the current three-script reproduction chain is not being misreported as the historical two-script run.

| Claim | Evidence label / novelty status | Executed command (Python path and environment as above) | Observed evidence | Review disposition |
|---|---|---|---|---|
| C1 far-zone scaling equivalence | Certification of written Fourier argument; no priority claim | `python code/verify.py` | Independent Gaussian Fourier quadratures agree with the scaling construction at three frequencies/angles; all assertions pass. Numerical checks are Empirical evidence only. | First referee: correct, full angular-plane and inversion hypotheses retained. |
| C2 deterministic all-probe classification | Certification; an optical synthesis of established mathematical ingredients, novelty not established | `python code/verify.py` | Symbolic Choi characteristic polynomials and arbitrary-complex-input determinant identities vanish exactly; B/C positive controls and trace whitening pass. Maximum direct-CSD/FFT matrix discrepancy `3.3473e-16`. | First referee: correct, including rank-deficient support, dimension-at-least-three exclusion and endpoint parameters. Joint numerical-range prior art added. |
| C3 all-mixtures factorization and two-mode degradation | Certification; elementary convexity, no novelty claim | `python code/verify.py` | Exact opposite-output mixture is `I/2`; polynomial mixed-input Bloch identity vanishes. Binary random-screen ensemble degree spans approximately `0.3342923–0.4998660`, while each realization has degree `0.5`; formula residual `1.1103e-16`. | First referee: correct; original/whitened response distinction explicitly added. |
| C4 independence of invariants | Certification of positive finite-energy analytic sources; no priority claim | `python code/verify.py` | Rational spectral weights exactly `5/13,8/13`; analytic far-zone degrees `0,1/3`; independent Fresnel FFT gives on-axis intensities `0.5000000000000002,0.8000000000000005`. | First referee: correct; same far-zone observation set and local-vs-integrated distinction retained. |
| C5 matched-achromatic joint criterion | Certification of polarization-identity argument; no novelty claim | `python code/verify.py` | Shared trace factors `2,3` give normalized spectrum `(0.4,0.6)` with residual `1.1103e-16`; nonproportional trace matrices give `(1/3,2/3)` versus `(1/2,1/2)`. | First referee: correct; chromaticity caveat retained. |
| C6 physical Fresnel/all-probe separation | Certification of explicit counterexample and symmetry; no novelty claim | `python code/fresnel_only.py` | Exact radial Gram matrix `I`, positive trace eigenvalues `3/4,1/4,3/8,1/8`, rank four; exact local/projector degrees `1/2,1`. FFT2/Hankel discrepancy at sampled positions/distances at most `2.0018e-14`. | Second referee: correct; source positivity, normalization, nonfactorization, Fresnel symmetry and projector all pass. |

Additional **Empirical evidence**: the factorized Gaussian Schell-model integral agrees with its analytic intensity matrix to `2.2378e-16`; unequal correlation widths change an initially zero degree to a sampled maximum of `0.2821377`. The astigmatic-lens negative control for C6 gives degree range approximately `[0.00173921,0.82036815]`. These are fixed-model numerical observations, not certified bounds for an arbitrary environment.

The propagation algorithms are independent **representations/implementations**, not independent physical models: source-CSD double integration versus covariance-factorized coherent Jones modes plus FFT; and, separately, FFT2 versus Hankel–Fresnel quadrature. They share the source definitions, paraxial assumptions, NumPy/SciPy floating arithmetic and the same machine. No continuum error bound is inferred from agreement.

### Development failures and conditioning amendment

Two early runs stopped at a symbolic eigenvalue-dictionary equality check. SymPy returned algebraically identical eigenvalues in different forms with split multiplicities; merely expanding the keys caused collisions without summing multiplicities. The verifier was changed to test the **complete characteristic polynomial identity**, eliminating representation-dependent dictionary comparison. No mathematical eigenvalue claim changed.

A subsequent run stopped in the focused non-Schell example: the normalized degree error was approximately `4.0323e-4` at a very dim sample even though the maximum matrix discrepancy was only `2.8305e-16`. The first matrix trace there was about `1.1e-14`, so normalization magnified double-integral cancellation. The numerical protocol was amended to assess degree only where intensity exceeds **`1e-6` of the sampled peak**, while retaining the matrix comparison at **all 33 samples**. Free-space cases keep 33 degree samples; focused cases keep 21. This amendment is disclosed, not portrayed as an unchanged preregistered test or a physical exception. C6 uses the same declared floor for its finite-grid degree measurements. Exact zero-intensity points remain excluded by the observable's definition; merely dim points are excluded only from the *numerical degree comparison*, not the theorem.

Both scripts then passed in the final combined run. There was no optimization search, best-seed selection, continuum-certification claim, or statistical generalization claim.

The book excerpt was compared byte-for-byte with its supplied `/tmp` source using `cmp` (exit 0). Its SHA-256 is `c331171ef26a7b4dd543a5b104e01bae450d76780d38ef79d3fa1d090671b7df`.

### Independent Codex review and dispositions

Both invocations used the live configured **`gpt-6.1-sol`**, effort **`max`**, Codex CLI **0.162.1**, **read-only** sandbox, ephemeral session, and explicit no-delegation/no-file-write instructions. Both returned exit **0**. Model/sandbox headers are retained in the two `review/*stderr.log` files. Prompts and untouched final reports are in `review/`. Reports' line numbers refer to the versions they inspected, before this integration.

**First report:** `review/codex-review.md`: “Mathematical claims: correct. Novelty: novelty not established.”

1. **Additional joint-numerical-range baseline — accepted.** Independently read Lau et al.'s primary article and checked the stated theorem and reference. Added the alternative established argument to C2 and the citation/status caveat to `STATUS.md`. No new-theorem claim is retained.
2. **Missing execution history / misleading code comment — accepted.** Added the preceding failure/conditioning history. Corrected the comment so the opposite-output mixture is not misdescribed as a test of the three-dimensional pure-input exclusion. Numerical ratio conditioning and unchanged all-sample matrix checks are explicit.
3. **C2 proof, support whitening, complex conventions and endpoints — confirmed.** Retained the complete proof; no mathematical correction was requested. The source contraction and transposed trace-block indexing were checked independently in the review.
4. **Whitened mixture response — clarification accepted.** Added \(S=T^{1/2}R_0T^{1/2}\) and the rational \(3/10\) example; the original theorem already used \(\Psi\) correctly.
5. **C1/C5 quantifier boundaries — confirmed.** Full paraxial angular plane, integrability and matched-achromatic-probe requirements remain explicit.
6. **C4 positive finite-energy witnesses — confirmed.** Both implications are tested over the same far-zone observation set; no comparison with an integrated Stokes degree is substituted.

**Second report:** `review/fresnel-bridge-review.md`: “Correct. The proposed source is a valid counterexample in the stated full-plane scalar paraxial Fresnel model.”

1. **Normalization, positivity and ranks — confirmed.** The independent radial integrals match the symbolic Gram identities.
2. **Nonfactorization — confirmed.** The phase-dependent diagonal-kernel ratio gives a direct argument independent of C2.
3. **Fresnel symmetry — confirmed.** The referee independently checked the Bessel sign and supplied closed-form propagated modes. The retained proof uses the independently checkable symmetry argument; the supplementary closed forms are not needed as an unverified dependency.
4. **Zero intensity — confirmed.** The reviewer notes that only the axis is dark at finite distance. Our weaker “wherever intensity is nonzero” statement already suffices and is retained.
5. **Projector response — confirmed.** The scalar functional is correctly conjugated and selects only the first mode.
6. **Numerical representation — confirmed.** Both FFT2 and Hankel implementations have the correct modes, weights, phase and measure. The review's extra numerical/tail estimates are advice, not promoted into this package's certified error bounds.
7. **Literal exact degree values / finite-grid scope — accepted and strengthened.** The inspected early script listed the degrees as literals. The final script constructs the source covariance and projected matrix, verifies positive semidefiniteness, and symbolically derives the local and projector degrees. The all-distance propagation statement still comes from the written proof, not the script. Fixed samples, periodic FFT approximation and intensity floor remain explicitly Empirical evidence.

All requested corrections are resolved; no referee found a mathematical counterexample to the stated C1–C6 claims. The original book target remains open **in this project**, and neither review supplies novelty clearance or a general Fresnel/Maxwell classification.

## C8. Approved scoped target: complete four-LG-mode Fresnel classification

### Frozen question and protocol

The user explicitly approved choosing precise subproblems. This target fixes a frequency \(k>0\), waist scale \(a>0\), and integer azimuthal magnitude \(m\geq1\). It allows **every PSD covariance** on radial indices \(n=0,1\), azimuthal sectors \(+m,-m\), and the two transverse polarization components, subject only to **zero cross-azimuthal-sector covariance blocks**. The question is whether the local spectral degree is a single prescribed \(P_\star\in[0,1]\) for every illuminated transverse point at every scalar full-plane Fresnel distance \(z\geq0\).

- **Baseline:** the opposite-azimuthal-order degeneracy in C6 and the established LG propagation/Gouy phases; C2's complete two-input-mode channel classification. No all-probe assumption is imposed on the physical four-mode source.
- **Missing bridge to close:** determine the actual two-radial-mode response set, then show that invariance on that set forces the sum-block polynomial identity. A guessed density of the forward responses in the whole projective line is false; the proof below uses their nonempty interior instead.
- **Decision value:** give a genuine necessity-and-sufficiency theorem for a physically specified subclass containing C6, while retaining arbitrary within-sector polarization/radial correlations and arbitrary PSD sharing between the two sectors.
- **Frozen verification:** symbolic arbitrary-\(m\) LG propagation/normalization identities; exact positive covariances from all classification branches, a rank-one trace with an attained dark direction, and a noninvariant diagonal negative control. Physical propagation uses \(m=1,3\), waist \(a=1\), \(k=7\), grid \(256^2\) on a side-24 square, \(z=1.5,4,8\), an intensity floor \(10^{-6}\) of the sampled peak for normalized numerical degrees, plus independent Hankel–Fresnel quadrature at fixed positions. No optimization or parameter search is involved. Universal quantifiers are carried by the written proof, not numerical tolerances.

**Scoped verdict: SOLVED. Correctness FRONTIER state: DELIVERY-READY. Evidence: Certification of the complete written argument, with independent referee agreement; finite propagation checks are Empirical evidence. Scientific novelty: NOVELTY-UNCLEAR, not established.** The original unrestricted book question remains outside this approved scope. This is not Lean/kernel certification.

### Modes, symmetry, and the exact sum reduction

Write \(R=r/a\), \(M=m+1\), and \(\epsilon\in\{+1,-1\}\). Define the orthonormal source modes

\[
\psi_{0,\epsilon}(r,\theta)
=\frac{R^m e^{-R^2/2}e^{i\epsilon m\theta}}
       {a\sqrt{\pi m!}},\qquad
\psi_{1,\epsilon}
=\frac{M-R^2}{\sqrt M}\psi_{0,\epsilon}.
\]

Here the usual LG radial index is denoted \(n\), avoiding confusion with the degree \(P_\star\). Orthogonality of the two angular sectors follows from \(m\geq1\). For the radial indices, put \(x=R^2\) and use
\(\int_0^\infty x^j e^{-x}\,dx=j!\). The normalized radial inner products are \(1,0,1\), because
\[
\frac{M m!-(m+1)!}{\sqrt M\,m!}=0,\quad
\frac{M^2m!-2M(m+1)!+(m+2)!}{M m!}=1.
\]

Let \(\Gamma_+,\Gamma_-\succeq0\) be arbitrary \(4\times4\) matrices, indexed by \((n,i)\) with \(n=0,1\), \(i=x,y\). Their direct sum is the full mode/polarization covariance; cross-sector blocks are zero. This assumption is invariance under **spatial rotations with the polarization coordinate labels held fixed**. It is specified algebraically, not confused with a simultaneous spin-and-space rotation of a Maxwell field.

The source kernel is
\[
W_{ij}(r_1,r_2)
=\sum_{\epsilon=\pm1}\sum_{b,c=0}^1
(\Gamma_\epsilon)_{bi,cj}\,
\psi_{b,\epsilon}(r_1)\psi_{c,\epsilon}(r_2)^*.
\]
Every such source is PSD and has finite transverse spectral power; conversely every covariance in the stated class has this form.

Put \(t=z/(ka^2)\), \(Q=1+it\). Under scalar Fresnel propagation, after suppressing a common longitudinal phase,
\[
U_z\psi_{0,\epsilon}=q_0(r,z)e^{i\epsilon m\theta},\qquad
q_0=\frac{R^m}{a\sqrt{\pi m!}\,Q^M}
\exp\!\left[-\frac{R^2}{2Q}\right],
\]
\[
U_z\psi_{1,\epsilon}=q_1(r,z)e^{i\epsilon m\theta},\qquad
\frac{q_1}{q_0}
=\frac{M|Q|^2-R^2}{\sqrt M\,Q^2}.
\tag{LG}
\]

**Derivation, not a fitted propagation formula.** A harmonic homogeneous polynomial \(H_m=(x+i\epsilon y)^m\) satisfies
\[
\Delta[H_m e^{-\alpha r^2/2}]
=H_m e^{-\alpha r^2/2}\,[\alpha^2r^2-2\alpha M].
\]
The Gaussian-polynomial expression
\[
F_\alpha(z)=
H_m(1+i\alpha z/k)^{-M}
\exp[-\alpha r^2/(2(1+i\alpha z/k))]
\]
satisfies \(\partial_zF_\alpha=i\Delta F_\alpha/(2k)\) and the required initial value; uniqueness follows by transverse Fourier transformation. Applying \(M+2\alpha\partial_\alpha\) to this expression, then setting \(\alpha=a^{-2}\), gives the \(n=1\) numerator \(M|Q|^2-R^2\). The source normalization is a fixed multiplicative constant in this differentiation. Schwartz regularity justifies the differentiation. This proves (LG).

Define the **sum block**
\[
K=\Gamma_++\Gamma_-\succeq0,\qquad
\Phi_K(X)=\sum_{b,c=0}^1X_{bc}K_{bc},
\]
where \(K_{bc}\) are \(2\times2\) polarization blocks. The local propagated coherency matrix is exactly
\[
J(r,\theta,z)=\Phi_K(q q^\dagger),\qquad
q=(q_0,q_1)^{\mathsf T}.
\tag{SUM}
\]
The angular factors cancel within each sector and the same radial \(q\) occurs in both. Thus local polarization depends on **the sum**, not on either sector separately. In particular, the relevant trace support for applying C2 is at most two, even if the full four-spatial-mode trace matrix has rank four.

### The response lemma: interior, not projective density

For every finite \(z\geq0\) and \(r>0\), \(q_0\neq0\). Write
\[
w=q_1/q_0
=\tau e^{-2i\zeta},\qquad
\tau=\frac{M-R^2/(1+t^2)}{\sqrt M}<\sqrt M,\qquad
\zeta=\arctan t\in[0,\pi/2).
\]

Every complex number in the **open upper half-plane** is attained. Indeed, for \(w=\rho e^{i\phi}\), \(\rho>0\), \(0<\phi<\pi\), choose
\[
t=\cot(\phi/2)>0,\qquad
R^2=(1+t^2)(M+\sqrt M\,\rho)>0.
\]
Then \(\tau=-\rho\), \(\zeta=(\pi-\phi)/2\), and the displayed response equals \(w\).

The forward response set is **not dense in \(\mathbb{CP}^1\)**. In the lower half-plane it requires \(\tau>0\), hence \(|w|<\sqrt M\); for example a neighborhood of \(-2i\sqrt M\) is missing. Its closure is the closed upper half-plane together with the lower closed half-disk \(|w|\leq\sqrt M\), and the point at infinity. The omitted open region invalidates the suggested density proof, but does not invalidate polynomial rigidity.

Let \(T=\Phi_K^*(I_2)\), so \(T_{bc}=\operatorname{tr}K_{cb}\), and suppose \(K\neq0\). Then \(T\succeq0\) is nonzero. On the chart \(v=(1,w)^{\mathsf T}\), intensity is \(v^\dagger T v\); it vanishes exactly when \(v\in\ker T\). Thus there are no dark chart directions if \(\operatorname{rank}T=2\), and at most one if it is one. The axis \(r=0\) is additionally dark because \(m\geq1\). The zero source \(K=0\) is excluded rather than assigned an arbitrary degree.

For a prescribed \(P_\star\), form the real polynomial
\[
\mathcal F(u,v)
=(1-P_\star^2)\,[\operatorname{tr}\Phi_K(ff^\dagger)]^2
-4\det\Phi_K(ff^\dagger),\qquad f=(1,u+iv)^{\mathsf T}.
\]
Its degree is at most four. Fresnel degree invariance makes this polynomial vanish on the attained upper half-plane except at most one dark direction, hence on a nonempty open set. A real polynomial vanishing on an open rectangle is identically zero: first fix one coordinate and use the univariate polynomial identity theorem, then apply it to the coefficient polynomials in the other coordinate. Therefore \(\mathcal F\equiv0\).

By homogeneity this identity holds for all \(f\) with first coordinate nonzero, and by polynomial continuity also for \(f=(0,f_1)\), including the unobserved projective point at infinity. At any dark direction a PSD output of zero trace is the zero matrix, so the polynomial identity remains valid without dividing by zero. Wherever trace is positive, the identity and \(P_\star\geq0\) give \(P[\Phi_K(ff^\dagger)]=P_\star\).

**Consequently, within precisely this source class, physical forward-Fresnel invariance is equivalent to the all-radial-probe property of the SUM block.** It is not equivalent to the all-four-spatial-probe property of the original source.

### Complete necessary-and-sufficient parameterization

For nonzero \(\Gamma_+\oplus\Gamma_-\), the following are equivalent:

1. \(P[J(r,\theta,z)]=P_\star\) at every illuminated point and every \(z\geq0\).
2. The sum block \(K\) has nonzero \(T=\Phi_K^*(I_2)\), and after restricting to its trace support and whitening,
   \[
   \Psi(X)=\Phi_K(T^{-1/2}XT^{-1/2}),
   \]
   it is exactly one of:
   - **Replacement:** \(\Psi(X)=\operatorname{tr}(X)C\), \(C\succeq0\), \(\operatorname{tr}C=1\), \(P(C)=P_\star\), for trace-support dimension one or two.
   - **Depolarizing branch:** trace-support dimension two and
     \(\Psi(X)=P_\star U XU^\dagger+(1-P_\star)\operatorname{tr}(X)I_2/2\), \(0\leq P_\star\leq1\).
   - **Transpose-depolarizing branch:** trace-support dimension two and
     \(\Psi(X)=P_\star U X^{\mathsf T}U^\dagger+(1-P_\star)\operatorname{tr}(X)I_2/2\), \(0\leq P_\star\leq1/3\).

Here \(U\) is an arbitrary polarization unitary and the transpose is in the fixed whitened radial basis. The two-mode proof and complete-positivity endpoint conditions are the already proved C2, now legitimately applicable by the response lemma. Rank-one trace support can only give replacement; all dark directions are handled as above.

For **all** physical covariances in the class, first choose any permitted nonzero sum block \(K\), then choose an arbitrary Hermitian \(L\) with
\[
0\preceq L\preceq K,\qquad \Gamma_+=L,\quad \Gamma_-=K-L.
\tag{SPLIT}
\]
Conversely every solution has exactly this description, because its two sector covariances are PSD and sum to \(K\). Neither sector must have degree \(P_\star\) by itself. The class includes C6: its sum block is
\(\operatorname{diag}(1,1/2)\otimes\operatorname{diag}(3/4,1/4)\), a replacement sum, while its full spatial trace support has rank four. ∎

### Precisely supported isotropic-ABCD corollary

The same classification is equivalent to invariance under **every centered, lossless, polarization-independent isotropic real ABCD system**, with \(AD-BC=1\), in the scalar paraxial model. For \(B\neq0\), its Collins kernel is proportional to
\[
\exp\!\left[\frac{ik}{2B}
\left(A r'^2+D r^2-2rr'\cos(\theta-\theta')\right)\right].
\]
Angular integration has the same \(J_{\pm m}\) identity as Fresnel propagation, so it produces common radial amplitudes \(q_0,q_1\) for the two azimuthal sectors. Thus (SUM) still holds and the classified sum block preserves the degree for those amplitudes. For \(B=0\), common scalar magnification and quadratic phase give the same conclusion directly. Necessity follows because forward Fresnel systems are members of this ABCD family. No density assertion for one fixed ABCD system is needed.

This does **not** cover astigmatism, polarization-dependent Jones kernels, cross-azimuthal-sector covariance, general other radial modes, random ensemble averaging, or full Maxwell propagation. C6's astigmatic negative control is deliberately retained.

### C8 executed exact identities and physical propagation evidence

Executed from this folder:

```sh
OPENBLAS_NUM_THREADS=1 OMP_NUM_THREADS=1 /Users/jinleic/jinleic-workspace/scratch/ai4s-venv/bin/python code/lg_fresnel_classification.py
```

The command exited **0** on its first run and printed five `PASS` groups, then `WROTE results/lg-fresnel-classification.json`. Earlier scripts were not rerun during this scoped continuation; the parent independently reported replaying all nine earlier PASS groups.

**Certification of exact sub-identities:** arbitrary positive-integer \(m\) radial paraxial PDE residuals are zero for both \(n=0,1\); their normalization/cross-inner-product identities reduce to \(1,0\). The upper-half-plane response and inverse identities simplify exactly. Seven rational/complex-rational PSD sector pairs have identically zero constant-degree polynomial: C6's split, complex-trace replacement, a nontrivially split depolarizing source, transpose endpoint \(P_\star=1/3\), trace-rank-one source, and endpoints \(P_\star=0,1\). At the physically attained dark direction \(m=3,t=1,R^2=12,w=i\), the rank-one-trace source has exactly zero coherency matrix; its degree is left undefined.

The negative sum \(K=\operatorname{diag}(3,1,1,3)\) gives residual \(-16(u^2+v^2)\) when \(P_\star=1/2\), and squared degrees \(1/4,0\) at the attained directions \(w=0,i\). A nontrivial PSD splitting has different individual-minus-sector squared degrees \(233/1024\) and \(76369/286225\), despite invariant degree \(1/2\) for the sum. Thus the verifier checks the **sum-only** condition rather than accidentally requiring each sector to satisfy it.

**Empirical evidence:** seven sources, two azimuthal magnitudes and three distances give **42 physical propagation cases**. Independent propagation of a covariance-factorized random Jones field with a 2D FFT agrees with the analytic sum-block prediction to maximum absolute matrix error **\(3.3308\times10^{-16}\)**. Maximum normalized-degree error on the declared non-dim sample set is **\(1.7786\times10^{-13}\)**. Independent radial Hankel–Fresnel quadratures at fixed points differ from the derived analytic modal amplitudes by at most **\(4.4816\times10^{-14}\)**. The noninvariant control spans sampled degrees approximately \(0.00138\)–\(0.49978\) for \(m=1\) and \(0.000959\)–\(0.49998\) for \(m=3\).

The numerical representations share the specified source and scalar paraxial model, but use different propagation encodings. Exact PSD checks precede floating covariance factorization; tiny negative numerical eigenvalues representing exact zeros are clipped only after exact PSD certification. The finite periodic grid, quadrature truncation and intensity floor are **not** rigorous continuum error bounds. No new isotropic-ABCD numerical run is claimed: that corollary follows from the exact common-radial-kernel argument; the earlier ABCD tests and astigmatic negative control are retained separately.

### C8 independent referee and final dispositions

The new scoped proof was reviewed independently through Codex CLI **0.162.1**, configured model **`gpt-6.1-sol`**, effort **`max`**, ephemeral **read-only** sandbox. The invocation returned **exit 0**. The prompt, untouched report and runtime identity header are retained in `review/lg-fresnel-prompt.md`, `review/lg-fresnel-review.md`, and `review/lg-fresnel-stderr.log`.

The referee's mathematical verdict is **correct**: “No mathematical proof obligation remains for this scoped theorem.” Its separate novelty verdict is **not established**. It inspected the saved physical results and made independent finite-matrix/derivation checks; it did **not** run the writing verification script. The author remains responsible for the complete argument above.

1. **All-\(m\) propagation and normalization — confirmed.** The referee independently checked the harmonic-polynomial evolution and Gaussian-parameter derivative with normalization held fixed. This agrees with the exact arbitrary-\(m\) PDE and factorial identities exercised by the script. No correction required.
2. **Attained set and polynomial necessity — confirmed.** The exact finite response set is the open upper half-plane, the lower open half-disk \(|w|<\sqrt{m+1}\), and the real interval \((-\infty,\sqrt{m+1})\). Its closure is as stated; the failed density route is not used. Open-set vanishing, homogeneity and polynomial continuity are sufficient. No correction required.
3. **PSD contraction, reversed trace-block indices and dark directions — confirmed.** \(T_{bc}=\operatorname{tr}K_{cb}\), support-restricted whitening and zero-trace annihilation are correct. Rank-one dark directions and the zero source are not assigned a polarization degree. No correction required.
4. **Complete channel branches and endpoints — confirmed.** The reviewer independently checked the two-mode affine-sphere argument and Choi positivity bounds, including \(P_\star=0,1\) and the transpose endpoint \(1/3\). No missing family found.
5. **SUM reduction and arbitrary PSD sharing — confirmed.** No covariance within a sector has been discarded. \(0\preceq L\preceq K\) is precisely the complete constraint on sector sharing. The original four-mode trace rank may still be four. C6 is preserved, not contradicted.
6. **Isotropic real ABCD corollary — confirmed.** The Bessel identity handles negative \(B\); at \(B=0\), negative magnification contributes the same \((-1)^m\) factor to both sectors. No unjustified general-astigmatic or arbitrary-chiral-kernel extension is made.
7. **Non-diagonal physical numerical sources — confirmed.** The nontrivially split case really includes complex radial/polarization correlations; its trace matrix is \(\begin{pmatrix}17/16&5i/8\\-5i/8&37/16\end{pmatrix}\). The full sector covariance is factored into coherent Jones fields before FFT propagation. The reviewer correctly distinguishes inspected saved results from independently rerun measurements.
8. **Novelty limitation — retained.** Primary LG/Gouy and channel machinery are established. The 2021/2022 pattern-invariance sources have different stated hypotheses, but absence of a matching earlier classification is not proved. The 2015 publisher full-text attempt led to a JavaScript access page and then a bot challenge; its verified abstract is not treated as full-text clearance.

No mathematical revision was requested, and no new verification run was needed after this documentation-only review integration. The approved class is fully characterized by a complete written proof; broader source classes and the original book-level question remain outside that result.
