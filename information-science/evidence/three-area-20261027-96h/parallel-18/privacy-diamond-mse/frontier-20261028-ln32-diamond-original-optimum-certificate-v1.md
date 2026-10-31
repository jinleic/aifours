# Exact diamond-side original optimizer certificate at epsilon=ln 32

**AUTHOR CANDIDATE — WRITTEN plus an owner-run exact Fraction certificate; NOT independently reviewed or parent-adopted.** Native pre-write observation: `Wed Oct 28 21:36:07 PDT 2026`.

## 1. Original all-law target and exact certified intervals

At epsilon=ln 32, b=1/32, the registered target is `V_J=inf E|X|_2^2` over ALL Borel additive-noise laws satisfying pure epsilon privacy for EVERY event and EVERY shift in the FULL CLOSED unit l1 diamond D.

The all-law/unique-law premise is the named parent-WRITTEN_SUPPORTED `institute/runs/three-area-2026-10-23-96h/privacy-all-law-self-contained-parent-v1.md`, SHA-256 `c08f6353f121ef9e35da0e9d5e8ec9c87b0da838be0d1adf38b807010a1cd979`, and its actual source `information-science/evidence/three-area-20261023-96h/parallel-18/privacy-diamond-mse/privacy-all-law-optimum-self-contained-v1.md`, SHA-256 `957cab2bcf3eff1860ff9f4b5a1e5838708aceaf894a97fdc2c5244c3e7d8e53`, §8.5 D-branch screen. The support is same-harness written reasoning at named standard imports, not a formal or independent-model proof. No earlier unreviewed author result is a premise.

Conditional on that named global theorem, the actual UNIQUE original optimal LAW is the fully private geometric shell with a diamond core `g_* D`, and

    441266095196338192/10^18 < g_* <441266095196338193/10^18,
    2659858724480402/10^16 < V_J <2659858724480403/10^16,
    5150475541477078/10^16 < Z_* <5150475541477079/10^16,
    756107917421474/10^15 < P_*(g_*D) <756107917421475/10^15.          (1)

Every displayed endpoint is rational and is checked exactly below. The density is

    p_*(x)=32^(-min{k:x in g_*D+kD})/Z_*.                                (2)

The shell-index triangle inequality gives the original full-event/full-D feasibility; the global optimum and uniqueness are the named parent premise, not consequences of a scalar sign check alone.

## 2. Exact screened scalar root

Put `m=1/31`, `T2=m+2m^2`, `T3=m+6m^2+6m^3`, `T4=m+14m^2+36m^3+24m^4`, and

    M2(g)=g^2+2mg+T2,
    M4(g)=g^4+4mg^3+6T2g^2+4T3g+T4,
    P(g)=g^5+5mg^4+(2m+12m^2)g^3+(12m^3-2m)g^2
           -m(1+2m)(1+6m)g+m^2(1+2m).                                  (3)

The exact signs at the endpoints in (1), together with P(0)>0,P(1)>0 and two coefficient sign changes, identify the larger unique scalar-family minimum root g_*. Its value is M4(g_*)/[3M2(g_*)]. For `a<g_*<z`, positive coefficients give the outward bounds `M4(a)/(3M2(z))<=V<=M4(z)/(3M2(a))`.

The parent D screen also requires `V>=g_*^2+2mg_*+T2=M2(g_*)`. The exact calculation proves the stronger bound `V_lower-M2(z)>1/125`. It checks `T2<V<4m^2+4m+1/3`; and since `ln 2<7/10`, epsilon=5ln2<7/2, so `4/epsilon^2>16/49` and the checked V upper is below this screen too. Hence the named global theorem applies to the certified root; this is not merely an unscreened stationary point.

For the actual law `Z_*=2M2(g_*)` and `P_*(g_*D)=g_*^2/M2(g_*)`, giving the last two intervals in (1). No all-law radiality is assumed: the unique original core is a diamond here BECAUSE the screened global theorem says so.

## 3. Standalone exact arithmetic certificate

The following `fractions.Fraction` code was run as ONE Python eval-kernel cell and printed the PASS line. All root signs, denominators, screens and interval comparisons are exact; no root optimizer, float or interval-library black box is used.

```python
from fractions import Fraction as F
m=F(1,31); T2=m+2*m*m
T3=m+6*m*m+6*m**3; T4=m+14*m*m+36*m**3+24*m**4
P=lambda g:g**5+5*m*g**4+(2*m+12*m*m)*g**3+(12*m**3-2*m)*g*g-m*(1+2*m)*(1+6*m)*g+m*m*(1+2*m)
M2=lambda g:g*g+2*m*g+T2
M4=lambda g:g**4+4*m*g**3+6*T2*g*g+4*T3*g+T4
a=F(441266095196338192,10**18)
z=F(441266095196338193,10**18)
assert P(0)>0 and P(a)<0<P(z) and P(1)>0
jl=M4(a)/(3*M2(z)); ju=M4(z)/(3*M2(a))
lamP=4*m*m+4*m+F(1,3)
assert F(2659858724480402,10**16)<jl<ju<F(2659858724480403,10**16)
assert T2<jl<ju<lamP and ju<F(16,49) and jl-M2(z)>F(1,125)
Zl=2*M2(a); Zu=2*M2(z)
assert F(5150475541477078,10**16)<Zl<Zu<F(5150475541477079,10**16)
pl=a*a/M2(z); pu=z*z/M2(a)
assert F(756107917421474,10**15)<pl<pu<F(756107917421475,10**15)
print('PASS')
```

The actual cell printed `PASS: exact quintic signs, all D screens, J, normalizer, core probability`; the code above shortens only the print text. It does not machine-verify the parent LAW642 theorem or any scientific novelty.

## 4. Source/phase boundary

The parent v241 separated threshold theorem, SHA `48274df7a84b16cd8ead4a0b9069b8359110e1b216bc72e6baea1de03e626138`, independently places epsilon=ln 32 on its diamond side since `s=sinh^2(epsilon/2)=961/128<10<s_t`. This is a prior recorded threshold reproduction, not a required input to the D-screen certificate and not a source-repair or novelty claim. No matching-norm MDA/PMLR claim is used.

The numeric certificate is WRITTEN plus exact owner-run arithmetic, conditional on the named parent all-law theorem; no formal, human/cross-model independent review, priority or parent adoption is claimed. Suggested review: all-law D-screen authority, exact root classification, ratio enclosure and core normalization.
