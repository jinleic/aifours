# From first-norm source to Euclidean-square target: three all-law regimes

**AUTHOR CANDIDATE — WRITTEN with explicitly scoped exact power-identity checks; NOT independently reviewed or parent-adopted.** Native pre-write observation: `Wed Oct 28 19:10:53 PDT 2026`.

## Statement and named dependency

Let b=e^(-epsilon)->0, s=b^(1/4), and let kappa=kappa(b)>=0 be an arbitrary weight. F_b is the class of ALL Borel laws satisfying the full closed l1-diamond unit-shift privacy condition. Write

    H(b,kappa)=inf_(mu in F_b) E_mu[|X|_2^2+kappa||X||_1].               (1)

This is the actual first-norm versus original Euclidean-square objective, not a squared-l1 surrogate. The finite critical-scale part is conditional on the preceding unreviewed source-independent candidate `frontier-20261028-mean-euclidean-critical-crossover-v1.md`, SHA-256 `7de42660b59814a1802d2fdeec3ca0c0a6d69c845beaa1d9f3c083fd3cbbc53d`; §3 proves the needed compact-theta extension. The supercritical part in §§4–6 is an independent all-law peak-floor proof, with no LAW642, MDA or PMLR theorem imported. Everything remains WRITTEN/unreviewed.

### A. Subcritical and critical

If `kappa/s->theta` for finite theta>=0, let T_theta be the UNIQUE positive root

    integral_R2 [T_theta-|z|_2^2-theta||z||_1]_+ dz=2/3.

Then

    H(b,kappa)=T_theta s^2+o(s^2),                                       (2)

and EVERY actual feasible sequence with cost `<=T_theta s^2+o(s^2)` satisfies

    Law(X/s) -> Uniform{ |z|_2^2+theta||z||_1<=T_theta } in TV.          (3)

In particular kappa/s->0 recovers the original target's uniform Euclidean disk and leading constant `2/sqrt(3pi)`, whereas any fixed positive critical ratio has the genuinely different mixed-degree sublevel.

### B. Supercritical, including fixed or unbounded kappa

If `kappa/s->infinity`, with NO assumption that kappa converges or remains bounded, put

    A_b=[b(1+2kappa)/kappa]^(1/3),
    C_b=[b kappa^2(1+2kappa)]^(1/3)=kappa A_b.                         (4)

Then

    H(b,kappa)=C_b(1+o(1));                                             (5)

EVERY actual feasible sequence with cost `<=C_b(1+o(1))` satisfies

    Law(X/A_b) -> Uniform(D) in TV.                                      (6)

This holds if kappa->0 more slowly than b^(1/4), if kappa has any fixed positive limit, and even if kappa->infinity. For kappa=1 the coefficient and core radius are `(3b)^(1/3)`. When kappa->infinity, the dominant first-norm optimum approaches `kappa(2b)^(1/3)` and A_b approaches `(2b)^(1/3)`. When kappa->0 but kappa/s->infinity, `C_b~b^(1/3)kappa^(2/3)` and `A_b~(b/kappa)^(1/3)`.

The limit is for the RESCALED laws, not a bounded-support assertion about the original private laws. These claims cover sequences in either stated regime; no result for a nonconvergent ratio is asserted beyond applying the appropriate conclusion on subsequences.

## 3. Why fixed-theta work extends to kappa/s->theta

For theta_b=kappa/s converging to finite theta, theta_b is eventually in a fixed compact interval [0,Theta]. The prior candidate's shell upper bound is uniform on this compact interval: all cost bodies have uniformly bounded radii and positive area, and the translated shell integrals have constants bounded in Theta. The root map T_theta is continuous by dominated convergence of G_theta(T), strict monotonicity in T, and bracketing. Hence its upper law gives `cost/s^2<=T_theta+o(1)`.

For the arbitrary-law lower proof, use the SAME fixed threshold T_theta but the actual scaled cost `c_b(z)=|z|^2+theta_b||z||_1`; on bounded sets c_b->c_theta uniformly and `G_b(T_theta)->2/3`. The actual peak-floor scaled cap y is bounded above by the squared-cost floor and bounded away from zero by the ordinary squared-cost capped-density bathtub, as in the dependency. Its mass tends to one. The nonnegative dual deficit for c_b and T_theta tends to zero. Their T_theta boundary bands have area O(d), uniformly for b small, because the radial equation `r^2+theta_b a(phi)r=T` has radial T-derivative bounded uniformly for T near the fixed positive T_theta. Also the c_b sublevel indicators converge in L1 to the c_theta one. Therefore the deficit forces the ENTIRE scaled densities to converge in L1 to the uniform c_theta sublevel, giving (2)–(3). No interchange of an unbounded theta limit is used here.

## 4. Supercritical scales and exact algebra

Suppose kappa/s->infinity. Set

    d=integral_D [|x|^2+kappa||x||_1]dx = (2+4kappa)/3,
    r=(b d/kappa)^(1/3),     alpha=r/kappa,
    T=(3/2)^(1/3).                                                       (7)

Then

    r->0,   alpha->0,   kappa/d<=3/4,
    integral_R2 (T-||z||_1)_+ dz=(2/3)T^3=1,
    T r=A_b,   T kappa r=C_b.                                            (8)

Indeed `alpha^3=b d/kappa^4`; for kappa<=1 this tends to zero because kappa/b^(1/4)->infinity, while for kappa>=1 it is O(b/kappa^3). Also r^3=b[(2/3)/kappa+4/3]->0. These comparisons cover arbitrarily oscillating and unbounded kappa inside the supercritical regime.

## 5. Source-independent all-law lower bound and universal shape

The full privacy condition gives a bounded all-point density p, with M=esssup p. Select x0 with `p(x0)>=(1-r)M`; then `p>=ell=b(1-r)M` on x0+D. Put

    y=r^2 M, g=p-ell 1_(x0+D), g^#(z)=r^2 g(rz),
    h=integral g^#=1-2ell.

Here `0<=g^#<=y` and `ell=(1-r)y kappa r/d`; the latter is O(y r) by (8). By even convexity, each translated floor integral is minimized at zero, so

    integral_(x0+D)[|x|^2+kappa||x||_1]dx >= d.                           (9)

In units of kappa r the floor therefore costs at least `(1-r)y`, and the scaled residual cost is

    integral [||z||_1+alpha|z|^2]g^#(z)dz.                               (10)

Use the FIXED L1 bathtub threshold T in (8), and write the exact nonnegative deficit

    Delta=integral_(||z||_1<T)(T-||z||_1)(y-g^#)
          +integral_(||z||_1>T)(||z||_1-T)g^#.                          (11)

Because its positive-part integral is exactly 1,

    integral ||z||_1 g^# = T h-y+Delta.                                  (12)

The floor and bulk therefore imply

    cost/(kappa r) >= T-2T ell-r y+Delta+alpha integral |z|^2 g^#.       (13)

The explicit upper law in §6 bounds cost/(kappa r) for a minimizing or first-order-near-minimizing sequence; (9) consequently bounds y above. Then ell=O(r)->0 and h->1. The L1 bathtub lower bound with mass h and cap y bounds y away from zero. Equation (13) gives the matching lower value T and forces Delta->0 for every near-optimal law.

For any fixed band width delta>0, Delta/delta bounds the L1 distance between g^# and `y 1_(||z||_1<=T)` outside the band `| ||z||_1-T |<delta`. This band's area is O(delta), uniformly, and both densities are bounded by y. Letting delta->0 after the sequence gives L1 convergence. Since h->1, `y->1/(2T^2)`; the floor has total mass 2ell->0. Thus `Law(X/r)->Uniform(TD)` in TV, which is exactly (6) after dividing by A_b=T r.

## 6. Matching ACTUAL full-D private law

Use the exact geometric shell law with compact core `S=r T D`, density proportional to `b^(min{k:x in S+kD})`. The D triangle inequality proves the original full event privacy, independent of kappa. Its top normalization is `r^2 |TD|` up to relative O(r), since `b/r^2=kappa r/d<=3r/4`. Its top scaled numerator is `integral_(TD)||z||_1+O(alpha)`. The first shell's numerator, normalized by `r^2 kappa r`, is

    [integral_(D+S)(|x|^2+kappa||x||_1)dx]/d =1+O(r),

uniformly in all kappa>=0 because `(1+kappa)/d` is bounded. All farther geometric shells are negligible relative to this term as b->0. Since `T|TD|-integral_(TD)||z||_1=1`, the normalized cost is T+o(1). This upper law proves (5) and supplies the near-minimizer cap bound in §5.

## 7. Exact diagnostic and limits of the claim

In the Python eval kernel, `fractions.Fraction` checked the identities in (7)–(8) for b=2^-120 and kappa=2^-12, 1, and 2^30. The exact cubes `alpha^3`, `C_b^3`, `A_b^3` were respectively:

```text
kappa=1/4096, kappa/s=262144
alpha^3=683/4835703278458516698824704
C^3=2049/45671926166590716193865151022383844364247891968
A^3=2049/664613997892457936451903530140172288
kappa=1, kappa/s=1073741824
alpha^3=1/664613997892457936451903530140172288
C^3=A^3=3/1329227995784915872903807060280344576
kappa=1073741824, kappa/s=1152921504606846976
alpha^3=715827883/883423532389192164791648750371459257913741948437809479060803100646309888
C^3=2147483649/1152921504606846976
A^3=2147483649/1427247692705959881058285969449495136382746624
```

Only these rational algebra checks were machine-executed; no finite numerical examples prove universal limits. There is no optimizer ansatz, imported source-equivalence claim, formal proof, independent review, priority/novelty clearance, or parent acceptance here. Suggested disjoint review targets: uniformity for variable kappa, the floor/dual scaling, the far-shell estimate, and exact near-optimality quantifiers.
