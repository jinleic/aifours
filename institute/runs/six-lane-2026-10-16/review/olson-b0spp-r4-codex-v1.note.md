**DISPOSITION: ACCEPT-WITH-FIXES**

**0 FATAL / 0 MAJOR / 1 MINOR.**

- **MINOR — [SOURCE00:L55–56](/Users/jinleic/repos/aifours/institute/runs/six-lane-2026-10-16/review/olson-b0spp-r4-review-v1/snapshot/00-proof-B0SPP-r4.md:55): the asserted universal floor bound is false.**  
  \(g(E)\ge(E-1)/2\) fails at \(E=0\): \(g(0)=-\kappa<-1/2\). Concrete admissible word parameters are
  \[
  (p,\kappa,k,R)=(5,1,3,9),\qquad
  r=(0,1,8),\qquad \ell=(3,3,3).
  \]
  Reflection values \((0,1,2)\) make the empty run genuine. This counterexample concerns the displayed bound, not solvability.

  **Repair:** replace it with
  \[
  g(E)\ge\min\!\left(E-\kappa,\frac{E-1}{2}\right),
  \]
  or restrict \(g(E)\ge(E-1)/2\) to \(E\ge2\kappa-1\). The subsequent proofs separately handle truncated arguments and do not require the false universal bound. Thus this is a local correction.

The remaining mathematical checks pass.

**C1 — SOURCE00:L65–76.** Nonempty, nonfull interval windows supply the unique representatives defining \(c\). The identity
\[
\operatorname{gap}(Q^c)=p-\operatorname{gap}(Q)
\]
gives \(c(Q)+c(Q^c)=J\), with the stated normalization of \(J\).

Both split implications have the correct directions and endpoints. Writing \(a=c(Q_1)+c(Q_2)\), condition (A′) gives
\[
(c(Q)-a)p\ge g(m_Q)+g(R-m_Q)+2-p>-p,
\]
hence \(c(Q)\ge a\). Condition (B′) gives the corresponding inequality for \((a-c(Q))p\), hence \(c(Q)\le a\). These arguments permit negative gap endpoints and zero masses.

**C2 — SOURCE00:L77–85.** The four cases in part (a) independently establish the stronger bound
\[
g(m_1)+g(m_2)+g(m_3)\ge0.
\]
They include two zero masses at \(R=4\kappa+1\), where this sum can equal zero.

For part (b), any two pair sums total at least \(R>4\kappa\), so at most one is small. If none is small, their floor sum is \(R\) or \(R-1\), sufficient because \(R\ge p\). If \(s\le2\kappa\) is small, the complete parity calculation is:

| Parities | Exact sum \(g(s)+g(s')+g(s'')\) |
|---|---|
| \(s\) even; \(s',s''\) even | \(R-\kappa+s/2\) |
| \(s\) even; \(s',s''\) odd | \(R-\kappa-1+s/2\) |
| \(s\) odd; \(s',s''\) opposite parity | \(R-\kappa+(s-1)/2\) |

Thus the common lower bound is
\[
R-\kappa-1+\lceil s/2\rceil.
\]
It reaches \(p-2\) exactly when \(\lceil s/2\rceil\ge\Delta\), equivalently \(s\ge2\Delta-1\). The induction proving \(c(Q)\ge0\), followed by the complement identity, correctly yields \(0\le c(Q)\le J\).

**SIGMA-2P — SOURCE00:L86–92.** For \(\Delta\le0\), every split satisfies both rules, forcing all proper-interval \(c\)-values to vanish.

For \(\Delta>0\), disjointness puts the two heavy pairs in complementary proper intervals, each containing at least two runs. Throughout either singleton-extension chain, the growing interval retains one heavy pair and its complement retains the other. Consequently all three pair sums meet the threshold at every split. Both final \(c\)-values vanish, giving \(J=0\).

Cyclic wrap causes no exception: relabeling cyclically gives exactly these two chains. Pairs sharing a run do not qualify and cannot justify this partition. SOURCE00:L119–121 correctly illustrates the excluded case: for \((17,4,24,18)\), the run vector
\[
(0,3,0,\underbrace{1,\ldots,1}_{15},
\underbrace{0,\ldots,0}_{6})
\]
has only two heavy pairs, both containing the run of length \(3\). No avoidance claim about that example is needed.

**Assembly and reused proof — SOURCE00:L96–113; SOURCE01:L72–113.** The singleton-gap lower bound directly replaces the old prefix-lift argument. It gives
\[
0\le\delta_t\le2\kappa-2-r_t,\qquad
r_t+\delta_t\in2\mathbb Z_{\ge1}
\]
for every defect, including genuine empty defects. Together with \(\sum x_t=p\), these are precisely the lift properties used subsequently.

At \(\kappa=1\), the defect bounds contradict the necessary existence of a defect. Otherwise the two \(\Phi(Z)\) cases exhaust the possibilities because \(\Phi\) is even. All six kill inequalities check:

| Condition | Case I | Case II |
|---|---|---|
| U1 | Left side \(\le4\kappa\) | \(\le r_y+1\le2p\), or \(\le3\kappa-7<2p\) |
| U2 | Greedy threshold | Filler threshold |
| U3 | \(\delta_P\ge0\) | \(\delta_P\ge\kappa+1-(\kappa-1)/2>0\) |
| L1 | Left side \(\le4\kappa\) | \(\le4\kappa-4<2p\) |
| L2 | Left side \(\le4\kappa\) | \(\le2\kappa+r_y-7\), or \(\le4\kappa-4\) |
| L3 | \(\delta_P\le4\kappa-2\le R-1\) | \(\delta_P\le2\kappa-2\le R-1\) |

The L2 comparisons require only the weaker thresholds listed in SOURCE00:L105,L111–112, all implied by (H). Case II’s filler count, cyclic nonadjacency and properness remain valid with empty runs.

I found no unrepaired use of \(k\le p\) or of the discarded prefix lifts. In particular, the endpoint
\[
k=2p-2\kappa-1,\qquad R=4\kappa+1
\]
satisfies every replacement inequality.

**Containment and corollaries — SOURCE00:L22–31.** These are correct:

- After the trivial \(R\ge2p\) case, B0S implies (H) and \(\Delta<0\). The earlier containment error is repaired.
- The reported B0S+ hypotheses are contained in the \(\Delta\le0\) branch; its additional bound follows after the same cut.
- At \(\Delta=1\), P0 supplies at least two nonempty runs. On a cycle with \(k\ge4\), two distinct nonempty runs admit disjoint adjacent pairs containing them, including when those runs are adjacent.
- For \(k\ge p+1\), (H) gives \(2\kappa\le p-2\); parity sharpens this to \(\kappa\le(p-3)/2\).

The RES\(_<(p)\) corollary uses its reported defining properties directly. It does not close the remaining \(B=0\) cases, the \(B\ge1\) cases, or establish unrestricted reflection rigidity or ordered Olson.

Audited: the new lemmas, defect reconstruction, reused kill argument and stated consequences. Imported: the accepted arbitrary-pattern H0 instance, general P0, GRX and the reported residual definition. No finite aid or prior review verdict supplies a mathematical premise; no circularity was found. All seven snapshot SHA256 hashes match the supplied pins.