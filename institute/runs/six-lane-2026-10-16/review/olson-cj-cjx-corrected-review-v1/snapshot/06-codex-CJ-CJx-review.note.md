1. **MINOR — [SOURCE00:12–17,71–72](/Users/jinleic/repos/aifours/institute/runs/six-lane-2026-10-16/review/olson-b0scjx-r3-review-v1/snapshot/00-proof-B0SCJx-r3.md:12): Corollary 2 cannot extend entirely “verbatim.”** Its automatic condition \(4\Delta\le2\kappa+7\) uses the original \(R\ge4\kappa+1\). Under the extension,
   \[
   R=p+\kappa-1-\Delta\ge4\kappa-4
   \quad\Longrightarrow\quad p\ge3\kappa-3+\Delta.
   \]
   The old shortcut fails at
   \[
   (p,\kappa,R,\Delta,k)=(13,4,13,3,21):
   \quad4\Delta=12\le15,\qquad p=13<14=\kappa+5\Delta-5.
   \]
   **Repair:** retain that shortcut explicitly under the original \(R\ge4\kappa+1\), or replace it under \((H''')\) by the sufficient condition \(4\Delta\le2\kappa+2\). The exclusion of the \(p\le23\) sentence does not address this separate clause.

2. **MINOR — [SOURCE01:29–31](/Users/jinleic/repos/aifours/institute/runs/six-lane-2026-10-16/review/olson-b0scjx-r3-review-v1/snapshot/01-proof-B0SCJ-r1.md:29): the unqualified implication \((D)\Rightarrow(2HA)\) omits the \(\Delta\le0\) branch.** For example,
   \[
   p=5,\qquad w=\rho_1^{11}\sigma_0^7
   \]
   has \(\kappa=1,\ k=1,\ \Delta=-6\), satisfies \((H)\) and \((D)\), and has no proper run interval at all.
   
   **Repair:** write “For \(\Delta\ge1\), the two-pair branch of \((D)\) implies \((2HA)\); the \(\Delta\le0\) branch is already shared by both theorems.” The containment of the theorem remains valid.

3. **MINOR — [SOURCE01:100–101](/Users/jinleic/repos/aifours/institute/runs/six-lane-2026-10-16/review/olson-b0scjx-r3-review-v1/snapshot/01-proof-B0SCJ-r1.md:100): the assertion that \((2HA)\) fails for the “all-ones words” at \((31,7,6)\) needs correction.** Take
   \[
   r=(1^{31},0^{14}),\qquad k=45,\quad R=31,\quad 2\Delta-1=11.
   \]
   Then \(S_1=[1,11]\) and \(S_2=[12,22]\) are disjoint heavy admissible intervals. Admissibility witnesses are \(x_1=21\) and \(x_2=1\), respectively; both required masses equal \(11\) in each case. This is realizable with odd block lengths \((47,1^{44})\) and genuine empties, for example using \(y_i=i\bmod31\).

   **Repair:** describe these triples as failures of the *numerical Corollary 2 condition*, and remove the blanket failure claim about \((2HA)\). The count of 43 such numerical triples is unchanged.

**SOURCE01 — DISPOSITION: ACCEPT-WITH-FIXES.**  
**0 FATAL / 0 MAJOR / 2 MINOR.**

**SOURCE00 — DISPOSITION: ACCEPT-WITH-FIXES.**  
**0 FATAL / 0 MAJOR / 1 additional MINOR; apply the base corrections above.**

The main theorem arguments pass with these local corrections.

- **Base Lemma CJ and assembly:** Both outward growth chains satisfy all three pair-mass requirements. The chosen \(x\) keeps every split proper, including cyclic wrap and zero-mass runs. The final superadditivity step gives \(c(Y_1^c)=0\), hence \(c(S)=J\). Two disjoint heavy admissible intervals then give \(J\ge2J\); since \(J\ge0\), \(J=0\). SOURCE02 §3 consequently applies with \(x_t=w_t\).

- **C1/C2 and singleton reconstruction:** The gap/complement identity and both split inequalities have the correct directions and endpoints. Negative representatives and zero masses cause no exception. The SOURCE02 r5 floor-bound erratum is sufficient; no subsequent argument requires the removed universal bound. The reconstructed defects satisfy exactly the properties used by SOURCE03’s Cases I/II.

- **Exact two-small \((A')\):** For \(T=m_3>2\kappa\) and \(m_1,m_2\le2\kappa\),
  \[
  \sum_i g(m_i)=R-2\kappa-\lceil T/2\rceil\ge-2
  \iff m_1+m_2\ge4\kappa-4-R.
  \]
  Thus this case holds throughout \(R\ge4\kappa-4\). The other cases also pass: the three-small case needs \(R\ge3\kappa-2\), which follows here using \(R\ge5\) for small \(\kappa\). In particular, C2(a) holds at \(R=4\kappa-3\).

- **Exact two-small C2(b):** If the two small pair sums share mass \(m_b\), their contribution is exactly
  \[
  \left\lfloor\frac{3R+m_b}{2}\right\rfloor-2\kappa.
  \]
  It reaches \(p-2\) iff
  \[
  3R+m_b\ge2p+4\kappa-4.
  \]
  This follows from \(R\ge p,\ R\ge4\kappa-4,\ m_b\ge0\). The none-, one-, and three-small cases also pass.

- **Last greedy step and exact (L3):** Adding the last defect changes the interval count by \(+1,0,-1\), giving respective bounds
  \[
  (\Phi,m):\quad
  (\le4\kappa,\ge2),\quad
  (\le4\kappa-2,\ge1),\quad
  (\le4\kappa-4,\ge1).
  \]
  Consequently,
  \[
  \delta_P\le4\kappa-4-\rho_P,\qquad
  \Phi(P)-4m(P)\le4\kappa-6.
  \]
  Because \(\delta_P\equiv\rho_P\pmod2\), SOURCE03:75’s exact (L3) is equivalent to \(\delta_P\le R\). The new bound establishes it down to \(R=4\kappa-4\), including \(\rho_P=0,\delta_P=R\). For the cardinality claim, apply the defect lower bound to \(P'\): \(|P'|\le\kappa-1\), hence \(|P|\le\kappa\). Properness also follows directly from \(P\subseteq Z\subsetneq[k]\).

- **(L2) and Case II:** Case I’s sharper bound needs \(R\ge3\kappa-2\). Case II’s stated bound \(4\kappa-4\) needs \(R\ge3\kappa-1\). Both follow from the extension hypotheses: use \(4\kappa-4\) for \(\kappa\ge3\), and \(R\ge p\ge5\) for \(\kappa\le2\). The singleton filler comparison, filler count, nonadjacency, properness, and remaining kill inequalities all check. No unrepaired use of \(k\le p\) remains.

The edge-cell treatment is correct. From \(R\ge4\kappa-4,\ R\le2p-1\), failure of \(2\kappa\le p-1\) leaves precisely
\[
\kappa=(p+1)/2,\qquad R\in\{2p-2,2p-1\}.
\]
There \(\Delta\le-1\), so the interval argument gives \(J=0\). The remaining unproved checks are exactly Case I’s (U1)/(L1): a violation requires \(\Phi=4\kappa=2p+2\), with respectively \(\delta_P=0\) or \(\rho_P=0\). These cells remain excluded.

The coverage counts check by direct integer counting. Write \(R=4\kappa-j\), \(0\le j\le4\). Non-edge cells have
\[
\lceil p/4\rceil\le\kappa\le(p-1)/2,\qquad R\ge p.
\]
For \(\Delta\ge2\), failure of the displayed parameter criterion is equivalent to
\[
14\kappa<4p+5j-10.
\]

| \(p\) | Non-edge cells | Fail numerical criterion |
|---:|---:|---:|
| 5 | 4 | 0 |
| 7 | 7 | 0 |
| 11 | 12 | 0 |
| 13 | 14 | 1 |
| 17 | 19 | 1 |
| 19 | 22 | 2 |
| 23 | 27 | 2 |
| 29 | 34 | 2 |
| 31 | 37 | 4 |
| 37 | 44 | 4 |
| 41 | 49 | 5 |
| 43 | 52 | 5 |
| 47 | 57 | 7 |
| 53 | 64 | 7 |
| 59 | 72 | 9 |
| 61 | 74 | 9 |
| **Total** | **588** | **58** |

The bottom two \(R\)-levels contribute \((p-3)/2\) cells per prime, totaling **224**. There are **32** excluded edge cells. Both \((7,3,8,1,12)\) and \((7,3,9,0,11)\) are covered. The base’s \(p\le23\) conclusion under its original hypothesis, its 12 listed triples through \(43\), and its total of 43 through \(61\) also check.

Audited here: SOURCE01’s mathematical argument and consequences, SOURCE00’s replacement estimates, SOURCE02’s setup/C1/C2/kill argument, SOURCE03’s reused kill algebra, and the needed GRX-to-H0 specialization. Imported premises remain P0 from SOURCE04:73–75, the foundational solvability criterion, and the reported residual-class scope; the external Theorem P and unrelated K0*/MXG arguments were not re-audited.

E14/E14b supply no premise: removing their descriptions leaves every proof step intact. Their numerical outputs were not validated. All eight supplied SHA256 pins match; only snapshot static reads and hashes were used.