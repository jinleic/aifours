# Seven-state normal form and failure of three-moment closure

Clock actually observed before creation: **2026-10-23T15:10:36-07:00**. Owner MathResearch96h, math-1. Written reasoning only; no scientific program or proof assistant. This is a candidate necessary-structure/failed-route checkpoint, not a PH7 impossibility theorem or an additional problem slot.

## 1. Why the unrestricted residual cannot assume real hidden modes

For a hypothetical seven-state PH representation of the frozen H_(1,2) at z=b^2/(a-c)^2>1/2, the reduced transfer denominator has degree five, so

    det(sI-T)=(s+c)((s+a)^2+b^2)^2 Q2(s)

for a real monic quadratic Q2. The two hidden eigenvalues may be a stable nonreal conjugate pair; the supported complex-hidden C7 construction now explicitly demonstrates that possibility. A lower-bound proof restricted to two hidden real poles would miss actual realizations.

There are no unreachable states: trimming one would give order<=6, excluded by the supported B6 theorem. Every state also reaches an exit, since a closed no-exit transient subgraph would have a conservative final class and eigenvalue zero. The usual positive Perron-block lower contribution to the density therefore applies to every block.

The target inverse transform has leading term

    [K/((a-c)^2+b^2)^2] exp(-ct),

and all remaining terms are degree-at-most-one polynomials times exp(-at). Thus the spectral abscissa of T is -c: an accessible/coaccessible block with larger abscissa would give a positive exponential lower contribution incompatible with that asymptotic; -c itself is an actual pole and eigenvalue.

## 2. Candidate structural lemma: every such PH7 must be irreducible

Here is the full Frobenius-block counting argument. A real irreducible Metzler block has a real Perron eigenvalue, algebraically simple and with strictly greater real part than its other eigenvalues. If it contains -a+ib, it contains -a-ib as well and its Perron eigenvalue -r has c<=r<a.

The following spectral inequalities are the already proved trace mechanisms, not a PH-transfer assumption about a block:

- A three-state block with spectrum {-r,-a+ib,-a-ib} has b^2<=(a-r)^2/3. Indeed shifting by r, its trace is -2(a-r), while its squared trace is 2[(a-r)^2-b^2], at least the squared-diagonal sum, which is at least 4(a-r)^2/3.
- A five-state block with one real Perron eigenvalue and both copies of the desired pair has b^2<=(a-r)^2/5, by the analogous trace-square argument.
- A six-state block with spectrum {-r,-u,-a+ib,-a-ib,-a+ib,-a-ib}, where u>=r, has b^2<=(a-r)^2/2. This is the spectral content of B6's centered-moment proof: put d_r=a-r, Delta=b^2-d_r^2/2, h=(r+u+4a)/6-a>=-d_r/3. Its traces are

      tau2=6h(2d_r+5h)-4Delta,
      tau3=-12h(d_r^2+6d_r h+10h^2+b^2).

  For Delta>=0, tau2>=0 forces h>=0. At h>0, Lemma M's constant4/sqrt30 forces tau2^3>=270h^2R^2, contrary to

      270h^2[(3/2)d_r^2+6d_r h+10h^2]^2
        -[6h(2d_r+5h)]^3
       =54h^2[(45/4)d_r^4+58d_r^3h+90d_r^2h^2]>0.

  Hence Delta>0 is impossible. This argument uses only the stated block spectrum, Metzler trace identities and Perron ordering. It does not assume the block's transfer is H_(1,2).

If Q2 has nonreal roots, -c is the only real eigenvalue of the entire seven-state matrix. Every Frobenius block needs a real Perron eigenvalue. Thus there can be only one block.

If Q2 has real roots, distribute the two copies of the desired conjugate pair among the blocks. If separate blocks contain the copies, each block has size at least three, and with total size seven at least one has size three. Its bound gives z<=1/3 since a-r<=a-c, a contradiction. If one block contains both copies, its size is at least five. In a reducible seven-state matrix it has size five or six, and the displayed corresponding bound gives z<=1/5 or z<=1/2, again a contradiction.

These alternatives exhaust the real and nonreal Q2 cases, including a hidden pair coinciding spectrally with a visible pair. Consequently any actual PH7 at z>1/2 must be irreducible. In particular -c is algebraically simple and every hidden eigenvalue has real part strictly below -c.

This is a necessary reduction only. It neither excludes PH7 above the current construction endpoint nor makes its holding rates constant.

## 3. Exact failed lemma: the n=7 cubic moment bound cannot by itself bound z

It is tempting to repeat B6 using only the characteristic binding, Perron ordering and the generic n=7 inequality

    tau2>=0,
    tau3>=-(5/sqrt42) tau2^(3/2).                  (M7)

Those scalar conditions do not give a finite bound on z, even with real hidden modes.

Fix arbitrary c>0, d>0 and b>0, with no upper bound on b/d. For L>d consider the formal conjugation-closed spectral list

    -c,
    -(c+d)+ib, -(c+d)-ib, each twice,
    -(c+L), twice.                                (8)

Its dominant eigenvalue is uniquely -c, all entries are strictly stable, and its two extra eigenvalues are strictly subordinate real modes. This is only a **spectral list**, not an asserted Metzler or PH realization.

Center (8) by adding mu=c+(4d+2L)/7. Write q=(4d+2L)/7. The centered eigenvalues are

    q,
    q-d+ib, q-d-ib, each twice,
    q-L, twice.

Their sum is exactly zero. Directly from this finite list, as L tends to infinity,

    tau2/L^2 -> 10/7,
    tau3/L^3 -> -30/49.

The limits are literal leading coefficients: five scaled eigenvalues tend to2/7 and two tend to-5/7. The fixed imaginary parts divided by L tend to zero. Thus tau2>0 and tau3<0 for every sufficiently large L.

More importantly the squared skewness ratio tends to

    (tau3^2)/(tau2^3) -> 9/70,

whereas the square of M7's constant is25/42. The strict difference is

    25/42-9/70=7/15>0.

Continuity of these rational trace expressions consequently proves that, for every fixed b/d, all sufficiently large L satisfy M7 strictly. Equivalently its squared slack divided by L^6 tends to the positive constant

    [(25/42)tau2^3-tau3^2]/L^6 -> 1400/1029>0.

There is no finite-value test, presumed realization, or limit interchange hidden here: these are leading coefficients of fixed-degree polynomials in L.

Therefore any claimed elimination deriving a finite upper bound on z using **only** the degree-seven spectrum binding, strict Perron/Hurwitz ordering, tau2>=0 and M7 must be false. This is an exact obstruction to that proof route, not a counterexample to the book question, not a nonnegative-matrix realization theorem, and not evidence that PH7 can exist for arbitrary z. Further necessary conditions, such as additional spectral constraints, the transfer-preserving positive couplings or the relative-degree-five support graph, remain essential.

## 4. Dependencies and next actual obstruction

The supported B6 source is `proof-unrestricted-six-state-barrier-v1.md`, SHA256 `8ba04931bb26e9fec097cb75793aa99b2e5d4d2309da94e1be9328dacb830c25`. Its self-contained Lemma M supplies both constants above. The proposed irreducibility reduction in Section2 is new written reasoning at this checkpoint, not an inherited separate review. The failure in Section3 is an author-written scalar argument, also not formal or independently reviewed.

The next unrestricted lower-bound obligation must use information genuinely absent from (M7). A matrix with the formal spectrum (8) is not being offered; finding or excluding one still would not discharge the actual alpha/exit transfer conditions. The PH8 construction C8 remains a separate unreviewed upper-bound candidate at this freeze. No scientific execution or enumeration is proposed or admitted here.
