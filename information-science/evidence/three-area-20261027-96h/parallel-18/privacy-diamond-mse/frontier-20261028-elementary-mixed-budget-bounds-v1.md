# Explicit finite-privacy mixed-cost and joint-budget bounds

**AUTHOR CANDIDATE — WRITTEN with floating diagnostics; NOT independently reviewed or parent-adopted.** Native pre-write observation: `Wed Oct 28 19:24:19 PDT 2026`.

## 1. Import and elementary cost lower bounds

Condition on the unreviewed finite-b all-law dual candidate `frontier-20261028-finite-privacy-dual-bound-v1.md`, SHA-256 `312c990ff6b0c98c1db13fe2687ef953827227a5007e3d690efb5b40ef51cfdc`. It supplies the root lower bound `(J+kappa L)>=B` for original full-D privacy, `J=E|X|^2`, `L=E||X||_1`, b=e^(-epsilon), and

    G_kappa(B)+2bB=b d,    d=(2+4kappa)/3,    kappa>=0.

Here `G_kappa(T)=integral(T-|x|^2-kappa||x||_1)_+ dx`. This note gives directly evaluable, weaker but elementary bounds; it does not assume the exact root B is an achievable finite-b optimum.

For any kappa>=0 define

    Q=[sqrt(4b^2+2pi b d)-2b]/pi
     =2bd/[sqrt(4b^2+2pi b d)+2b].                                       (1)

For kappa>0 additionally define

    C=2kappa sqrt(b) sinh{(1/3)asinh[3d/(4kappa sqrt(b))]}.              (2)

Then every actual full-D-private law obeys

    J+kappa L >= Q,                           kappa>=0,
    J+kappa L >= max(Q,C),                    kappa>0.                   (3)

At kappa=0, Q exactly coincides with the predecessor root B, namely `sqrt[4b/(3pi)+4b^2/pi^2]-2b/pi`. The displayed C is the UNIQUE nonnegative real root of `2C^3/(3kappa^2)+2bC=bd`.

## 2. Proof and comparison with the exact root

For T>=0, kappa>=0,

    G_kappa(T) <= integral (T-|x|^2)_+ dx =pi T^2/2;
    G_kappa(T) <= integral (T-kappa||x||_1)_+ dx =2T^3/(3kappa^2),

with the second bound for kappa>0. Since both right-side root equations and the exact root equation are increasing, their roots Q,C are <=B. Substituting `C=2kappa sqrt(b)sinh u` in the cubic gives `sinh(3u)=3d/(4kappa sqrt(b))`, which proves (2). The whole argument is written and valid at each finite b, including kappa and b chosen dependently.

## 3. Explicit joint J/L budget implication

Suppose an original private law must satisfy budgets `J<=j`, `L<=ell`, where j,ell>=0. For ANY choice kappa>=0 put

    H=j+kappa ell,       d=(2+4kappa)/3.

If `H<d/2`, then necessarily

    b <= [pi H^2/2]/[d-2H].                                             (4)

For kappa>0 this strengthens to the minimum of two explicit expressions:

    b <= min{ pi H^2/2, 2H^3/(3kappa^2) }/[d-2H].                       (5)

Equivalently epsilon must be at least the logarithm of the reciprocal of the displayed right side; optimize over all admissible kappa to get the best elementary joint-budget lower bound. If H=0, the right side is 0 and no finite-epsilon private law can meet the budgets. If the right side exceeds 1, this inequality is simply noninformative beyond epsilon>=0. If H>=d/2, the rearrangement is not used.

Proof: by the predecessor, B<=J+kappa L<=H. Monotonicity of `G_kappa(T)+2bT` gives `b d<=G_kappa(H)+2bH`; upper-bound G by either expression in §2 and rearrange. At kappa=0, (4) reproduces the nonasymptotic necessary condition `b<=3pi j^2/[4(1-3j)]` for j<1/3. For fixed finite j and ell<2/3, taking kappa->infinity in (5) also yields the first-norm-only condition `b<=ell^3/(2-3ell)`; independently it follows by applying the same floor/dual proof directly to cost `||x||_1`. These are necessary budget constraints, not sufficient mechanisms or an exact finite-b Pareto region.

## 4. Optional exact elementary formula for G_kappa

For kappa>=0 and T>0, set

    A=kappa^2+2T,
    p=[sqrt(kappa^2+4T)-kappa]/2,
    q=sqrt(kappa^2+2T)-kappa,
    F_A(z)=[z sqrt(A-z^2)(5A-2z^2)+3A^2 asin(z/sqrt(A))]/8.

An exact quadrant change of variables `u=x+y`, `v=x-y` yields

    G_kappa(T)=2T p^2-(4kappa/3)p^3-(2/3)p^4
                +(4/3)[F_A(q+kappa)-F_A(p+kappa)].                       (6)

The first term integrates where `|v|<=u` is binding; the second integrates the circular cross-section where `|v|<=sqrt(A-(u+kappa)^2)` is binding. Indeed `p` is the positive solution of `u^2+kappa u=T`, q the positive solution of `u^2+2kappa u=2T`, and `F_A` is an antiderivative of `(A-z^2)^(3/2)`. This formula reduces to pi T^2/2 at kappa=0. It expresses the predecessor's B by a monotone scalar root with only arithmetic, square roots and asin, without numerical 2D integration. The differences in (6) can be ill-conditioned in floating arithmetic; high precision or certified interval treatment would be needed for rigorous computed bounds.

## 5. Actual floating diagnostics and limits

An eval-kernel Python `math` cell used (6) and 80 bisections; the compared elementary roots are (1)–(2). Output:

```text
b=0.5  kappa=1.0   B≈0.7974887005802815   Q≈0.540725011832535   C≈0.7351392590499015
b=0.1  kappa=1.0   B≈0.5757467738706719   Q≈0.2987974023069499  C≈0.5230395601095226
b=0.01 kappa=0.1   B≈0.08392503065622453  Q≈0.06528215642628067 C≈0.04729802940570428
b=0.01 kappa=10.0  B≈2.414963881358762    Q≈0.2922427381856809  C≈2.3988160704880697
G_0(1)≈1.5707963267948972; pi/2≈1.5707963267948966
```

These are unverified floating diagnostics, not enclosures or proof. The exact inequalities and formulae are WRITTEN conditional on the pinned predecessor; no formal, independent-review, novelty, finite-b attainability or parent-acceptance claim is made.
