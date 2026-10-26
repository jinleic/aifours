# Independent written reconstruction: exact sign of the upper endpoint

Before-creation clock observed: **2026-10-23T13:18:08-07:00**. Reviewer: PhysicsResearch96h. No author edit, scientific program, solver, model CLI or formal proof was performed.

## Snapshot and verdict

Reviewed all 98 lines of `/Users/jinleic/repos/aifours/information-science/evidence/three-area-20261023-96h/proof-upper-endpoint-sign-v1.md`, SHA-256 **`35fa16a6570a91c1f8722e1f49ed29a6b43c980f08cb82c4a0d2e720b6a57306`**.

**0 FATAL / 0 MAJOR / 0 MINOR. No substantive defect found at the exact compatibility, h>0 and gamma>0 boundary.** The dichotomy, equality cases, nonnegativity of U and matched binary specialization reconstruct from the main sharp-bound formula. No stronger monotonicity or clinical assumption has been inserted.

## 1. Lower-tail strictness and a nonnegative attainable endpoint (lines 27–49)

For a positive selected mass x, a measure concentrated at one has ell(x)=x. If it has any positive mass below one, choose a positive portion of that mass up to x and fill the rest arbitrarily. The selected integral is strictly below x: the integral of the strictly positive deficit 1-y over a positive selected submeasure is positive, even if values approach one. Hence ell(x)<x. The argument works with atoms and full-mass selection.

Every selected first moment is at most the complete first moment because y>=0, so ell_s(x)<=m_s.

Under h=q-p>0, p0>0 and the masses r=h,t=0 are feasible. Moreover

`eta=gamma+m0+p-m1>m0`,

because gamma>0 and m1<=p. The main upper formula at these masses is

`G_eta(h)=min(eta,h)-ell0(h)`.

Both arguments of the minimum are at least ell0(h); eta is actually strictly greater. Thus G_eta(h)>=0 and the attainable maximum U is nonnegative. If mu0 has positive mass below one, ell0(h)<h as well, so both arguments are strictly larger and G_eta(h)>0. This proves case A with a compatible attaining law supplied by the base theorem.

## 2. Exact ceiling-stratum reduction (lines 51–78)

If mu0 is concentrated at one, m0=p0 and ell0(r)=r. The compatibility upper bound becomes `gamma<=g_min+1=m1`. Set `kappa=m1-gamma>=0`; then eta=1-kappa.

Because eta>m0=p0 and r<=p0, `min(eta,r)=r` for every feasible switch mass. Cancelling this term against ell0(r) in G gives

`G_eta(r)=t-(t-kappa)_+-ell1(t)=min(t,kappa)-ell1(t)`.

The feasible t interval is exactly `[0,min(p,1-q)]`, obtained from r in `[h,min(p0,q)]`. This is the full optimization in the ceiling case, not a restricted search over selected r.

Compatibility plus gamma>0 forces m1>0 and hence p>0. Therefore when q<1, the upper endpoint of the t interval is strictly positive; no zero-stratum exception invalidates the converse below.

## 3. All and only the equality exceptions (lines 80–88)

- If q=1, then t_max=0 and U=0.
- If gamma=m1, then kappa=0 and the objective is -ell1(t)<=0, while t=0 attains zero.
- If mu1 is concentrated at one, then ell1(t)=t and `min(t,kappa)-t<=0`, again with value zero at t=0.

These are precisely the failures of the three conditions in B. There is no extra case gamma>m1 because it is incompatible here.

Conversely, if q<1, mu1 has positive mass below one and gamma<m1, then p>0, t_max>0 and kappa>0. Any positive `t<=min(t_max,kappa)` satisfies ell1(t)<t, giving the strictly positive value `t-ell1(t)`. Thus U>0 exactly as stated. Combined with case A and the nonnegative lower witness, every remaining compatible case has U=0; it cannot have a negative U.

The conditional factual mu0 mass is necessarily nonempty when h>0. In the ceiling case, an empty mu1 would force gamma<=m1=0 and violate gamma>0. Thus the stated exclusions genuinely cover all compatible empty-stratum possibilities rather than silently dividing by zero.

## 4. Binary and interpretation boundaries (lines 90–98)

For binary factual cells, A is c>0. If c=0, the ceiling case has m1=b and mass below one in mu1 exactly d. Therefore B becomes q<1, d>0 and gamma<b. Compatibility already imposes gamma<=b, so the complement is exactly `c=0` and at least one of q=1, d=0 or gamma=b. This is the displayed all-binary equality condition.

U>=0 means at least one compatible law is nonharmful, not that the surrogate paradox is impossible. The lower endpoint can remain negative; the manuscript explicitly retains that distinction. U=0 excludes a strictly beneficial compatible law but need not force strict harm for every law. All conclusions use the stated bounded support and unrestricted latent dependence; removing either changes the problem and is not justified here.

This is independent in-harness written checking only. Population-model correctness is separate from novelty, human/kernel verification, clinical assumptions, statistical inference and the Kuroki primary-source gate.
