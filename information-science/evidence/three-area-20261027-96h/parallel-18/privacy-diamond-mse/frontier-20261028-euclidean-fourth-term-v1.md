# Original Euclidean DP optimum: fourth low-privacy term

**AUTHOR CANDIDATE — WRITTEN with bounded high-precision numerical diagnostics; NOT independently reviewed or parent-adopted.** Native clock before diagnostic-source pin: `Wed Oct 28 17:46:42 PDT 2026`.

## 1. All-law target and precise conditional result

Let V(epsilon) be the original infimum of `E|X|_2^2` over ALL Borel additive-noise laws on R^2 satisfying the epsilon event inequality for EVERY Borel event and EVERY shift in the FULL CLOSED l1 unit diamond D. Put

    b=e^(-epsilon),  s=b^(1/4),  R=(4/(3pi))^(1/4),
    c0=2/sqrt(3pi),  c1=8sqrt(2)/(3pi R),
    c2=8sqrt(2)/(5pi R^3 4^(2/3)).

The following is a conditional AUTHOR-WRITTEN candidate as epsilon->infinity:

    V = c0 s^2 + c1 s^3 - c2 s^(11/3) + (1+2/pi)s^4 + o(s^4).        (1)

Thus, after subtracting the nonanalytic fractional term, the coefficient of `e^(-epsilon)` is exactly `1+2/pi`. This concerns the actual all-law Euclidean optimum, not merely the explicit disk-shell trial or a squared-l1/first-norm cost. No finite-epsilon exact disk optimizer, convergence rate beyond o(s^4), source-equivalence or novelty is inferred.

This successor uses the parent-WRITTEN_SUPPORTED LAW642 original optimum/rounded stationarity and the following THREE complete own candidates, each still UNREVIEWED:

- `frontier-20261028-euclidean-low-privacy-disk-limit-v1.md`, SHA `b277d099eb211302b73754a971f63d81dc781f160a5096ad6f30db85de85d7b3`;
- `frontier-20261028-euclidean-second-term-and-disk-law-v1.md`, SHA `188cd3ff1648e9f46ac00fdc1d0068272715559143fe9ec5643a7af03740b4d4`;
- `frontier-20261028-euclidean-fractional-third-term-v1.md`, SHA `4efc24ca86ef336292f27d7130c456ff35fc84022ab05fd33a0c72f5815a50c6`.

Their own status is not upgraded here. The exact LAW source §8.4–8.5 and parent boundary are pinned in those files. A full independent review must cover all three dependencies as well as the new geometric error and coefficient cancellation below. No old held result, MDA cost theorem, v253 threshold, or publisher-source priority claim is a premise.

## 2. Stronger actual facet-depth and area expansions

Use the previous candidate's notation: S_* is the unique actual optimal core, `K=S_*/s`,

    r_b=sqrt(V-T2)/s,  a_b=sqrt(2)t/s,  delta=r_b-a_b,
    T2=m+2m^2, m=b/(1-b),

where `(t+d,t-d)` is the active rounded-arc/facet junction. The earlier proof gives

    r_b=R+r1 s+o(s),       r1=c1/(2R)=4sqrt(2)/(3pi R^2),
    d=4^(-1/3)s^(4/3)(1+o(1)),
    delta=D0 s^(2/3)(1+o(1)),    D0=4^(-2/3)/R.                        (2)

The exact R-branch stationarity is

    (4/3)d^3+2m d^2+m^2d = m/3+(3/2)m^2+m^3+t(m+m^2).                   (3)

Since t=O(s) and d=O(s^(4/3)), (3) sharpens `d^3=m/4 [1+O(s)]`, hence

    d=4^(-1/3)s^(4/3)[1+O(s)].

The exact rationalized junction formula from the third-term candidate and `d^2/t^2=O(s^(2/3))`, `m/t=O(s^3)` then give

    delta=D0 s^(2/3)+O(s^(4/3)) = D0 s^(2/3)+o(s).                     (4)

This stronger remainder matters: it permits extracting the next s^2 coefficient in the scaled objective without hiding an unknown s*delta error.

The actual K is O(s^3) in symmetric-difference area and bounded quadratic moment from the disk of radius r_b with four equal diagonal caps removed. One cap has area

    (4/3)sqrt(2r_b) delta^(3/2) [1+O(delta)].

Together with (2) and `D0^(3/2)=1/(4R^(3/2))`, the area is

    A:=|K| = A0 + A1 s + o(s),
    A0=pi R^2,        A1=2pi R r1 - 4sqrt(2)/(3R)
                         = 4sqrt(2)/(3R).                               (5)

All constants are for the ACTUAL optimal core, and its four caps are disjoint once s is small.

## 3. Core cost through scaled order s^2

Let I=integral_K |z|^2 dz. The full-disk term in `I+2/3-R^2 A` equals `(pi/2)(r_b^2-R^2)^2`. For one removed cap, write `u=r_b-n·z`. Its exact radial deficit is

    integral_cap (r_b^2-|z|^2) dz
       = (4/3) integral_0^delta (2r_b u-u^2)^(3/2)du
       = (8/15)(2r_b)^(3/2) delta^(5/2) + O(delta^(7/2)).             (6)

Replacing r_b^2 with R^2 in the cap contributes `(R^2-r_b^2)` times cap area. Using r_b=R+r1 s+o(s), delta=Theta(s^(2/3)), four caps, and (5), one obtains

    (I+2/3)/A = R^2
      + [32(2R)^(3/2)/(15 A0)] delta^(5/2)
      + [2r1^2 - 2R r1 A1/A0]s^2 + o(s^2).                            (7)

Details: the full-disk quadratic shift contributes `2r1^2 s^2`; the cap area times `(R^2-r_b^2)` contributes `-2R r1 A1/A0 s^2`; radius replacement in the leading cap term and the delta^(7/2) remainder are both o(s^2). The true-core-to-clipped-disk error O(s^3) is also o(s^2). The denominator variation against the s^(5/3) cap term is O(s^(8/3)), so does not alter (7).

## 4. Second-order tail moment without an unproved general expansion

A potential gap at this order is replacing `M(D+sK)` by a disk parallel-body expansion: a crude Hausdorff sandwich alone loses the s*delta term, which is LARGER than s^2. We pay this carefully using the actual facet support.

For small s, `a_b B subset K subset r_b B`. The right inclusion is immediate. For the left: the diamond constraint contains a_b B, while the quadratic/l-infinity constraint has margin `r_b^2-a_b^2=Theta(s^(2/3))`, much larger than its additional `2(m/s)a_b=O(s^3)` term. Moreover each of the four D-edge normals n has `h_K(n)=a_b`, because the actual facet is active.

Let L=D+s a_b B. If x belongs to `D+sK` but not L, choose its nearest point y in D. If y lies in an edge interior, the edge-normal support inequality gives `dist(x,D)<=s h_K(n)=s a_b`, contradicting x outside L. Thus y is a vertex of D. Also `dist(x,D)<=s r_b`, so the difference lies in four O(s)-radius vertex neighborhoods.

After scaling such a neighborhood by 1/s, D is its fixed vertex tangent cone on the bounded region in question. The two compared convex sets there are `(cone+K)` and `(cone+a_b B)`. Because `a_b B subset K subset a_b B+delta B`, their nested difference inside a fixed bounded disk has area O(delta): use the standard planar outer-parallel area bound for a compact convex set, with perimeter bounded by the fixed disk. Scaling back yields O(s^2 delta) area, and the integrand |x|^2 is uniformly bounded. Hence

    M(D+sK)=M(D+s a_b B)+O(s^2 delta)
            =2/3+(8sqrt(2)/3)s a_b+(4+pi)R^2 s^2+o(s^2).             (8)

The last identity uses the exact Euclidean parallel-diamond formula of the preceding candidate, a_b->R, and delta->0. This is NOT an appeal to a second derivative for arbitrary convex bodies. The enclosing-k>=2 tail contributes only O(s^4) after numerator scaling.

## 5. Complete s^2 coefficient and cancellation

The normalized shell layer identity yields, uniformly for the actual K,

    V/s^2 = [I+M(D+sK)]/[A+s^2 |D+sK|+O(s^6)] + O(s^4).              (9)

Here `|D+sK|=2+o(1)` and (5) gives the area expansion. Use (4), `a_b=r_b-delta`, (7)–(8), and denote `E=8sqrt(2)/3`. The two fractional terms in V/s^2 are exactly the previous third-term expression and combine to `-c2 s^(5/3)`. All errors in delta of order s^(4/3), in cap expansions of order delta^(7/2), and in the vertex comparison O(s^2 delta) are o(s^2).

The remaining s^2 coefficient in V/s^2 is

    2r1^2 - 2R r1 A1/A0        [core]
    + E r1/A0 - E R A1/A0^2    [tail first variation / area]
    + (4+pi)R^2/A0 - 2R^2/A0  [tail second variation / normalization]. (10)

Because `2R A1=E`, the second and third terms cancel. Because `r1=E/(2A0)` and `A1=E/(2R)`, the first and fourth terms also cancel. Since `A0=pi R^2`, (10) reduces EXACTLY to

    (4+pi)/pi - 2/pi = 1+2/pi.

Multiplying the expansion of V/s^2 by s^2 proves the candidate (1). Importantly, the o(s^4) remainder relies on the refined actual-facet estimate (4), not merely on the older `delta=D0 s^(2/3)(1+o(1))`.

## 6. Bounded numerical diagnostic and precision disclosure

A reproducible LOCAL diagnostic script `frontier-20261028-rounded-asymptotic-decimal-diagnostic-v1.py`, SHA `5684fdb4113c406e3c1ac41caf10a90ce9735eb1a891f285d119dc283baf4c47`, 100 LF / 3331 bytes, numerically solves the source's R-branch scalar equation H_R=0 by 160 bisections at 110 Decimal digits. It checks the rounded screens, uses an arctan series for arcsin, and prints scaled residuals. Command actually executed:

```sh
python3 -B information-science/evidence/three-area-20261027-96h/parallel-18/privacy-diamond-mse/frontier-20261028-rounded-asymptotic-decimal-diagnostic-v1.py
```

Observed values (not interval enclosures):

| s | scaled facet depth | `(V-c0*s^2-c1*s^3+c2*s^(11/3))/s^4` | rounded/sign screens |
|---:|---:|---:|---|
| 1e-6 | 0.491691482137 | 1.635405832977 | PASS |
| 1e-7 | 0.491679732160 | 1.636064136123 | PASS |
| 1e-8 | 0.491677200846 | 1.636363542125 | PASS |
| 1e-9 | 0.491676655498 | 1.636501200065 | PASS |
| predicted limit | 0.491676505742 | 1.636619772368 | — |

An earlier 70-digit, 120-bisection exploratory run produced fourth-scaled 1.638377523 at s=1e-8, visibly inconsistent with the 110-digit rerun's 1.636363542125. This is disclosed as a numerical-precision/bracketing sensitivity, not averaged away or treated as proof; the error's exact origin was not isolated. The 110-digit samples are consistent with, but do not certify, (1). The proof is the conditional written argument above; no floating result substitutes for its uniform error analysis.

## 7. Exact assurance boundary

This is an author candidate depending on the named LAW642 rounded stationarity and all three unreviewed predecessor steps. In particular, (8)'s vertex-neighborhood comparison, the O(s^(4/3)) facet-depth remainder, the cap/moment errors, and cancellation (10) need complete disjoint review. A numerical branch root, sampled sign bracket, successful code execution or matching coefficient is not formal proof, parent acceptance or novelty. All original held histories remain historical and are not used as premises.
