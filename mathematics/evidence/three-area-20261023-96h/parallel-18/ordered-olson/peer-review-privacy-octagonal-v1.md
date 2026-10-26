# Priority mathematical reconstruction — octagonal-shell privacy/MSE comparison

Observed before exclusive creation: **2026-10-23T15:00:55-0700 PDT**. Reviewer MathOlson-2, primary math-2. Parent-assigned bounded mathematical review; only this named file is written in my own root. No author/source mutation, scientific executable, finite enumeration, solver, compiler, model CLI or formal check was used.

## Exact source, baseline and verdict

Reviewed complete364-line `information-science/evidence/three-area-20261023-96h/parallel-18/privacy-diamond-mse/proof-diamond-staircase-counterexample-v1.md`, independently observed SHA256:

    d2f7771852c05edb32905b2d99c42a0403faecb42c08a16a90e8df1662d8c148

This matches the assigned pin. Read the complete same-root selection and startup, including the exact all-shift diamond model, squared-Euclidean loss, entire gamma-family definition and the distinction from same-norm results. Freshly read [Geng–Viswanath arXiv1312.0655v1](https://arxiv.org/html/1312.0655v1), SectionII constraint, SectionIII formula(14)/normalization and its final squared-Euclidean conjecture paragraph; its Theorem1 is for l1 LOSS, while the final paragraph conjectures the SAME displayed staircase family for squared-l2 loss. That is the matched comparison, not a claim against every staircase-shaped mechanism.

**No substantive mathematical defect found at the stated scope: 0 FATAL / 0 MAJOR / 0 MINOR.** The all-shift feasibility, full-tail cost formulas and strict comparison against EVERY gamma reconstruct correctly for0<b<=10^-16. This is not an unrestricted minimizer/optimality theorem. The SCDF/current-priority gate is separate; no novelty clearance is supplied.

**Endpoint clarification, not an error:** at b0=10^-16 one has epsilon0=16 ln10 EXACTLY, not with positive epsilon-margin. The hypothesis is non-strict epsilon>=16 ln10, so equality is valid. The UTILITY separation has its explicit strict positive margin. A report must not call epsilon0 strictly larger than the threshold.

## 1. Baseline reconstruction against the entire optimized gamma family

For tD, where D={|x1|+|x2|<=1}, quadrant integration gives area2t² and moment(2/3)t⁴. Indeed the x² integral in one quadrant triangle is t⁴/12, likewise y², and four quadrants give2t⁴/3.

The unnormalized staircase definition from the selection and primary SectionIII formula(14), at sensitivityDelta=1, is a.e.

    q_gamma(x)=(1-b)sum_(k>=0)b^k 1_((k+gamma)D)(x).

For a radius between successive gamma+k boundaries, the geometric tail is exactly the required level b^n. Let G have probability(1-b)b^k. Tonelli therefore gives

    Z_gamma=2 E(G+gamma)²,
    C_gamma=(1/3) E(G+gamma)⁴/E(G+gamma)².

This also matches the PRIMARY paper's explicit d=2 normalization(24): its denominator is2[gamma²+2b gamma/(1-b)+b(1+b)/(1-b)²]. Endpoint gamma0 differs from gamma1 by an unnormalized factor b a.e., so the two normalized laws agree; no gamma endpoint is lost. Since b>0, the denominator is positive even at gamma0, and cost continuity on[0,1] justifies an attained minimum, although no optimizer is required in the proof.

The listed raw geometric moments T1 through T4 follow from differentiating the geometric series before multiplying by(1-b). I independently checked the central-moment coefficients. With a=b/(1-b), v=b/(1-b)²,

    tau3=T3-3aT2+2a³=b(1+b)/(1-b)³,
    tau4=T4-4aT3+6a²T2-3a⁴=b(1+7b+b²)/(1-b)⁴.

For example the fourth central numerator combines as

    [b+11b²+11b³+b⁴]
     -4b²(1+4b+b²)+6b³(1+b)-3b⁴
      =b+7b²+b³.

Let m=gamma+a>=0. Then E(G+gamma)²=m²+v and E(G+gamma)⁴=m⁴+6m²v+4m tau3+tau4>=m⁴+b. The crucial uniform inequality is the actual identity

    z²+b-2(sqrt(b)-v)(z+v)=(z+v-sqrt(b))²+v²>=0,

valid for EVERY z>=0. Division by z+v>0, with z=m², yields C_gamma>=(2/3)(sqrt(b)-v) simultaneously for EVERY gamma. No gamma-specific surrogate or asymptotic optimizer was inserted.

For b<=10^-16, v<=2b because(1-b)²>=9/16>1/2; also2sqrt(b)<=2*10^-8<1/1000. Thus

    C_gamma>=(2/3)sqrt(b)(1-2sqrt(b))
            >=(333/500)sqrt(b)

for the ENTIRE family and hence its minimum. The lower bound need not be attained or globally sharp to refute the conjecture: a candidate upper bound BELOW this rigorously uniform lower bound already beats every gamma, including its worst minimizing gamma. This resolves the requested worst-gamma issue without a hidden tightness assumption.

## 2. All-shift privacy, including every shell corner/interface

The candidate sets are A_k=rP+kD, with r>0, convex centrally symmetric P and0∈rP. They are compact, nested and exhaust R². Hence n(x)=min{k>=0:x∈A_k} is finite and measurable, with the specified closed-set boundary convention.

For EVERY x and EVERY h∈D,

    x∈A_(n(x)) implies x+h∈A_(n(x))+D=A_(n(x)+1),

so n(x+h)<=n(x)+1. Apply the SAME inclusion at x+h and -h∈D to get n(x)<=n(x+h)+1. This proves |n(x+h)-n(x)|<=1 pointwise. The argument uses exact Minkowski inclusion, not a local normal or derivative; it therefore includes shifts that cross a vertex, change facets, touch two interfaces, or start/end exactly on a closed shell boundary. There is no omitted corner case that requires generic positions.

Since0<b<1, the index inequality gives b^(n(x))<=b^(-1)b^(n(x+h)). Once Z is shown finite/positive below, integration over every Borel E and translation of variables yields exactly mu(E)<=b^(-1)mu(E+h), for the full CONTINUOUS diamond, not just vertices or integer shifts.

The initial plateau rP is genuinely non-l1-radial: for example a point with coordinates(5r/4,0) is outside rP while(5r/8,5r/8) has the same l1 radius and lies inside it. These inequalities persist in neighborhoods, so this is not merely a boundary distinction.

## 3. Exact Minkowski shape: no unhandled clipping regime

For every k>=0 put L=k+r and c=k+r/2. The inequalities give one inclusion

    rP+kD subset {|x1|<=L,|x2|<=L, |x1|+|x2|<=k+3r/2}.

The polygon on the right has precisely the eight vertices(±L,±r/2) and(±r/2,±L). Each is a vertex of rP plus an axis vertex of kD. Convexity supplies the reverse inclusion. This validates the EXACT shell geometry for all k and every positive r, not a homothetic-octagon approximation.

The potential clipping issue is resolved by

    L-c=r/2>0.

Thus the four removed corner triangles have legs c STRICTLY smaller than L at every k, including k0 and arbitrarily large k. They never cross a coordinate axis, overlap, disappear or require a different moment regime. The facet positions are not mere translates of one fixed shell, but the stated L,c formula remains valid throughout.

Area is4L²-2c²=2k²+6rk+(7/2)r². For the upper-right removed triangle use x=L-u,y=L-v with u,v>=0,u+v<=c. The required elementary integrals are

    integral1=c²/2,
    integral(u+v)=c³/3,
    integral(u²+v²)=c⁴/6.

Its quadratic moment is L²c²-(2/3)Lc³+c⁴/6. Subtract four copies from the square's8L⁴/3 to obtain

    M(A_k)=(8/3)L⁴-4L²c²+(8/3)Lc³-(2/3)c⁴.

I hand-expanded the coefficients using

    L²c²=k⁴+3k³r+(13/4)k²r²+(3/2)kr³+r⁴/4,
    Lc³=k⁴+(5/2)k³r+(9/4)k²r²+(7/8)kr³+r⁴/8,
    c⁴=k⁴+2k³r+(3/2)k²r²+kr³/2+r⁴/16.

Together with L⁴ these give EXACTLY

    (2/3)k⁴+4rk³+8r²k²+(20/3)r³k+(47/24)r⁴.

No finite sample evaluations or interpolation were used to infer this polynomial identity.

## 4. Exact normalization and all infinite tails

Nesting gives, including the selected closed boundaries,

    b^(n(x))=(1-b)sum_(k>=0)b^k 1_(A_k)(x).

All terms and cost are nonnegative, so Tonelli is legitimate BEFORE finiteness is established. Substituting the exact polynomial area/moment and the finite geometric moments proves

    Z=(7/2)r²+6rT1+2T2>0,

and the EXACT normalized MSE

    J=[(47/24)r⁴+(20/3)r³T1+8r²T2+4rT3+(2/3)T4]
      /[(7/2)r²+6rT1+2T2].

Polynomial geometric moments are finite for0<b<1, so this proves an actual probability density, finite quadratic cost and finite first moment. Central symmetry then gives mean zero. No tail is truncated, no normalization factor(1-b) is missing, and the auxiliary geometric variable is only a summation device, not the actual output noise.

## 5. Strict upper bound and the exact parameter endpoint

For k>=1 and j<=4, k^j<=k⁴, so T_j<=T4. With b<=10^-16, the elementary estimates

    11b²+b³<=b,
    (1-b)⁴>=1-4b>0,

imply T4/b<=(1+12b)/(1-4b)<=1001/1000, because the last inequality is exactly16004b<=1. These estimates hold uniformly, not only at b0.

Drop positive denominator-tail terms, set t=b^(1/4),r=3t/4, and divide by sqrt(b)=t². I independently recover the five coefficients:

    leading(47/84)r²/t²=141/448;
    T4 term (4/21)b/(r²t²)=(64/189);
    T3 term (8/7)b/(rt²)=(32/21)t;
    T2 term (16/7)b/t²=(16/7)t²;
    T1 term (40/21)br/t²=(10/7)t³.

The last four all carry factor1001/1000. Since t<=10^-4,

    141/448<63/200,
    64/189<339/1000,
    (32/21)t+(16/7)t²+(10/7)t³<6t<=6/10000.

Thus the parenthesis is less than17/50, and

    J/sqrt(b)<63/200+(1001/1000)(17/50)
             =32767/50000<33/50.

Combining with the simultaneous baseline lower bound gives J<(33/50)sqrt(b)<(333/500)sqrt(b)<=min_gamma C_gamma. This is a strict finite inequality, not only a leading-order improvement or a comparison with Laplace/a fixed gamma.

At b0=10^-16, t0=10^-4 and r0=3/40000 exactly. Epsilon0=-ln(b0)=16 ln10 meets the NON-STRICT parameter hypothesis at equality; there is no positive epsilon-threshold margin. The strict objective gap is nevertheless greater than[(333/500)-(33/50)]10^-8=(3/500)10^-8, as stated. For b<10^-16 epsilon does have positive threshold margin, but that is not needed for the explicit endpoint example.

## 6. Prior-containment firewall and exact honest delta

The parent explicitly separates the SCDF source/priority gate. For limited containment context I read the retained primary extraction `source-soria-comas-2013-UOC.txt` at its general-shell construction/Theorem13(lines930–967) and privacy proof(lines1293–1299), not a complete novelty audit. It constructs geometric density levels on successive sensitivity-set Minkowski shells from a star-shaped initial region S0 inside the sensitivity set. Here S0=rP is convex/star-shaped and lies strictly inside D in the stated regime because max_l1(rP)=3r/2<=9/80000<1. Its cumulative expansions are exactly rP+kD; the candidate rings are their successive differences. Thus the mechanism/privacy construction is contained in that older general FAMILY at the read interface. It must not be advertised as invention of Minkowski-shell/geometric-level DP noise.

This does NOT invalidate the independently proved MSE comparison against the specific homothetic-diamond f_gamma family. The honest mathematical delta in this packet is the explicit octagonal specialization, exact all-tail area/moment normalization and strict ALL-gamma squared-Euclidean comparison. Whether even that comparison/specialization was already published, and what the prior paper's term 'optimal' proves under its own order/utility notion, remain for the separate SCDF/current-source gate. This review does not certify novelty or settle that gate.

## Scope disposition

The mathematical packet supplies a valid candidate negative answer to the FROZEN literal assertion V(epsilon)=min_gamma C_gamma for every epsilon: the displayed endpoint law alone suffices, and the proof actually gives the entire stated large-epsilon regime. It does not determine V, establish global optimality of the octagonal family, refute same-norm staircase theorems, or refute every generalized staircase mechanism. Correctness, comparison scope, mechanism containment, novelty and publication acceptance remain separate.

No author edit is requested for the checked mathematics. Preserve the endpoint-equality and prior-containment qualifications in any parent assessment. The bounded review is returned; I resume only ordered Olson, with its existing parent-directed FC/rigidity gate respected.
