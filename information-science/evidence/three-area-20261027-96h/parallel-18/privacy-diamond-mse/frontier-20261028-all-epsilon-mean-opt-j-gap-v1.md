# Every first-norm optimizer has a positive squared-Euclidean gap

**AUTHOR CANDIDATE — WRITTEN plus exact polynomial coefficient controls; NOT independently reviewed or parent-adopted.** Native pre-write observation: `Wed Oct 28 21:39:42 PDT 2026`.

## 1. Exact original model, named premises and claim

Fix ANY finite epsilon>0. Let F be ALL Borel additive-noise laws satisfying pure epsilon privacy for EVERY Borel event and EVERY shift in the FULL CLOSED unit l1 diamond D. Define

    V_J=inf_(mu in F) E_mu |X|_2^2,
    V_L=inf_(mu in F) E_mu ||X||_1,
    Opt_L={mu in F:E_mu ||X||_1=V_L}.

The written conclusion is

    inf_(mu in Opt_L) E_mu |X|_2^2 - V_J >0       for EVERY epsilon>0.    (1)

In particular no actual L-optimal law can also be a J optimizer, and this is a STRICT INFIMUM gap, not merely a pointwise exclusion. No numeric or uniform-in-epsilon lower gap is asserted.

This original-model result is CONDITIONAL on THREE SEPARATE named parent-WRITTEN_SUPPORTED inputs:

* LAW642 `privacy-all-law-self-contained-parent-v1.md`, SHA `c08f6353f121ef9e35da0e9d5e8ec9c87b0da838be0d1adf38b807010a1cd979`: unique attained original all-law J optimizer and its shell law.
* The separated v241 phase result `privacy-v241-separated-threshold-and-norm-gap-entire-parent-v1.md`, SHA `48274df7a84b16cd8ead4a0b9069b8359110e1b216bc72e6baea1de03e626138`: the J-optimal core is a diamond up to the threshold and genuinely rounded/non-diamond above it. This is the ADOPTED separated derivation, NOT the held original threshold manuscript.
* The parent MDA26 matching-norm alternative `privacy-MDA26-entire-norm-cost-and-weighted-decay-parent-v1.md`, SHA `75614a6fc5cb66d9b26f13e64e58935fe6ea52121948e7a56592b91611576ac3`: an actual full-D-private centered staircase attains V_L, and the same-law level-set radial rearrangement is full-D private. Its source/version/printed-proof qualifications remain intact.

The fresh scalar algebra below is rederived, not imported from an unreviewed author theorem. Equation (1) concerns exactly this additive/full-D model and these two costs; it is NOT a publication-wide source non-equivalence, priority, novelty or source-proof-repair claim.

## 2. Diamond phase: exact selector separation

Put b=e^(-epsilon), m=b/(1-b), v=m(m+1), t=1+2m and x=g+m. For an actual centered staircase P_g, exact geometric moments give `L=2M3/(3M2)` and `J=M4/(3M2)`. The derivative sign polynomials, in x, are

    Q=x^4-2vt x+3v^2,
    P=x^5+2v x^3-2vt x^2-v(1+3v)x+2v^2t.                            (2)

At g=0,1 each is positive. Each original-g polynomial has exactly two coefficient sign changes; at `g0=sqrt(v)-m in (0,1)`,

    Q(g0)=2v^(3/2)(2sqrt(v)-t)<0,   P(g0)=-v sqrt(v)<0.

Hence each has exactly two simple positive roots in (0,1); let g_L and g_J be their respective larger roots. Since P_0=P_1 as laws, they uniquely minimize their respective scalar staircase costs. In particular `x_L=g_L+m>sqrt(v)`.

The following exact identities show g_L<g_J. Let

    R=2x^3-(1+6v)x+2vt,      P=xQ+vR.

At Q=0, `2vt=(x^4+3v^2)/x`, so `R=[3(x^2-v)^2-x^2]/x`. Write `z=x^2/v>1`. Squaring the root equation and using `t^2=4v+1` gives

    1/v=[(z^2+3)^2-16z]/(4z),
    1/v-3(z-1)^2/z=(z-1)^3(z+3)/(4z)>0.                               (3)

Thus R<0 and P(g_L)<0; g_L lies strictly before P's larger root g_J. Q is positive between g_L and 1, so `L(P_gJ)>L(P_gL)>=V_L`. In the parent v241 diamond phase, LAW642 identifies P_gJ with the unique actual J-optimal law P_*. This covers the equality threshold as well.

## 3. Rounded phase: strict rearrangement, not a radiality assumption

Above the parent threshold, LAW642/v241 say the UNIQUE original J law has density `p=Z^(-1)b^(n_S)` with S genuinely non-diamond and a positive-length curved arc. In particular S has positive area and differs in positive measure from every equal-area l1 diamond. For ALL amplitude thresholds `u in (b/Z,1/Z)`, its strict superlevel set is S up to a null boundary.

The named MDA rearrangement bridge replaces each superlevel by its equal-area l1 diamond, giving an ACTUAL full-D-private law p^sharp of the same mass. The elementary strict bathtub inequality for the strictly increasing radial cost r=||x||_1 gives

    integral_S r dx > integral_(equal-area diamond) r dx.

For every other amplitude level the corresponding inequality is nonnegative. Integrate over u by Tonelli; the displayed strict difference occurs throughout the positive-length interval `(b/Z,1/Z)`. Thus

    L(P_*) > L(p^sharp) >= V_L.                                          (4)

No assumption that an arbitrary L optimizer is radial, unique or has a particular source version is needed. The MDA premise supplies feasibility of the rearranged law; strictness is the separate written equality argument above.

Combining §§2–3 establishes `L(P_*)>V_L` for EVERY finite epsilon.

## 4. From exclusion to a strictly positive infimum gap

MDA's per-cost theorem supplies an ACTUAL L-optimal staircase with finite J, so Opt_L is nonempty and the infimum of J over it is finite. Take a minimizing sequence inside Opt_L with bounded J. It is tight by Markov; weak subsequential limits preserve all full-D event inequalities by nonnegative continuous tests. Lower semicontinuity gives `L(mu)<=V_L`, and feasibility forces equality, so the limit remains in Opt_L. J is lower semicontinuous, hence the restricted infimum is attained.

If that infimum equaled V_J, its attainer would be the UNIQUE LAW642 J-optimal law P_*, contradicting (4) or §2. Thus (1) is strictly positive. This compactness step is essential: nonmembership of P_* alone would not establish a positive infimum gap.

## 5. Actual checks and status

Python-kernel exact `fractions.Fraction` sparse-polynomial arithmetic checked the all-variable identity `P=xQ+vR` and the coefficient factor `(z^2+3)^2-16z-12(z-1)^2=(z-1)^3(z+3)`. These checks do NOT independently verify the parent theorems, strict rearrangement or compactness argument. No source publication, held manuscript, numerical root, formal proof, novelty, cross-model/human review or parent adoption is claimed. Priority review should check the root sign ordering, positivity of the strict level-set gap, actual feasibility of p^sharp from the NAMED MDA parent, and weak-closure/attainment of Opt_L.
