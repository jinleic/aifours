# Two negative Bell phases: an explicit rational PPT-negative target and a uniform two-positivity obstruction

Actual `/bin/date` observation before writing: **Sun Oct 25 06:25:04 PDT 2026**. Owner PhysicsPPT44-2. **AUTHOR-WRITTEN CANDIDATE; separate reconstruction and parent disposition pending.** Written mathematics and source reading only. No scientific eval/interpreter/arithmetic program/enumeration/certificate replay/solver, no CLI/subagents, no new GO.

## 1. Frozen source validity and exact scope

The source/scope freeze is `rank2-phase-pair-source-freeze-v1.json`, SHA-256 `a0b512c92cef751c288c6b2256ae13faccbab9b0f3a8d16cee094859c3a132ee`. It preceded this consolidated manuscript, and explicitly disclosed the informal written lead already considered during scoping; it is not represented as preregistration before all reasoning.

The source boundary is precise:

- Hou–Li–Poon–Qi–Sze, [primary2015 PDF](https://faculty.sites.iastate.edu/ytpoon/files/inline-files/pmaps_LAA_2015.pdf), Propositions2.2–2.3: Choi/Schmidt-rank k-positivity and elementary operators with arbitrary numbers of positive and negative terms. This permits a genuinely higher-rank negative part as an exact formulation. It does **not** supply an existing indecomposable two-positive M4 example.
- Chruściński–Kossakowski–Sarbicki, [arXiv:0908.1846v2](https://arxiv.org/html/0908.1846v2),19August2009, SectionII/Theorem1: its sufficient spectral criterion requires the sum of squared k-Schmidt norms of the negative rays to be **strictly less than1**. Two normalized maximally entangled ququart rays contribute1/2 each at k=2, so this condition FAILS at equality. Dividing by that criterion's zero denominator or reading it as a necessary-and-sufficient test would be invalid. Its SectionIV also proves decomposability of its stated spectral-certified class; that is not a theorem about every witness with a spectral decomposition.

We therefore derive an exact simultaneous complex two-functional criterion below rather than borrowing an inapplicable spectral certificate.

**Outcome.** The literal family below has a genuine rank-two negative spectral part and an explicit different rational PPT target with a strictly negative candidate expectation. Nevertheless, every two-block-positive member of the ENTIRE specified cyclic three-parameter family is decomposable. The obstruction is proved by a concrete rank-two test and an explicit PSD-plus-partial-transpose identity. Thus the example is not an SN3 certificate, and the whole stated family is closed as that route if the proof is reconstructed.

The family is not all rank-two-negative witnesses or all two-positive M4 maps. Unrestricted P44 is not answered.

## 2. Literal higher-rank negative part and positive coefficient family

Use indices modulo4, computational kets ij and unnormalized projectors P(v)=v v*. Let zeta=i and set

```
Omega0=sum_(j=0)^3 |jj>,
Omega1=sum_(j=0)^3 zeta^j |jj>,
B=P(Omega0)+P(Omega1).
```

The two kets are orthogonal and each has squared norm4. Thus B=4Pi where Pi is a rank-two orthogonal projection on the coherent subspace span{00,11,22,33}. In that subspace its matrix is

```
B_ij=1+i^(i-j),
B=[ 2    1-i   0     1+i ]
  [ 1+i  2     1-i   0   ]
  [ 0    1+i   2     1-i ]
  [ 1-i  0     1+i   2   ].                              (1)
```

Let N be the eight ordered neighboring pairs with i-j=+1 or-1 modulo4, and O the four ordered opposite pairs with i-j=2. Define

```
D(a,b,c)=a sum_i P(ii)+b sum_((i,j) in N)P(ij)
                         +c sum_((i,j) in O)P(ij),
W(a,b,c)=D(a,b,c)-B, a,b,c>=0.                            (2)
```

The coherent eigenvalues are a-4 twice and a twice; the other eigenvalues are b eight times and c four times. In particular, for0<a<4 and b,c>=0 the negative spectral part has **rank two**. This cannot be another literal single-Bell D-type coefficient choice: a PSD operator minus one rank-one projector has at most one negative eigenvalue. Invertible local congruences preserve that inertia distinction. No assertion is made that rank-two negative part alone ensures two-positivity or indecomposable-positive-map headroom.

## 3. Exact universal complex rank-two criterion

Assume a,b,c>0 in this section only. Let alpha_ij be the product-basis coefficients of D(a,b,c). For every complex4 by2 isometry U define

```
u_j=U*e_j,
A_j=U*diag(alpha_0j,alpha_1j,alpha_2j,alpha_3j)U,
s_j=u_j* A_j^(-1)u_j,
S=sum_j s_j, T=sum_j i^j s_j.                            (3)
```

Each A_j is positive definite and every s_j is real nonnegative.

**Exact criterion:** W(a,b,c) is nonnegative on EVERY complex Schmidt-rank-at-most-two vector iff

```
S(U)+|T(U)|<=1 for EVERY complex4 by2isometry U.            (4)
```

This is a universal inequality, not a real subspace test or finite sample assertion. Here is its complete derivation.

Write any rank-at-most-two coefficient matrix C=UZ, with z_j the columns of Z. Put `V_j=[u_j, i^j u_j]`. The two negative overlaps are exactly the entries of

```
h=sum_j V_j* z_j
 = (Tr C, Tr(diag(1,i,-1,-i)* C))^T.
```

The positive energy is `E=sum_j z_j* A_j z_j`. The simultaneous inverse-Gram matrix is

```
G(U)=sum_j V_j* A_j^(-1)V_j
    =[ S T;conj(T) S ].                                 (5)
```

Weighted Cauchy–Schwarz gives `||h||^2<=lambda_max(G) E`. Conversely, if G has a unit eigenvector v with eigenvalue g>1, choosing `z_j=A_j^(-1)V_j v` makes E=g and h=gv, so the witness expectation is `g-g^2<0`. Every such C still has rank at most two. Therefore positivity for all Z at fixed U is exactly G<=I2. Its largest eigenvalue is S+|T|, proving (4). Changes of basis within the same complex plane conjugate consistently. Lower-rank C is included by extending its column space to a two-plane.

The zero-coefficient boundaries do not require an inverse in the no-go below; Sections5–7 use only literal finite rank-two tests and PSD pair blocks, and cover all a,b,c>=0.

## 4. A different fully explicit rational PPT target and negative candidate pair

Define

```
R*=B+2 sum_((i,j) in N)P(ij),
rho*=R*/24,
W*=W(7/2,1/8,1).                                        (6)
```

R* is positive by its displayed Gram/projector sum. The two coherent kets contribute trace8, and the eight product diagonals contribute16, so its trace is24. All entries of rho* are Gaussian rational with denominator dividing24, and both local supports are all4 dimensions. It is not x1111 or another local-filter parameter in that old family.

For Bob partial transpose, the coherent diagonals are2. Every unordered neighboring pair has the2 by2 block

```
[2 B_ij;conj(B_ij) 2],
```

whose determinant is4-|1+i|^2=2>0. Opposite-pair blocks are zero. These mutually orthogonal blocks prove PPT exactly, without an eigenvalue computation or numerical replay.

Since B^2=4B and Tr(B)=8, `Tr(B^2)=32`. The positive diagonal contribution to Tr(W*R*) is

```
8*(7/2)+16*(1/8)=28+2=30.
```

Hence

```
Tr(W* rho*)=(30-32)/24=-1/12.                            (7)
```

This is an actual rational PPT-negative candidate pair, but it is NOT a Schmidt-three certificate: its missing universal rank-two property fails explicitly below. A negative expectation without that property says nothing about SN>=3, and even ordinary witness block-positivity of this particular W* is not asserted.

## 5. A literal rank-two matrix rejects the candidate and constrains the whole family

Take

```
C0=[1 1 0 0]
   [1 1 0 0]
   [0 0 1 1]
   [0 0 1 1].                                          (8)
```

It has rank exactly two: each of the two supported2 by2 blocks has rank one. Its two negative overlaps are Tr(C0)=4 and `Tr(diag(1,i,-1,-i)* C0)=0`. Its positive energy is4a+4b. Thus

```
<vec(C0),W(a,b,c)vec(C0)>=4(a+b-4).                       (9)
```

For W*, this is `4*(29/8-4)=-3/2<0`. It directly refutes the required universal property, without relying on a source sufficient test or a scalar spectral bound.

Equivalently, in (4) take U with columns `(|0>+|1>)/sqrt2` and `(|2>+|3>)/sqrt2`. Each s_j is1/(a+b); hence S=4/(a+b),T=0. W* gives S=32/29>1. This is the same obstruction at the actual universal-criterion boundary, not a second unrelated diagnostic.

For ANY two-block-positive member, (9) forces

```
a+b>=4.                                                 (10)
```

The product ket ii independently forces

```
a>=2.                                                   (11)
```

These two necessary conditions are not claimed sufficient for two-positivity. They suffice to prove that no two-positive member detects any PPT state.

## 6. Exact PSD-plus-partial-transpose certificate for the entire cyclic family

First, if a>=4 then the coherent block `aI4-B` is PSD because B=4Pi. All remaining entries are nonnegative product diagonals, so W itself is PSD and cannot detect a positive state.

Now suppose2<=a<4 and define

```
kappa=(a-2)/2, 0<=kappa<1,
P0=2(a-2)(I4-Pi)>=0.                                   (12)
```

Embed P0 into the physical coherent subspace as P_coh. Its coherent diagonals are a-2, and its neighboring off-diagonals are `-kappa B_ij`. Its opposite off-diagonals vanish, since B_ij=0 there.

Let E={{0,1},{1,2},{2,3},{3,0}} be the four unordered neighboring edges. For each edge define

```
Q_ij=b[P(ij)+P(ji)]
     -(1-kappa)[B_ij|ij><ji|+conj(B_ij)|ji><ij|].          (13)
```

The two diagonal entries are b, and the off-diagonal modulus is

```
(1-kappa)|B_ij|=(4-a)/sqrt2.
```

Thus each Q_ij is PSD whenever

```
b>=(4-a)/sqrt2.                                         (14)
```

The complete operator identity is

```
W(a,b,c)=P_coh+c sum_((i,j) in O)P(ij)
                  +sum_({i,j} in E) Q_ij^Gamma.          (15)
```

Every entry group is accounted for:

- coherent diagonals: P_coh contributes a-2, exactly the diagonal of aI4-B;
- neighboring coherent pairs: coefficients `-kappa B_ij` and `-(1-kappa)B_ij` sum to -B_ij;
- opposite coherent pairs: all coefficients are zero;
- neighboring product diagonals: each coefficient b comes from its unique Q_ij;
- opposite product diagonals: coefficient c is supplied by the displayed PSD diagonal part;
- all other entries vanish.

If W is two-block-positive, (10) gives b>=4-a. Since4-a>0, this implies (14). Consequently the first two terms of (15) are PSD and the sum of Q_ij is PSD. Therefore W is decomposable and

```
Tr(W rho)>=0 for EVERY PPT rho.                          (16)
```

This includes a=2, b=0 or c=0 wherever (10)–(11) hold, and a=4 was already included in the PSD case. There is no exceptional boundary left to a numerical limit. The theorem is for the ENTIRE literal cyclic three-parameter two-Bell family, not just W* or small denominators.

## 7. The PPT detection boundary can itself be characterized exactly

For completeness, for this family with a,b,c>=0 the condition of being nonnegative on every PPT state is exactly

```
a>=2 AND a+sqrt2 b>=4.                                  (17)
```

Sufficiency: if a>=4, W is PSD. Otherwise (17) is precisely2<=a<4 and (14), so the explicit decomposition(15) applies.

Necessity: if a<2, ii is a PPT product negative direction. If a>=2 but a+sqrt2 b<4, use

```
R_opt=B+sqrt2 sum_((i,j) in N)P(ij).
```

Its coherent block is B>=0 and its partial-transpose neighboring blocks have diagonals sqrt2 and off-diagonal modulus sqrt2, hence are PSD. Its expectation is `8(a+sqrt2 b-4)<0`. This is a literal algebraic PPT test state, not an optimizer claim. If a,b are rational, any strict inequality allows a rational t>sqrt2 sufficiently close to sqrt2 such that a+t b<4. Replacing sqrt2 by t preserves PPT and gives a rational negative target; b=0 is immediate. Formula(6) is the concrete rational example t=2.

The contrast is sharp at the level needed for obstruction: the actual universal-rank-two test requires a+b>=4, while the PPT-negative region requires a+sqrt2 b<4 (or a<2). The former cannot enter the latter for b>=0. We do not need to solve every isometry inequality in (4) or characterize the full two-positive parameter set.

## 8. What this settles and the exact remaining P44 gap

The higher-rank source validity, entire complex rank-two criterion, exact rational PPT-negative target, explicit failed candidate, and whole-family obstruction are all delivered in one packet. No source was inflated into a promise of nondecomposable two-positive headroom. In particular the inapplicable spectral denominator-zero condition was not used as a certificate.

This is a genuinely different negative spectral part from single-Bell D-type, but the extra cyclic positive-part symmetry is still too restrictive. No conclusion is drawn about arbitrary rank-two negative parts, arbitrary positive completions of these two rays, higher numbers/nonmaximally-entangled rays, or unrestricted two-positive M4 maps. The three-parameter family alone is closed if independently reconstructed.

The accepted x1111 and single-Bell D-type results remain exactly at their parent v8-qualified dispositions; neither is rerun or repackaged here. Native N4 remains UNKNOWN/incomplete with actual historical exit unestablished, and no retry follows.

Unrestricted P44 still requires a different exact rational PPT/SN3 certificate or an all-state theorem. Any next positive use of these two rays must escape the cyclic D(a,b,c) positive part, or choose a genuinely different negative subspace with a sound full-complex certificate. Another a,b,c increment or an unsupported claim of two-positivity from spectral data would not be progress.

Correctness: complete author-WRITTEN candidate, separate reconstruction pending. Formal/kernel, scientific execution/replay, cross-vendor/human review, novelty and full-target acceptance are not claimed. No new GO is requested; the HOLD remains binding.
