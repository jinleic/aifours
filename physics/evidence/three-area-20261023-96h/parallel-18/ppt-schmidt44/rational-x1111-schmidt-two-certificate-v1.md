# The frozen x1111 PPT input has an explicit Schmidt-two countercertificate

Observed clock before writing: **Sun Oct 25 04:13:24 PDT 2026** (`/bin/date`). Owner PhysicsPPT44 / physics-3. **WRITTEN CANDIDATE; independent reconstruction and parent disposition absent.** This is a new successor packet, not an edit to any pinned proposal or execution receipt.

## 1. Actual result, unchanged target, and the arithmetic correction

The frozen N4 input is the rational 4 by 4 PPT density matrix `rho=R/49` at `x=(1,1,1,1)`. It was outside the old small-mixing Schmidt-two region; that did not establish Schmidt number three. The new result is an explicit finite **Schmidt-number-at-most-two decomposition of this very input**, using eight algebraic vectors, two core vectors and 21 Gaussian-rational conjugate pairs. A simple range argument supplies the matching entanglement lower bound, hence the candidate theorem is **SN(rho)=2**.

This eliminates the actual proposed input rather than restating a prior restriction or reporting another timeout. It does **not** solve P44. No new SN3 state, all-state Schmidt-two theorem, symmetric-extension obstruction, or novel indecomposable two-positive map is produced.

The separate exact-data packet is [rational-x1111-schmidt-two-certificate-v1.json](rational-x1111-schmidt-two-certificate-v1.json), SHA-256 `b2d8e13a63fa4be2a2c6deead8b2b04921dd1d92f7f75e5b9d6ea50794ebe761`. Its 21 rows are the actual returned coefficients, not placeholders or fitted floating-point approximations.

**Mandatory process qualification.** Before the parent correction, this resumption used the explicit but erroneous exception in checkpoint026 and the supplied assignment: 21 eval cells, of which the first failed immediately importing unavailable sympy and the other 20 performed exact Fraction/integer/Gaussian-rational work. No install or native scientific process was launched. There was no separate source/input-pinned GO. The parent then withdrew that exception, explicitly attributing it to the parent rather than the owners. Scientific eval stopped immediately; no further scientific arithmetic, replay or solver was run. The exact returned data are preserved, but this packet does not retroactively admit those computations or claim accepted verification credit. See [the immediate correction ACK](arithmetic-hold-correction-ack-v1.json).

The theorem below is WRITTEN, with explicitly identified pre-correction arithmetic observations. It is not proof-assistant/kernel verification, a separate reconstruction, cross-vendor/human review, a repaired N4 child-exit attestation, or novelty acceptance.

## 2. An explicit rational density matrix and its positive partial transpose

Use computational kets `ij=|i>_A tensor |j>_B` and unnormalized projectors `P(v)=v v*`. Define

```
a = 00+11+22,        b = 01+12,           c = 10-21,
d = 02+30+31+32+33, e = 20+33,
f = 30,             g = 32,              h = 00+01+02+03,
j = 23.
```

The matrix is completely specified by the integer Gram formula

```
R = P(a)+P(b)+P(c)+3[P(d)+P(e)+P(f)+P(g)+P(h)+P(j)],
rho = R/49.
```

Thus every entry of rho is a rational with denominator dividing49. This is exactly the proposal's `B_x=[I4|x]`, x1111 input, not another state substituted for it. Positivity is immediate. The trace count is `3+2+2+3(5+2+1+1+4+1)=49`.

For direct PPT certification, write `l=30+31+32+33`. Entrywise partial transpose on Bob gives

```
R^Gamma = P(02+11-20)+2P(02+20)
          +P(01+10)+P(12+21)+P(00)+P(22)
          +3P(32+h)+3P(30+23)+3P(l)+3P(33).
```

Every coefficient is positive, so this is an exact integer Gram certificate of PPT; it does not import a solver status or the original source's PPT assertion. The two non-core coherences move as follows: `02/3r` becomes `0r/32`, giving the `32+h` projector, and `20/33` becomes `23/30`, giving `30+23`. Their remaining diagonal contributions are precisely `3P(l)+3P(33)`.

**Actual pre-correction observation:** an entrywise Fraction comparison found this displayed Gram operator equal to the explicitly transposed16 by16 R. The observed trace was49, rank(R)=9 and rank(R^Gamma)=10. An independent rational elimination of the same partial transpose within that cell returned the nonnegative pivots retained in the JSON. The checker anchor `Gamma(Gamma(P(a)))=P(a)` passed. These are historical arithmetic observations under the withdrawn exception, not newly admitted replays.

## 3. Eight exact rank-two vectors absorb the Schmidt-three core direction

Let

```
delta = +2i/3 or -2i/3.
```

For the positive sign set `gamma=sqrt(30)(1-i)/12`; for the negative sign take its complex conjugate. Independently choose `beta=+gamma or -gamma` and `chi=+gamma or -gamma`. This gives eight triples. They satisfy

```
|beta|^2=|chi|^2=5/12,
beta^2+chi^2=delta+delta^(-1),
|delta|^2=4/9.
```

For each triple define

```
psi = a+beta b+chi c+delta d-delta e
      +delta(chi-1)f+delta(beta-1)g.                   (1)
```

Its coefficient matrix is

```
[ 1          beta       delta        0 ]
[ chi        1          beta         0 ]
[ -delta     -chi       1            0 ]
[ delta chi  delta      delta beta   0 ].
```

Row3 is delta times row1. The determinant of the first three rows/columns is

```
1-delta(beta^2+chi^2)+delta^2=0.
```

Consequently the full matrix has rank at most two. In fact its upper-left2 by2 minor is `1-beta chi`, nonzero because `|beta chi|=5/12`; the rank is exactly two. This proof covers the actual complex vectors, not a real-only rank test.

Put `v=d-e-f-g`, and average (1) uniformly over the eight choices. The sign means of beta and chi vanish independently. Their covariance vanishes, and averaging delta over its two signs removes the remaining beta/g and chi/f cross terms. The complete identity is

```
A := (1/8) sum_eight P(psi)
   = P(a)+(5/12)[P(b)+P(c)]
     +(4/9)P(v)+(5/27)[P(f)+P(g)].                   (2)
```

For example, the f coefficient is delta(chi-1). Its variance is `(4/9)(1+5/12)`, its covariance with delta is `-4/9`, and its covariance with the g coefficient is `4/9`. These are exactly the f diagonal and d/f, f/g entries on the right of (2). Beta and chi have zero covariance with those groups after both sign averages. This accounts for every possible nonzero entry of (2).

Identity (2) and the rank proof are **WRITTEN**; they were not replayed in an algebraic-number interpreter. They require only the displayed square identities and independent two-point sign averaging.

## 4. A six-vector residual has a useful two-product representation

Let F have columns `(d,e,f,g,h,j)`. Denote its coefficient vector by

```
y=(p,q,t,u,r,s).
```

This coordinate order is important. The vector `Fy` is

```
r|0,x> + p|0,2> + p|3,x> + u|3,2>
 +t|3,0> + q|2,0> + q|3,3> + s|2,3>,              (3)
```

where `x=|0>+|1>+|2>+|3>` here. The same identity holds for the general chart's x.

Suppose the two symmetric arrays have rank at most one:

```
[ r p ] = eta [ alpha^2       alpha beta0 ],
[ p u ]       [ alpha beta0  beta0^2     ],

[ t q ] = zeta [ gamma0^2      gamma0 delta0 ],
[ q s ]        [ gamma0 delta0 delta0^2      ].
```

Then (3) is exactly

```
eta (alpha|0>+beta0|3>) tensor (alpha x+beta0|2>)
 +zeta (gamma0|3>+delta0|2>) tensor (gamma0|0>+delta0|3>).
                                                               (4)
```

It is therefore a sum of at most two product vectors. No division, nonzero-coordinate hypothesis, limiting argument or numerical rank inference is used. The zero-array cases are included.

Each of the21 Gaussian-rational y vectors in the JSON is constructed from arrays of precisely this form: `(r,p,u)=(1,z,z^2)` or an axis, and `(t,q,s)=phase*(1,w,w^2)` or an axis, with one array also allowed to vanish. The phases are among `1,-1,i,-i`. Their conjugates have the same property. Equivalently their two literal identities are `r u=p^2` and `t s=q^2`. This gives a written rank-two certificate for every physical residual vector.

This representation is the substantive replacement for the stalled scientific extension assay. It identifies an exactly parameterized cone of rank-two vectors inside the six-generator residual; it does not assert that every positive operator on that residual is Schmidt-two.

## 5. Explicit finite positive residual identity

Subtracting (2) from R gives

```
R = A+(7/12)[P(b)+P(c)]+F M F*,                     (5)
```

where, in the coordinate order of Section4,

```
M = 3I6-(4/9) z z^T-(5/27)(E_tt+E_uu),
z = (1,-1,-1,-1,0,0)^T.
```

All36 rational entries are displayed in the JSON. Its observed trace is428/27.

The JSON gives21 vectors y_l and strictly positive rational coefficients t_l with the exact identity

```
M = sum_l t_l Re(y_l y_l*)
  = sum_l (t_l/2)[P(y_l)+P(conj(y_l))].              (6)
```

Here `Re` is entrywise real part. The weight field is literally `coefficient_Re_yy_star`; it is **not** the already-halved pure-projector weight. This distinction avoids a factor-two ambiguity. For example its first coefficient is4/141 and its first vector is `(-3/4,0,0,9/16,1,0)`.

**Actual pre-correction observation:** Fraction/Gaussian-rational conic elimination produced the21 positive pairs; a separate direct matrix sum in the same kernel compared the right side of (6) entrywise with the specified M and returned equality. The positivity of every retained rational coefficient was also checked. The final residual used1386 distinct conjugate-averaged generators and reached exact phase-one objective0 in68 pivots. Earlier finite frames and other residual guesses failed; those failures imply no physical nonexistence claim and are not a symmetric-extension obstruction.

Combining (1), (4), (5) and (6) yields the explicit finite decomposition

```
R = (1/8) sum_eight P(psi)
    +(7/12)[P(b)+P(c)]
    +sum_l (t_l/2)[P(F y_l)+P(F conj(y_l))].          (7)
```

Every coefficient is positive and every displayed vector has Schmidt rank at most two. There are at most52 pure terms before merging identical conjugate terms. Divide (7) by49 and normalize its nonzero vectors, assigning each its coefficient times squared norm/49. The weights sum to one because (7) is an operator identity. This proves the candidate upper bound SN(rho)<=2.

No full16 by16 replay of the algebraic eight-vector assembly was performed. No JSON reparse, scientific replay or coefficient validation was run after the parent's hold correction. The written assembly rests on (2), (4), the actually observed exact rational (6), and the transcribed table. Independent reconstruction of those precise bytes is a remaining acceptance gate, not a task silently performed by the author.

## 6. Matching entanglement lower bound

Project Alice locally onto levels0,1,2. Its nonzero output T has range coefficient matrices

```
[ A+H  B+H  D+H  H ]
[ C    A    B    0 ]
[ E   -C    A    J ].
```

If such a matrix has rank one and its Bob3 column is nonzero, that column forces the Alice1 component to vanish, hence its entire middle row is zero and in particular A=0.

If its Bob3 column vanishes, then H=J=0. The two core2 by2 minors on rows0,1/columns0,1 and rows1,2/columns1,2 are `A^2-BC` and `A^2+BC`. Rank one makes both zero, again forcing A=0 over the complex numbers.

Thus **every product vector in Ran(T) has computational coefficient11 equal to zero**. A positive separable state's pure product summands belong to its range, so such a state would have its11 diagonal entry zero. But the actual T has `T_(11,11)=1`, from P(a). Contradiction. T is entangled, and local projection cannot create entanglement from a separable rho. Therefore SN(rho)>=2. Together with (7), the written candidate has SN(rho)=2.

This is a written range argument, not an additional arithmetic execution. Notice that the relevant vanishing linear functional is the11 coefficient; it is not an unjustified assertion that every such product vector is orthogonal to a after h was added.

## 7. A separate uniform obstruction to a qualitative nullspace-only attack

For the general filter chart retain

```
d_x=02+|3> tensor x, h_x=|0> tensor x,
e=20+33, f=30, g=32, j=23,
R_x=P(a)+P(b)+P(c)+3[P(d_x)+P(e)+P(f)+P(g)+P(h_x)+P(j)].
```

The source generators other than a already have Schmidt rank at most two. The missing a direction can also be spanned by a rank-two vector for **every complex x**, not just x1111:

- If x3 is nonzero, choose any complex tau with `tau^2 x3=-1`. The vector

  `a+tau d_x-tau x3 e-tau x0 f-tau x2 g`

  has rows `(1,0,tau,0)`, `(0,1,0,0)`, `-tau x3` times the first row, and `tau x1` times the second row.

- If x3=0, use

  `a+c+d_x+(x1-x0)f-x2 g`.

  Its rows are `(1,0,1,0)`, `(1,1,0,0)`, the first row minus the second, and x1 times the second.

Both are rank at most two and have a coefficient1. Along with the other eight generators they span the whole range of R_x. Consequently a qualitative test requiring that **all** rank-two vectors in the range miss the a direction cannot work anywhere in this chart. In particular, a kernel-penalty witness whose restriction to this range is only a negative multiple of the squared a-coordinate is not two-block-positive: the displayed vector has zero kernel penalty and strictly negative expectation.

This is a no-go for that **qualitative support/nullspace certificate**, not for arbitrary witnesses, normalized symmetric extensions, all filters, or unrestricted P44. A Schmidt-three state can have a range spanned by rank-two vectors. The uniform statement is not used as a substitute for the quantitative decomposition (7).

## 8. Provenance, actual scope and precise remaining gap

The state is the existing Krebs–Gachechiladze4 by5 construction [2509.07086v1](https://arxiv.org/html/2509.07086v1), Theorem5/Fig.1, compressed by B_x at x1111. The frozen proposal is [proposal-normalized-Bose-N4-v1.md](proposal-normalized-Bose-N4-v1.md), SHA-256 `de428a73ccca38fdd9066c9a64f319f8da8c2d60c238ed56df2ae5886ad15f6d`. Its separately returned [normalized-cone review](../../../../../mathematics/evidence/three-area-20261023-96h/parallel-18/shor-completion/peer-review-PPT-normalized-N4-soundness-v1.md) established the stated soundness interface, not this input's Schmidt number. The old N4 run remains UNKNOWN/incomplete with unestablished historical child exit; this packet neither recovers a result from it nor authorizes another run.

The earlier all-complex auxiliary merge theorem and its received review remain unchanged. Their restricted proof is not imported as an unrestricted theorem here. The new input-specific countercertificate was not reviewed by that historical reviewer.

**No rerun of the x1111 extension search is scientifically justified as an SN3 attack if (7) is independently reconstructed.** Every universally two-block-positive witness is nonnegative on all terms of (7), so it cannot be negative on this rho. The hold alone is not the reason: there is now an explicit candidate mathematical obstruction for the actual input.

The named acceptance criterion is still **UNMET**. What is missing is either:

1. a **different** explicit rational4 by4 PPT density matrix with a Hermitian separator nonnegative on **every complex** Schmidt-rank-at-most-two vector and strictly negative on that matrix, including a sound exact certificate of the required extension obstruction; or
2. a proof that **every**4 by4 PPT state has Schmidt number at most two.

Neither the six-generator representation, the generic-chart range lemma, the input-specific decomposition, nor any failed finite conic attempt supplies either missing statement. Formal verification, independent written reconstruction and novelty clearance are not performed. All further scientific computation, including eval replay of this table, remains blocked without a separate exact source/input-pinned named GO under HOLD v2.
