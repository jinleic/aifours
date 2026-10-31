# Strictly stronger finite privacy bound by retaining peak-floor overlap

**AUTHOR CANDIDATE — WRITTEN with explicitly nonrigorous float comparisons; NOT independently reviewed or parent-adopted.** Native pre-write observation: `Wed Oct 28 19:34:28 PDT 2026`.

## 1. New source-independent all-law bound

Fix any epsilon>0, b=e^(-epsilon) in (0,1), and kappa>=0. For EVERY original all-Borel, all-event, full closed l1-unit-diamond-private law set `J=E|X|_2^2`, `L=E||X||_1`,

    phi(x)=|x|^2+kappa||x||_1,
    G(T)=integral_R2 (T-phi)_+ dx,    d=integral_D phi=2/3+4kappa/3.

Let B be the UNIQUE positive root

    (1-b)G(B)+2bB=b d.                                                    (1)

Then the written, SOURCE-INDEPENDENT all-law claim is

    J+kappa L >= B.                                                       (2)

The root always satisfies `B<=d/2<kappa+1/2`, so its sublevel `{phi<=B}` lies INSIDE D. For every b>0 and kappa>=0, this bound is STRICTLY stronger than the prior independently written floor/cap relaxation `frontier-20261028-finite-privacy-dual-bound-v1.md`, SHA-256 `312c990ff6b0c98c1db13fe2687ef953827227a5007e3d690efb5b40ef51cfdc`: its root had `G(B_old)+2bB_old=bd`, i.e. it forgot that the residual cap is lower on the already occupied floor. No earlier candidate is imported in the proof.

For the original squared-Euclidean target kappa=0, (1) is explicit:

    J >= B_0(b)
       = (2b/3)/[b+sqrt(b^2+(pi/3)b(1-b))].                              (3)

This holds at every finite epsilon, without assuming any optimizer form. It tends to 1/3 as b->1 and to `(2/sqrt(3pi))sqrt(b)` as b->0. It is a necessary lower bound, not a claim of finite-b exactness.

## 2. All-point density and the occupied-cap refinement

Full event privacy implies an absolutely continuous bounded law: integrating `mu(A)<=b^(-1)mu(A+h)` over h in D gives `mu(A)<=|A|/(2b)`. The all-point representative `p(x)=limsup_(rho->0) mu(B_rho(x))/|B_rho|` obeys both privacy directions pointwise, equals the density a.e., and is at most M=esssup p everywhere.

For eta>0 choose a near-peak x0 with `p(x0)>=(1-eta)M`; p is at least `ell=(1-eta)bM` on E=x0+D. Set `g=p-ell 1_E`. Importantly,

    0<=g<=M-ell 1_E  almost everywhere,    integral g=1-2ell.             (4)

For any T>=0, the capped-density bathtub inequality gives

    integral phi g >= T(1-2ell)-M G(T)+ell integral_E(T-phi)_+.

Adding the actual floor `ell integral_E phi` and combining pointwise yields the EXACT strengthened dual inequality

    J+kappa L >= T-M G(T)+ell integral_(x0+D)(phi-T)_+.                  (5)

This retains the overlap correction; replacing the residual cap by M everywhere loses its final positive term.

The function `(phi-T)_+` is even and convex, so its translate integral over symmetric D is even convex and minimized at x0=0. Define `d(T)=integral_D(phi-T)_+`. Equation (5) implies

    J+kappa L >= T+M[(1-eta)b d(T)-G(T)].                                (6)

Here G increases strictly for T>0, d(T) decreases continuously from d>0 to 0, so `G(T)=b d(T)` has exactly one positive root B. Let eta->0 in (6) to get (2).

## 3. Root reduction and strict improvement

For any T>=0,

    G(T)-d(T) >= integral_D[(T-phi)_+-(phi-T)_+] =2T-d.                   (7)

Thus at T=d/2, `G(T)>=d(T)`, and because b<1 the root B is <=d/2. If x is outside D, then `|x|^2>=||x||_1^2/2` and `phi(x)>=1/2+kappa>d/2`. Hence `{phi<=B}` is contained in D. At this B,

    d(B)=d-2B+integral_D(B-phi)_+=d-2B+G(B),

which turns `G(B)=b d(B)` into (1).

For the earlier root B_old>0, the left side of (1) is smaller than bd by `b G(B_old)>0`. Since it is strictly increasing, B>B_old. The strict comparison is between two proven LOWER BOUNDS, not a claim of strictness or equality versus the actual optimum.

At kappa=0, `G(T)=pi T^2/2`; solving (1) yields (3). The expression is rationalized and remains well-conditioned as b->1.

## 4. Improved exact finite joint-budget constraints

Suppose J<=j and L<=ell, j,ell>0. If `H=j+kappa ell<d/2`, actual feasibility forces B<=H. The same sublevel containment applies at H, so monotonicity of (1) implies

    b <= G(H)/[d-2H+G(H)].                                               (8)

For kappa>0, `G(H)<=2H^3/(3kappa^2)`, and t/(d-2H+t) is increasing. Let r=j/ell and `F(r)=27r(1-2r)^2/4`. Choosing `kappa=2r/(1-6r)` for r<1/6 and j<1/9 gives the explicit STRICT improvement of the earlier finite necessary condition:

    b <= ell^3 F(r)/[1-9j+ell^3 F(r)].                                   (9)

The same occupied-cap proof for the cost phi=||x||_1 has diamond integral 4/3, `G(T)=2T^3/3`, and root <=2/3<1, giving

    b <= ell^3/[2-3ell+ell^3]                 if ell<2/3.                (10)

For j<1/3 the original squared-Euclidean-only necessary condition is

    b <= 3pi j^2/[4-12j+3pi j^2].                                       (11)

Equations (9)–(11) strictly improve their corresponding previous finite bounds whenever the budgets are positive and the denominators have the stated signs. They are NECESSARY conditions, not sufficient mechanisms or exact finite-b optima.

## 5. Diagnostics and status

A Python `math` eval cell compared old and new original-J lower bounds; actual floating output was

```text
b=0.01 old≈0.05909111882108342 new≈0.05935971840483336
b=0.1  old≈0.15196308045258433 new≈0.15765128068926104
b=0.5  old≈0.24162562298805274 new≈0.2742577804065216
b=0.9  old≈0.26980699911590084 new≈0.324163217120009
```

These are diagnostic floats, not interval enclosures. `fractions.Fraction` also checked example r-coefficients 121/512, 25/64, 49/108. All-event density, occupied-cap dual, root containment and budget claims are WRITTEN arguments using standard analysis, not formally proved, independently reviewed, novelty-cleared or parent-adopted. Suggested review: (4)–(5), translate convexity, root containment, and all budget denominator conditions.
