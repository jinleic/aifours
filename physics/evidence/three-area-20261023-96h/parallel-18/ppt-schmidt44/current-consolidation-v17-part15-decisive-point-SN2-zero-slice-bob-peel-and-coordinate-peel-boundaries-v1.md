# CURRENT P44 CONSOLIDATION v17 — PART15/15: the decisive point x0=(1,1,-1,0) has Schmidt number exactly two; a u-free Bob-peel theorem on the z=0 slice; forced-family failure of every coordinate peel on the far balanced ray

PhysicsPPT44-2. Actual pre-write `/bin/date`: **Sun Oct 25 23:29:50 PDT 2026**. Exact WRITTEN mathematics. Every number below is computed by hand and displayed for line-by-line reconstruction. No scientific interpreter/calculator/eval/program/CAS, enumeration, solver, replay, build/test, CLI, nested agent or GO was used. Same original cutoff (2026-10-27T11:05:38-07:00) and deadline (12:35:38).

## Q0. Scope, union rule, imports

New claims C34.1–C34.4 continue the ORIGINAL compression chart R_x of Part10 H1.1. The complete current union is:
- all fourteen parts bound in `checkpoint-090-complete-current-v16-fourteen-part-manifest-v1.json` (SHA256 1c6b74d62a96055c880c2d94145ce0add3708e12c2efcc345b59f3f87d1a8b9e);
- THIS part;
- every mandatory overlay named there.

Parts 9–15 are LATER UNREVIEWED; nothing is inherited.

Named classical imports:
- **(I1) Horodecki.** A PSD operator on C^2⊗C^2 or C^2⊗C^3 with PSD partial transpose is separable. Separable implies PPT in every dimension.
- **(I2) Sylvester and zero-row rules.** A Hermitian matrix is positive definite iff all leading principal minors are positive. A PSD matrix with a zero diagonal entry has that whole row and column zero. A PSD matrix has all principal minors >= 0.
- **(I3) Cauchy–Schwarz.**

The peel lemma is proved below (Q2). It agrees with 2509.07086 Theorem 2, but that source's proof is not used.

**Status.** C34.1 resolves Part14's decisive point: SN(R_x0)=2. It does NOT solve P44, does NOT give an SN3 state and does NOT settle the far balanced ray.

## Q1. Chart and notation

Write |ij>=|i>_A⊗|j>_B on C^4⊗C^4 and P(y)=yy* (unnormalized). For x=(u,v,w,z):
- a=|00>+|11>+|22>, b=|01>+|12>, c=|10>-|21>;
- d_x=|02>+|3>⊗x, e=|20>+|33>;
- f=|30>, g=|32>, j=|23>, h_x=|0>⊗x.

The chart state is `R_x=P(a)+P(b)+P(c)+3[P(d_x)+P(e)+P(f)+P(g)+P(j)+P(h_x)]`.

A peel is a compression (1⊗B)R(1⊗B) or (A⊗1)R(A⊗1), where A or B is 1-|φ><φ|. A coordinate peel has φ a basis vector.

## Q2. Lemma L (peel lift)

**Lemma L.** Let ρ>=0 on H_A⊗H_B and φ in H_B a unit vector, with B=1-|φ><φ|. If Z=(1⊗B)ρ(1⊗B) has Schmidt number <=m, then SN(ρ)<=m+1. The same holds with the roles of A and B exchanged.

*Proof.* Order H_A⊗H_B as (H_A⊗φ) ⊕ (H_A⊗φ⊥) and write ρ=[[X,Y],[Y*,Z]]. Let Z=WW*, where W=[z_1,...,z_N] has columns with SR(z_i)<=m. Since ρ>=0, range(Y*) is inside range(Z)=range(W). Put C=W^+Y*, so that Y*=WC.

The i-th column of C* has the form ξ_i⊗φ. Set v_i=z_i+ξ_i⊗φ. Then

`Σ v_i v_i* = [[C*C, C*W*],[WC, WW*]] = [[YZ^+Y*, Y],[Y*, Z]]`.

Hence ρ-Σv_iv_i* = (X-YZ^+Y*)⊕0, which is Q⊗|φ><φ| with Q>=0 by the Schur-complement condition. That term is separable, and SR(v_i)<=SR(z_i)+1<=m+1. ∎

**Use.** If some peel compression of R_x is separable, then SN(R_x)<=2.

## Q3. The Bob-0 compression on the slice z=0 is independent of u

Let B0=1-|0><0|_B and put p=|1>_B, q=|2>_B. For x=(u,v,w,0), compress each vector:
- a→|1>p+|2>q;
- b unchanged;
- c→-|2>p;
- d_x→|0>q+|3>⊗(vp+wq);
- e→|33>;
- f→0;
- g, j unchanged;
- h_x→|0>⊗(vp+wq).

Hence

```
S(x) := (1⊗B0)R_x(1⊗B0) = T(v,w) + 3P(|33>) + 3P(|23>),
T(v,w) = P(t1)+P(t2)+P(t3)+3P(t4)+3P(t5)+3P(t6),                         (Q3.1)
t1=|1>p+|2>q, t2=|0>p+|1>q, t3=|2>p, t4=|0>q+|3>(vp+wq), t5=|3>q, t6=|0>(vp+wq).
```

**u does not occur.** T lives on C^4⊗span{p,q}, and the two extra terms are products on Bob |3>. Therefore S(x) is separable iff T(v,w) is: compressing Bob onto span{p,q} gives one direction, and the other is immediate.

**Phase lemma.** Let U_A=diag(1,e^{iτ},e^{2iτ},e^{iθ}) and U_B=diag(e^{iτ},1) on (p,q). Their action on each vector is:
- t1 → e^{2iτ}t1;
- t2 → e^{iτ}t2;
- t3 → e^{3iτ}t3;
- t5 → e^{iθ}t5;
- t4(v,w) → t4(v',w');
- t6(v,w) → e^{-iθ}t6(v',w').

Here v'=e^{i(θ+τ)}v and w'=e^{iθ}w. So (U_A⊗U_B)T(v,w)(U_A⊗U_B)*=T(v',w'). Every (v,w) with |v|=V, |w|=W is therefore locally unitarily equivalent to (V,W), and also to (V,-W).

## Q4. C34.1 — Theorem E0: SN(R_x)=2 for every x=(u,1,-1,0), u in C; in particular for x0=(1,1,-1,0)

Here T=T(1,-1), with t4=|0>q+|3>p-|3>q and t6=|0>p-|0>q. For each sixth root of unity r (r^6=1) define the product vector

`π_r = [ (r - r^2/2)|0> + |1> + r^{-1}|2> + ((r^2-r^3)/2)|3> ] ⊗ (p + r q).`      (Q4.1)

Its components are:

| Alice ⊗ Bob | coefficient |
|---|---|
| \|0>p | r - r^2/2 |
| \|0>q | r^2 - r^3/2 |
| \|1>p | 1 |
| \|1>q | r |
| \|2>p | r^{-1} |
| \|2>q | 1 |
| \|3>p | (r^2-r^3)/2 |
| \|3>q | (r^3-r^4)/2 |

Group them by the power r^k, so that π_r = Σ_{k=-1}^{4} r^k V_k:
- V_{-1}=|2>p=t3;
- V_0=|1>p+|2>q=t1;
- V_1=|0>p+|1>q=t2;
- V_2=-(1/2)|0>p+|0>q+(1/2)|3>p =: y;
- V_3=-(1/2)(|0>q+|3>p-|3>q)=-t4/2;
- V_4=-(1/2)|3>q=-t5/2.

Since (1/6)Σ_{r^6=1} r^m=0 for 1<=|m|<=5,

`(1/6)Σ_r P(π_r) = P(t1)+P(t2)+P(t3)+P(y)+(1/4)P(t4)+(1/4)P(t5).`

Therefore

```
T(1,-1) = (1/6)Σ_{r^6=1} P(π_r) + Res,
Res := (11/4)P(t4) + (11/4)P(t5) + 3P(t6) - P(y).                           (Q4.2)
```

**Res>=0.** We have y=-(1/2)t6+(1/2)t4+(1/2)t5. Componentwise this is (-1/2, 1/2+1/2, 1/2, -1/2+1/2) = (-1/2,1,1/2,0) ✓. The vectors t6,t4,t5 are independent. So Res>=0 iff K=diag(3,11/4,11/4)-cc^T>=0 with c=(-1/2,1/2,1/2). This holds because |c|^2=3/4<=11/4.

**Explicit matrix.** In the ordered basis (|0>p,|0>q,|3>p,|3>q):

```
        [ 11 -10   1    0 ]
4Res =  [-10  19   9  -11 ]
        [  1   9  10  -11 ]
        [  0 -11 -11   22 ]
```

Entry derivation:
- (0p,0p): 3-1/4;
- (0p,0q): -3+1/2;
- (0p,3p): +1/4;
- (0q,0q): 11/4+3-1;
- (0q,3p): 11/4-1/2;
- (0q,3q): -11/4;
- (3p,3p): 11/4-1/4;
- (3p,3q): -11/4;
- (3q,3q): 11/4+11/4.

Check: 4Res·(1,1,-1,0)^T=0, the normal of span{t4,t5,t6}.

**PPT of Res.** View Res on the 2x2 system Alice{0,3}⊗Bob{p,q}. The partial transpose transposes the off-diagonal Alice block [[1,0],[9,-11]] to [[1,9],[0,-11]]:

```
          [ 11 -10   1    9 ]
4Res^Γ =  [-10  19   0  -11 ]
          [  1   0  10  -11 ]
          [  9 -11 -11   22 ]
```

Its leading principal minors are all positive:
- 11;
- 11·19-100 = 109;
- 11·(19·10) + 10·(-100) + 1·(-19) = 2090-1000-19 = 1071;
- **252.** Expand along row three, (1,0,10,-11). The deleted-row-three minors with columns {2,3,4}, {1,2,4} and {1,2,3} are M31=-968, M33=1508 and M34=-1260. The cofactors are C31=+M31=-968, C33=+M33=1508 and C34=-M34=+1260.

The three 3x3 minors, written out:
- [[-10,1,9],[19,0,-11],[-11,-11,22]] = 1210-297-1881 = -968;
- [[11,-10,9],[-10,19,-11],[9,-11,22]] = 3267-1210-549 = 1508;
- [[11,-10,1],[-10,19,0],[9,-11,-11]] = -2299+1100-61 = -1260.

The cofactor signs give det = 1·(-968) + 10·(+1508) + (-11)·(+1260) = 252.

So Res^Γ>0 by (I2), and Res is separable by (I1). Hence T(1,-1) is a finite sum of product projectors, S(x) is separable for EVERY x=(u,1,-1,0), and Lemma L gives SN(R_x)<=2. Q6 gives SN>=2. ∎

**Consequence for Part14 C33.3.** The decisive limit point x0 has SN exactly two. The branch "if R_x0 has Schmidt number 3, then the far balanced ray is SN3" is therefore vacuous. The far ray itself is NOT settled (Q8).

## Q5. C34.2 — Theorem E: the diagonal-modulus slice

**Theorem E.** Let x=(u,v,w,0) with u in C arbitrary, arbitrary phases, and |v|=|w|=t, T:=t^2 in [1/2,9/8]. Then SN(R_x)=2.

*Proof.* By Q3 it suffices to show T(t,t) is separable. Here t4=|0>q+t|3>p+t|3>q, t5=|3>q, t6=t|0>p+t|0>q. For r^6=1 put

`π_r = [ (r + r^2/2)|0> + |1> + r^{-1}|2> + (t/2)(r^2+r^3)|3> ] ⊗ (p + r q).`

This family is the Q4 family in the phase frame of Q3. Its components:
- |0>p: r+r^2/2;
- |0>q: r^2+r^3/2;
- |1>p: 1;
- |1>q: r;
- |2>p: r^{-1};
- |2>q: 1;
- |3>p: (t/2)(r^2+r^3);
- |3>q: (t/2)(r^3+r^4).

Charge groups:
- V_{-1}=t3, V_0=t1, V_1=t2;
- V_2 = y2 := (1/2)|0>p+|0>q+(t/2)|3>p;
- V_3 = (1/2)|0>q+(t/2)|3>p+(t/2)|3>q = t4/2;
- V_4 = (t/2)|3>q = (t/2)t5.

The sixth-root average therefore leaves

```
Res_t = 3P(t6) + (11/4)P(t4) + (3-T/4)P(t5) - P(y2),
y2 = (1/(2t)) t6 + (1/2) t4 - (t/2) t5.                                       (Q5.1)
```

Check of y2: (1/(2t))t6 = (1/2,1/2,0,0) and (1/2)t4 = (0,1/2,t/2,t/2). Subtracting (t/2)t5 removes the |3>q entry. The sum is (1/2,1,t/2,0) ✓.

**Res_t>=0.** K_t=diag(3,11/4,3-T/4)-cc^T with c=(1/(2t),1/2,-t/2). Because 3-T/4>0, K_t>=0 iff c^T diag(3,11/4,3-T/4)^{-1} c <= 1, that is

`1/(12T) + 1/11 + T/(12-T) <= 1.`

On [1/2,9/8], 1/(12T)<=1/6 and T/(12-T)<=(9/8)/(87/8)=3/29. Since 1/6+1/11+3/29<1, the condition holds.

**Explicit partial transpose.** In the basis (|0>p,|0>q,|3>p,|3>q), with each entry computed directly from (Q5.1):

```
            [ 12T-1   12T-2   -t     9t     ]
4Res_t^Γ =  [ 12T-2   12T+7    0     11t    ]
            [  -t       0     10T    11T    ]
            [  9t      11t    11T   10T+12  ]
```

Entries of Res_t:
- (0p,0p) = 3T-1/4;
- (0p,0q) = 3T-1/2;
- (0p,3p) = -t/4;
- (0p,3q) = 0;
- (0q,0q) = 7/4+3T;
- (0q,3p) = 9t/4;
- (0q,3q) = 11t/4;
- (3p,3p) = 5T/2;
- (3p,3q) = 11T/4;
- (3q,3q) = 3+5T/2.

The partial transpose swaps the (0p,3q) and (0q,3p) entries.

**Leading minors.**
- m1 = 12T-1.
- m2 = (12T-1)(12T+7)-(12T-2)^2 = 120T-11.
- m3 = 10T·m2 - t·t(12T+7) = 1188T^2-117T.
- m4 = det = -2592T^3+4248T^2-1404T = -36T(72T^2-118T+39).

The m4 derivation expands along row three with polynomial minors M31=-144t^5+1028t^3+84t, M33=1152T^2+488T-132 and M34=1296T^2-36T:

`m4 = (-t)M31 + 10T·M33 - 11T·M34 = 144T^3-1028T^2-84T + 11520T^3+4880T^2-1320T - 14256T^3+396T^2.`

**Spot checks of m4**, each by an independent direct elimination or expansion of the numeric matrix:
- T=1: 252 (matches Q4 up to the diagonal sign similarity diag(-1,1,1,-1)).
- T=1/4: the matrix 4·(4Res^Γ) = [[8,4,-2,18],[4,40,0,22],[-2,0,10,11],[18,22,11,58]] has determinant -32256 = 256·(-126). Gaussian elimination: pivot 8, then the 3x3 [[38,1,13],[1,9.5,15.5],[13,15.5,17.5]] with determinant -4032.
- T=4: determinant -103536 = -144·719, with minors M31=3784, M33=20252, M34=20592. These also match the polynomial minors.

**Positivity on [1/2,9/8].**
- m1>=5.
- m2>=49.
- m3=T(1188T-117)>=(1/2)(477)>0.
- m4>0, because q(T)=72T^2-118T+39 is convex with q(1/2)=18-59+39=-2 and q(9/8)=(729-1062+312)/8=-21/8.

So Res_t^Γ>0, Res_t is separable by (I1), T(t,t) is separable, and Lemma L applies. ∎

**Remarks.**
1. The same certificate works on the whole open interval (59-√673)/72 < T < (59+√673)/72, the zero set of q, where K_t>=0 also holds. Only the rational subinterval is claimed as the theorem.
2. **General frame, for later reconstruction only.** For real V,W>0, use the same family with F=r^2/(2W). The residual coefficient matrix is diag(3, 3-V^2/(4W^2), 3-V^4/(4W^2)) - c c^T, with c=(1/(2W),1/2,-W/2). The partial-transpose entries, in the layout above, are:
   - A=3V^2-V^2/(4W^2);
   - B=3VW-V/(2W);
   - C=2+3W^2-V^2/(4W^2);
   - D=(11/4)V^2-V^4/(4W^2);
   - E=3VW-V^3/(4W);
   - G=3+3W^2-V^2/4-V^4/(4W^2);
   - X=-V^2/(4W);
   - Y=3W-V^2/(4W);
   - Z=(5/2)V-V^3/(4W^2).

   Here X and Z are the moved entries. At V=W=t these reduce to the displayed matrix. Strict positivity at interior diagonal points gives, by continuity, an open neighbourhood of the diagonal segment in (|v|,|w|). No explicit radius is claimed.

## Q6. Lower bound: every R_x is entangled

This is Part14 B4, re-stated so the bound does not depend on an unreviewed part. Compress Alice onto span{|0>,|1>,|2>}. Take a range product with a nonzero Alice-1 row. Its Alice-1 and Alice-2 rows are (c3,c1,c2,0) and (c5,-c3,c1,c7). Proportionality forces the Bob vector ∝ (-r^2,r,1,0), with Alice-2 amplitude r times the Alice-1 amplitude.

The Alice-1 diagonal block is I_3 on Bob{0,1,2}, contributed by a, b and c only. Cauchy–Schwarz then forces |r|=1 on every term. The (Alice0,Alice1) block equals e0e1^T+e1e2^T and comes only from a and b. Its (0,1) and (1,2) entries become -S and +S with S=Σ w α0 r. They cannot both equal 1. So the compression is entangled, R_x is entangled, and SN(R_x)>=2 for every x.

## Q7. C34.3 — forced-family boundaries of every coordinate peel

Each statement below says that a specific compression is ENTANGLED. Lemma L then cannot certify SN<=2 through that peel. These are METHOD barriers, not statements about SN(R_x).

**(a) Alice-1 and Bob-1 peels.** Assume z!=0. If the compression is separable, then

`|z| >= 1/(6 sqrt(1+|w|^2)).`

*Alice-1 proof.* Compress away Alice |1>. The range rows are:
- Row0 = (α+ηu, β+ηv, δ+ηw, ηz);
- Row2 = (ε, χ', α, κ);
- Row3 = (δu+φ, δv, δw+γ, δz+ε).

Products with a nonzero |22>-component need α!=0; set α=1. Then Row0=s·Row2 and Row3=t·Row2. The fourth entries give ηz=sκ and δz+ε=tκ, so sε = s(tκ-δz) = z(tη-sδ).

The (|00>,|22>) entry of the compression is 1, coming only from P(|00>+|22>), and it receives contributions only from these products. Hence

`1 = Σ w sε = z Σ w (tη - sδ).`

The budgets are:
- Σw|t|^2 <= (|32>,|32>) = 3+3|w|^2, from g and d;
- Σw|s|^2 <= (|02>,|02>) = 3+3|w|^2, from d and h;
- Σw|η|^2 <= 3 and Σw|δ|^2 <= 3, by the exact coefficient Gram diag(1,1,1,3,...,3). The nine compressed vectors are independent for z!=0.

Cauchy–Schwarz gives 1 <= |z|·2·sqrt(9(1+|w|^2)).

*Bob-1 proof.* The Bob-1 compression is P(|12>)+P(|10>)+Q(x), where Q lives on Alice{0,2,3}⊗Bob{0,2,3}. Q has the identical row structure, with x̌=u|0>+w|2>+z|3>, so the same inequality follows. ∎

**(b) Alice-2 and Bob-2 peels.** Both are entangled whenever z!=0 and v!=0.

*Alice-2 proof.* Here η=0 is forced by z!=0. The products carrying Alice |1> are (σ|0>+|1>+σ^2v|3>)⊗(|0>+σ|1>+σ^2|2>), together with σ=0 members. Their (|12>,|30>) entry is conj(v)Σw|σ|^4. The compression has 0 there. Forcing Σw|σ|^4=0 kills the Alice-1 block, which must contain (|11>,|11>)=1.

*Bob-2 proof.* The forced family is (-r^{-1}|0>+|1>+r|2>+(v/z)r^2|3>)⊗(-r|0>+|1>), with Σw=Σw|r|^2=1. It saturates the (Alice2,Bob1) diagonal, so the residual is 0 there. The residual's (|20>,|31>) entry is conj(v/z)Σw|r|^4!=0. After the partial transpose this entry sits in row (Alice2,Bob1), whose diagonal is 0. So the residual is not PPT by (I2), and the compression is entangled. ∎

**(c) Alice-0 peel.** It is entangled when z=0, and when z!=0 with v!=0.

*Proof.* For z=0, products carrying Alice |1> must have Bob vector |2>, so they cannot produce the required I_3 block. For z!=0 the forced family is (|1>+r|2>+(r^2v/z)|3>)⊗(-r^2|0>+r|1>+|2>). It puts -conj(v/z)Σw|r|^4!=0 at the (|10>,|32>) entry, where the compression has 0. ∎

**(d) Alice-3 and Bob-3 peels.** Both are entangled at every x: Q6 for Alice-3, and the same sign contradiction (-S versus +S) for Bob-3.

**(e) Bob-0 peel off the slice.** Take z!=0, v!=0, V=|v|^2, W=|w|^2. Products with an Alice |1> row must have zero h-coefficient and |r|=1, and the moments m1..m4 must vanish, so their sum is fixed: P(t3)+P(t1)+P(t2)+P(|0>q+v|3>p)+V P(|3>q). The remainder is

`Res''=3P(t4)+3P(|3>q)+3P(|3>s)+3P(t6)-P(|0>q+v|3>p)-VP(|3>q),`

with s=|3>_B, t4=|0>q+|3>x̃, t6=|0>x̃ and x̃=vp+wq+zs. It must be separable, and on this 2x3 system that is equivalent to PPT.

The principal block of Res''^Γ on (|0>q,|3>p,|3>q) is

`[[2+3W,0,3w̄],[0,2V,3v̄w],[3w,3vw̄,3+3W-V]]`,

with determinant V(12-6W-4V-9W^2-6VW). **Whenever 12-6W-4V-9W^2-6VW<0, the compression is entangled.** At V=W=1 the determinant is -13.

**(f) Adapted Bob peel.** Take φ ∝ |0>+(z/u)|3>, with u,z!=0. This choice removes the |3> component of the compressed x. For products carrying Alice |1>, the new |0>⊗s-component of a forces the Alice-0 to Alice-1 amplitude ratio to be -1/ρ. Every such product then contributes -|c2|^2<=0 to the (|0>p,|1>q) entry, which must equal +1. So this compression is entangled too.

## Q8. C34.4 — the far balanced ray after Q4–Q7

By the Part6 involution, R_(s,s,s,s) ~ R_(1,1,-1,1/s). Put ζ=1/s and take 0<|ζ|<1/(6√2), that is s>6√2. Then, at the representative (1,1,-1,ζ):
- (a) fails, since |ζ|<1/(6√2);
- (b) and (c) fail, since v=1;
- (d) fails always;
- (e) fails, with determinant -13 for every ζ!=0;
- (f) fails.

So **no coordinate peel and not the adapted peel certifies the far ray.**

There is also an exact discontinuity: the Bob-0 compression is separable at ζ=0 (Q4) and entangled at every ζ!=0 on this line (Q7e). This is a method barrier, not evidence of Schmidt number three. The far ray remains OPEN in both directions. Proved SN<=2 points on the ray remain s=1,2,3,5 (Parts 13–14).

## Q9. Updated map and the original gap

New proved SN=2 points and regions (author-WRITTEN, pending reconstruction):
- the decisive point x0;
- the whole complex line (u,1,-1,0);
- the diagonal-modulus slice {(u,v,w,0): |v|=|w|=t, t^2 in [1/2,9/8]} with all phases and all u in C — mostly outside the Part6 ball, Theorem C and Theorems D/D' (for example x0 and (2,1,1,0));
- a qualitative open neighbourhood of that slice inside z=0.

OPEN:
- the comparable-component core with z!=0, including the far balanced ray;
- the rest of the z=0 slice.

**Original physics-3/P44 remains UNMET.** No explicit rational 4x4 PPT state with Schmidt number >=3 and no universal complex SR2-nonnegative strict negative separator is delivered. Nor is an all-state SN2 theorem. N4 stays historical UNKNOWN/exit-unestablished, and old21 stays NOT_RECONSTRUCTED. All earlier process findings are retained.

These are not formal/kernel/executable/triple/configured-family/human/cross-vendor/novelty acceptance, not a park and not a closeout.

**END OF COMPLETE CURRENT v17 PART15/15.**
