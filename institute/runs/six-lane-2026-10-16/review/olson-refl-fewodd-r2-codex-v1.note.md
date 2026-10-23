**DISPOSITION: ACCEPT**, relative to the specified accepted inputs. **FATAL: 0; MAJOR: 0; MINOR: 0 new findings against SOURCE00.** The monotonicity argument closes the stated restricted reflection theorem. ROT-few-E’s two applications fit this restriction, subject to its stated expansion properties; its standalone SHgen-E lemma still requires the broader REFL assumption as written.

All seven snapshot hashes match the supplied pins. Only static file listing and hashing were performed.

**1. The four moves preserve avoidance and do not increase \(o_F\).**

Normalization multiplies reflection values by an invertible scalar and possibly negates them. These automorphisms preserve avoidance, block lengths, equality of adjacent values, and the cyclic maximal decomposition. Thus they preserve \(o_F\) (SOURCE02:L14–16, L35–36).

Throughout the process, use the maximal decomposition after each move. A temporary representation with equal blocks across an empty gap is permitted when applying H0.

- **P1 — FUS** (SOURCE00:L60–64; SOURCE02:L84–97).  
  The corrected spectrum inclusions recolour the **even** block to its neighbour’s value. SPEC therefore preserves avoidance, including when the affected segment crosses the chosen cut.

  A single fusion of lengths \(a\) and even \(b\) preserves the parity of \(a\). A double fusion has lengths \(a,b,c\), with \(b\) even. Its odd-block contribution changes from
  \[
  [a\text{ odd}]+[c\text{ odd}]
  \quad\text{to}\quad
  [a+c\text{ odd}],
  \]
  giving a decrease of two precisely when both outer blocks are odd, and otherwise no change.

  There is no further cascade: an original neighbouring empty gap was genuine, so the next block already had a different value. With \(R\ge1\), a double fusion cannot accidentally count the same outer block twice around the cycle.

- **P2 — PM0** (SOURCE00:L65–66; SOURCE02:L107–114).  
  Each pattern after contraction lifts to a pattern containing both or neither of the merged rotation-run indices. Its \(m,D_P,\beta,u_P,B,\kappa\), hence its H0 windows, agree with the original pattern. The empty/full-pattern window also agrees. Thus avoidance is preserved.

  The removed block is even, and adding its length to the receiving block preserves that block’s parity. Both merged rotation runs were nonempty, so their union remains nonempty; other gaps and neighbouring values are unchanged. Consequently \(o_F\) is unchanged. The required \(k\ge2\) holds whenever the active state has a genuine empty run.

- **P3 — TR-fill** (SOURCE00:L67–68; SOURCE02:L104–106).  
  For every zone-sign pattern, a transferred \(\rho_1,\rho_{-1}\) pair contributes one effectively positive and one effectively negative rotation at either location. Thus \(E_+,E_-\), and all remaining GR0 data, agree. Avoidance is preserved in both directions.

  The donor has length at least three and remains nonempty. The recipient gap was between different reflection values, so filling it changes no constant reflection block. Hence \(o_F\) is unchanged and \(g\) decreases by one.

- **P4 — M0′** (SOURCE00:L69–71; SOURCE01:L144–147).  
  Retain the old representation temporarily, before fusing equal neighbours. Deleting the opposite rotation pair and inserting an equal reflection pair gives
  \[
  A'=A-1,\quad B'=B-1,\quad H'=H+1,\quad \kappa'=\kappa-1.
  \]
  Every \(D_P,m,\beta,u_P\) remains unchanged. In H0,
  \[
  D_P+B'-\kappa'+m-\beta
  =D_P+B-\kappa+m-\beta,
  \]
  while the floor term can only decrease. Therefore \(\lambda'(P)\le\lambda(P)\), and \(I'(P)\subseteq I(P)\). The same calculation gives \(I'(\varnothing)\subseteq I(\varnothing)\). This proves avoidance preservation without assuming that the temporary empty gap is genuine.

  The inserted pair preserves its block’s parity. If deleting the rotation run joins equal-valued blocks, merging them changes the odd count by zero or minus two. Existing genuine empty gaps survive, so P4 cannot produce an exit with \(g=0\).

The imported wording “which lowers kappa by one more” at **SOURCE01:L147** needs its already-recorded qualification: for a general fusion, the additional decrease occurs **only when both fused blocks are odd**. SOURCE04:L39 acknowledges this erratum. SOURCE00’s parity argument already handles it correctly. Moreover, under RED’s first-applicable priority, P4 is reached only after even blocks have been eliminated.

All moves preserve total length and keep the remaining rotations in the normalized nonzero pair. A hypothetical resulting avoider with \(R=0\) is excluded by AR, exactly as SOURCE01:L138–139 states. These observations also cover cyclic wrap and prevent an exceptional all-reflection terminal state.

**2. The terminal bound and the κ-cases are valid.**

At a terminal state with \(g\ge1\):

- Any even block would enable P1 if an adjacent run were empty, or P2 if both were nonempty. Thus every constant reflection block is odd.
- Any mixed rotation run would enable P3 when its length is at least three, or P4 when it is a \((1,1)\)-run. Thus every rotation run is pure or empty.

Here **\(k\) counts maximal constant reflection blocks**, equivalently rotation-run slots **including empty slots**. It does not count only nonempty rotation runs or maximal reflection runs. Therefore
\[
k=o_F(w_{\mathrm{terminal}})
 \le o_F(w_0)\le p.
\]
This establishes SOURCE00:L55–58 with the required meaning of \(k\).

The accepted RED proof supplies the remaining cases, at their stated scopes:

- Negative κ is excluded for avoiders by the disjoint-pair argument.
- With \(g\ge1\), κ \(=0\) is excluded by K0*.
- At termination, \(B\le\kappa\); Corollary B=K excludes equality.
- If κ \(=1\), this leaves \(B=0\), excluded by K1*.

Thus the terminal avoider belongs to \(\mathrm{RES}_{<}(p)\) with κ \(\ge2\) (SOURCE01:L162–164). Its \(k\le p\) contradicts SOURCE03:L3 and L13: B0S covers \(B=0\), and MXG covers \(B\ge1\).

Exits with \(g=0\) remain the accepted RED exits P1 and P3. Their RGR imports apply to the **produced RGR words**, not to \(w_0\). No INV*, inherited condition, ROT result, or additional RGR hypothesis on \(w_0\) enters the argument.

The reflection-free case is vacuous; the rotation-free case is excluded by AR.

**3. The rotation interface is correct, with a scope distinction.**

SOURCE00:L75–81 correctly requires, for the actual expanded word \(u\):

\[
|u|=4p-2,\qquad
\operatorname{Rot}(u)\subseteq\{\rho_c,\rho_{-c}\},\ c\ne0,\qquad
o_F(u)\le p.
\]

Under these conditions, a nonconstant maximal cyclic reflection run implies an identity \(2p\)-subword. A genuine empty gap witnesses that nonconstancy. A nonmaximal representation with at most \(p\) odd blocks also suffices, because merging equal blocks cannot increase the odd count.

For the applications inside ROT-FEW-E:

- **Expanded \(u^\circ(h)\):** SOURCE06:L32–35 states the length and rotation-pair properties and says that expansion removes reflection pairs inside blocks while leaving every block nonempty and preserving the genuine empty gap. Starting from the all-odd normal form, each surviving block has length
  \[
  \ell_i-2h_i\ge1,
  \]
  still odd. With the same block values and genuine empty gaps, its maximal decomposition therefore has
  \[
  o_F(u^\circ)=k\le o_F(w)\le(2p+4)/5\le p.
  \]
  This verifies the missing odd-count obligation from the described operation, rather than merely accepting SOURCE00’s peer report.

- **Original \(w\):** after the rotation conclusion is established, its original length, nonzero rotation pair and given odd-block bound supply the three hypotheses directly.

**Concrete caller edit:** SOURCE06 currently assumes unrestricted REFL. To replace that assumption by SOURCE00, state a restricted SHgen-E variant with \(k\le p\), carry that bound through its induction, and explicitly record \(c\ne0\) and \(o_F(u^\circ)\le k\). The low-odd theorem supplies this bound. The supplied text does not establish it over the entire standalone SHgen-E domain.

**Audited versus imported:** independently checked here are MON, avoidance preservation for P1–P4 through SPEC/GR0/H0, maximalization and cyclic edge cases, terminal \(k=o_F\), and compatibility of the two rotation call sites. Imported are K0*, RED’s accepted auxiliary arguments and exits with (I1)–(I4), and the B0S/MXG residual exclusion. The underlying SHgen construction, FLEXa, and the remainder of ROT-FEW-E were not independently established by this audit.