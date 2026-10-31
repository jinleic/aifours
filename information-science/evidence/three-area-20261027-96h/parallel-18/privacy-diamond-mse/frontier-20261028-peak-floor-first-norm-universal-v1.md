# Source-independent first-norm optimum and law scaling at low privacy

**AUTHOR CANDIDATE — WRITTEN, with a bounded Decimal diagnostic; NOT independently reviewed or parent-adopted.** Native pre-write clock: `Wed Oct 28 18:53:52 PDT 2026`.

## 1. Exact model and new first-moment result

For finite epsilon>0 put b=e^(-epsilon), D the FULL CLOSED unit l1 diamond, and let F_b contain ALL Borel laws satisfying the epsilon event inequality for EVERY Borel event and EVERY shift in D. Let

    L_*(b)=inf_(mu in F_b) E_mu ||X||_1,      C=2^(1/3),    y0=2^(-5/3).

The candidate source-independent conclusions as b->0 are:

1. An explicit all-b lower bound holds for EVERY feasible original law:

       E_mu||X||_1 >= C b^(1/3) - 2 b^(2/3).                             (1)

   A genuinely private shell law matches it to that order, so `L_*(b)=C b^(1/3)+O(b^(2/3))`.
2. For ANY b_n->0 and ANY actual feasible laws with mean cost `<=C b_n^(1/3)+o(b_n^(1/3))`,

       Law(b_n^(-1/3) X_n) -> Uniform(C D)  in TOTAL VARIATION.           (2)

   No existence/uniqueness/radiality/parameterized-family assumption is made of the laws.
3. For ANY such sequence and EVERY fixed r>0, its density obeys

       integral_(|x|_2>r) |p_n(x)/b_n^(1/3)-y0 1_D(x)| dx ->0.          (3)

   Its scaled cost measures satisfy

       [||x||_1/b_n^(1/3)]mu_n(dx)
          => (2C/3) delta_0 + y0 ||x||_1 1_D(x)dx.                       (4)

   The two terms have total masses 2C/3 and C/3. Consequently the scaled TV convergence in (2) is NOT W1 convergence: the limiting uniform law's mean cost is 2C/3 while the actual scaled means tend to C.

These statements concern FIRST-power l1 cost. The PMLR publisher's theoretical objective is first-power l1, but this is an independently written asymptotic argument, not attribution of an as-printed proof or a priority/novelty claim.

## 2. Inputs, model caveat and exact geometry

The proof uses NO named research theorem, LAW642, MDA, PMLR, v241, f68 or earlier unreviewed result. Standard inputs are RN/Lebesgue differentiation, Tonelli, elementary l1-diamond geometry, Riemann integral inequalities and layer cake. Each feasible law has a bounded all-point private density representative by integrating over D and taking shrinking-ball limsups; no common exception set for uncountably many shifts is assumed.

For the radius-r diamond, area is 2r^2 and the integral of ||x||_1 is `(4/3)r^3`. The unit diamond therefore has area 2 and first-norm integral 4/3. Its centered translate minimizes the integrated norm: x->integral_(x+D)||z||_1 dz is even and convex, with unique minimum at 0 as proved in §5.

## 3. All-law nonasymptotic peak-floor bound

Let p be the all-point private representative of an arbitrary feasible mu and let M=esssup p>0, finite. For eta>0 choose an actual x0 with `p(x0)>=(1-eta)M`; privacy forces p>=ell=b(1-eta)M on all x0+D. Set `g=p-ell 1_(x0+D)`. Then 0<=g<=M and `integral g=h=1-2ell>=0`.

Among all such capped g of mass h, the first-norm cost is minimized by filling the centered diamond of radius `sqrt[h/(2M)]` at density M. This elementary strict bathtub argument subtracts the threshold radius times equal masses and uses monotonicity inside/outside. The minimum is

    (2/(3sqrt(2))) h^(3/2) M^(-1/2).

The floor costs at least `(4/3)ell`; let eta->0 and put x=bM in (0,1/2]. Every actual feasible law obeys

    E||X||_1 >= F_b(x)
      := (4/3)x + [2/(3sqrt(2))]sqrt(b)(1-2x)^(3/2)/sqrt(x).           (5)

This is an all-law peak-floor inequality, not an assumption that the optimizer itself is a staircase or has an attained density maximum.

Write s=b^(1/3). The convex tangent inequality `(1-2x)^(3/2)>=1-3x` on [0,1/2] gives

    F_b(x) >= (4/3)x+[2/(3sqrt(2))]sqrt(b)/sqrt(x)-sqrt(2b x).

The minimum of the first two terms over x>0 is C s, attained at `x=y0 s`. If x<=2s the last term is at most `2s^2`; if x>2s then the ORIGINAL nonnegative expression (5) is at least `(8/3)s>C s`. Thus every x in its allowed range gives (1), even if its right side is negative at a nonasymptotic b.

## 4. Matching actual private upper law

Set `q=C s` and take the normalized ACTUAL shell law with core qD and density `b^(min{k:x in(q+k)D})`. Its index changes by at most 1 under every closed-D shift, so it obeys every event inequality. Geometric layers give

    Z=2 M2,       E||X||_1=(2/3)M3/M2,
    M2=q^2+2m q+m+2m^2,
    M3=q^3+3m q^2+3(m+2m^2)q+m+6m^2+6m^3,
    m=b/(1-b).

Since q=C s, C^3=2 and m=s^3+O(s^6), the cost is `C s+O(s^2)`. Combining with (1) proves conclusion 1. This constructs a genuinely feasible upper law; it does not import or assert a first-norm exact finite-epsilon source selector.

## 5. Actual peak location and uniform scaled core limit

Take ANY sequence in (2) and set s_n=b_n^(1/3). Select x_n within factor 1-s_n of its all-point density supremum M_n. Set

    y_n=s_n^2 M_n,   ell_n=b_n(1-s_n)M_n,
    g_n=p_n-ell_n 1_(x_n+D),   h_n=1-2ell_n,
    g_n^#(z)=s_n^2 g_n(s_n z),  t_n=sqrt[h_n/(2y_n)].

The floor term bounds y_n above; the residual bathtub term then bounds it below, and ell_n=O(s_n), h_n->1. With `F(x)=integral_(x+D)||z||_1 dz`, the rescaled cost is exactly

    E||X_n||_1/s_n
       =(1-s_n)y_n F(x_n) + [2/(3sqrt(2))]h_n^(3/2)y_n^(-1/2)+Delta_n,
    Delta_n=integral (||z||_1-t_n)[g_n^#-y_n 1_(t_n D)] dz >=0.         (6)

The function `f(y)=(4/3)y+[2/(3sqrt(2))]y^(-1/2)` has unique minimum C at y0. Since the total cost tends to C and F>=4/3, (6) forces `y_n->y0` and `Delta_n->0`.

To see `x_n->0`, the diamond's coordinate marginal has density of area `2(1-|u|)` for |u|<=1. For a>=0 define `G(a)=integral_D |z1+a| dz`. Then

    G(a)-G(0)=2a^2-(2/3)a^3  for 0<=a<=1,
    G(a)-G(0)>0                for a>0,

and G is even. Therefore `F(x)-F(0)=[G(x1)-G(0)]+[G(x2)-G(0)]` is strictly positive away from 0 and grows at infinity. The near-equality in (6) and y_n bounded below imply x_n->0, without assuming the peak was initially centered.

The bathtub threshold `t_n->sqrt[1/(2y0)]=C`. The deficit is nonnegative pointwise. Outside a band `| ||z||_1-t_n |<d` it dominates d times the density L1 error; the band's area is O(d) uniformly because t_n stays bounded, and the density cap y_n is bounded. Taking n->infinity then d->0 gives

    ||g_n^#-y_n 1_(t_n D)||_1 ->0.

The latter tends to `y0 1_(C D)` in L1; the scaled floor has probability mass `2ell_n=O(s_n)->0`. Thus the ACTUAL scaled densities converge in L1 and (2) follows. This is a full-law equality/compactness argument, not a source-staircase mixture claim.

## 6. Universal tail and cost-measure limits

Fix r>0. For n large, `r/s_n>t_n`. The nonnegative deficit in (6) implies

    integral_(||x||_2>r) g_n(x)dx / s_n
       <= Delta_n/[r-s_n t_n] ->0,

because `||z||_1>=||z||_2`. The floor coefficient `ell_n/s_n=(1-s_n)y_n->y0`, and x_n->0 makes `1_(x_n+D)->1_D` in L1. This proves (3).

Similarly, the contribution of g_n to the scaled COST outside any fixed neighborhood of 0 tends to zero: in scaled coordinates it is at most Delta_n plus t_n times the negligible scaled-tail mass. Its total scaled cost tends to the bathtub optimum `2C/3`, so it converges as a cost measure to `(2C/3)delta_0`. The floor component tends to `y0||x||_1 1_D dx`, with mass `y0*(4/3)=C/3`. This proves (4). Since the limit uniform law in (2) has mean norm 2C/3 but the scaled actual means tend to C, W1 convergence to that uniform law is impossible.

## 7. Cross-objective corollary, separately conditional

If the independent but still-UNREVIEWED squared-cost peak-floor candidate `frontier-20261028-peak-floor-low-privacy-universal-v1.md`, SHA `d44029e458b8af871d2d849e2a5159e1885e99402d615a88eabe39d89ab4ad43`, also survives review, ANY first-order-near-optimal mean-l1 law and ANY first-order-near-optimal original Euclidean-squared law satisfy TV->1 as b->0. Indeed the first concentrates on radius O(b^(1/3)), while the second, scaled by b^(-1/4), converges in TV to a non-atomic uniform disk; the smaller radius divided by b^(1/4) tends to 0. Both unscaled laws still converge weakly to delta_0. This is a conditional two-objective corollary, not a source-priority claim.

## 8. Actual bounded diagnostic and review boundary

A 70-digit Decimal evaluation at b=10^-9 of the exact lower expression in (1) and the actual q=C b^(1/3) staircase upper law gave

```text
b=1e-9: lower/s= 1.257921049895 trial/s= 1.260714252418 limit= 1.259921049895
lower<=trial: True y0 cubed=1/32, limit cubed=2
```

These are numerical diagnostics, not interval enclosures or the proof of the all-law limits. No floating solver, research theorem import, source-priority or novelty conclusion is used. Request disjoint review of the all-b lower bound, unique translated-floor minimizer, fractional bathtub deficit, tail normalization and every-near-minimizer quantifiers before adoption. No formal/kernel/human/configured-family or independent-model acceptance is claimed; historical held outcomes are nonpremises.
