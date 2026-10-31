# A fully explicit nonradial obstruction on a continuous low-privacy window

**AUTHOR CANDIDATE — WRITTEN plus exact Fraction coefficient controls; NOT independently reviewed or parent-adopted.** Native pre-write observation: `Wed Oct 28 21:04:32 PDT 2026`.

## 1. Original model and finite-ε statement

For every finite epsilon>=ln 20737, put b=e^(-epsilon), `m=b/(1-b)`, `s=m^(1/4)`; hence 0<s<=1/12. The original class is ALL Borel additive-noise laws satisfying epsilon privacy for EVERY Borel event and EVERY shift in the FULL CLOSED unit l1 diamond D. Let `J=E|X|_2^2`.

Define g as the UNIQUE root in `(9s/10,2s)` of the explicit quintic P_m in (4) below, and set

    eta=s/12000,
    K=gD intersect {||x||_infinity<=g-eta}.                              (1)

The ACTUAL geometric shell law P_K is fully private. The source-independent WRITTEN claim is the quantitative, uniform original-class obstruction

    J(P_K)+ s^2/1080000000000 <= min_(0<=gamma<=1) J(P_gamma),          (2)

where P_gamma is the actual centered diamond staircase with core gamma D. Thus for EVERY epsilon in the entire stated finite range, no centered diamond staircase attains the original all-law J optimum. The right side is a family minimum, not an unqualified all-law formula; P_K itself is not claimed optimal.

**Separate conditional radial extension:** the named parent MDA26 matching-norm alternative `institute/runs/three-area-2026-10-23-96h/privacy-MDA26-entire-norm-cost-and-weighted-decay-parent-v1.md`, SHA-256 `75614a6fc5cb66d9b26f13e64e58935fe6ea52121948e7a56592b91611576ac3`, states that over this same all-Borel/full-D class, the minimum of `W=E||X||_1^2` is attained by a centered diamond staircase. Every l1-radial density satisfies J=(2/3)W. IF that parent result is valid, (2) consequently beats EVERY l1-radial private law by the displayed positive amount. This is not inferred from a mean-only theorem or claimed to establish an original all-law optimizer.

No earlier unreviewed author theorem, LAW642, v241, v253 or MDA premise is needed for the unconditional staircase obstruction. This is a finite-ε exact inequality over a continuous half-line, not a novelty, printed-proof or global source-equivalence claim.

## 2. Exact costs and scalar root

For 0<=gamma<=1, let P_gamma have core gamma D and density proportional to `b^(min{k:x in gamma D+kD})`. It is an actual fully private law. Let N be geometric with `P(N=k)=(1-b)b^k`, and `M_j(g)=E(g+N)^j`. The exact layer-sum identity gives

    J(P_g)=M4(g)/(3M2(g)),
    M1=g+m, M2=g^2+2mg+m+2m^2,
    M4=g^4+4mg^3+6(m+2m^2)g^2
       +4(m+6m^2+6m^3)g+m+14m^2+36m^3+24m^4.                         (3)

Its derivative has the sign of

    P_m(g)=g^5+5mg^4+(2m+12m^2)g^3+(12m^3-2m)g^2
              -m(1+2m)(1+6m)g+m^2(1+2m).                                (4)

The polynomial has exactly two coefficient sign changes, P_m(0)>0 and P_m(1)>0. Section 3 proves `P_m(9s/10)<0<P_m(2s)`, with 2s<1. Descartes and IVT therefore give exactly two simple positive roots, the larger g lying in (9s/10,2s). Since P_0=P_1 as normalized laws, that root is the global minimizer of the staircase family.

## 3. Explicit all-window sign and shape bounds

Set c=9/10. Direct expansion of P_m(cs)/s^5, dropping negative terms, gives for 0<s<=1/12

    P_m(cs)/s^5
     <= c^5-c+2c^3 s^2+(5c^4+1)s^3+12c^3s^6+2s^7+12c^2s^9
     <= -531931917329/1791590400000 < -1/4.                              (5)

Similarly, dropping positive terms yields

    P_m(2s)/s^5 >=30-8s-16s^4-24s^8
                 >=525519359/17915904 >29.                               (6)

Write `S(g)=3M2(g)^2-M4(g)`. Its exact polynomial is

    S=2g^4+8mg^3+12m^2g^2-(4m+12m^2)g
          -m-11m^2-24m^3-12m^4.                                        (7)

For g>=cs, `S'(g)/s^3 >=8c^3-4s-12s^5>5`. Also

    S(cs)/s^4 >=2c^4-1-4cs-11s^4-12cs^5-24s^8-12s^12
                >=5398913833871/464380231680000 >1/100.                 (8)

Thus at the scalar minimizing root g, S(g)>s^4/100. The interval `g<2s` gives `M2(g)<=5s^2`, `M1(g)<=3s` throughout the window. Consequently

    B:=M2(g)-J(P_g)=S(g)/[3M2(g)] >=s^2/1500.                          (9)

No selected example is used to infer these inequalities.

## 4. Actual clipped competitor and its certified gap

For eta as in (1), eta<g/2. Its normalized geometric shell law is full-D private because any allowed shift changes its shell index by at most 1. Exactly, for every k>=0,

    K+kD=(g+k)D intersect {||x||_infinity<=g+k-eta}.                      (10)

The reverse inclusion follows by clipping each positive-quadrant coordinate at g-eta (cost <=k, using eta<g/2), then lowering their sum to g if needed; signs/permutations complete the proof.

The four omitted caps of height eta at radius g+k each have area eta^2 and squared moment `(g+k)^2 eta^2-(4/3)(g+k)eta^3+(2/3)eta^4`. Their exact geometric sum gives

    J(P_K)-J(P_g)
      =[4eta^2/Z_K] [-B+(4/3)M1(g)eta-(2/3)eta^2],
    Z_K=2M2(g)-4eta^2>0.                                                 (11)

Because `M1(g)<=3s` and eta=s/12000, `(4/3)M1 eta<=s^2/3000<=B/2`. Using `Z_K<=2M2(g)` and (9),

    J(P_g)-J(P_K) >=eta^2 B/M2(g)
       >=s^2/1080000000000.                                              (12)

As P_g is the exact staircase-family minimum, (12) is precisely the original-class statement (2).

## 5. Exact checks and limits

Python-kernel `fractions.Fraction` arithmetic checked the endpoint rational inequalities in (5),(6),(8) and `4+4/12^3+1/12^2+2/12^6<5`. It also checked the complete bivariate coefficient identity `3M2^2-M4=S`; the algebraic sign arguments are written and apply to ALL s in (0,1/12], not just the endpoint. No native solver, external model or new source was used.

The optional ALL-radial conclusion requires the exactly named parent MDA26 alternative, with its independent source/version and printed-proof qualifications; this note does not repair or certify those source edges. No original all-law optimizer form, priority, novelty, formal verification, independent/cross-model review or parent adoption is claimed. Priority review should verify the window signs, S monotonicity, the gap denominator constants, all-k clipped dilation and optional radial bridge.
