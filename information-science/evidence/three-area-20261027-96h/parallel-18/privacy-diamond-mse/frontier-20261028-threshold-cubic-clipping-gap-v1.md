# Cubic onset of an actual full-D clipping improvement

**AUTHOR CANDIDATE — WRITTEN with explicitly nonrigorous Decimal diagnostics; NOT independently reviewed or parent-adopted.** Native pre-write observation: `Wed Oct 28 21:10:32 PDT 2026`.

## 1. Exact original-class claim

Let epsilon>0, b=e^(-epsilon), and let the original all-law class require pure epsilon privacy for EVERY Borel event and EVERY shift in the FULL CLOSED unit l1 diamond D. Let J=E|X|_2^2 and let P_g be the best ACTUAL centered diamond staircase. Define

    C(s)=2s^3-9s^2-108s-81,
    s_t=its unique positive root,  epsilon_t=2 asinh(sqrt(s_t)).         (1)

For eta in `[0,g/4]`, let P_(g,eta) be the ACTUAL full-D-private geometric shell with core `gD intersect {||x||_infinity<=g-eta}`. Define its finite family gain

    G_clip(epsilon)=J(P_g)-min_(0<=eta<=g/4)J(P_(g,eta)).                 (2)

The source-independent written local result is

    G_clip(epsilon)=0                 for epsilon<=epsilon_t nearby,
    G_clip(epsilon)=K_t(epsilon-epsilon_t)^3+O((epsilon-epsilon_t)^4)
                                     for epsilon>epsilon_t nearby,        (3)

where the explicitly defined K_t in (7) is strictly positive. Thus the constructive clipping gain has a cubic one-sided onset and zero first/second derivatives from the right. In particular the original all-law infimum satisfies `V_J<=J(P_g)-G_clip`; the result is a quantitative LOWER bound on the true advantage over centered staircases, not an equality or a claim that the clipped family is all-law optimal.

The cubic threshold (1) is already present in the explicitly named parent v241 `privacy-v241-separated-threshold-and-norm-gap-entire-parent-v1.md`, SHA `48274df7a84b16cd8ead4a0b9069b8359110e1b216bc72e6baea1de03e626138`; its appearance is a REPRODUCTION, not a priority claim. The proof here independently reconstructs the LOCAL algebra and does not assume the parent global phase theorem or any unreviewed author result.

**Separate conditional application:** parent MDA26 `privacy-MDA26-entire-norm-cost-and-weighted-decay-parent-v1.md`, SHA `75614a6fc5cb66d9b26f13e64e58935fe6ea52121948e7a56592b91611576ac3`, supplies equality of the actual all-radial J infimum and the centered staircase minimum via `J=(2/3)E||X||_1^2`. If that input holds, the original l1-radial-versus-all-law infimum gap is at least the cubic gain in (3). We do NOT claim the true radial gap equals that lower bound or that every norm-radial class has the same constant.

## 2. Threshold point and transverse sign

Set `m=b/(1-b)`, `v=m(m+1)=1/(4s)`, `t=1+2m=sqrt(1+4v)`, and x=g+m. The exact staircase derivative equation is

    Phi(x)=x^5+2v x^3-2vt x^2-v(1+3v)x+2v^2t=0.                       (4)

The underlying quintic in g has positive endpoints, two sign changes and is negative at `g0=sqrt(v)-m`; therefore g is its larger simple root and `Phi'_x(x)>0`. Put

    psi(x)=x^3-3vx-2vt,
    B(epsilon)=M2(g)-J(P_g)=psi(x)/(3x),
    Phi-(x^2+5v)psi=v[(12v-1)x+12vt].                                  (5)

These are elementary moment identities, not a parent source import.

At s=s_t in (10,11), `v<1/12`. Set `x_c=12vt/(1-12v)=3t/(s-3)`. Exact substitution gives

    psi(x_c)=-v t C(s)/[(1-12v)^3 s^3],
    Phi(x_c)=(x_c^2+5v)psi(x_c).                                         (6)

At the root of C, Phi(x_c)=0. The simple bounds 10<s_t<11 give `3/8<x_c<9/20`, `m<1/40`, `sqrt(v)<1/6`; hence `g_c=x_c-m in (0,1)` and x_c is the larger scalar root. Denote its values by `(v_t,t_t,x_t)` and `Phi'_t=partial_x Phi(x_t)>0`.

The two roots x_c(s), x_J(s) are locally smooth. Comparing Phi(x_c,s) to Phi(x_J,s)=0 in (6) yields

    B(epsilon)=beta_t(epsilon-epsilon_t)+O((epsilon-epsilon_t)^2),
    beta_t= v_t^2 t_t C'(s_t) sqrt[s_t(1+s_t)]
             /[3 x_t (1-12v_t)^2 s_t^3 Phi'_t] >0.                     (7)

Here `C'(s_t)=6(s_t-6)(s_t+3)>0` and `ds/depsilon=sqrt[s(1+s)]`. Every denominator is strictly positive. This establishes transversality, not merely a sign on sampled epsilons.

## 3. Exact clipping and optimization

For every 0<=eta<=g/4, the clipped core's full geometric shell is an ACTUAL private law by the closed-D triangle inequality. Its all-layer cost follows by integrating the four disjoint axis caps:

    J(P_(g,eta))-J(P_g)
      = [4eta^2/(2M2-4eta^2)]
          [-B+(4/3)x eta-(2/3)eta^2],   M2=x^2+v.                       (8)

All terms are exact, with no truncated shell or asymptotic mechanism. At B=0 the right side is strictly positive for every eta in (0,g/4]; the same holds for B<0. For B>0 it is negative at eta=B/(2x) for small B.

At epsilon_t, eta=0 is the only minimizer on [0,g/4]. Uniform positivity away from zero makes any nearby post-threshold minimizer tend to zero. Dividing the eta derivative by its factor eta, the leading stationarity equation is `-2B+4x eta+O(B eta+eta^2)=0`. The implicit function theorem gives the unique nearby minimizer

    eta_*=B/(2x)+O(B^2).

Substitution in (8) yields

    G_clip=B^3/[6 M2_t x_t^2]+O(B^4),
    K_t=beta_t^3/[6(x_t^2+v_t)x_t^2]>0,                                 (9)

which proves (3). The O constants concern this SPECIFIED finite clip family and its smooth scalar root, not all-law minimizer regularity.

## 4. Checks, limits and disclosure

A Python Decimal cell at precision 70 evaluated selected points solely as diagnostics: s_t≈10.1895934017, epsilon_t≈3.7550176381, beta_t≈0.0231491404; at delta-epsilon 0.001 and 0.0001, the computed `B/delta-epsilon` approached beta and `gain/B^3` approached `1/(6M2 x^2)`. These are NOT interval enclosures, formal proof, global-optimality checks or source novelty evidence. The identity (5) was also previously checked coefficient-by-coefficient in exact Fraction arithmetic for all formal x,v,t; that does not replace the written sign/IFT argument.

No LAW642, v241, v253, MDA, unreviewed author theorem or review verdict is imported in the local clip result (1)–(9). The already-recorded v241 threshold is named as a prior reproduction; the optional radial bridge explicitly names its separate parent premise. No source-proof repair, priority, formal or independent/cross-model review, or parent adoption is claimed. Priority review should check threshold-root identification, the beta factor in (7), the derivative/IFT coefficient 1/6, and the difference between a clipping-family gain and the true original-law gap.
