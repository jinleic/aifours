# Quantitative all-law mixed-objective stability from one dual deficit

**AUTHOR CANDIDATE — WRITTEN; NOT independently reviewed or parent-adopted.** Native pre-write observation: `Wed Oct 28 19:26:01 PDT 2026`.

## 1. Exact scope and theorem

Condition on the unreviewed all-real-theta definitions and peak-floor identities in `frontier-20261028-full-critical-moment-region-v1.md`, SHA-256 `c8ce61fb2d40463f5fdf488cb2ed5aebe40bf59c8bd97dc18b7674caf94bf463`. No LAW642, MDA or PMLR theorem is imported. Let b=e^(-epsilon)->0, s=b^(1/4), theta be ANY FIXED real number, and

    c_theta(z)=|z|^2+theta||z||_1,
    integral(T_theta-c_theta)_+=2/3,
    K_theta={c_theta<=T_theta}, A_theta=|K_theta|,
    f=(J+theta s L)/s^2, delta=(f-T_theta)_+.

For every original full-D-private law with finite J and `f<=T_theta+1`, and all sufficiently small s, there is a constant C_theta independent of the law and b such that

    TV(Law(X/s),Uniform(K_theta)) <= C_theta sqrt(delta+s^nu),           (1)
    |s^2 esssup p - 1/A_theta| <= C_theta sqrt(delta+s^nu),              (2)

where p is any all-point private density representative and `nu=2` for theta>=0, `nu=1` for theta<0. For the actual `(1-s^2)`-near-peak x0 selected in the proof,

    |x0| <= C_theta sqrt(delta+s^nu).                                      (3)

The same rate also controls BOTH scaled cost components:

    |L/s - V_theta| + |J/s^2-(T_theta-theta V_theta)|
       <= C_theta sqrt(delta+s^nu),  V_theta=T'_theta.                     (4)

In particular every true private sequence with `f<=T_theta+O(s)` has all of (1)–(4) at rate O(s^(1/2))=O(b^(1/8)). For theta=0 this is an all-law rate about the original squared-Euclidean leading optimum, with NO exact-core assumption. Bounds remain conditional on the pinned written predecessor, and are not an accepted finite-b optimizer theorem.

## 2. Peak-floor deficit and bounded cap

Write M=esssup p, y=s^2 M, and select x0 with `p(x0)>=(1-s^2)M`. Let `ell=b(1-s^2)M`, `g=p-ell 1_(x0+D)` and `g#(z)=s^2 g(sz)`. Then g# has cap y, mass h=1-2ell, and the exact dual deficit is

    Delta=integral_(c<T)(T-c)(y-g#)+integral_(c>T)(c-T)g# >=0,
    integral c g#=T h-(2/3)y+Delta,  T=T_theta.                           (5)

The assumption f<=T+1 and `L/s<=sqrt(2J/s^2)` imply a law-independent bound on J/s^2 even for theta<0. The J floor implies y is bounded above. The residual J bathtub and h->1 bound y away from zero. Thus `0<y_min(theta)<=y<=y_max(theta)` uniformly for small s, and ell=O_theta(s^2).

If theta>=0, the translated floor cost satisfies `F_s(x0)>=2/3+2|x0|^2`; if theta<0, the exact identity and translated-norm bound in the import give `F_s(x0)>=2/3-O_theta(s)+|x0|^2`. Plugging into (5), using the actual `(1-s^2)` factor and h, gives respectively

    Delta+c_theta |x0|^2 <= delta+C_theta s^2      (theta>=0),
    Delta+c_theta |x0|^2 <= delta+C_theta s        (theta<0),            (6)

for a positive constant c_theta independent of the law. Here lower-case c_theta denotes a constant in (6), not the cost function; the distinction is only typographical. Put `E=delta+C_theta s^nu` and enlarge its constant as needed. Then `Delta<=E` and `|x0|<=C_theta sqrt(E)`.

## 3. Uniform geometric band bound and total variation

For ANY real theta, any T and any h>0, each quadrant's cost is a translated squared Euclidean norm minus theta^2/2. Its band `|c_theta-T|<h` is contained in a circular annulus with squared-radii difference at most 2h. Thus, without any regularity or topology assumption,

    |{z:|c_theta(z)-T|<h}| <= 8pi h.                                      (7)

Both g# and `y 1_(c<=T)` are bounded by y. Outside the band the deficit controls their L1 difference, hence

    e=||g#-y 1_(c<=T)||_1 <= Delta/h+8pi y h.                           (8)

Choosing h=sqrt(Delta/(8pi y_max)) (and using the limiting argument when Delta=0) yields `e<=2sqrt(8pi y_max Delta)`. Since `|h_mass-yA_theta|<=e` and `1-h_mass=2ell`, the full scaled density differs in L1 from `1_K/A_theta` by at most `2e+4ell`. Thus TV<=e+2ell, giving (1). The same mass identity gives `|y-1/A_theta|<=(e+2ell)/A_theta`, proving (2). Formula (7) also holds when K_theta is an annulus or has multiple components.

## 4. BOTH moments, including the macro privacy floor

Choose one sufficiently large fixed R=R_theta so that K_theta lies in the R-ball and `c_theta(z)-T_theta>=|z|^2/2` outside it. The second term in (5) then gives

    integral_(|z|>R)|z|^2 g# <=2 Delta.                                  (9)

Inside the ball, the L1 error e controls both the first and second residual moments. Outside it, (9) controls them by O_theta(Delta). Consequently

    integral ||z||_1 g# = y integral_K ||z||_1 +O_theta(e+Delta),
    integral |z|^2 g#   = y integral_K |z|^2   +O_theta(e+Delta).        (10)

The first-norm physical floor contributes O_theta(s) to L/s because x0 is bounded and ell/s=O(s); this is at most O_theta(sqrt(E)) for either nu. The squared physical floor contributes exactly `(1-s^2)y[2/3+2|x0|^2]` to J/s^2. Equations (2)–(3), (10), and `T A_theta=integral_K c_theta+2/3` prove (4). The 2/3 floor term is essential: the limiting bulk's own squared moment alone is not the limiting J/s^2.

## 5. Status

No numerical, formal or independent verification of the universal inequalities was performed. The proof is written, explicitly conditional on the unreviewed c8ce predecessor's density/dual framework and on standard elementary geometry. The rate is for fixed theta, not an unproved uniform statement over unbounded theta; it does not establish the exact second-order value, finite-b optimizer form, novelty, or parent adoption.
