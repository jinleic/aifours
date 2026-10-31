# Source-independent finite and uniform joint-budget theorem

**AUTHOR CANDIDATE — WRITTEN with exact rational sample checks; NOT independently reviewed or parent-adopted.** Native pre-write observation: `Wed Oct 28 19:32:17 PDT 2026`.

## 1. Stronger source-independent result

Fix the original all-Borel, all-event, FULL closed l1-unit-diamond private noise class. Write `b=e^(-epsilon)`, `J=E|X|^2`, `L=E||X||_1`, and let `b_max(j,ell)` be the supremum of b for which J<=j and L<=ell. Let `j,ell>0`, `r=j/ell`, and

    F(r)= (27/4)r(1-2r)^2  if 0<r<1/6,
          1/2                if r>=1/6.                                  (1)

The exact finite-b NECESSARY conditions for ANY feasible law are

    b <= ell^3 F(r)/(1-9j)      if r<1/6 and j<1/9,                     (2)
    b <= ell^3/(2-3ell)         if r>=1/6 and ell<2/3.                   (3)

Furthermore, if ell->0 and ell^2/j->0, with r=j/ell arbitrary and possibly nonconvergent, the ACTUAL optimum satisfies the uniform relative estimate

    b_max(j,ell)=ell^3 F(r)[1+O(ell+ell^2/j)],                           (4)
    epsilon_min=3log(1/ell)-log F(r)+O(ell+ell^2/j).                     (5)

The big-O constants are universal over all r>0 in this regime. In particular (4) is RELATIVE even if r->0. This source-independent written argument strengthens and replaces the dependence chain of the earlier unreviewed `frontier-20261028-all-ratio-joint-budget-inversion-v1.md` (SHA-256 `7fc5ce61d0b4f25d83db7e73da9ddfe6214fa79f455819729b14dbbcfdc592f1`) for the ell/sqrt(j)->0 window; the earlier file remains frozen and is not retroactively reviewed.

## 2. A finite joint lower plane from first principles

For kappa>0 put `H=j+kappa ell`, `d=(2+4kappa)/3`. The all-point density representative p of any fully private law is bounded; if M is its essential peak, an arbitrarily near-peak x0 gives density at least `(1-eta)bM` on x0+D. For `phi(x)=|x|^2+kappa||x||_1`, the translate integral is at least d by even convexity, and the residual density has cap M. The capped-density dual at any T says

    J+kappa L >= T+M[(1-eta)b(d-2T)-G(T)],
    G(T)=integral (T-|x|^2-kappa||x||_1)_+ dx.                          (6)

Let eta->0 and choose the unique positive B with `G(B)+2bB=bd`. Then `J+kappa L>=B`. Since the L1 budget forces `H>=B`, monotonicity and the elementary containment `G(H)<=2H^3/(3kappa^2)` yield the FINITE inequality

    b <= H^3/[kappa^2(1+2kappa-3H)]

whenever `H<(1+2kappa)/3`. No source theorem, optimizer ansatz or limiting step is used. The same argument applied directly to cost `||x||_1`, whose diamond floor integral is 4/3 and whose positive-part integral is `2T^3/3`, yields (3) for any r when ell<2/3.

For r<1/6 choose the exact optimizing weight `kappa=2r/(1-6r)`. Then

    H/(1+2kappa)=3j,
    H^3/[kappa^2(1+2kappa)]=ell^3 F(r).

The condition becomes j<1/9 and the finite inequality becomes (2). These two identities hold identically in r, including arbitrarily small r; no singular relative error is hidden in the substitution.

## 3. Explicit genuine private diamond shells

For any a>0, let S=aD and give x density proportional to `b^(min{k:x in S+kD})`. Every D shift changes the shell index by at most 1, so this is an ACTUAL full-event, full-D private law. Since S+kD=(a+k)D, the exact normalizer and cost numerators are

    Z=2(1-b) sum_(k>=0) b^k(a+k)^2,
    N_L=(4/3)(1-b) sum_(k>=0) b^k(a+k)^3,
    N_J=(2/3)(1-b) sum_(k>=0) b^k(a+k)^4,                               (7)

and L=N_L/Z, J=N_J/Z. For small a and `0<b<=a^3/2`, uniformly in the ratio b/a^3,

    L=(2/3)[a+b/a^2][1+O(a)],
    J=(b/[3a^2])[1+O(a+a^4/b)].                                         (8)

Proof: write each sum as its k=0 and k=1 terms plus O(b^2), use `b/a^2<=a/2` for the denominator, and keep the top a^4 term explicitly in the J error. All implicit constants are absolute.

## 4. Uniform matching constructions

Set `eta=ell+ell^2/j`; by assumption eta->0. Choose `gamma=1-K eta` with a sufficiently large absolute K, so 0<gamma<1 eventually.

If 0<r<1/6, choose

    a=gamma (3/2)(1-2r)ell,       b=gamma^3 ell^3 F(r).                   (9)

Exactly `b/a^2=3gamma j`, `b/a^3=2r/(1-2r)<=1/2`, and `a^4/b=O(ell^2/j)` uniformly in r. Equation (8) gives

    L=gamma ell[1+O(ell)],
    J=gamma j[1+O(ell+ell^2/j)].                                        (10)

The chosen K makes both inequalities strict for all small eta. These are true private shell laws at the specified b.

If r>=1/6, take `a=gamma ell`, `b=a^3/2`. Equation (8) gives `L=gamma ell[1+O(ell)]` and `J=(gamma ell/6)[1+O(ell)]<=gamma j[1+O(ell)]`; the same K gives actual feasibility. Consequently BOTH cases yield

    b_max >= ell^3 F(r)[1-O(ell+ell^2/j)].                               (11)

For r<1/6, j<ell/6, so (2) gives the matching upper factor `1+O(ell)`. For r>=1/6, (3) also gives `1+O(ell)`. These bounds prove the uniform relative assertion (4), its log form (5), and require neither subsequences nor previously claimed mixed-objective optimality.

## 5. Exact sample checks and limitations

The Python eval kernel used `fractions.Fraction` for (1): `F(1/24)=121/512`, `F(1/12)=25/64`, `F(1/9)=49/108`, and `F(1/6)=1/2`. These are finite algebra checks only. All-event density, dual inequality, finite conditions and uniform shell estimates are WRITTEN proofs using standard analysis; no external research theorem, LAW642, MDA, PMLR or prior unreviewed result is imported. This is not a formal proof, independent review, novelty claim, exact finite-b optimum, or parent acceptance. Disjoint review should examine (6), the relative error in (8) as b/a^3->0, and the uniform construction when r crosses 1/6.
