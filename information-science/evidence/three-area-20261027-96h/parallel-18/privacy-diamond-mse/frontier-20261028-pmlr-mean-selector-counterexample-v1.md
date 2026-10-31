# Exact first-moment selector counterexample for the registered squared costs

**AUTHOR CANDIDATE — WRITTEN with exact rational checks; NOT independently reviewed or parent-adopted.** Native pre-write clock: `Wed Oct 28 17:51:52 PDT 2026`.

## 1. What is actually disproved

At the single EXACT finite privacy parameter `epsilon=log(2)`, with every Borel event and every shift in the full CLOSED unit l1 diamond D, there is an actual globally mean-l1-optimal generalized staircase law mu_mean and another explicitly specified feasible staircase law nu such that

    E_mu_mean ||X||_1 < = E_mu ||X||_1       for EVERY feasible Borel law mu,
    E_mu_mean ||X||_1^2 - E_nu ||X||_1^2 > 564269/8003167500,
    E_mu_mean ||X||_2^2 - E_nu ||X||_2^2 > 564269/12004751250.         (1)

Thus even a genuinely global FIRST-power l1-optimal Kulesza staircase cannot be blindly carried over as a squared-l1 or registered squared-Euclidean optimizer. The comparison is between TWO ACTUAL full-D-private Borel probability laws; it is not merely a mismatch between objective labels or a selected pointwise cost comparison. The strict lower bounds are rational, with no evaluated transcendental root.

This does **not** refute anything asserted in the PMLR paper: its printed theorem optimizes FIRST-power sensitivity norm, not the two squared losses. It does not say no other theorem/source could solve the registered problem, prove worldwide non-equivalence, or establish novelty/priority. It is not an independent reproof of the already supported all-law squared-Euclidean optimum.

## 2. Sources, exact inputs and named import

The PMLR source is the retained publisher PDF `institute/runs/three-area-2026-10-27-96h/public-sources/kulesza-suresh-wang-pmlr258-2025.pdf`, SHA-256 `4e67a46d80e705df6b23a92e8fb88599a8b14c874af3f7b434a0ed217ca71df3`. I visually re-opened my previously rendered page 3: its Definition 5 objective is the FIRST moment E||Z||_K, Definition 6 gives gamma in (0,1] and the generalized staircase, and Theorem 2 states existence of a staircase optimal at that objective. The source's proof NR-K17/NR-K10/other cuts remain as recorded; this note does not assert that every printed proof step was independently paid.

For unconditional GLOBAL mean-optimality at the present model I use the separate prior parent-WRITTEN_SUPPORTED alternative per-cost theorem, `institute/runs/three-area-2026-10-23-96h/privacy-MDA26-entire-norm-cost-and-weighted-decay-parent-v1.md`, SHA-256 `75614a6fc5cb66d9b26f13e64e58935fe6ea52121948e7a56592b91611576ac3`, §I: for ANY nonnegative nondecreasing matching-norm cost, some centered norm-staircase attains the infimum among ALL full-ball-private Borel laws. Here K=D and phi(r)=r, so its hypotheses actually match. This is the accepted supplied ALTERNATIVE proof at its written scope, not a claim that I repaired the printed MDA NR-A/NR-D proof. No LAW642, v241, v253, or original Euclidean optimizer theorem is an input.

The epsilon=log(2) substitution is an authorized exact finite example; it is not a prior selected-check outcome or novelty test. Exact arithmetic below uses Python `fractions.Fraction` and integer inequalities; no floats, root solver or external model.

## 3. Actual laws and exact scalar costs

Put b=1/2, m=b/(1-b)=1 and r(x)=|x1|+|x2|. For gamma in [0,1] define

    n_gamma(x)=min{k>=0: r(x)<=gamma+k},
    q_gamma(x)=Z_gamma^(-1) b^(n_gamma(x)).

At gamma=0, q_0=q_1 a.e. after normalization. For all gamma, `n_gamma(x+h)<=n_gamma(x)+1` whenever h belongs to the CLOSED D, and the reverse follows from −h. Hence q_gamma gives the actual Borel-event DP inequality for every h, including boundary shifts. Its moment is finite; no restricted shift grid or approximate privacy is used.

The exact radius-layer formulas and area `|rD|=2r^2` yield

    Z_gamma=2(gamma^2+2gamma+3),
    L(gamma)=E_q_gamma ||X||_1
      = (2/3)(gamma^3+3gamma^2+9gamma+13)/(gamma^2+2gamma+3),
    W(gamma)=E_q_gamma ||X||_1^2
      = (gamma^4+4gamma^3+18gamma^2+52gamma+75)
        /[2(gamma^2+2gamma+3)].                                        (2)

For every centered D-radial q_gamma, quadrant polar integration also gives

    J(gamma)=E_q_gamma ||X||_2^2 = (2/3) W(gamma).                      (3)

This angular identity is made ONLY for these actual radial densities, never for an arbitrary law. Positivity and normalization follow from the geometric-layer sum, including the endpoint law.

## 4. The unique mean-optimal staircase is an exact quartic root

Let `D_gamma=gamma^2+2gamma+3`. Direct differentiation gives

    L'(gamma)=(2/3) Q(gamma)/D_gamma^2,
    Q(gamma)=gamma^4+4gamma^3+6gamma^2-8gamma+1.                       (4)

Its nonzero coefficient signs `+,+,+,-,+` have two changes. Descartes' rule gives at most two positive roots counted with multiplicity. Exact evaluation gives

    Q(0)=1, Q(1/2)=-15/16,
    Q(7/10)=-479/10000, Q(71/100)=3036081/100000000, Q(1)=4.         (5)

Thus there is one positive root in (0,1/2) and a second in `(7/10,71/100)`; they are the only positive roots and both are simple. L rises, falls, then rises. Since q_0=q_1 as laws, their mean costs coincide, and the second root is the unique global minimizer over all gamma in [0,1]. Call this EXACT quartic root gamma_mean and define `mu_mean=Q_gamma_mean`.

By the named full-law matching-norm per-cost theorem, some centered staircase achieves the global mean-l1 infimum; the scalar uniqueness just proved forces that staircase to be mu_mean. Hence the first line of (1) holds for ALL original feasible laws. I do NOT need or claim that every other mean-optimal law is radial/unique. The same scalar computation identifies the staircase that the PMLR first-moment theorem would select, without attributing a squared-cost theorem to PMLR.

## 5. An explicit rational competitor and a positive gap

Differentiating W in (2) yields

    W'(gamma)=P(gamma)/D_gamma^2,
    P(gamma)=gamma^5+5gamma^4+14gamma^3+10gamma^2-21gamma+3.           (6)

The coefficient signs have two changes, `P(0)=3`, `P(1/2)=-93/32`, `P(1)=12`. Thus P has exactly two simple positive roots, the first below 1/2 and the second above 1/2. Exact evaluation at the RATIONAL competitor gamma_c=18/25 gives

    P(18/25)=-1692807/9765625<0.

It follows that P is negative throughout `[gamma_mean,18/25]`, since `gamma_mean in (7/10,71/100)` and `71/100<18/25`. Thus the actual feasible nu=`Q_(18/25)` strictly improves both squared costs by (3).

We can quantify this without any approximation to gamma_mean. On `[71/100,18/25]`,

    P'(gamma)=5gamma^4+20gamma^3+42gamma^2+20gamma-21
             >=42(7/10)^2+20(7/10)-21 =679/50 >0.

Consequently `-P(gamma)>=1692807/9765625`, while

    D_gamma<=D_(18/25)=3099/625.

The interval has exact length 1/100. Integrating `-W'` over that interval and using gamma_mean<71/100 gives

    W(gamma_mean)-W(18/25)
       > [1692807/9765625] / [100(3099/625)^2]
       = 564269/8003167500.                                              (7)

By (3) this gives the Euclidean squared-loss gap in (1). Direct substitution provides the RATIONAL comparator values

    E_nu ||X||_1^2 = 16085017/1291250,
    E_nu ||X||_2^2 = 16085017/1936875.                                   (8)

Since the original global Euclidean optimum V is no larger than the cost of this admissible nu, the same positive rational bound separates this actual mean-optimal staircase from the original Euclidean optimum. This conclusion does NOT require determining V or using the separately adopted diamond/rounded threshold.

## 6. Actual exact rational checks

The following bounded local Eval cell used Python `fractions.Fraction` only. It evaluates the displayed polynomial signs, comparator moments and rational gap; it does not solve a floating root or certify the named global per-cost theorem.

```python
from fractions import Fraction as F

def Qmean(g): return g**4+4*g**3+6*g*g-8*g+1
def Psq(g): return g**5+5*g**4+14*g**3+10*g*g-21*g+3
for g in (F(7,10),F(71,100),F(18,25)):
 print('gamma=',g,'Qmean=',Qmean(g),'Psq=',Psq(g))
m=F(1); g=F(18,25)
A=m+2*m*m; B=m+6*m*m+6*m**3; C=m+14*m*m+36*m**3+24*m**4
D=g*g+2*m*g+A; N=g**4+4*m*g**3+6*A*g*g+4*B*g+C
W=N/(2*D); J=F(2,3)*W
p0=-Psq(g); lbW=p0/(100*D*D); lbJ=F(2,3)*lbW
print('competitor W=',W,'J=',J,'Dmax=',D,'-P=',p0)
print('gap lower bounds W=',lbW,'J=',lbJ)
print('Pprime elementary lower bound=',42*F(7,10)**2+20*F(7,10)-21)
```

Actual arithmetic observed across the original cells:

```text
gamma= 7/10 Qmean= -479/10000 Psq= -62943/100000
gamma= 71/100 Qmean= 3036081/100000000 Psq= -4072390149/10000000000
gamma= 18/25 Qmean= 43801/390625 Psq= -1692807/9765625
b=1/2, squared-competitor gamma= 18/25 W_l1_squared= 16085017/1291250 J_euclidean_squared= 16085017/1936875
Dmax= 3099/625 -P(18/25)= 1692807/9765625 squared_l1_gap_lower_bound= 564269/8003167500 euclidean_squared_gap_lower_bound= 564269/12004751250
Pprime lower bound at g>=7/10 via 42g²+20g−21 = 679/50
```

The code block consolidates expressions from those cells; output labels are recorded as actually printed rather than pretending that exact block was itself separately rerun. Descartes, DP, global first-moment optimality and the strict integration argument are the written proof and named import, not established by this finite calculator check.

## 7. Exact source and assurance limits

The first failed direct PMLR-to-original-target edge is concretely stronger than “the costs are different”: at epsilon=log 2, the actual theorem-selected FIRST-moment optimal staircase loses to an explicitly admissible law under BOTH squared costs by the displayed rational margins. The PMLR theorem did NOT claim those squared optimizers; its validity is not refuted. Global first-moment attainment imports the named prior alternative proof. This candidate does not settle SOURCE-MATCH-U1 for other sources, priority or novelty, and no parent, independent-model, human, formal/kernel or full-proof executable acceptance follows from this write. Request a disjoint full proof review at these exact hypotheses and source bounds.
