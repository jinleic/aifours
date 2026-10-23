# BOTTOM close: exclusion of the whole e=(p+1)/2 cell, v1

Owner OlsonPP1Exclusion. Written after /bin/date 2026-10-19T18:54:15-0700. CANDIDATE_UNVERIFIED FULL PROOF for the specified cell, not an
accepted result or a full ordered-Olson proof. Same pre-derivation scope BOTTOM-scope-v1.md SHA256
ab9ee0251454d4242b2d268e73eacacf875df6172467f3a24fef6c3cbc22d99e (2026-10-19T18:30:34-0700) and transition
RUN/control/written-olson-upperhalf-bottom-transition-v1.json SHA256
a0deb9816a303dc65d75b7728889696e2dcc2cfb3e53d25a570eae9374be586f.

Read together with proof-BOTTOM-parity-v1.md SHA256 b648411f7ed7b2b17fdd9bcc4a51f2df24ca7a1540eb88cd4c7fbd2e6080a9f3 ("P").
This companion COMPLETES that earlier labelled partial; it does not edit it. Every used P claim is proved inline in this
same bottom-cell proof unit, from the accepted inputs in P Sec. 9 (NF, GRX if, RS(b), CD, UH-A/E at literal scopes). No
unreviewed RUH3/RUH2/KP3/KP4/R7 result is a premise. No scientific computation/enumeration, script, assertion, solver, Lean,
model CLI or nested agent. No novelty/priority/first/human-review claim. Parent owns review and verdict.

## 0. Theorem and exact antecedent

THEOREM BOTTOM [NEW]. For every prime p>=11, let e=(p+1)/2 and kappa=(p-1)/2. Under the FULL antecedent (a length-(4p-2)
avoider over D_(2p) has SOME admissible NF with terminal k=p+1 and kappa_hat=kappa; all H=e-1 extra reflection pairs may lie
anywhere in the odd blocks; empty NF runs separate different reflection values), no case A=p-1+c with 3<=c<=p-1 exists.
No o_F, nonempty-run, reflection-rigidity or rotation-pair hypothesis is added. There is no multiset-only assertion outside
this word/NF antecedent.
COROLLARY BOTTOM. For every prime p>=11 no length-(4p-2) avoider has an admissible NF with terminal k=p+1 and
kappa_hat=(p-1)/2. (P Sec. 1, using accepted UH-A, forces the displayed c-range.)

Notation from P: N=p+1=2e runs, R=2p-2=2N-4 rotation letters, A=p-1+c, A'=p-1-c-delta, d(P)=sum_P(alpha_i-beta_i),
d(all)=2c+delta, k0=floor(e/2)+1. Every proper nonempty set is low (d<=c-1) or high (d>=c+1+delta), complements swap types.
For a low set put g=c-d>=1. With g=2r+1 odd, a LOW CRITICAL pattern has
  1<=g<=e-1,  r+1<=m(P)<=e-r.
P Lemma C proves: all its signed values are a,-a,3a; its signed a-multiplicity is phi=p-1+g, minority w0=p-1-g;
and 2T(z_P)=D_z. For even g=2r>=2, no low pattern has r+1<=m<=e-r (MW has q=g+1). These hold for the whole displayed
m-window, not just m<=k0. P Theorem E0 proves every run nonempty; hence with s1 the number of singleton rotation runs,
  s1=4+sum_(L_i>=3)(L_i-2)>=4.                                                (LEN)
Only P Secs. 1-5 and this identity are load-bearing below; P's later necessary-profile assertions are not needed.

## 1. Minimal interior critical pattern [NEW]

Call a low critical pattern INTERIOR if
  g=2r+1,   r+2<=m(P)<=e-r-1.                                                 (IC)
If one exists, choose its smallest g (ordinary minimum of a nonempty finite set of integers, no enumeration performed).
We show that its two m-boundaries must coincide.

(1) Every singleton rotation run is signed -a under z_P.
Indeed Lemma C gives only a,-a,3a. Flipping a singleton signed a decreases g to g-1; if g=1 this gives d=c, forbidden by (W).
Otherwise g-1=2r is even, and the new interval count m' lies in [m-1,m+1] subset [r+1,e-r], the forbidden even window.
Flipping a singleton signed 3a keeps g unchanged (its original letter is outside {a,-a}), and m' stays in [r+1,e-r], so
Lemma C would apply to a pattern containing signed -3a, impossible for p>=11. Thus all singleton runs are signed -a.
Flipping one of these increases g to 2r+2, whose forbidden even window is EXACTLY [r+2,e-r-1]. So the new m' must leave
that interval.

(2) If m is strictly between the boundaries of (IC), every flip has m' in that interval, impossible by (1) and (LEN).
If m=r+2<e-r-1 (sole lower boundary), every singleton flip must have m'=m-1, so each such vertex is an isolated sign vertex
of P or P^c (its neighbours have the opposite sign). There are 2m maximal sign intervals in the cycle; since N=2e>2m at
least one has length >1, so at most 2m-1=g+2 vertices are isolated. Hence s1<=g+2.
If m=e-r-1>r+2 (sole upper boundary), every singleton flip has m'=m+1, so it is FLAT (same sign as both neighbours). If
l_1,...,l_(2m) are the lengths of the maximal sign intervals, the number of flat vertices is
  sum_j max(l_j-2,0)=N-4m+s_sign1 <= N-2m-1=g,
where s_sign1 counts singleton sign intervals and is <=2m-1 because N>2m. Hence s1<=g.
In either sole-boundary case (LEN) implies sum_(L_i>=3)(L_i-2)<=g-2, so EVERY rotation run has L_i<=g. If g=1 this is already
impossible (LEN requires >=4 singletons but the displayed bounds allow at most 3 or 1); otherwise keep this length bound.

(3) There is a pure signed-a run: every run not pure signed a contains a minority letter, so at most w0=p-1-g of the N=p+1
nonempty runs can be non-pure; at least g+2 are pure signed a. Such a run cannot be a singleton by (1); choose one, of length
2<=L<=g by (2). Flipping it changes g to g'=g-L in [0,g-2] and m to m' in [m-1,m+1] subset [r+1,e-r].
- If g'=0, (W) is violated.
- If g'=2r'>=2 is even, L is odd >=3, so r'<=r-1; m' lies in [r'+1,e-r'], the forbidden even window.
- If g'=2r'+1>=1 is odd, L is even >=2, so r'<=r-1; m' lies in [r'+2,e-r'-1], giving a smaller INTERIOR low critical g'.
  This contradicts the minimal choice of g.
Thus neither sole boundary can occur. The boundaries must coincide:
  r+2=e-r-1,  e=2r+3=g+2 is odd,  g=e-2,  m=(e+1)/2.                          (TOP)

Consequences. If e is even, NO interior low critical pattern exists. If e is odd and any interior one exists, its minimum
g is e-2, while (IC) always gives g<=e-2. Thus EVERY interior low critical pattern has exactly the parameters (TOP).
The singleton statement (1) did not use minimality and holds for every interior low critical pattern.

## 2. Small-m caps and a large rotation run [NEW]

Recall the window fact proved in P Sec. 2: for 1<=m<=k0, a violation of the cap-e low bound
  d(P)<=c-min(e,2m-1)
has odd g<=min(e-1,2m-2), with r<=m-2. Such an escape is interior unless e is even and
  g=e-1, m=k0=e/2+1;
this follows directly from m+r<=e-1 for e odd, and m+r<=e with equality only in that exceptional even case.
By Sec. 1, for e even the only possible escapes have g=e-1, m=k0. Therefore all low sets with m<=k0 obey
  d(P)<=c-min(e-1,2m-1).                                                      (EV)
For e odd, every escape is interior, so Sec. 1 forces g=e-2, m=k0=(e+1)/2. Therefore all low sets with m<=k0 obey
  d(P)<=c-min(e-2,2m-1).                                                      (OD)
For clarity, a violation of either displayed weakened cap would have a strictly smaller g, hence would be one of the
forbidden escapes just classified (even g was already excluded by MW).

Large-run lemma. If all low sets with m<=k0 obey d<=c-min(ell,2m-1) for ell in {e,e-1,e-2}, then some run h has
  d_h>=2ell+delta, and hence L_h>=2ell+delta.                                  (LR)
Proof: at m=k0, 2k0-1>=e, so low sets have d<=c-ell; complements give high sets d>=c+delta+ell, a gap 2ell+delta. The
single-run-toggle path of P Sec. 4 exists at m=k0, since N=2e>=2k0+2; its endpoints are complements. Orient low to high.
Some step crosses the gap. A removal could increase d by at most A'<=e-1<2(e-2)<=2ell (e>=6), so the crossing adds a run h,
with d_h>=2ell+delta. This proof uses NO single-toggle path at m=e. []

With E=0, a run always has L_h<=R-(N-1)=p-2 because all p other runs are positive. Therefore absence of every escape is
impossible: it would give ell=e, and (LR) would give L_h>=2e+delta=p+1+delta>p-2. Thus at least one escape exists. In the
odd-e case, at least one interior low critical pattern consequently exists and has (TOP).

## 3. Contradiction in both parity cases [NEW]

If e is even, use (EV) and (LR) with ell=e-1. Then
  L_h>=2e-2+delta=p-1+delta>p-2,
contradicting the positive-run bound. So no even-e avoider exists.

If e is odd (e>=7), use (OD) and (LR) with ell=e-2. Then L_h>=p-3+delta. The p other positive runs have total length at most
  R-L_h <= (2p-2)-(p-3+delta)=p+1-delta.
If s_other counts their singleton runs, their total length is at least s_other+2(p-s_other)=2p-s_other, so
  s1>=s_other>=p-1+delta.                                                     (MANY)
But an interior critical pattern exists and has g=e-2 by Sec. 2. By Sec. 1(1) EVERY singleton rotation run is signed -a at
that pattern. Its ENTIRE signed minority has only
  w0=p-1-g=p-1-(e-2)=p+1-e=e
letters. Hence s1<=e. This contradicts (MANY), since p-1=2e-2>e. (If the length bound already exceeds the total budget for
some delta, that is an earlier contradiction, not a separate case.)

Both parities are impossible. This proves Theorem BOTTOM. Corollary BOTTOM follows because P Sec. 1 and accepted UH-A force
the full c-range under exactly its literal existential-NF antecedent. []

## 4. Verification boundary

The full proof unit is P Secs. 1-5 plus this companion: critical row rigidity; exclusion of empty runs using the exact
missing-set interval and position bounds; singleton counting, minimal interior g and the m=k0 path above. This is a new
written CANDIDATE, not a parent or model verdict, and is not Lean-checked. No prior candidate is promoted by it. It excludes
only terminal k=p+1, kappa_hat=(p-1)/2, prime p>=11 with the full NF/word antecedent; no lower-half, o_F, unrestricted
normalisation/inverse theorem, full ordered Olson, novelty or priority claim follows. The earlier failed-route regime is
preserved in residual-BOTTOM-v1.md; its apparent remaining regime is closed by the present companion, subject to review.
