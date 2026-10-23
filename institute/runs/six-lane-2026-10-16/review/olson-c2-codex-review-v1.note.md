VERDICT: ACCEPT

The SHA256 matches. I found no fatal, major, or minor mathematical gap. LF references below refer to the pinned [proof-C2.md](/Users/jinleic/repos/aifours/institute/runs/six-lane-2026-10-16/review/olson-c2-parent-inputs-v1/mixdef-high__c2__proof-C2.md).

1. **R2 arithmetic and Claim 1″ — L20–26.**  
   \(E=R-k=W-3\), hence \(r_t\le E+1=W-2\). Since each nonsingleton consumes at least one excess unit, there are at least \(k-E=2k-2p+2\ge4\) singletons. The congruences for \(W\) follow from \(W=2p-2\kappa-1\) and odd \(p\).

   Write \(\kappa=2h\): then \(m_0=h+1,M=2h\), and
   \[
   \kappa+1-m_0=h=M/2,\qquad (R-M)/2=p-m_0.
   \]
   For \(\kappa=2h+1\), \(m_0=h+1,M=2h+2\), giving
   \[
   \kappa+1-m_0=h+1=M/2,\qquad (R-M)/2=p-m_0-1.
   \]
   Thus both competing terms are at least \(E'/2\) for each even \(E'\in\{x,R-x\}\). The claimed equality \(g(x)+g(R-x)=p-1\) is correct.

2. **Moves, initial cuts, and rotation tail — L10–13, L27–34.**  
   Moving a cut onto an adjacent free reflection position replaces exactly one boundary edge and toggles exactly the intervening rotation run. The boundary count remains \(2m\), so the block count remains \(m\); the change in \(x\) is \(\pm(a_u-b_u)\), bounded by \(r_u\).

   The four prescribed cut/free positions are distinct. After fixing two cuts and two free positions, completion requires \(2m_0-2\le k-4\), precisely \(k-2m_0\ge2\). That difference is \(\kappa\) for even \(\kappa\), and \(\kappa+1\) for odd \(\kappa\).

   The stated rotation order is legal. Before \(c\) moves, it remains at \(S_{s-1}\), while \(S_s\) remains free. After \(\tau\), \(c\) crosses \(s,s^+\), then \(i^*\) crosses \(s^-\). These are exactly the remaining three toggles. More generally, the rotation crosses each run exactly once because its traversed arcs partition the cycle. Consequently the tail bound is
   \[
   1+r_{s^+}+r_{s^-}=3+\operatorname{ex}(s^+)+\operatorname{ex}(s^-)\le W.
   \]

3. **R2 entry indices and parity repair — L35–46.**  
   For even \(\kappa\), \(x_0\le\kappa-1\) implies
   \(x_\tau\ge R-x_0-W\ge\kappa\). First entry therefore occurs by \(\tau\), with
   \(x_j\le\kappa-1+(W-2)=R-\kappa-2\). The upper-side argument is symmetric. Odd values in \(Z\) lie strictly between its even endpoints, so either singleton toggle lands on an even value inside \(Z\).

   For odd \(\kappa,W=3\), every run is singleton and the complementary endpoints straddle the integer midpoint \(\kappa+1\); unit steps must meet it. For \(W\ge7\), the improved tail bound yields \(x_\tau\ge\kappa+1\) when \(x_0\le\kappa\). Steps are at most \(W-2=|Z'|\); skipping an interval of \(L\) integers requires a step of at least \(L+1\). Thus entry cannot overshoot \(Z'\). Its endpoints are even, so the singleton repair again stays inside.

4. **Claim 3 — L47–51.**  
   Here \(E=W-3\ge4\). Adjacent singletons force some neighbouring nonsingleton \(u\) to carry at least \(E-1\) excess. Among at least four singletons, one is not adjacent to \(u\); its neighbours carry at most \(1\), contradicting the assumed lower bound \(E-1\). If singletons are isolated, they occupy distinct slots between \(q\) nonsingletons. The other \(q-2\) nonsingletons carry at most one excess unit, forcing \(q\le3\), again contradicting four singletons.

5. **BR Steps 0–2 — L65–82.**  
   Swapping the rotation signs sends \(x\) to \(R-x\) and preserves all relevant hypotheses and window widths. Since \(\operatorname{ex}(u)\ge W\), other runs satisfy \(r_v\le j\). Also
   \[
   j\le2p-k-2=W-3\le k-4,\qquad B\ge j+1.
   \]
   All nine term-pair inequalities in Step 1 hold. In particular the mixed linear/floor sum is at least
   \[
   (x+2m-3-2\kappa+R)/2\ge p-1
   \]
   using \(x\ge k+1-2m\). The three alternatives defining \(M_m\) give interval sizes at least \(j+3,j+3,j+1\), respectively.

   The jump lemma is sound: \(u\) is toggled exactly once, removing it lowers \(x\), and every other step has magnitude at most \(j\). If no earlier window is met, the eventual endpoint above \(R-M_m\) forces entry.

6. **BR cases (2), (2′), (3) — L83–97.**  
   \(Q_0\) has exactly \(c\) cyclic blocks because excluded \(u\) separates the end stretches; \(x(Q_0)=B+N_\alpha=k-1+\epsilon\). Case (2)’s three lower bounds follow as written.

   In (2′), \(k=2c\) forces \(k=p+1\), with every block and gap one run. The removed stretch is aligned, and its excess is included in \(\epsilon\), giving \(x(Q)\ge k-2=p-1\ge M_{c-1}\).

   In (3), \(m_{\max}\) satisfies the window range, \(M_m=\kappa\), and \(k\ge2m+1\). Moreover
   \[
   \tau\le(k-j)/2-1,\quad N_\alpha-\tau=(k-j)/2-1+\epsilon\ge\tau.
   \]
   The largest-mass selection and the alternative \(B\ge2m_{\max}>\kappa\) are valid. Selected stretches remain distinct cyclic blocks.

7. **BR case (1) — L98–106.**  
   Each flip creates two permanent boundaries, so neither that run nor its neighbours can later qualify. Excess losses are therefore charged only once, proving \(x(Q)\ge k-1-c_{\rm lo}+c\). The no-eligible-run counting contradiction is correct; when \(b=0\), eligibility is immediate.

   For \(c=0\), the displayed hypotheses imply \(3k+j\ge4p+4\); combining this with \(j\le2p-k-2\) gives \(k\ge p+3\). This supplies the needed exceptional inequalities. All three lower bounds for \(M_{c_{\rm lo}}\), and \(k\ge2c_{\rm lo}+1\), follow.

8. **FW+ — L119–123.**  
   The split is exhaustive. FWH permits arbitrary rotation letters and arbitrary \(B\); its applicable clauses require only the supplied \(k\ge p+1\ge6\). The oversized threshold is exactly the integer complement of \(|d_u|\le W\). BR’s hypotheses match, and NMH supplies all stronger sign-count restrictions.

Independent in-memory arithmetic and cut-rotation checks also passed; recorded finite-check results were not used as premises.