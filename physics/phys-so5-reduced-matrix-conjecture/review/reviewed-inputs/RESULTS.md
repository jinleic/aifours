# Proof of the CRW SO(5)-reduced matrix-element formula

Date: 2026-10-14 (America/Los_Angeles).

**Claim class: Certification. Novelty status: NOVELTY-UNCLEAR.** The argument below is a corollary of classical spherical-harmonic theory and Rogers's Gegenbauer linearization. Neither the formula nor those ingredients are claimed as new. The historically explicit conjecture is Caprio–Rowe–Welsh (CRW), *Computer Physics Communications* **180**, 1150–1163 (2009), arXiv:0902.0020, §2.5, Eq. (29). This is a proof of that precise statement in its own convention, not a solution of every CFP recurrence in Bao's book problem.

## 1. Statement and conventions

Let \(\mathcal H_v\) be the space of degree-\(v\) spherical harmonics on the unit sphere \(S^4\subset\mathbb R^5\). Its dimension is
\[
d_v={v+4\choose4}-{v+2\choose4}
=\frac{(v+1)(v+2)(2v+3)}6,
\]
where a binomial coefficient with upper argument smaller than 4 is zero. These are the symmetric irreducible SO(5) representations \((v,0)\) of CRW. The SO(3) branching multiplicity label is retained in an orthonormal basis; no multiplicity-free SO(3) hypothesis is imposed.

**Use CRW's measure**, not unit probability measure and not ordinary surface area:
\[
d\mu=\sin3\gamma\,d\gamma\,d\Omega,
\quad0\le\gamma\le\pi/3,
\quad\int_{\mathrm{SO}(3)}d\Omega=8\pi^2,
\quad V:=\int d\mu=\frac{16\pi^2}{3}.
\tag{1}
\]
On functions of the quadrupole direction, this is the invariant sphere measure scaled to mass \(V\). Ordinary unit-sphere area is \(8\pi^2/3\); substituting it would give a wrong factor of two in the squared reduced element. This measure and the constant harmonic \(\sqrt3/(4\pi)\) are given in CRW §2.2 and Table I, and Welsh–Rowe (2016), Eqs. (43)–(44).

Write
\[
R(v_3;v_2,v_1)
=\langle\Psi_{v_3}\|\widehat\Psi_{v_2}\|\Psi_{v_1}\rangle.
\]
Here \(\widehat\Psi\) is **multiplication by the normalized harmonic**, not an arbitrary SO(5) tensor operator. The reduced-element normalization is CRW Eqs. (26)–(28). Its phase is chosen positive as stated immediately after Eq. (28). Different CG phase choices need not give the same signed number.

### Theorem 1 (the full quantified CRW Eq. (29))

For every \(v_1,v_2,v_3\in\mathbb Z_{\ge0}\), the multiplication reduced element is zero unless the sum is even and all triangle inequalities hold. For every admissible triple, set
\[
s=(v_1+v_2+v_3)/2,\qquad j_i=s-v_i\in\mathbb Z_{\ge0}.
\]
Then, in the specified positive phase,
\[
\boxed{
R(v_3;v_2,v_1)=\frac1{4\pi}
\frac{(s+1)!}{j_1!j_2!j_3!}
\sqrt{\frac{(2v_1+3)(2v_2+3)}{(v_3+1)(v_3+2)}}
\sqrt{\frac{(2s+4)(2j_1+1)!(2j_2+1)!(2j_3+1)!}{(2s+3)!}}.
}
\tag{2}
\]
The forbidden-case rule precedes factorial evaluation. There are no negative factorials or limiting prescriptions.

## 2. Reduced-element normalization as a basis-independent trace

Choose any orthonormal bases \(Y_{v,a}\) in \(L^2(S^4,d\mu)\), and put
\[
T_{abc}=\int_{S^4}\overline{Y_{v_3,c}(x)}Y_{v_2,b}(x)Y_{v_1,a}(x)\,d\mu(x).
\]
Combining the ordinary SO(3) Wigner–Eckart convention in CRW Eq. (20) with its Eq. (26) cancels the factor \(\sqrt{2L_3+1}\). Thus
\[
T_{abc}=R(v_3;v_2,v_1)\,C_{ab}^{c},
\]
where \(C\) is the full SO(5) Clebsch–Gordan coefficient, including the ordinary SO(3) CG factor. For each fixed output index \(c\), unitarity in Eq. (25), equivalently Eq. (27) followed by ordinary SO(3) CG orthogonality, gives \(\sum_{a,b}|C_{ab}^c|^2=1\). Consequently
\[
\boxed{d_{v_3}|R|^2=\sum_{a,b,c}|T_{abc}|^2.}
\tag{3}
\]
This is precisely the squared quantity in Eq. (28), not an independently redefined reduced element.

There is no suppressed SO(5) outer multiplicity in this coupling of three symmetric traceless representations. One way to see this is to realize each representation as traceless symmetric tensors. An invariant contraction of three such tensors must contract indices between different tensors. The numbers of pairwise contractions are uniquely \(j_1,j_2,j_3\); contractions within one tensor vanish by tracelessness. An SO(5) epsilon invariant would require five independent antisymmetrized slots, but with only three symmetric tensor groups at least two slots come from the same group and it vanishes. Thus the invariant space has dimension at most one. Positivity of the integral below proves it is nonzero for every admissible triple. SO(3) internal multiplicities have all been summed in (3), rather than discarded.

## 3. Addition theorem and one-dimensional reduction

Define the reproducing kernel
\[
K_v(x,y)=\sum_aY_{v,a}(x)\overline{Y_{v,a}(y)}.
\]
Rotational invariance makes it a polynomial of \(t=x\cdot y\). A zonal degree-\(v\) harmonic satisfies
\[
(1-t^2)u''-4tu'+v(v+3)u=0.
\]
Its polynomial solution is a multiple of the Gegenbauer polynomial \(C_v^{3/2}(t)\). Since \(K_v(x,x)\) is constant and its integral is \(d_v\),
\[
K_v(x,y)=\frac{d_v}{V}P_v(x\cdot y),
\quad P_v(t)=\frac{C_v^{3/2}(t)}{k_v},
\quad k_v=C_v^{3/2}(1)=\frac{(v+1)(v+2)}2.
\tag{4}
\]
This also proves the needed addition theorem normalization without importing an area convention.

For fixed \(y\), the first-coordinate distribution of a uniform point on \(S^4\) has density \(\tfrac34(1-t^2)\) on \([-1,1]\). The exponent follows from the three-dimensional latitude sphere; the factor follows from \(\int_{-1}^1(1-t^2)dt=4/3\). Thus
\[
\frac1V\int_{S^4}f(x\cdot y)d\mu(x)=\frac34\int_{-1}^1f(t)(1-t^2)dt.
\tag{5}
\]
Expanding the finite sum of \(|T|^2\) and using the three kernels gives a double integral of \(K_{v_1}K_{v_2}K_{v_3}\). There are no convergence or exchange-of-infinite-sum issues. Equations (3)–(5) give
\[
|R|^2=\frac{3d_{v_1}d_{v_2}}{4V}
\int_{-1}^1P_{v_1}(t)P_{v_2}(t)P_{v_3}(t)(1-t^2)dt.
\]
Since \(d_v/k_v=(2v+3)/3\), this is
\[
\boxed{|R|^2=\frac1{32\pi^2}
\frac{(2v_1+3)(2v_2+3)}{(v_3+1)(v_3+2)}I(v_1,v_2,v_3),}
\tag{6}
\]
where \(I=\int_{-1}^1C_{v_1}^{3/2}C_{v_2}^{3/2}C_{v_3}^{3/2}(1-t^2)dt\).

## 4. Evaluate the classical integral

The following is a **classical theorem**, not a conjecture or a new result here. Rogers's linearization formula (DLMF [18.18.22](https://dlmf.nist.gov/18.18.E22); Andrews–Askey–Roy, *Special Functions* (1999), Theorem 6.8.2) states, for \(\lambda>0\),
\[
C_m^\lambda C_n^\lambda=\sum_{\ell=0}^{\min(m,n)}A_{m,n,\ell}^{\lambda} C_{m+n-2\ell}^\lambda,
\]
\[
A_{m,n,\ell}^{\lambda}=
\frac{(m+n+\lambda-2\ell)(m+n-2\ell)!}
{(m+n+\lambda-\ell)\ell!(m-\ell)!(n-\ell)!}
\frac{(\lambda)_\ell(\lambda)_{m-\ell}(\lambda)_{n-\ell}(2\lambda)_{m+n-\ell}}
{(\lambda)_{m+n-\ell}(2\lambda)_{m+n-2\ell}}.
\tag{7}
\]
Here \((z)_q=z(z+1)\cdots(z+q-1)\), with \((z)_0=1\). The polynomial identity and all its coefficients are well-defined for \(\lambda=3/2\).

Gegenbauer orthogonality and its squared norm, specialized to this parameter, are
\[
\int_{-1}^1C_p^{3/2}(t)C_q^{3/2}(t)(1-t^2)dt
=\delta_{pq}\frac{2(p+1)(p+2)}{2p+3}.
\tag{8}
\]
For completeness, the norm and orthogonality follow without gamma conventions from \(C_n^{3/2}=P'_{n+1}\), the Legendre differential equation, integration by parts with vanishing \((1-t^2)\) boundary term, and \(\int_{-1}^1P_kP_l=2\delta_{kl}/(2k+1)\). Endpoint normalization in (4) follows either from the Gegenbauer generating function at \(t=1\), or \(P'_{v+1}(1)=(v+1)(v+2)/2\).

Set \(a=j_1,b=j_2,c=j_3\). Then
\[
v_1=b+c,\quad v_2=a+c,\quad v_3=a+b,\quad s=a+b+c.
\]
In (7), set \(m=b+c,n=a+c,\ell=c,\lambda=3/2\); the output degree is \(p=a+b\). All other terms vanish on integrating against \(C_p^{3/2}(1-t^2)\). Multiplying its coefficient by (8) and cancelling the factor involving \(p\) gives
\[
I=\frac{2}{(s+3/2)a!b!c!}
\frac{(3/2)_a(3/2)_b(3/2)_c(3)_s}{(3/2)_s}.
\tag{9}
\]
For example, the cancelled product is exactly
\[(p+3/2)\,p!\,\frac{2}{(p+2)!}\,
\frac{2(p+1)(p+2)}{2p+3}=2.\]
Using
\[
(3/2)_q=\frac{(2q+1)!}{4^q q!},\qquad (3)_s=\frac{(s+2)!}{2},
\]
with the powers of 4 cancelling because \(a+b+c=s\), (9) becomes
\[
\boxed{I=\frac{4(s+1)!(s+2)!}{(2s+3)!}
\prod_{i=1}^3\frac{(2j_i+1)!}{(j_i!)^2}.}
\tag{10}
\]
This integral is also the \(l'=0,n=5\) case of Ališauskas's published general triple-Gegenbauer integral: arXiv:math-ph/0509035v1, **PDF Eq. (13b)** (the experimental HTML labels the corresponding formula (23b)). That paper explicitly attributes the \(l'=0\) case to Vilenkin. It is prior art, not an original identity of this project.

## 5. Finish the proof, including every boundary

Substitution of (10) in (6) gives
\[
|R|^2=\frac1{8\pi^2}
\frac{(2v_1+3)(2v_2+3)}{(v_3+1)(v_3+2)}
\frac{(s+1)!(s+2)!}{(2s+3)!}
\prod_i\frac{(2j_i+1)!}{(j_i!)^2}.
\tag{11}
\]
Since \((s+2)!=(s+2)(s+1)!\) and \(2s+4=2(s+2)\), (11) is exactly the square of (2). Every factor is strictly positive for an admissible triple. Taking the **positive** square root, as required by CRW's phase convention, proves (2).

If the sum of the three degrees is odd, the integrand defining \(I\) is odd and the integral vanishes. If the sum is even but a triangle inequality fails, \(v_3\) is not among the degrees \(v_1+v_2-2\ell\), \(0\le\ell\le\min(v_1,v_2)\), in (7), so (8) makes the integral zero. Equation (3) then makes every corresponding multiplication matrix element zero. (When no coupled irrep exists, the reduced-element notation is extended by zero rather than positing a CG coefficient.)

The proof permits \(a,b,c=0\), including triangle saturation and the all-zero triple; \(s+3/2>0\) always. It does not use a large-\(v\) asymptotic approximation, finite verification cutoff, or missing-label convention. **This completes the universal proof.**

## 6. Independent controls and their limits

The scientific replay is

```sh
cd /Users/jinleic/jinleic-workspace/ai4s/phys-so5-reduced-matrix-conjecture
/Users/jinleic/jinleic-workspace/scratch/ai4s-venv/bin/python code/verify.py
```

It uses three separate representations:

1. `code/crw_formula.py`: the factorial expression (2) as the rational number \(\pi^2R^2\).
2. `code/verify.py`: exact Legendre recurrence followed by differentiation and direct monomial integration against \(1-t^2\); **no Rogers formula** is used in this finite oracle. It separately simplifies the unrestricted symbolic ratios of (7)–(10) and (10)–(2) for nonnegative symbolic \(a,b,c\).
3. `code/cartesian_oracle.py`: exact real harmonic polynomials in five Cartesian coordinates, obtained by harmonic projection and rational Gram–Schmidt. It uses neither Gegenbauer polynomials nor the addition theorem nor CRW's formula. Uniform-sphere monomial moments are
\[
\mathbb E\prod_i x_i^{2k_i}=
\frac{\prod_i(2k_i-1)!!}{5\cdot7\cdots(5+2\sum_i k_i-2)},
\]
with odd moments zero; these follow by factoring a standard five-dimensional Gaussian into independent radius and uniform direction. For unnormalized orthogonal polynomials \(h_a\) of squared norm \(q_a\), it sums \(\mathbb E(h_ah_bh_c)^2/(q_aq_bq_c)\), then multiplies by \(3/(16d_{v_3})\) to obtain \(\pi^2R^2\). The bases have degrees at most 3; this is an intentionally independent **finite** control, not a second universal proof.

Negative controls deliberately use the wrong sphere-volume convention, omit the output-dimension division, replace Gegenbauer by Legendre polynomials, or insert nonzero forbidden values. They must disagree with the independent exact oracles. They check sensitivity to specified mistakes; they are not an exhaustive mutation campaign.

The following boundaries also follow directly from the proof:
\[
\pi^2R(v;0,v)^2=3/16,\quad
\pi^2R(0;v,v)^2=3d_v/16,
\]
\[
\pi^2R(v+1;1,v)^2=\frac{15(v+1)}{16(2v+5)},\qquad
\pi^2R(v-1;1,v)^2=\frac{15(v+2)}{16(2v+1)}\quad(v\ge1).
\]
The last two match the known quadrupole formula after \(Y_1=\sqrt{15}Q/(4\pi)\). In particular \(\pi^2R(2;2,2)^2=7/8\). The quantity \(d_{v_3}R^2\) is symmetric in all three seniorities, as the triple trace requires.

## 7. Claim scope and novelty boundary

- **Certification:** Theorem 1 proves the entire all-seniority formula CRW called conjectural; the proof is §§1–5. It handles the normalization and positive phase explicitly.
- **Reproduction:** the finite exact scripts reproduce the formula in two independent small-instance representations and classical scalar/quadrupole boundaries. Their limits are reported in the machine-readable run receipt, not extrapolated to a universal theorem.
- **No method-novelty claim:** the Gegenbauer integral was classical before 2009; Ališauskas gives a general version and cites earlier work. The normalization bridge to the particular empirical CRW expression is the deliverable.
- **No worldwide priority claim:** the current bounded citation screen found no explicit proof of CRW (29), but some texts were inaccessible or title-only. A publication could contain the proof or an equivalent convention. See `STATUS.md` for exact screen depth.
- **Not the full book problem:** this closes a concrete SO(5) multiplication reduced-element conjecture related to the spin-2/CFP representation-theory machinery. It does not give every SO(5)→SO(3) isoscalar factor, solve the missing-label problem, or furnish all general-spin many-particle CFPs.

## 8. Observed scientific replay

The command in §6 was executed successfully with Python 3.13.9 and SymPy 1.14.0. Its exact output was:

```text
PASS: symbolic ratios 1,1; exact univariate triples 2197 {'admissible': 616, 'forbidden': 1581}
PASS: Cartesian dimensions [1, 5, 14, 30] ; ordered triples 64 ; overlaps 58840
PASS: negative controls 5 ; pi^2 R(2;2,2)^2 = 7/8
```

The receipt is `results/exact-checks.json`; it includes the source-code hashes, all 64 Cartesian values, and every control outcome. `results/source-sha256.json` pins the preserved sources. The univariate range is **every ordered triple with each seniority 0 through 12**, including all 1,581 forbidden triples in that cube. The Cartesian range is **every ordered triple with each degree 0 through 3**, with 58,840 triple overlaps computed before symmetry reuse. These are exact-arithmetic Reproduction controls. The unlimited quantifiers are justified by the written proof, not by these counts.

## 9. Independent review

Review prompts, fixed-snapshot hashes, and raw responses are retained under `review/`. Review disposition is completed after the read-only referees return; no acceptance is inferred from merely launching a review.
