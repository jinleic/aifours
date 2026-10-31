# First-norm versus squared-cost optimal laws: total variation tends to one

**AUTHOR CANDIDATE — WRITTEN with exact rational selected-parameter bounds; NOT independently reviewed or parent-adopted.** Native pre-write observation `Wed Oct 28 17:59:45 PDT 2026`.

## 1. Exact model and nontrivial result

For finite epsilon>0 set `b=e^(-epsilon)`, `m=b/(1-b)` and `D={h:||h||_1<=1}`. All laws below satisfy the actual additive privacy inequality for EVERY Borel event and EVERY h in the FULL CLOSED D. Define the first-norm, squared-l1 and squared-Euclidean objectives by E||X||_1, E||X||_1^2 and E||X||_2^2, respectively.

At the named per-cost theorem, choose the actual globally first-norm-optimal staircase `mu_1=Q_gamma1` and the actual globally squared-l1-optimal staircase `mu_2=Q_gamma2`, with the unique scalar offsets from the preceding selector candidate. Let mu_E be the actual original unique all-law Euclidean optimum imported from LAW642, and `R=(4/(3pi))^(1/4)`.

As epsilon->infinity (m,b->0), the candidate exact asymptotics are

    TV(mu_1,mu_2) = 1 - 2^(2/3)m^(1/6) + o(m^(1/6)),                 (1)
    TV(mu_1,mu_E) = 1 - 2^(2/3)sqrt(3/pi)m^(1/6) + o(m^(1/6)).      (2)

Thus these actually feasible optimal laws become asymptotically mutually singular in total variation, even though EACH converges weakly to the point mass at zero. This is an exact quantitative distinction between the PMLR first-moment selector and the squared-cost objectives, not just distinct finite-epsilon parameter names.

On their natural scales the stronger law limits are

    Law(m^(-1/3) X_1) -> Uniform(2^(1/3)D) in total variation,
    Law(m^(-1/4) X_2) -> Uniform(D) in total variation,
    Law(b^(-1/4) X_E) -> Uniform(B_2(0,R)) in total variation.          (3)

The third limit is an explicitly named prior author candidate, not newly assumed source equivalence. A separate still-unreviewed strict-cost equality candidate would make (1)–(2) apply to EVERY globally mean-optimal law and (1) to EVERY squared-l1-optimal law; the present proof needs only the actual centered optimizing laws named here. No nonadditive privacy, finite-epsilon disjointness, endpoint law at epsilon=infinity, source priority or novelty is claimed.

## 2. Exact inputs and assurance status

- Parent-WRITTEN_SUPPORTED matching-norm per-cost staircase attainment, `institute/runs/three-area-2026-10-23-96h/privacy-MDA26-entire-norm-cost-and-weighted-decay-parent-v1.md`, SHA `75614a6fc5cb66d9b26f13e64e58935fe6ea52121948e7a56592b91611576ac3`, applies separately to r and r^2 on the FULL closed D.
- My own UNREVIEWED `frontier-20261028-universal-pmlr-selector-separation-v1.md`, SHA `4c92d56867a959298836063d0045634cd61a0efb8f3175fcb701c4ac4a722fc6`, supplies globally selected scalar roots gamma_1<gamma_2 in (0,1). Their limiting scales are derived independently below.
- Parent-WRITTEN_SUPPORTED LAW642 original all-law optimizer, `privacy-all-law-self-contained-parent-v1.md`, SHA `c08f6353f121ef9e35da0e9d5e8ec9c87b0da838be0d1adf38b807010a1cd979`, gives mu_E with positive density `b^(n_S)/Z_E` on compact convex core S_E.
- My own UNREVIEWED `frontier-20261028-euclidean-low-privacy-disk-limit-v1.md`, SHA `b277d099eb211302b73754a971f63d81dc781f160a5096ad6f30db85de85d7b3`, gives `|S_E|~pi R^2 sqrt(b)`, `Z_E~pi R^2 sqrt(b)` and the last TV limit of (3). My own UNREVIEWED `frontier-20261028-euclidean-second-term-and-disk-law-v1.md`, SHA `188cd3ff1648e9f46ac00fdc1d0068272715559143fe9ec5643a7af03740b4d4`, upgrades the rescaled convex core to Hausdorff convergence to R B, supplying an inner disk. A reviewer must reconstruct these inputs; their hashes are not proof acceptance.

The optional all-optimizer strengthening is `frontier-20261028-strict-radial-optimizer-equality-v1.md`, SHA `e4f4a4909e5cf6ae734f17fdaf2edb4c4919c9162048dc2cf249209b99c5ff97`, also UNREVIEWED. PMLR's first-moment theorem is not attributed any squared-cost claim.

## 3. Different scales of the actual scalar minima

The exact scalar stationarity polynomials are

    Q_m(g)=g^4+4mg^3+6m^2g^2-2m(1+3m)g+m^2,                           (4)
    P_m(g)=g^5+5mg^4+(2m+12m^2)g^3+(12m^3-2m)g^2
              -m(1+2m)(1+6m)g+m^2(1+2m).                               (5)

The globally selected second roots are gamma_1 for Q and gamma_2 for P. Put `u=m^(1/3)`, g=u z. Direct expansion gives

    Q_m(u z)/u^4 = z^4-2z + u^2(4z^3+1)-6u^3 z+6u^4 z^2.             (6)

For any fixed z_-<2^(1/3)<z_+ with z_->0, the leading sign is negative at z_- and positive at z_+. The positive point used in the preceding root-selection proof lies at `sqrt(m(1+m))-m=O(m^(1/2))=o(u)`, so the selected L-minimizing SECOND root lies between u z_- and u z_+ for small m. The implicit function theorem at z=2^(1/3), where the derivative of z^4−2z is 6, gives

    gamma_1=2^(1/3)m^(1/3)+O(m).                                       (7)

Similarly, with `w=m^(1/4)` and g=w z,

    P_m(w z)/w^5 = z^5-z+O(w)

uniformly on bounded z. The global squared-l1 minimum is the SECOND positive root, so the sign around z=1 and the nonzero derivative 4 give

    gamma_2=m^(1/4)[1+O(m^(1/4))].                                     (8)

Consequently

    gamma_1/gamma_2 = 2^(1/3)m^(1/12)[1+o(1)],
    gamma_1^2/gamma_2^2 = 2^(2/3)m^(1/6)[1+o(1)].                     (9)

## 4. Core mass and natural-scale law limits

For any gamma in (0,1), Q_gamma is uniform on its top core gamma D. Its exact normalizer and core probability are

    Z_gamma=2[gamma^2+2m gamma+(m+2m^2)],
    Q_gamma(gamma D)=gamma^2/[gamma^2+2m gamma+m+2m^2].                 (10)

The complement probability is therefore

    [2m gamma+m+2m^2]/[gamma^2+2m gamma+m+2m^2].

By (7), this is O(m^(1/3)) for gamma_1; by (8), it is O(m^(1/2)) for gamma_2. Conditional on each core the law is exactly uniform. After scaling by u or w, the relevant core is a diamond whose radius tends respectively to 2^(1/3) or 1. Uniform laws on concentric diamonds with radii tending to each other converge in TV, and adding the vanishing outside-core mass proves the first two limits in (3).

Each unscaled core radius tends to zero, and its tail mass tends to zero, so mu_1 and mu_2 both converge weakly to delta_0. The named prior disk-limit input gives the third TV limit in (3) and similarly mu_E converges weakly to delta_0. The limit delta_0 is NOT claimed to be epsilon-private at a finite parameter.

## 5. Exact overlap for first-norm versus squared-l1 laws

For sufficiently small m, gamma_1<gamma_2 and their normalizers obey `Z_1/Z_2~gamma_1^2/gamma_2^2 ->0`. Hence on the smaller core gamma_1 D the first-norm density 1/Z_1 is strictly larger than the squared-l1 density 1/Z_2. The core is contained in the larger core, so

    integral_(gamma_1 D) min(q_1,q_2) dx = 2 gamma_1^2/Z_2.              (11)

Outside gamma_1 D, the overlap is at most mu_1's outside-core mass O(m^(1/3)), which is `o(m^(1/6))`. Since `Z_2~2 gamma_2^2`, equation (9) gives

    integral min(q_1,q_2) dx
      = 2^(2/3)m^(1/6)+o(m^(1/6)).                                     (12)

For probability densities `TV(mu,nu)=1-integral min(p,q)`, so (12) proves (1). This also agrees with the exact all-offset staircase TV formula in the separate UNREVIEWED strict-equality candidate, but does not require it as a premise.

## 6. Exact overlap for first-norm versus original Euclidean optimizer

The preceding actual-core disk/Hausdorff proof gives, for all sufficiently small b, an inner disk `(R/2)b^(1/4)B` contained in S_E. Since `gamma_1/b^(1/4)~2^(1/3)b^(1/12)->0` and gamma_1 D lies inside the Euclidean disk of radius gamma_1, the whole mean-optimal core gamma_1 D is contained in S_E.

On that core the Euclidean optimum density is exactly 1/Z_E, whereas the mean density is 1/Z_1. By (7) and the named normalizer asymptotic, `Z_1/Z_E=Theta(m^(1/6))->0`; hence the min of the densities on this core is exactly the Euclidean density. The overlap is

    integral_(gamma_1 D) min(q_1,p_E) dx
       = 2 gamma_1^2/Z_E
       ~ [2*2^(2/3)/(pi R^2)] m^(1/6)
       = 2^(2/3)sqrt(3/pi)m^(1/6).                                     (13)

As before, ALL overlap outside that mean core is at most its O(m^(1/3)) tail mass, which is negligible at order m^(1/6). This proves (2) without assuming the actual Euclidean optimizer is radial or replacing it with a disk-shell trial. Convex inner inclusion, canonical core density and actual normalizer are all named inputs; they are not inferred solely from weak convergence.

## 7. Actual bounded exact rational parameter check

For the selected exact rational `m=10^(-12)`, both gamma roots were bracketed by 50 Fraction bisections with exact polynomial signs; interval arithmetic was then applied to the exact two-staircase TV formula. Since `m^(1/6)=1/100`, the entire resulting overlap-scaled interval lies strictly in `(3/2,8/5)`. This is a selected diagnostic, not a proof of either asymptotic.

```python
from fractions import Fraction as F
m=F(1,10**12); b=m/(1+m)
def qm(m,g): return g**4+4*m*g**3+6*m*m*g*g-2*m*(1+3*m)*g+m*m
def pm(m,g): return g**5+5*m*g**4+(2*m+12*m*m)*g**3+(12*m**3-2*m)*g*g-m*(1+2*m)*(1+6*m)*g+m*m*(1+2*m)
def bis(f,lo,hi,n=50):
 assert f(m,lo)<0<f(m,hi)
 for _ in range(n):
  x=(lo+hi)/2
  if f(m,x)<0:lo=x
  else:hi=x
 return lo,hi
a,bb=bis(qm,F(1,10000),F(2,10000));c,d=bis(pm,F(1,2000),F(1,500))
def DD(g):return g*g+2*m*g+m+2*m*m
Slo=(c-bb)*(a+c+2*m)/(1-b); Shi=(d-a)*(bb+d+2*m)/(1-b)
Hlo=1/DD(d)-b/DD(a); Hhi=1/DD(c)-b/DD(bb)
assert 0<Hlo<=Hhi and 0<Slo<=Shi
tvlo=Slo*Hlo;tvhi=Shi*Hhi
ratio_lo=100*(1-tvhi);ratio_hi=100*(1-tvlo)
print('m=1/10^12 root_sign_brackets_valid=',qm(m,a)<0<qm(m,bb),pm(m,c)<0<pm(m,d))
print('rigorous TV-overlap scaled interval contained in (3/2,8/5):',F(3,2)<ratio_lo<=ratio_hi<F(8,5))
print('g1_minus_g2 root intervals disjoint=',bb<c,'bits_of_each_bisection=',50)
```

Actual output:

```text
m=1/10^12 root_sign_brackets_valid= True True
rigorous TV-overlap scaled interval contained in (3/2,8/5): True
g1_minus_g2 root intervals disjoint= True bits_of_each_bisection= 50
```

The interval arithmetic is exact at this single rational m; it does not prove the global all-epsilon selector theorem, actual Euclidean core limit, or the asymptotic expansion.

## 8. Limits and review request

The asymptotic law separation is WRITTEN conditional on the named original-all-law and matching-norm source theorems and the three unreviewed author candidates. Historical held outcomes are not accepted premises. Request full disjoint review of the root-branch limits, tail-overlap error, Euclidean inner-core inclusion, normalizer and constants before adoption. No formal/kernel, human/configured-family or novelty/source-priority gate is claimed.
