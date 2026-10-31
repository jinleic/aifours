# Exact source–target tradeoff when BOTH optimal laws are diamond staircases

**AUTHOR CANDIDATE — WRITTEN plus an owner-run exact Fraction certificate; NOT independently reviewed or parent-adopted.** Native pre-write observation: `Wed Oct 28 21:37:45 PDT 2026`.

## 1. Same actual model, distinct cost theorems

At epsilon=ln 32, b=1/32, let the original class be ALL Borel additive-noise laws private for EVERY event and EVERY shift in the FULL CLOSED unit l1 diamond D. Write J=E|X|_2^2, L=E||X||_1.

The source-independent calculation below constructs two ACTUAL full-D-private centered staircases P_L and P_J, each the unique minimizer of its own cost within that scalar staircase family, and proves

    J(P_L)-J(P_J)>3/500,        L(P_J)-L(P_L)>1/125.                    (1)

Two SEPARATE named same-harness written parent results upgrade their roles:

* Parent LAW642 `privacy-all-law-self-contained-parent-v1.md`, SHA `c08f6353f121ef9e35da0e9d5e8ec9c87b0da838be0d1adf38b807010a1cd979`, and its 642LF source SHA `957cab2bcf3eff1860ff9f4b5a1e5838708aceaf894a97fdc2c5244c3e7d8e53`, identify the SCREENED P_J as the UNIQUE original all-law J optimizer.
* Parent MDA26 matching-norm alternative `privacy-MDA26-entire-norm-cost-and-weighted-decay-parent-v1.md`, SHA `75614a6fc5cb66d9b26f13e64e58935fe6ea52121948e7a56592b91611576ac3`, identifies P_L as an actual all-law L optimizer in the SAME full-D class. It does not establish uniqueness of all L-optimal laws.

Thus, conditional on the two named premises, (1) compares actual globally optimal laws of DIFFERENT objectives. The discrepancy survives even though both chosen laws are centered diamond staircases; neither theorem by itself selects the other's offset. No unreviewed author candidate, external source proof, or source-identity claim is imported.

## 2. Exact roots, moments and parent D screen

Let m=1/31, `T2=m+2m^2`, `T3=m+6m^2+6m^3`, `T4=m+14m^2+36m^3+24m^4`,

    M2(g)=g^2+2mg+T2,
    M3(g)=g^3+3mg^2+3T2g+T3,
    M4(g)=g^4+4mg^3+6T2g^2+4T3g+T4,
    L(P_g)=2M3/(3M2),       J(P_g)=M4/(3M2).                            (2)

Their derivative signs are respectively

    Q(g)=g^4+4mg^3+6m^2g^2-2m(1+3m)g+m^2,
    P(g)=g^5+5mg^4+(2m+12m^2)g^3+(12m^3-2m)g^2
           -m(1+2m)(1+6m)g+m^2(1+2m).                                   (3)

Both have exactly two coefficient sign changes and positive endpoint values. Exact signs in §4 put their LARGER simple roots in the disjoint rational intervals

    3646185443795757/10^16 < g_L <3646185443795759/10^16,
    441266095196338192/10^18 < g_J <441266095196338193/10^18.          (4)

Since P_0=P_1 as laws, those roots are the family minima. Exact ratio bounds also verify the LAW642 D screen for g_J, including `J_lower-M2(g_J_upper)>1/125`, the lambda bounds, and the Laplace screen `J<16/49<4/(ln32)^2` from ln2<7/10. Thus the global J identification explicitly uses the parent screen, not just stationary root signs.

## 3. Exact objective enclosures

For any root in a rational bracket (a,z), the positive-coefficient moments give safe outward bounds by evaluating numerator at a and denominator at z for the lower, and the reverse for the upper. Exact Fraction checks give

    2722245736255/10^13 < J(P_L) <2722245736256/10^13,
    4807783720535/10^13 < L(P_L) <4807783720536/10^13,
    4890839136388/10^13 < L(P_J) <4890839136389/10^13,
    2659858724480402/10^16 < J(P_J) <2659858724480403/10^16.         (5)

Subtracting the appropriate outward endpoints proves (1). There is no float-based sign decision, epsilon approximation, or claim that one chosen law is the other cost's optimizer.

## 4. Complete exact arithmetic control

The following standalone code was run in the Python eval kernel (the final J(P_J) interval assertion was a second successful cell). It uses only `fractions.Fraction`.

```python
from fractions import Fraction as F
m=F(1,31); T2=m+2*m*m
T3=m+6*m*m+6*m**3; T4=m+14*m*m+36*m**3+24*m**4
P=lambda g:g**5+5*m*g**4+(2*m+12*m*m)*g**3+(12*m**3-2*m)*g*g-m*(1+2*m)*(1+6*m)*g+m*m*(1+2*m)
Q=lambda g:g**4+4*m*g**3+6*m*m*g*g-2*m*(1+3*m)*g+m*m
M2=lambda g:g*g+2*m*g+T2
M3=lambda g:g**3+3*m*g*g+3*T2*g+T3
M4=lambda g:g**4+4*m*g**3+6*T2*g*g+4*T3*g+T4
a=F(3646185443795757,10**16); z=F(3646185443795759,10**16)
u=F(441266095196338192,10**18); w=F(441266095196338193,10**18)
assert Q(0)>0 and Q(a)<0<Q(z) and Q(1)>0
assert P(0)>0 and P(u)<0<P(w) and P(1)>0
Jsl=M4(u)/(3*M2(w)); Jsu=M4(w)/(3*M2(u))
assert T2<Jsl<Jsu<4*m*m+4*m+F(1,3)
assert Jsl-M2(w)>F(1,125) and Jsu<F(16,49)
Jml=M4(a)/(3*M2(z)); Jmu=M4(z)/(3*M2(a))
Lml=2*M3(a)/(3*M2(z)); Lmu=2*M3(z)/(3*M2(a))
Lsl=2*M3(u)/(3*M2(w)); Lsu=2*M3(w)/(3*M2(u))
assert F(2722245736255,10**13)<Jml<Jmu<F(2722245736256,10**13)
assert F(4807783720535,10**13)<Lml<Lmu<F(4807783720536,10**13)
assert F(4890839136388,10**13)<Lsl<Lsu<F(4890839136389,10**13)
assert F(2659858724480402,10**16)<Jsl<Jsu<F(2659858724480403,10**16)
assert Jml-Jsu>F(3,500) and Lsl-Lmu>F(1,125)
print('PASS')
```

The main cell printed `PASS: both root brackets, D global screens, three objective intervals, two strict tradeoff margins`; the additional J interval passed in a separate cell. Earlier float renderings only displayed the exact rational enclosures. Arithmetic checks do NOT verify either parent theorem or source version.

## 5. Scope and review

This is an exact finite-epsilon distinction between the matching-first-norm source application and the registered squared-Euclidean target, conditional on the TWO separately named parent boundaries. It is not a source-proof repair, a global literature search, novelty or priority clearance, formal proof, independent review or parent adoption. Suggested review: moment/derivative identities, D-screen theorem mapping, first-norm all-law premise, exact rational interval directions and the distinction between the selected source optimizer and all mean-optimal laws.
