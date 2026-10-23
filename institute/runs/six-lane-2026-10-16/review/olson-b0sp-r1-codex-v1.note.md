**DISPOSITION: ACCEPT-WITH-FIXES**

**0 FATAL / 0 MAJOR / 1 MINOR.**

- **MINOR — SOURCE00:L16–18: the literal containment justification needs qualification.**  
  The B0S hypotheses do not automatically imply (H2)–(H3) before removing the trivial \(R\ge2p\) case. For example,
  \[
  (p,\kappa,k,R)=(5,3,5,11)
  \]
  satisfies B0S’s hypotheses, but \(11<4\kappa+1=13\) and \(2\kappa=6>p-1=4\). These parameters are realized by reflection-block lengths \((3,1,1,1,1)\) and rotation-run lengths \((3,2,2,2,2)\).

  **Repair:** replace L16 with: “B0S follows from B0S+ together with the trivial \(R\ge2p\) case. After assuming \(R\le2p-1\), \(k\le p\) implies (H1)–(H3).” The stated conditional theorem is unaffected.

The extension under **(H1)–(H3) checks out**. I found no unrepaired use of \(k\le p\) in SOURCE01 Sections 1–5.

**Set-up and windows — SOURCE01:L38–56; SOURCE00:L24–33.**

All blocks odd gives \(F=2H+k\), hence
\[
R=4p-2-(2H+k)=2p-k+2\kappa.
\]
After the rotation-only solution removes \(R\ge2p\), integrality gives
\[
R\le2p-1,\qquad k\ge2\kappa+1.
\]
Thus these are valid reductions.

Both replacement facts are correct:
\[
\begin{aligned}
\text{(F1)}\quad
R-\kappa-1&=2p-k+\kappa-1\ge p-2,\\
R&\ge p+\kappa-1\ge p;\\
\text{(F2)}\quad
2p-k&=R-2\kappa\ge2\kappa+1\ge3.
\end{aligned}
\]
Also, (H2) is exactly \(k\le2p-2\kappa-1\).

The complete dependency check is:

| SOURCE01 location | Former consequence or requirement | SOURCE00 replacement; assessment |
|---|---|---|
| L39–40 | \(p\ge2\kappa+1\) | Explicit (H3); correct |
| L40 | \(R\ge p+2\kappa\), \(R-\kappa-1\ge p-1\) | Weakened to (F1); subsequent steps need only \(R-\kappa-1\ge p-2\) |
| L41–43 | Redundancy of the \(p-1\) cap in \(g_1\) | Uses only \(E\le R\le2p-1\); unchanged |
| L47–51 | Positive window sums | Re-established by (H2)/(F2); correct |
| L53–56 | Unique prefix representatives and \(\sum bh=k-2\kappa\) | Avoidance and the window bounds suffice; no bound \(k\le p\) |
| L57–63 | Eight Step 1 branch bounds | Replaced correctly by four possible branches |
| L64–68 | Defect bound, parity and empty-defect bounds | Uses \(R<2p\), integrality and genuineness; unchanged |
| L72–81 | Kill equivalences, proper/nonempty \(Z\), \(\kappa=1\) | Generic; no small-\(k\) requirement |
| L85–89 | Case I numerical bounds | Correctly replaced by (H2)–(H3) |
| L93–109 | Case II identities, filler count and properness | Generic; lower bound \(k\ge2\kappa+1\) remains available |
| L110–113 | Case II upper/lower kill bounds | Correctly re-established, including both \(W\) branches |

In Step 0, the truncation case has lower bound
\[
\min\!\left(R-2\kappa,\frac{R-1}{2}-\kappa\right)
\ge\min(2\kappa+1,\kappa)\ge1.
\]
The floor case gives \(R/2-1>0\). This includes \(E=0,R\). Avoidance excludes full windows and therefore supplies the unique prefix representatives. No additional chain assumption is needed.

**Step 1 and defects — SOURCE01:L57–68; SOURCE00:L34–42.**

The floor comparison is correct:
\[
E-\kappa-\lfloor E/2\rfloor
=\lceil E/2\rceil-\kappa\ge1
\quad(E\ge2\kappa+1).
\]
Writing \(A=\rho_t\), \(B=R-\alpha\), \(C=R-r_t\), their pair sums are
\[
R+r_t,\qquad R+\alpha,\qquad 2R-\rho_t,
\]
all at least \(R>4\kappa\). Consequently, at most one argument can be \(\le2\kappa\), including arguments at branch ties.

The four lower expressions cited from SOURCE02:L97–100 are correct:

| Case | Lower bound for \(S\) | Excess over \(R-\kappa-1\) |
|---|---|---|
| FFF | \(R-\tfrac32\) | \(\kappa-\tfrac12\) |
| TFF | \(R-\kappa-1+\rho_t/2\) | \(\rho_t/2\) |
| FTF | \((3R-\alpha)/2-\kappa-1\) | \((R-\alpha)/2\) |
| FFT | \((3R-r_t)/2-\kappa-1\) | \((R-r_t)/2\) |

Every excess is nonnegative, so \(S\ge R-\kappa-1\ge p-2\). These are lower expressions obtained by bounding floors, rather than literal exact values of \(S\).

For \(t=1,k\), the prefix definitions give \(x_t\ge U^t+1\), and Step 0 gives \(U^t+L^t\ge1\); hence \(x_t\ge-L^t\). Empty runs and \(r_t=0\) cause no exception.

The defect argument retains precisely the required strict inequality:
\[
r_t/2+L^t\le R/2<p.
\]
It therefore yields (2.1), the parity identity, and \(r_t+\delta_t\ge2\). For empty defects, genuineness excludes \(x_t=0\), giving \(x_t\in[1-\kappa,-1]\). At \(\kappa=1\), these bounds give \(2\le r_t+\delta_t\le0\), closing that case immediately.

**Selection and kill bounds — SOURCE01:L72–113; SOURCE00:L46–54.**

The six kill inequalities remain exact for arbitrary proper patterns. Their \(p-m\) terms introduce no additional \(k\le p\) assumption.

The following Case II facts are all generic and correctly retained:
\[
\begin{gathered}
\delta_Z=2\kappa-|Z|+s,\quad |Z|\le\kappa-m_Z,\quad s\le g_Z-2m_Z,\\
\delta_Z-\rho_Z\ge4m_Z,\quad
2\le d\le g_Z\le\kappa-1,\quad
\kappa+1\le\delta_Z\le2\kappa-2.
\end{gathered}
\]
The filler-count condition holds because
\[
2+2|Z|-\rho_Z\le2\kappa<k.
\]
The alternating selection is valid since \(U\) is proper. Properness of \(P=Z\cup W\) follows from an outside neighbour of \(Z\), which belongs to neither \(U\) nor \(W\). Each filler has odd \(r_y\ge1\), and \(|W|\le d/2\) in both branches.

All numerical kill checks pass:

| Condition | Case I | Case II |
|---|---|---|
| U1 | At most \(\Phi(P)\le4\kappa\le2p-2\) | Singleton: \(\le r_y+1\le R+1\le2p\). Multiple fillers: \(\le3d-2-2m_Z\le3\kappa-7<2p\) |
| U2 | Greedy crossing | Filler threshold |
| U3 | \(\delta_P\ge0\) | \(\delta_P\ge\kappa+1-(\kappa-1)/2>0\) |
| L1 | At most \(\Phi(P)\le4\kappa\le2p-2\) | \(\le\delta_Z-\rho_Z+2m_Z\le4\kappa-4<2p\) |
| L2 | \(\le4\kappa\); sufficient \(R\ge3\kappa+1\) | Singleton: \(\le2\kappa+r_y-7\); sufficient \(R\ge4\kappa-5\). Multiple fillers: \(\le4\kappa-4\); sufficient \(R\ge3\kappa-1\) |
| L3 | \(\delta_P\le4\kappa-2\le R-1\) | \(\delta_P\le2\kappa-2\le R-1\) |

(H2) supplies every displayed requirement on \(R\); (H3) supplies the comparisons with \(2p\). In particular, SOURCE00:L54’s singleton equivalence
\[
2\kappa+r_y-7\le2R-2\kappa-2
\iff r_y\le2R-4\kappa+5
\]
has the correct constants.

**Statement, scope and imports.**

The stated new \(k>p\) range is exactly the elimination of \(R\) from (H1)–(H3). Its nonemptiness further forces \(\kappa\le(p-3)/2\); the written \((p-1)/2\) bound merely leaves an empty interval at its upper endpoint.

The RES\(_<(p)\) corollary is correctly limited using the defining properties reported in SOURCE02:L12. The primary RED definition is absent from this packet, so that definitional identification is imported. SOURCE05’s \(k\le p\) corollary was not used to justify the extension.

Audited: SOURCE00’s theorem argument and every reused step in SOURCE01 Sections 1–5. Imported: accepted H0 at \(B=\beta=0\) for arbitrary proper patterns, GRX, notation/normalisation, and the reported residual defining properties. The SOURCE02 case expressions were independently checked. E9/E9b and the prospective Section 4 lemmas supplied no premises. This was an inlined-text audit; hashes were not recomputed.