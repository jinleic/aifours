# A norm-ranked spiral dense forest

Date: 2026-10-14 (America/Los_Angeles).

**Evidence label: Certification of the exact theorem below, using established ingredients. Novelty state: NOVELTY-UNCLEAR until the bounded source screen and independent review are dispositioned.** Finite-grid dense forests and the classical circle-discrepancy estimate are prior art, not claimed inventions. This addresses Tevet's explicitly stated spiral-forest existence conjecture, not the physics book's cone-energy minimization problem, optimal visibility, or a Danzer set.

## 1. Exact target and construction

Tevet, *Chabauty Limits of Fermat Spirals*, arXiv:2506.22863v2, defines a spiral set as \(\{\sqrt{k}u_k:k\ge1\}\), with arbitrary \(u_k\in S^1\). Its Further Questions section, PDF p.12, conjectures existence of such a set that is a dense forest. No constant angular increment, uniform separation, continuity of the angle sequence, or Delone hypothesis is part of this target.

Use
\[
Q=\frac1{\sqrt3}\begin{pmatrix}1&-\sqrt2\\\sqrt2&1\end{pmatrix},\quad
G=\mathbb Z^2\cup Q\mathbb Z^2,\quad F=G\setminus\{0\},\quad c=\sqrt{2\pi}.
\tag{1}
\]
Each nonzero point has a unique label \((t,a,b)\), with \(t\in\{0,1\}\), \((a,b)\in\mathbb Z^2\setminus\{0\}\), representing \(Q^t(a,b)\); uniqueness is proved below. Order these labels lexicographically by
\[
(a^2+b^2,\ t,\ a,\ b).
\tag{2}
\]
Write the resulting points as \(f_k\), their norms as \(r_k\), and define
\[
u_k=f_k/r_k,\qquad s_k=\sqrt{k}\,u_k,\qquad S=\{s_k:k\ge1\}.
\tag{3}
\]
This is a deterministic effective construction using integer squared norms for ordering, not rounded irrational physical coordinates.

### Theorem

1. Every nonzero point of both lattices occurs once, \(r_k\to\infty\), and \(\|s_k\|^2=k\) exactly. Thus \(S\) is locally finite and \(\#(S\cap\overline B_R(0))=\lfloor R^2\rfloor\).
2. Uniformly through all tied lattice shells,
   \[
   \|s_k-cf_k\|=O(r_k^{-1/3})=o(1).
   \tag{4}
   \]
3. There is a finite nonincreasing visibility function \(W:(0,\infty)\to(0,\infty)\) such that **every open rectangle of width \(\varepsilon\) and length \(W(\varepsilon)\), at every position and orientation, contains a point of \(S\)**.

Consequently \(S\) is a spiral dense forest in Tevet's precise definition. Neither optimal growth of \(W\) nor the Danzer property nor uniform discreteness is asserted.

## 2. No common rational direction and no nonzero overlap

For nonzero integer vectors \(p=(a,b)\), \(q=(d,e)\),
\[
\sqrt3\det(p,Qq)=(ae-bd)+\sqrt2(ad+be).
\tag{5}
\]
If the determinant vanished, irrationality of \(\sqrt2\) would force both integer coefficients to vanish. But
\[
(ae-bd)^2+(ad+be)^2=(a^2+b^2)(d^2+e^2)>0,
\tag{6}
\]
a contradiction. Therefore the two lattices have no common nonzero rational line direction. In particular, they have no common nonzero point. This includes vertical directions; no division by a slope denominator is used.

Also \(Q^TQ=I\), so both copies have exactly the same integer squared-norm shells and covolume one. Each finite disk contains finitely many labels. Every label eventually appears, and only finitely many lie before any fixed norm, proving the enumeration assertions in Theorem 1.

## 3. Established ingredient: a union of two grids is a dense forest

Finite-grid forest constructions and their irrationality characterization are established in Adiceam–Solomon–Weiss (2022) and Shirandami (2023), Theorem 1.1. Here is a self-contained sufficient argument for (1), so no qualitative-to-uniform gap is delegated to a citation.

### 3.1 Irrational directions give dense positive-time torus lines

For \(v\in\mathbb R^2\setminus\{0\}\) not parallel to an integer vector, the positive-time line \(a+tv\pmod{\mathbb Z^2}\), \(t\ge0\), is dense in \(\mathbb T^2\). Indeed, \(v_1\ne0\) and \(v_2/v_1\) is irrational. To hit a prescribed first coordinate modulo one, take \(t=(x-a_1+m)/v_1\) with integers \(m\) of the sign making \(t\to+\infty\). The second coordinates are an irrational circle rotation and are dense. Density of positive multiples of an irrational number follows from the pigeonhole principle: arbitrarily small nonzero fractional steps exist, and their forward multiples form arbitrarily fine nets of the circle. Hence every nonempty torus ball is hit at some finite nonnegative time, from every initial phase.

By §2, for every unit direction \(v\), at least one of \(v\) and \(Q^{-1}v\) is irrational in this sense. We do **not** claim that the combined flow is dense in a four-dimensional torus; density in one of its two factors suffices.

### 3.2 Compactness makes the hitting time uniform in position and direction

Fix \(\delta>0\). On the compact parameter space
\[
K=S^1\times\mathbb T^2\times\mathbb T^2
\]
let, for each real \(t\ge0\),
\[
U_t=\{(v,a,b):\min(d_{\mathbb T^2}(a+tv,0),
 d_{\mathbb T^2}(b+tQ^{-1}v,0))<\delta\}.
\tag{7}
\]
Each \(U_t\) is open because the torus distance is continuous. Section 3.1 says \(\bigcup_{t\ge0}U_t=K\). A finite subcover exists. Thus some finite integer \(H_G(\delta)\ge1\) bounds all the selected times.

For any physical starting point \(x\), substitute \(a=[x]\), \(b=[Q^{-1}x]\). A hit in either factor means that \(x+tv\) is within **strict distance \(\delta\)** of a point of \(G\), since \(Q\) is orthogonal. Hence every length-\(H_G(\delta)\) segment is \(\delta\)-close to \(G\), uniformly over all starts and directions. One may define \(H_G(\delta)\) as the least positive integer with this universal property; it is finite and nonincreasing in \(\delta\).

The density of \(G\) is finite by lattice counting. Scaling preserves the visibility property, and
\[
H_{cG}(\delta)=cH_G(\delta/c)
\tag{8}
\]
is a finite nonincreasing segment-visibility function for \(cG\). Deletion of the origin is harmless by the finite-core argument in §5, rather than by ignoring that point.

## 4. Classical circle discrepancy gives a uniformly vanishing radial correction

### 4.1 The required error estimate, including real radii

Let \(N_0(R)=\#(\mathbb Z^2\cap\overline B_R)\). We use the classical bound
\[
N_0(R)=\pi R^2+O(R^{2/3})\qquad(R\ge2\text{ real}).
\tag{9}
\]
It is the planar positive-curvature estimate stated in Guo, *Rev. Mat. Iberoam.* 31 (2015), p.411, DOI 10.4171/rmi/839; **not** Guo's stronger almost-every-rotation theorem. To state all assumptions explicitly, a short standard proof follows.

Choose a nonnegative smooth function \(\phi\), supported in the open unit disk, with integral one. Put \(\phi_h(x)=h^{-2}\phi(x/h)\). For \(0<h\le1\), the smooth inner/outer functions
\[
f_-=1_{B_{R-h}}*\phi_h,\qquad f_+=1_{B_{R+h}}*\phi_h
\]
satisfy \(f_-\le1_{\overline B_R}\le f_+\), also at the disk boundary. Their Fourier transforms, using \(e^{-2\pi ix\cdot\xi}\), satisfy for nonzero integer \(\ell\)
\[
\widehat{1_{B_R}}(\ell)=\frac{R}{\|\ell\|}J_1(2\pi R\|\ell\|),\qquad
|\widehat{1_{B_R}}(\ell)|\ll R^{1/2}\|\ell\|^{-3/2}.
\tag{10}
\]
The formula is the disk-slicing/Bessel integral and the bound is the fixed-order estimate \(J_1(x)=O(x^{-1/2})\) for \(x\ge1\); see DLMF [10.9.4](https://dlmf.nist.gov/10.9.E4) and [10.17.3](https://dlmf.nist.gov/10.17.E3).

Poisson summation applies to the smooth compactly supported \(f_\pm\), not directly to the discontinuous disk indicator. Since \(\widehat\phi(h\ell)\ll_M(1+h\|\ell\|)^{-M}\) for any fixed \(M>2\), and the number of lattice vectors in a unit-width annulus of radius \(j\) is \(O(j)\), the nonzero Fourier contribution is
\[
\ll R^{1/2}\sum_{j\ge1}j^{-1/2}(1+hj)^{-M}
\ll R^{1/2}h^{-1/2}.
\]
The zero-frequency volume difference is \(O(Rh)\), so the sandwich gives
\[
|N_0(R)-\pi R^2|\ll Rh+R^{1/2}h^{-1/2}.
\]
Taking \(h=R^{-1/3}\) proves (9), uniformly for all real \(R\ge2\). The lattice-annulus estimate follows by comparing the disjoint unit squares centered at lattice points with an annulus enlarged by a fixed width. No thin discrete shell is replaced by its area.

### 4.2 Strict counts, ties, and the normalization constant

Since the only overlap of the two lattices is the origin,
\[
N_F(R)=2(N_0(R)-1)=2\pi R^2+O(R^{2/3}).
\tag{11}
\]
For \(r>2\), taking real \(R\uparrow r\) gives the same estimate for the strict count \(N_{F,<}(r)\). Local finiteness ensures that this left limit is the strict count. The finitely many radii \(1\le r\le2\) can be absorbed by increasing the absolute constant. Thus both count estimates hold for every shell radius \(r\ge1\).

For every possible rank in a shell,
\[
N_{F,<}(r)+1\le k\le N_F(r),
\qquad |k-2\pi r^2|\le C r^{2/3}
\tag{12}
\]
for a single constant \(C\). This controls the **entire tie**, not just its last element. Now
\[
\|s_k-cf_k\|=|\sqrt{k}-\sqrt{2\pi}\,r_k|
=\frac{|k-2\pi r_k^2|}{\sqrt{k}+\sqrt{2\pi}\,r_k}
\le\frac{C}{\sqrt{2\pi}}r_k^{-1/3}.
\tag{13}
\]
This proves (4). The scale is \(\sqrt{2\pi}\), not \(\sqrt\pi\): the base set has two covolume-one grids. Merely knowing \(N_F(R)\sim2\pi R^2\), or an \(O(R)\) error, would not imply a vanishing displacement.

## 5. Vanishing-displacement stability, with the finite core handled

We prove exactly the stability needed, without requiring uniform separation.

**Lemma.** Let \(A\subset\mathbb R^2\) have a finite segment-visibility function \(H_A(\delta)\), nonincreasing in \(\delta\). Suppose a map \(p\mapsto\psi(p)\in B\) is defined for all \(p\in A\) outside a fixed ball, and
\[
\sup_{p\in A,\ \|p\|>R}\|\psi(p)-p\|\longrightarrow0
\quad(R\to\infty).
\tag{14}
\]
Then \(B\) has uniform segment visibility. If \(B\) is locally finite and of finite density, it is a dense forest. Additional points of \(B\) and arbitrary changes inside the finite core cannot harm this conclusion.

**Proof.** Given \(\eta>0\), take \(\delta=\min(\eta/4,1/4)\). Choose an integer \(R(\delta)\ge1\) so that the map is defined and its error is strictly less than \(\delta\) for all \(\|p\|>R(\delta)\). These radii may be chosen nonincreasing in \(\delta\), by choosing the least admissible integer above the fixed domain threshold. Set
\[
L_B(\eta)=2H_A(\delta)+2R(\delta)+4.
\tag{15}
\]
A segment of this length spends at most \(2(R(\delta)+1)\) of its length inside the closed ball \(\overline B_{R(\delta)+1}\). Its outside portion has at most two components and total length at least \(2H_A(\delta)+2\). Therefore one outside component contains a **closed** subsegment of length \(H_A(\delta)\), entirely and strictly outside that ball; the extra unit of length supplies room to avoid boundary endpoints.

Visibility of \(A\) supplies a point \(p\in A\) within strict distance \(\delta\) of this subsegment. Its norm is greater than \(R(\delta)+1-\delta>R(\delta)\), so it is not in the exceptional core and the displacement estimate applies. Its image is within distance \(<2\delta\le\eta/2<\eta\) of the original segment. The length (15) is finite, independent of start and direction, and nonincreasing in \(\eta\). This proves the lemma. It also proves stability under deletion of finitely many points by using the identity map outside a ball containing them. ∎

Apply the lemma with \(A=cG\), \(B=S\), and \(\psi(cf_k)=s_k\) on all nonzero points. The omitted origin lies inside the core. Equation (13) proves (14) uniformly outside a radius, not just along a selected subsequence. Section 3 supplies \(H_A\). Exact radii in (3) give local finiteness and finite density of \(S\), so it is a dense forest.

## 6. Match Tevet's open-rectangle and decreasing-function definition

Let \(L_S\) be (15) for this construction. For \(\varepsilon>0\), put
\[
W(\varepsilon)=L_S(\min(\varepsilon,1)/4)+1.
\tag{16}
\]
This is finite and nonincreasing on the whole positive half-line. In any open rectangle of width \(\varepsilon\) and length \(W(\varepsilon)\), take the centerline segment obtained by removing length \(1/2\) at each longitudinal end. It has length \(L_S(\min(\varepsilon,1)/4)\). The preceding lemma supplies an \(S\)-point at distance strictly less than \(\min(\varepsilon,1)/4\) from this inner segment. Its transverse distance is strictly less than \(\varepsilon/2\), and its longitudinal overshoot is less than \(1/4\), smaller than the end padding. The point is therefore **strictly inside** the rectangle. This addresses endpoints and open boundaries, rather than identifying a segment's tubular neighborhood with a rectangle without padding.

Finally, distinct exact radii make all \(s_k\) distinct, and
\[
\#(S\cap\overline B_R)=\lfloor R^2\rfloor,
\qquad\lim_{R\to\infty}\#(S\cap\overline B_R)/R^2=1.
\tag{17}
\]
For open balls only the possible boundary point changes. Thus the finite-density condition in Tevet's Eq. (1) is satisfied. Equations (3), (16), and (17) prove every clause of the stated theorem. **The proof is universal; it does not depend on the finite smoke computations.**

## 7. Scientific checks and evidence limits

`code/verify.py` constructs deterministic finite prefixes with two independent integer enumerators, verifies algebraic norm and direction identities, handles complete/partial ties, and uses rational Machin-series bounds on pi for finite radial-correction bounds. A finite set of segment-distance observations is explicitly labeled Empirical evidence; it does not certify a visibility function or extrapolate to all rectangles.

The finite pi enclosure uses \(\pi=16\arctan(1/5)-4\arctan(1/239)\) and the alternating-series next-term bound (20 terms per arctangent). The rational tangent calculation gives \(\tan(4\arctan(1/5)-\arctan(1/239))=1\); the angle is strictly between zero and one, hence in \((0,\pi/2)\), fixing the correct branch of Machin's identity. For each shell, the stored rational upper bound uses both endpoint ranks and integer lower bounds for the square-root denominator in (13). Absolute radial displacement is maximized at an endpoint rank. Thus each recorded rational bound covers every tie rank in the specified finite annulus; the rounded decimal is for display only.

Negative controls use actual changed constructions or assumptions: a rational/zero rotation has a common lattice direction and an infinite empty strip; omitting one grid changes the rank count; a wrong \(\sqrt\pi\) normalization has a rigorously detected large finite radial discrepancy. Bounded displacement alone is insufficient: sending every point of \(G\) to a nearest integer lattice point moves it by at most \(\sqrt2/2\), and its image is \(\mathbb Z^2\), which has infinite empty strips. This does not contradict §5 because that displacement does not tend to zero.

## 8. Observed scientific replay

Command actually run from this folder:

```sh
/Users/jinleic/jinleic-workspace/scratch/ai4s-venv/bin/python -B code/verify.py
```

The exact-control output was:

```text
PASS: exact norm identities 25704 ; independent enumerators at radii (8, 16, 32, 64)
PASS: exact direction pairs 6400 ; radial thresholds 257 ; largest tie 64
PASS: omitted-grid, zero-rotation, wrong-scale controls; wrong-scale lower bound > 1
```

The rational certified finite displacement bounds, for base shell radii in each interval \([R/2,R]\), have decimal approximations:

| R | Upper bound, approximate display |
|---|---:|
| 8 | 0.8730275078038984 |
| 16 | 0.5386217666756009 |
| 32 | 0.4828258150919155 |
| 64 | 0.3187965753376709 |

The exact fractions, not these decimal displays, are in `results/verification.json`. The wrong \(\sqrt\pi\) normalization has a certified finite displacement lower bound approximately 46.6765 at the final sample point, hence strictly greater than 1. The complete prefix contains 25,704 points. Both integer enumerators agree at all four radii, including the same partial-shell ordering; all 25,704 algebraic norm identities, 6,400 nonzero integer direction pairs in the coordinate box \([-4,4]^2\), and 257 radial thresholds passed.

**Empirical evidence only:** 216 fixed-center/fixed-direction segments of length 24 had maximum sampled nearest distance 0.25049494379344645; another 216 of length 48 had maximum 0.15025703193696194. These are float64 observations without an interval error certificate. They neither establish a global visibility bound nor carry any step of the theorem.

## 9. Claim ledger and review boundary

- **Certification:** §§1–6 prove the exact all-radius spiral dense-forest existence statement, including uniform visibility and the finite core.
- **Reproduction:** the two-grid forest and classical disk-discrepancy ingredients are established prior art. The source/formula choices are independently checked in `STATUS.md`.
- **Exact finite controls:** the algebraic identities, independent enumerators, and rational finite displacement bounds above validate the finite construction. They are not an infinite-set proof.
- **Empirical evidence:** only the two sampled segment-distance observations.
- **Novelty:** no worldwide-first, new-grid-forest, improved-visibility, Danzer, Delone-separation, or broad book-energy claim. The exact source question is explicitly conjectural; the bounded screen did not identify a settling source, but cannot certify its absence.

Read-only independent referee prompts, pinned inputs, and raw outcomes are retained under `review/`. Their disposition is recorded after completion rather than inferred from launch or partial logs.
