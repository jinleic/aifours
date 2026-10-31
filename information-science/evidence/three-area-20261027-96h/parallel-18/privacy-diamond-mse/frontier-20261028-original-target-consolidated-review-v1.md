# Review packet: original rounded optimum at ln 64 and all-epsilon cost incompatibility

**AUTHOR CANDIDATE — WRITTEN with owner-run exact Fraction checks; NOT independently reviewed or parent-adopted.** Native observation immediately before writing: `Wed Oct 28 21:49:09 PDT 2026`.

## 1. Exact original contract and TWO claims

For ANY finite epsilon>0, set b=e^(-epsilon), and let F_epsilon contain ALL Borel laws of query-output-independent additive noise in R^2 satisfying

    mu(A)<=b^(-1)mu(A+h) for EVERY Borel A and EVERY h in
    D={h:||h||_1<=1},                                                    (1)

where D is the FULL CLOSED unit l1 diamond. Define `J(mu)=E|X|_2^2`, `L(mu)=E||X||_1`, `V_J=inf_F J`, `V_L=inf_F L`, and `Opt_L={mu in F:L(mu)=V_L}`.

**Claim A — exact original optimum at one finite epsilon.** Conditional on the single named parent LAW642 global/uniqueness theorem in §2, at epsilon=ln 64 the unique actual all-law J optimizer is the rounded-core shell (6), and

    1630066277350703/10^16 < V_J(ln 64) <1630066277350704/10^16.       (2)

Its exactly screened scalar root and normalization are enclosed in §3. The law in (6) is actually full-D private, not a radial surrogate. The interval is established by exact Fraction arithmetic and explicit alternating-arctangent bounds; that arithmetic does not prove the parent global theorem.

**Claim B — one strongest source–target incompatibility.** Conditional on that SAME LAW642 theorem, for EVERY finite epsilon>0,

    inf_(mu in Opt_L) J(mu)-V_J >0.                                     (3)

The infimum is interpreted in the extended sense if every L-optimal law has infinite J. In particular no actual first-norm optimizer can be an original squared-Euclidean optimizer; this is a STRICT INFIMUM gap, not merely different chosen scalar selectors. Opt_L is nonempty by the direct compactness proof in §6. No numerical or uniform-in-epsilon lower size is claimed.

Both claims are WRITTEN author candidates, NOT independently reviewed or newly parent-adopted. They concern exactly this additive/full-D model and the two costs; neither is a publication-wide source non-equivalence, novelty/priority, source-proof-repair or all-norm claim.

## 2. Exact dependency and authority table

| Claim or step | Required named research record | Scope and limits |
|---|---|---|
| Original J optimizer exists uniquely as a law, is a compact convex-core geometric shell, and each globally screened R-branch zero identifies it | Parent `institute/runs/three-area-2026-10-23-96h/privacy-all-law-self-contained-parent-v1.md`, SHA `c08f6353f121ef9e35da0e9d5e8ec9c87b0da838be0d1adf38b807010a1cd979`; source `information-science/evidence/three-area-20261023-96h/parallel-18/privacy-diamond-mse/privacy-all-law-optimum-self-contained-v1.md`, SHA `957cab2bcf3eff1860ff9f4b5a1e5838708aceaf894a97fdc2c5244c3e7d8e53`, §8.5 | Parent-WRITTEN_SUPPORTED same-harness proof at named standard analysis imports; not formal, human or independent-model-family verification. |
| Exact ln 64 signs, interval, normalizer and screened-root arithmetic | **No additional research record**; all inputs and reproducible owner-run Fraction code are in §§3–4 | Conditional mapping from the screened root to the all-law optimum uses the preceding LAW642 row. |
| All-epsilon strict L/J incompatibility | **Only LAW642 above**, plus the explicitly written Brunn–Minkowski/measure/geometry arguments in §§5–6 | No matching-norm theorem, phase threshold or assertion that L optimizers are unique/radial is used. |
| Corrected ln 64 explicit nonradial competitor beating centered staircases | Parent `institute/runs/three-area-2026-10-27-96h/dispositions/info-1-ln64-nonradial-staircase-gap-parent-v1.md`, SHA `d67b0ac9cbde8c6d1f81f0f407106070ea3cee640984b4d166929b12d6dd6516` | **Supporting context only, NOT a premise here.** It adopts the corrected >10^-6 staircase-family gap, not an all-law optimum, all-radial theorem or novelty. Its mandatory prior numeric correction remains in force. |
| MDA26 matching-norm source, v241 threshold, v253 composition and all later author candidate packets | **None required** | They do not inherit proof or adoption from this packet; no held source is read or repaired. |

Standard non-research facts used below: Radon–Nikodym/Lebesgue differentiation for feasible densities, Fubini–Tonelli, Brunn–Minkowski, compact-set volume/bathtub geometry, Descartes' sign rule, elementary geometric sums, the alternating arctan remainder, Prokhorov/Portmanteau and weak measure-order closure. The original LAW642 theorem remains a named premise, not an unverified hidden import.

## 3. Screened rounded root at epsilon=ln 64

Set `b=1/64`, `m=1/63`, `v=m(m+1)`,

    T2=m+2m^2,  T3=m+6m^2+6m^3,
    T4=m+14m^2+36m^3+24m^4, C0=m/3+(3/2)m^2+m^3.

For d define the R-branch quantities from the named source

    t=[(4/3)d^3+2md^2+m^2d-C0]/v,
    lambda=2t^2+2d^2+2m(t+d)+T2,
    c=t-d, A=lambda-v, w=2t.                                             (4)

Let `M2(w)=w^2+2mw+T2`, `M4(w)=w^4+4mw^3+6T2w^2+4T3w+T4`, `H_D=(2/3)M4-2lambda M2`. The source's explicit primitive gives H_R=H_D+8(Rint-Uint), with

    J3=[c sqrt(A-c^2)(5A-2c^2)+3A^2 asin(c/sqrt A)]/8,
    Rint=-(2/3)J3+(mA-m^3/3)c-c^4/3+lambda c^2/2,
    Uint=[w^3/3+mw^2+(T2-lambda)w]c
      +[-w^2-2mw+2lambda-T2]c^2/2
      +(2/3)(w+m)c^3-(2/3)c^4.                                          (5)

The exact identity `A-c^2=(t+d+m)^2` makes `asin(c/sqrt A)=atan[z]` with `z=c/(t+d+m)>0`. Therefore H_R is EXACTLY the rational expression Hrat in the code below minus `2A^2 atan(z)`. For 0<z<1, the odd/even alternating sums `L_11`, `U_12=L_11+z^25/25` enclose atan(z). Exact checked signs give

    17899568185394517/10^17 < d_* <17899568185394518/10^17,
    H_R(left)>10^-18,      H_R(right)<-10^-18.                           (6)

The rational arctan enclosure width is <10^-35 at BOTH endpoints. On the full interval, `t'(d)=(4d^2+4md+m^2)/v>0` and `lambda'(d)=(4t+2m)t'(d)+4d+2m>0`; the exact endpoint checks `t(left)>d(right)`, `0<d<1/2`, and `T2<lambda(left)<lambda(right)<4m^2+4m+1/3` verify the source screens throughout. The additional parent bound `lambda<=4/epsilon^2` holds because `lambda<100/441` and `ln64=6ln2<21/5` (ln2<7/10 follows from the first four positive exponential-series terms).

By continuity H_R has a root in (6). The NAMED LAW642 screen says such a root is the unique globally optimal original law, so lambda is V_J and (2) follows. Its exact law is

    S_*={x:||x||_1<=2t_*, |x|_2^2+(2/63)||x||_infinity+65/3969<=lambda_*},
    p_*(x)=64^(-min{k:x in S_*+kD})/Z_*.                                 (7)

The core has c_*=t_*-d_*>0 and a genuine rounded arc under the source geometry. Its shell index changes by at most one under h in D, proving feasibility directly. With `A=lambda-v`, `z=c/(t+d+m)`, its exact normalizer simplifies to

    Z_*=8td+4m(t+d)+2T2+4A atan(z),
    339888889366/10^12 < Z_* <339888889367/10^12.                       (8)

All interval signs and directions are checked below.

## 4. Reproducible exact arithmetic for Claim A

The following full rational code was executed as ONE Python eval-kernel cell; it printed the PASS line stated after the block. Every assertion is exact `fractions.Fraction`. The only analytic enclosure is the explicitly proved alternating arctan remainder. No float, numerical optimizer, CAS or interval-library black box establishes a bound.

```python
from fractions import Fraction as F
m=F(1,63); v=m*(1+m); T2=m+2*m*m
T3=m+6*m*m+6*m**3; T4=m+14*m*m+36*m**3+24*m**4
C0=m/F(3)+F(3,2)*m*m+m**3

def atan_bounds(z):
    L=sum((-1)**k*z**(2*k+1)/F(2*k+1) for k in range(12))
    return L,L+z**25/F(25)

def cert(d):
    t=(F(4,3)*d**3+2*m*d*d+m*m*d-C0)/v
    lam=2*t*t+2*d*d+2*m*(t+d)+T2
    c=t-d; A=lam-v; w=2*t
    M2=w*w+2*m*w+T2
    M4=w**4+4*m*w**3+6*T2*w*w+4*T3*w+T4
    HD=F(2,3)*M4-2*lam*M2
    U=(w**3/F(3)+m*w*w+(T2-lam)*w)*c
    U+=(-w*w-2*m*w+2*lam-T2)*c*c/2
    U+=F(2,3)*(w+m)*c**3-F(2,3)*c**4
    Hr=HD-F(2,3)*c*(t+d+m)*(5*A-2*c*c)
    Hr+=8*((m*A-m**3/3)*c-c**4/3+lam*c*c/2-U)
    z=c/(t+d+m); al,au=atan_bounds(z)
    return t,lam,Hr-2*A*A*au,Hr-2*A*A*al

lo=F(17899568185394517,10**17)
hi=F(17899568185394518,10**17)
tl,Ll,Hll,Hlu=cert(lo); tu,Lu,Hul,Huu=cert(hi)
assert Hll>F(1,10**18) and Huu<-F(1,10**18)
assert Hlu-Hll<F(1,10**35) and Huu-Hul<F(1,10**35)
assert 0<lo<hi<F(1,2) and tl>hi and 2*tu<1
assert T2<Ll<Lu<4*m*m+4*m+F(1,3) and Lu<F(100,441)
assert F(1630066277350703,10**16)<Ll<Lu<F(1630066277350704,10**16)
assert F(1882704899884405,10**16)<tl<tu<F(1882704899884407,10**16)
assert F(92748081344953,10**16)<tl-hi<tu-lo<F(92748081344955,10**16)
cl=tl-hi; cu=tu-lo; yl=tl+lo+m; yu=tu+hi+m
zl=cl/yu; zu=cu/yl; assert 0<zl<zu<1
Al=Ll-v; Au=Lu-v; atl,_=atan_bounds(zl); _,atu=atan_bounds(zu)
Zl=8*tl*lo+4*m*(tl+lo)+2*T2+4*Al*atl
Zu=8*tu*hi+4*m*(tu+hi)+2*T2+4*Au*atu
assert F(339888889366,10**12)<Zl<Zu<F(339888889367,10**12)
print('PASS')
```

The actual cell printed `PASS exact H signs/remainders, global screens, d/t/c/lambda intervals, and normalizer`. The code above shortens only that print label. Earlier floating scans located the bracket but are NOT used for the displayed exact inequalities.

## 5. Constructive proof of Claim B, without MDA or a phase theorem

Let P_* be the unique LAW642 J-optimal law, with density `b^(n_S)/Z` for compact convex core S of positive area. There are two exhaustive cases.

### 5.1 If S is not an l1 diamond up to null sets

For k>=0 set `R_k=sqrt(|S+kD|/|D|)`. Brunn–Minkowski gives `R_(k+1)>=R_k+1`. Therefore the radial index `n_sharp(x)=min{k:||x||_1<=R_k}` changes by at most one under every h in D. The ACTUAL full-D-private density `p_sharp=b^(n_sharp)/Z` has the SAME normalization as P_* because

    Z=(1-b)sum_(k>=0)b^k|S+kD|
     =(1-b)sum_(k>=0)b^k|R_k D|.                                       (9)

For each k, the equal-area diamond minimizes `integral ||x||_1`; the k=0 inequality is STRICT because S has positive symmetric difference with its equal-area centered diamond. This follows by splitting the symmetric difference inside/outside its radius; the radius boundary is null. Exact layer summation gives

    L(P_*)-L(P_sharp)
      =(1-b)/Z sum_(k>=0)b^k [integral_(S+kD)||x||_1
                               -integral_(R_kD)||x||_1] >0.              (10)

The geometric sums converge by compactness. Thus the true J optimizer has L>V_L without any source matching-norm theorem or assumption about mean optimizers.

### 5.2 If S is an l1 diamond

Write S=gD, g>0. If g>1, unnormalized shells satisfy `u_(g-1)=b u_g+(1-b)1_((g-1)D)`. Normalization makes P_(g-1) a genuine mixture of P_g and the uniform inner diamond; the inner component has strictly smaller E||X||_1^2, and J=(2/3)E||X||_1^2 for both radial laws. That contradicts global J optimality. The endpoint laws P_0=P_1 agree, while the scalar J derivative at 0 is positive, so g cannot be an endpoint. Hence 0<g<1 and is the unique scalar J-minimizer.

For a centered diamond staircase, put `m=b/(1-b)`, `v=m(m+1)`, `t=1+2m`, `x=g+m`. The L and J derivative sign polynomials are

    Q=x^4-2vt x+3v^2,
    P=x^5+2v x^3-2vt x^2-v(1+3v)x+2v^2t.                            (11)

Explicitly, with `M2=g^2+2mg+m+2m^2`, the derivatives are `L'=2Q/(3M2^2)`, `J'=2P/(3M2^2)`, and in g

    Q=g^4+4mg^3+6m^2g^2-2m(1+3m)g+m^2,
    P=g^5+5mg^4+(2m+12m^2)g^3+(12m^3-2m)g^2
       -m(1+2m)(1+6m)g+m^2(1+2m).

Their endpoint values are respectively `(m^2,(1+m)^2)` and `(m^2(1+2m),(1+m)^2(1+2m))`.

In g both have two coefficient sign changes, positive endpoint values, and at `g0=sqrt(v)-m in (0,1)`, `Q=2v^(3/2)(2sqrt(v)-t)<0`, `P=-v sqrt(v)<0`. Descartes plus IVT give two simple positive roots for each; let g_L,g_J be the respective larger scalar minima. Then `x_L=g_L+m>sqrt(v)`.

Set `R=2x^3-(1+6v)x+2vt`. Exact algebra gives `P=xQ+vR`. At Q=0, `R=[3(x^2-v)^2-x^2]/x`. With `z=x_L^2/v>1`, the root equation and t^2=4v+1 give

    1/v-3(z-1)^2/z=(z-1)^3(z+3)/(4z)>0.                               (12)

Hence R<0, P(g_L)<0 and g_L<g_J. Since the L derivative is positive on (g_L,1), the actual global J law satisfies `L(P_*)=L(P_gJ)>L(P_gL)>=V_L`. P_gL itself is actually full-D private; it need not be globally L-optimal for this argument.

## 6. Mean-optimal attainment and strict INFIMUM gap

Product Laplace is feasible with finite L, so V_L<infinity. Any minimizing sequence for L is tight by Markov. Weak subsequential limits preserve ALL full-D event inequalities via nonnegative bounded continuous tests, and L is lower semicontinuous; its limit is therefore in Opt_L. Thus Opt_L is nonempty without an MDA premise.

If `inf_(Opt_L)J=+infinity`, (3) is immediate. Otherwise a J-minimizing sequence in Opt_L has bounded J and is tight. Its weak limit remains private; lower semicontinuity gives `L(limit)<=V_L`, hence equality by global minimality, and J attains the restricted infimum. If that infimum were V_J, LAW642's UNIQUE J-law would force the minimizer to be P_*, contradicting §5. Therefore (3) is strictly positive. This compactness argument is what converts pointwise optimizer exclusion into a nonzero infimum gap.

## 7. Owner controls, failures and review ceiling

* The §4 exact code was executed in one Python eval-kernel cell and passed all listed arithmetic checks. Those checks do NOT verify LAW642's all-law theorem or independently review the proof.
* Separate exact `fractions.Fraction` sparse-polynomial cells checked the COMPLETE formal identities `P=xQ+vR`, the centered-coordinate conversions of Q/P, and `(z^2+3)^2-16z-12(z-1)^2=(z-1)^3(z+3)`. These checks do not prove scalar root ordering, Brunn–Minkowski, privacy or compactness.
* Prior unreviewed author artifacts are supporting history, not premises; no f145 correction is silently folded into them. An unrelated exploratory guess that a different radial witness had J gap <10^-6 was false (the owner assertion failed); that guess and witness are not used in either claim here.

This is ONE self-contained author review packet, not a parent disposition. No external-model/human/formal verification, source-proof repair, source identity/priority, worldwide novelty, or new adoption is claimed. A disjoint reviewer should reconstruct the precise named LAW642 screens, arctan remainder signs, all interval directions, the Brunn–Minkowski shell/strict bathtub step, scalar selector sign, full-D weak closure and restricted-optimum attainment.
