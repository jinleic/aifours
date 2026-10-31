# Exact finite-epsilon threshold for clipping the best diamond staircase

**AUTHOR CANDIDATE — WRITTEN plus exact symbolic and rational checks; NOT independently reviewed or parent-adopted.** Native pre-write observation: `Wed Oct 28 21:06:57 PDT 2026`.

## 1. Exact model and claimed sharp deformation threshold

Fix ANY finite epsilon>0 and b=e^(-epsilon). The original class contains ALL Borel additive-noise laws satisfying epsilon privacy for EVERY Borel event and EVERY shift in the FULL CLOSED unit l1 diamond D; the registered objective is `J=E|X|_2^2`.

Let g be the best actual centered diamond-staircase offset, uniquely determined in §2. Define

    s=sinh^2(epsilon/2)=(1-b)^2/(4b),
    C(s)=2s^3-9s^2-108s-81,
    s_t=the UNIQUE positive root of C,   epsilon_t=2 asinh(sqrt(s_t)).  (1)

For `0<eta<g/2`, let P_(g,eta) be the ACTUAL full-D-private shell law with clipped core

    K_(g,eta)=gD intersect {||x||_infinity<=g-eta}.                       (2)

The source-independent written claims are:

* If `epsilon>epsilon_t`, there is an explicitly specified eta>0 such that `J(P_(g,eta))<min_(0<=gamma<=1)J(P_gamma)`. In particular no centered diamond staircase can be an original all-law J optimizer.
* If `epsilon<=epsilon_t`, EVERY clip in exactly the family (2), with `0<eta<g/2`, has `J(P_(g,eta))>J(P_g)`. This is a statement about this particular clipping family only; it is NOT a proof that P_g is globally optimal in that regime.

The first claim is a concrete all-event/full-D feasible counterexample throughout an exact continuous finite-epsilon interval; it does NOT assert P_(g,eta) is the all-law optimum. The same cubic threshold is already recorded in parent v241 `privacy-v241-separated-threshold-and-norm-gap-entire-parent-v1.md`, SHA-256 `48274df7a84b16cd8ead4a0b9069b8359110e1b216bc72e6baea1de03e626138`. Thus the threshold is explicitly a REPRODUCTION/consequence at this narrower deformation scope, not a novelty or priority claim; the parent theorem is not a premise of the proof below.

**Separate conditional radial bridge:** parent MDA26 `privacy-MDA26-entire-norm-cost-and-weighted-decay-parent-v1.md`, SHA-256 `75614a6fc5cb66d9b26f13e64e58935fe6ea52121948e7a56592b91611576ac3`, states that the same full-D class's matching-norm `W=E||X||_1^2` optimum is attained by a centered diamond staircase. Every l1-radial density has J=(2/3)W. IF this named parent result holds, the first claim upgrades to P_(g,eta) beating EVERY l1-radial private law, and every original J optimizer, if one exists, is nonradial. This optional bridge is NOT part of the standalone threshold proof and does not repair a printed source proof.

## 2. Scalar family and two roots

Put `m=b/(1-b)`, `v=m(m+1)`, `t=1+2m=sqrt(1+4v)`, and let N have geometric law `(1-b)b^k`. For a centered staircase P_gamma,

    M_j(gamma)=E(gamma+N)^j,    J(P_gamma)=M4/(3M2).

Its derivative has the sign of

    P_m(gamma)=gamma^5+5m gamma^4+(2m+12m^2)gamma^3
       +(12m^3-2m)gamma^2-m(1+2m)(1+6m)gamma+m^2(1+2m).                (3)

It has exactly two coefficient sign changes, positive endpoints P_m(0),P_m(1), and is negative at `gamma0=sqrt(v)-m in (0,1)` as shown below. Descartes and IVT therefore give exactly two simple positive roots, the larger g in (gamma0,1); normalized P_0=P_1, so this is the UNIQUE global scalar-family minimum.

Let x=gamma+m. The exact identities

    M1=x,  M2=x^2+v,  M3=x^3+3vx+vt,
    M4=x^4+6v x^2+4vt x+v(1+9v)

show the stationary polynomial in x is

    Phi(x)=x^5+2v x^3-2vt x^2-v(1+3v)x+2v^2 t.                         (4)

At x=sqrt(v), direct substitution gives `Phi=-v sqrt(v)<0`, establishing the sign used above.

## 3. Exact sign elimination and the cubic

At the larger root x_J=g+m, the derivative equation is `2M3 M2=M4 M1`. Define the actual clipped-cost sign scalar

    B=M2(g)-J(P_g)=[x_J^3-3v x_J-2vt]/(3x_J).

Write `psi(x)=x^3-3vx-2vt`. Direct expansion gives the EXACT polynomial identity

    Phi(x)-(x^2+5v)psi(x)=v[(12v-1)x+12vt].                            (5)

At x=x_J,

    sign B = sign[(1-12v)x_J-12vt].                                      (6)

C(s) has exactly one positive root by Descartes; C(10)=-61 and C(11)=304, so `10<s_t<11` and C is negative below s_t and positive above it.

If v>=1/12 then (6) is negative and s=1/(4v)<=3<s_t, so B<0. If v<1/12 define `x_c=12vt/(1-12v)>0`. Exact substitution and t^2=1+4v give

    psi(x_c)=-v t C(s)/[(1-12v)^3 s^3],
    Phi(x_c)=(x_c^2+5v)psi(x_c).                                         (7)

If x_c<=sqrt(v), then x_J>sqrt(v)>=x_c, while psi(x_c)<0, so B>0 and (7) makes C(s)>0. If x_c>sqrt(v), it lies to the right of the smaller positive root; the sign of `x_J-x_c` is the negative of sign Phi(x_c), which is the sign of C(s) by (7). Therefore in ALL cases

    sign B = sign C(s), including B=0 exactly at s=s_t.                   (8)

This is an exact all-parameter elimination, not a numerical phase guess.

## 4. Actual clipping and the direction on BOTH sides

For eta in (0,g/2), the full closed-D triangle inequality makes the geometric shell P_(g,eta) an ACTUAL private law. Exact cap geometry gives, for every k>=0,

    K_(g,eta)+kD=(g+k)D intersect {||x||_infinity<=g+k-eta}.

Indeed reduce positive-quadrant coordinates to at most g-eta with l1 cost <=k, then reduce their sum to g if necessary; eta<g/2 and the two outer inequalities bound the total. The four removed caps of height eta have area eta^2 and squared moment `R^2 eta^2-(4/3)R eta^3+(2/3)eta^4` each at R=g+k. Summing ALL geometric layers yields

    J(P_(g,eta))-J(P_g)
       =[4eta^2/Z_eta][-B+(4/3)M1(g)eta-(2/3)eta^2],
    Z_eta=2M2(g)-4eta^2>0.                                                (9)

If C(s)>0, B>0; choose explicitly

    eta=min{g/4, 3B/[8M1(g)]}>0.

Then `(4/3)M1 eta<=B/2`, so (9) is strictly negative and the actual full-private law beats every P_gamma. If C(s)<=0, B<=0; because eta<g/2 and M1(g)=g+m>g, the expression `(4/3)M1 eta-(2/3)eta^2` is strictly positive, so EVERY admissible nonzero eta gives strictly positive cost difference. This establishes both claimed directions without equating the family with the all-law optimum.

As elementary exact examples, at epsilon=ln 32 one has `s=961/128<10<s_t`, so every such clip worsens J; at epsilon=ln 64 one has `s=3969/256>11>s_t`, so the explicit clipped construction strictly improves every centered staircase. These examples use no decimal threshold value.

## 5. Checks, source boundaries and status

The Python eval kernel used exact `fractions.Fraction` sparse-polynomial arithmetic to check the FULL three-variable identity (5), and exact rational bisection/sign arithmetic for C(10)=-61, C(11)=304 and its positive-root enclosure. A floating rendering of the latter was about 10.1895934; it is diagnostic only. The checked polynomial identity does not itself verify the all-law privacy proof, signs or source theorem.

The cubic was already in the specifically named v241 parent result, and its occurrence here is explicitly a reproduction at the narrower clipping scope. No new literature search, priority claim, source-proof repair, formal verification, independent/cross-model review or parent adoption occurred. Parent MDA26 is used ONLY for the separately conditional all-radial bridge. Disjoint review should examine (7)'s sign, the x_c<=sqrt(v) case, strict direction of (9), all-k dilation and source/registered-target distinction.
