# At ln 2, the J-optimal mechanism is not the closest TV repair

**AUTHOR CANDIDATE — WRITTEN plus exact Fraction checks; NOT independently reviewed or parent-adopted.** Native pre-write observation: `Wed Oct 28 20:24:13 PDT 2026`.

## 1. Exact concrete comparison and named assumptions

At epsilon=ln 2 let `gamma=3^(1/3)-1` and let Q be the product of two actual 1D epsilon-private gamma-staircases. Q is an auxiliary product, NOT a pure-full-D 2D law. Take the ACTUAL pure-full-D radial staircase P_repair with offset

    eta=2gamma-1/2.                                                       (1)

Its exact finite-epsilon total-variation distance from Q is

    TV(Q,P_repair)
       =2gamma(1-gamma)(12gamma^2+5)
          /[(gamma+1)^2(16gamma^2+8gamma+9)]
       in (111217186059/10^12,111217186060/10^12).                        (2)

The unreviewed target comparison `frontier-20261028-ln2-target-vs-marginal-product-tv-v1.md`, SHA-256 `622ec43783deb6d2e0d3b969926ae202461a874e026b0f72abc4e1fe2a45da6a`, conditional on its named parent v253/v241 and cde9 inputs, gives for the true original 2D J-optimal P_J

    TV(Q,P_J)>140433557476/10^12.                                        (3)

Consequently, conditional on those inputs, an explicitly constructed full-D-private law P_repair is closer to Q in TV than the true all-law J optimizer, by MORE than 7/250. The interpretation of Q as a product of two individually J-optimal 1D marginals additionally uses the named cde9 result. The exact law-to-law formula (2) itself is source-independent. No claim that P_repair is the globally closest private law is made.

## 2. Exact shell geometry for the repair

At b=1/2, m=1, exact cube inequalities give `0<eta<gamma<1/2`. Define the normalizer ratio

    C=Z_repair/Z_1^2
      =(eta^2+2eta+3)/[2(gamma+1)^2],       1/2<C<1.

The product/radial density ratio is `q/p=C b^k`, with k=n1+n2-n_R in {-1,0,1}. Hence Q exceeds P_repair EXACTLY on k=-1, equivalently `u1+u2>eta`, where `|x_i|=n_i+u_i`, `u_i in [0,gamma]` for n_i=0 and in [gamma-1,gamma] otherwise.

For both n_i positive, the high triangle has area `(2gamma-eta)^2/2=1/8`. For exactly one zero index its area is `3gamma^2/2-gamma eta`; for both zero indices its area is `gamma^2-eta^2/2`. Summing the four sign quadrants and geometric weights at m=1 simplifies exactly to

    Q(k=-1)=2gamma(1-gamma)/(gamma+1)^2.

On the high region p/q=b/C, so `TV=Q(k=-1)(1-b/C)`. Substituting eta=2gamma-1/2 simplifies to (2). No assumption of optimizer structure is used for this actual trial.

## 3. Actual checks and limits

The Python eval kernel used `fractions.Fraction` and the bracket `gamma in (4422495703074083823216,4422495703074083823217)/10^22` to verify the cubic root, eta regime, 1/2<C<1 and outward bounds for (2). It checked that the lower endpoint in (3) minus the upper endpoint in (2) exceeds 7/250. A first helper call completed the interval checks but then raised `TypeError` because an existing Decimal variable shadowed a function name; the failed regime-check step alone was rerun successfully with a new helper. A separate Decimal illustration gave TV≈0.1112171860592075; it is not the certificate.

The exact comparison (2) is WRITTEN with exact finite arithmetic checks; (3) and its original-optimal interpretation have their explicitly named parent/unreviewed dependencies. No formal, independent review, novelty, source-equivalence, exact nearest-private solution or parent adoption is claimed. Suggested review: k range, both central triangles, normalization and outward rational bounds.
