# Original Euclidean optimum: second low-privacy term and exact disk-shell law

**AUTHOR CANDIDATE — WRITTEN with exact rational geometric controls; NOT independently reviewed or parent-adopted.** Native pre-write observation `Wed Oct 28 17:33:15 PDT 2026`.

## 1. Target, exact new assertions, and scope

For finite epsilon>0 let `b=e^(-epsilon)`, `D={h:||h||_1<=1}` and F_epsilon be ALL Borel probability laws satisfying the original privacy inequality for EVERY Borel event and EVERY shift in the FULL CLOSED D. Define the original all-law squared-Euclidean value

    V=inf_(mu in F_epsilon) integral |x|_2^2 mu(dx).

Let `s=b^(1/4)` and `R0=(4/(3pi))^(1/4)`. The new second-order candidate as b->0 is

    V = [2/sqrt(3pi)] s^2 + [8sqrt(2)/(3pi R0)] s^3 + o(s^3).          (1)

Equivalently, the first two terms scale as `e^(-epsilon/2)` and `e^(-3epsilon/4)`. The sign of the second coefficient is positive. This is for the ACTUAL original all-law value, not just the disk-shell trial, a selected radial family, or the source's first-power norm objective.

The same note gives an exact genuinely admissible Euclidean-disk-core/l1-shell law with a closed finite-epsilon normalizer and squared-Euclidean cost for EVERY t>0, epsilon>0, and proves that the explicit choice `t=R0 s` achieves the first TWO terms of (1). In particular, its cost minus V is `o(s^3)`; this is not a claim that the trial law is the exact finite-epsilon optimizer.

For the centered D-radial restricted value V_rad, the separately imported matching-norm/averaging results also imply

    V_rad = (2/3)s^2 + (4/3)s^3 + o(s^3),
    V_rad-V = (2/3-2/sqrt(3pi))s^2
              +(4/3-8sqrt(2)/(3pi R0))s^3 + o(s^3).                    (2)

This is a two-term CENTERED DIAMOND-radial gap only. It does not claim the same gap for the union of all translated norm-radial families. No finite-epsilon global selector, source equivalence, priority or novelty conclusion is asserted.

## 2. Named input, prior candidate, and what is reused

The named research input is the parent-WRITTEN_SUPPORTED LAW642 original all-law unique optimizer/core theorem, `institute/runs/three-area-2026-10-23-96h/privacy-all-law-self-contained-parent-v1.md`, SHA `c08f6353f121ef9e35da0e9d5e8ec9c87b0da838be0d1adf38b807010a1cd979`. It yields the actual convex compact positive-area core S_*, containing 0 in its interior, and the exact original privacy density `p_*=Z^(-1)b^(n_S)`, `n_S=min{k:x in S+kD}`.

The preceding own **UNREVIEWED** candidate `frontier-20261028-euclidean-low-privacy-disk-limit-v1.md`, SHA `b277d099eb211302b73754a971f63d81dc781f160a5096ad6f30db85de85d7b3`, proves from that input:

- with s=b^(1/4), `K_b:=S_*/s` is uniformly bounded and has area bounded above and below away from zero;
- `|K_b triangle B_2(0,R0)| -> 0` and `V/s^2 -> 2/sqrt(3pi)`;
- the shell normalizer/cost have the nonnegative layer representation recalled below.

The previous candidate remains an explicit named UNREVIEWED dependency here; nothing is presented as accepted merely by its hash. For ease of review, its leading area/moment mechanism is recapped in §4. An independent reviewer must read/reconstruct its full proof or mark this successor conditional. No v241 threshold, v253, original held diagnostic, numerical root or other old result is used in (1).

For (2) only, import the separately parent-supported MDA matching-norm per-cost staircase attainment and the centered angular identity `V_rad=(2/3) W`, as pinned in the previous candidate. I rederive the two-term radial VALUE via a simple scalar envelope in §6, not by claiming that the publisher's first-norm theorem asserts squared-Euclidean optimality.

## 3. Exact Euclidean parallel-diamond moments

Let B be the unit Euclidean disk. For a nonnegative radius a define `M(A)=integral_A |x|_2^2 dx`. A diamond edge joining (1,0) to (0,1) is `y(u)=(u,1-u)`, 0<=u<=1, with outward unit normal `(1,1)/sqrt(2)` and arc element sqrt(2)du. Thus

    integral_edge |y|^2 ds = sqrt(2) integral_0^1 [u^2+(1-u)^2]du
                           = 2sqrt(2)/3,
    integral_(partial D) |y|^2 ds = 8sqrt(2)/3.                          (3)

The outward normal strips over the four edges and the four vertex sectors partition D+aB up to null boundaries. Integrating |y+vn|^2 in the strips and then each vertex polar sector gives the exact finite-a identities

    |D+aB| = 2 + 4sqrt(2)a + pi a^2,
    M(D+aB) = 2/3 + (8sqrt(2)/3)a + (4+pi)a^2
                    + 4sqrt(2)a^3 + (pi/2)a^4.                          (4)

Details: each strip contributes `(2sqrt(2)/3)a+a^2+(sqrt(2)/3)a^3`; each right-angle vertex sector contributes `(pi/4)a^2+(2sqrt(2)/3)a^3+(pi/8)a^4`. Their sum plus M(D)=2/3 is (4). Thus the first-variation formula follows without assuming smoothness of the diamond.

Scaling extends (4) to every integer k>=0:

    |kD+tB| = 2k^2 + 4sqrt(2)kt + pi t^2,
    M(kD+tB) = (2/3)k^4 + (8sqrt(2)/3)k^3 t
                 +(4+pi)k^2 t^2 + 4sqrt(2)k t^3 +(pi/2)t^4.           (5)

At k=0 these are the actual disk's area and moment. The formulas can be checked either by direct scale for k>0 or the k=0 disk integral.

## 4. Exact feasible disk-shell law and actual first-order core limit

Fix arbitrary epsilon>0 and t>0. Let `n_t(x)=min{k>=0:x in tB+kD}` and define the normalized density `p_t=Z_t^(-1)b^(n_t)`. The pointwise inequality `n_t(x+h)<=n_t(x)+1` for every h in D, with the reverse obtained from −h, proves that p_t is a genuine ALL-event/FULL-CLOSED-D feasible law. This is not a pointwise-only privacy surrogate.

Put `m=b/(1-b)` and geometric raw moments

    T2=m+2m^2,  T3=m+6m^2+6m^3,  T4=m+14m^2+36m^3+24m^4.

Using `(1-b) sum b^k 1_(tB+kD)=b^(n_t)` and (5), its EXACT normalizer and squared-Euclidean numerator are

    Z_t = pi t^2 + 4sqrt(2)m t + 2T2,
    N_t = (pi/2)t^4 + 4sqrt(2)m t^3 +(4+pi)T2 t^2
           +(8sqrt(2)/3)T3 t +(2/3)T4.                                  (6)

Therefore `J(p_t)=N_t/Z_t` for every finite epsilon,t>0. With t=R0 s, direct expansion gives

    J(p_(R0s)) = [2/sqrt(3pi)]s^2
                  +[8sqrt(2)/(3pi R0)]s^3 + O(s^4).                     (7)

This is an explicit actual upper law with a written exact closed formula.

For the actual optimizer S_*, the prior candidate obtains its scaled disk limit by: (i) the above disk gives V=O(s^2); (ii) the LAW642 core is in a ball of radius sqrt(V), while the k=1 shell forces |S_*|=Theta(s^2); (iii) the fixed-area moment inequality `I(S)>=|S|^2/(2pi)` and the unique minimizer of `A/(2pi)+2/(3A)` force the scaled-area and moment deficit to their disk values; (iv) a band estimate turns moment deficit into symmetric-difference convergence. Those are statements ABOUT THE ACTUAL OPTIMIZER, not merely a stationary trial. The full earlier proof, including all uniform errors, remains the named review dependency.

## 5. Hausdorff upgrading and the exact second term

Each K_b=S_*/s is compact convex: the LAW642 core is an intersection of convex l1 and convex quadratic-plus-linfinity sublevel sets. It lies in one fixed large disk and converges in symmetric-difference area to the disk B_(R0), by the preceding candidate.

I use the standard Blaschke compactness theorem for bounded nonempty compact convex sets. Every sequence has a Hausdorff-convergent subsequence with convex limit K. Hausdorff convergence of compact convex sets implies pointwise indicator convergence off the null boundary of K: points outside K are eventually outside, while support-function convergence puts every fixed interior point eventually inside. Bounded convergence therefore identifies the limit indicator with that of B_(R0) almost everywhere, using the previously proved symmetric-difference convergence. The disk has positive area, so K is full-dimensional; two closed full-dimensional convex bodies equal a.e. are equal as sets, since any strict disagreement yields a separating halfspace with a positive-area cap. Hence every Hausdorff subsequential limit is B_(R0), so the entire K_b converges in Hausdorff distance. Equivalently, by support functions, for every fixed eta in (0,R0) and sufficiently small b,

    (R0-eta)B subset K_b subset (R0+eta)B.                               (8)

All support functions/disk inclusions concern the ACTUAL scaled core, not a chosen surrogate.

By monotonicity of M and (4), (8) implies the exact one-sided limit

    [M(D+s K_b)-M(D)]/s -> (8sqrt(2)/3) R0.                             (9)

The bound is obtained by sandwiching between `D+s(R0±eta)B`, taking s->0 and then eta->0; no general differentiability theorem for an unknown core family is assumed.

Let A_b=|K_b| and I_b=M(K_b). They are uniformly bounded, A_b is bounded below, and `A_b->pi R0^2`. Since b=s^4 and S_*=sK_b, the exact shell-layer sums and the uniform `k>=2` tail bound give

    V/s^2 = [I_b + M(D+sK_b)]/A_b + O(s^2)
          = F0(K_b) + s [(M(D+sK_b)-M(D))/(s A_b)] + O(s^2),            (10)
    F0(K)=(M(K)+2/3)/|K|.

The O(s^2) is uniform for these K_b because their area is bounded away from 0, their diameter is bounded, and the denominator's k=1 term is O(s^2) after division by s^2. The k>=2 terms are O(s^8) before the numerator/denominator rescalings.

The same equal-area Euclidean bathtub argument as in the preceding candidate gives for every measurable positive-area K

    F0(K)>=2/sqrt(3pi),

with equality only for the disk B_(R0) up to null sets. From (9) and A_b->pi R0^2, the bracket in (10) tends to `8sqrt(2)/(3pi R0)`. The actual lower bound is therefore

    V/s^2 >= 2/sqrt(3pi) + s[8sqrt(2)/(3pi R0)] + o(s).

The ACTUAL disk-shell upper law (7) supplies the reverse bound through O(s^2). Together these prove (1) and `J(p_(R0s))-V=o(s^3)`. No assertion that the core is exactly a disk for any finite b, nor any unjustified interchange of a global minimum with a first derivative, is used.

## 6. Two-term centered radial value

MDA's per-cost input identifies W=inf E||X||_1^2 with the minimum over actual centered D-staircases of offset gamma in [0,1]. Its scalar value is `N/(2D0)` with

    D0=gamma^2+2m gamma+m+2m^2,
    N=gamma^4+4m gamma^3+6(m+2m^2)gamma^2
      +4(m+6m^2+6m^3)gamma+m+14m^2+36m^3+24m^4.

Writing b=s^4 and gamma=s z, a trial z=1 and the positive lower bound from §7 of the preceding candidate show that EVERY scalar minimizing z lies in a compact positive interval and z->1. Uniform expansion on that interval is

    W(Q_(sz))/s^2 = (z^2+z^(-2))/2 + 2s/z + O(s^2).                    (11)

The first term is >=1 with unique equality at z=1. Thus the trial gives `W/s^2<=1+2s+O(s^2)` while the minimizing z->1 gives `W/s^2>=1+2s+o(s)`. Therefore `W=s^2+2s^3+o(s^3)`. The named parent angular identity then gives V_rad=(2/3)W and (2). This argument does not use a symbolic root, an unreviewed squared-l1 uniqueness theorem, or any original Euclidean equality with a radial law above the threshold.

## 7. Actual bounded geometric arithmetic

The following local Python Eval cell used only exact `fractions.Fraction`; it checked the edge polynomial integral, the four-edge coefficient, and selected geometric moments without floating-point fitting:

```python
from fractions import Fraction as F
edge_integral=F(1)-F(2,2)+F(2,3)
print('exact integral_0^1(u^2+(1-u)^2)du=',edge_integral)
print('four-edge first-variation coefficient of t*sqrt(2)=',4*edge_integral)
b=F(1,3); m=b/(1-b)
T2=m+2*m*m; T3=m+6*m*m+6*m**3; T4=m+14*m*m+36*m**3+24*m**4
print('for b=1/3 exact geometric moments T2,T3,T4=',T2,T3,T4)
print('disk-core area and second-moment formulas include constants 2,2/3 and edge coefficient 8/3*sqrt(2)')
```

Actual output:

```text
exact integral_0^1(u^2+(1-u)^2)du= 2/3
four-edge first-variation coefficient of t*sqrt(2)= 8/3
for b=1/3 exact geometric moments T2,T3,T4= 1 11/4 10
disk-core area and second-moment formulas include constants 2,2/3 and edge coefficient 8/3*sqrt(2)
```

The final line is a human-readable label, not a machine proof of (4)–(6). The integral and geometric-moment arithmetic alone were machine checked; shell validity, compactness, Hausdorff upgrading, actual-minimizer envelope and asymptotic remainder are WRITTEN. This is not a numerical fit, independent review, or formal verification.

## 8. Residual and review request

The conclusion is conditional on the exact named LAW642 and previous author's disk-limit candidate; neither is certified by this file. The small-o remainder is deliberately not strengthened to O(s^4) for the actual optimum. Other norms, nonadditive/data-dependent channels, eps=0/infinity as actual admissible endpoints, source equivalence/priority and global novelty remain out of scope. Request disjoint full review of (4)–(6), area-to-Hausdorff inference, uniform denominator/tail errors, actual-minimum envelope and named input scopes before adoption; no old held outcome is accepted as a premise.
