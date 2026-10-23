**Findings: 0 FATAL, 0 MAJOR, 0 new MINOR.**

**DISPOSITION: ACCEPT**, conditional as stated. INV*-FEW is read with the existing citation erratum in **SOURCE03:3**: REFL-few-odd r2 and ROT-FEW-E v2. No additional repair or counterexample was found.

- **SOURCE00:25–26 — \(R\le2\) passes.** Here \(F\ge4p-3\), and both stated ranges give \(B\le2p-3\). Thus
  \[
  \sum_{\text{blocks }C}\left\lfloor |C|/2\right\rfloor
  =\frac{F-o_F(w)}2\ge p.
  \]
  Choose \(p\) disjoint equal-reflection pairs in a cyclic frame. Their ordered product is identity. Returning to the original index order cyclically permutes the selected factors, preserving identity by conjugation. A wrapping block therefore causes no obstruction.

- **SOURCE00:27–29 — long odd-block deletion passes, including both directions of RGR equivalence.** The chosen block survives with even length at least two. No block disappears, no rotation gap changes, and no constant blocks fuse—even across the cyclic seam or across empty rotation gaps. Consequently \(o_F(w')=o_F(w)-1\). The rotation multiset is unchanged, and every reflection run retains exactly its sequence of constant-block values. Hence \(w\) is RGR **iff** \(w'\) is RGR.

- **SOURCE00:30–32 — rotation-deletion bookkeeping passes.** If the rotation run survives, reflection blocks are unchanged. If it disappears, neighboring blocks either remain distinct or fuse. Writing \(\epsilon(n)=n\bmod2\), fusion changes the odd count by
  \[
  \epsilon(a+b)-\epsilon(a)-\epsilon(b)\in\{0,-2\}.
  \]
  Thus \(o_F(w_i)\le o_F(w)\). With \(R\ge3\), deleting one rotation cannot eliminate all rotations; the potentially degenerate disappearance of the sole rotation run is excluded.

- **SOURCE00:30–35 — availability and reconstruction pass.** After Case 1, \(R\ge3\); absence of a long odd block means every odd block is a singleton. Choose two distinct rotation **occurrences**, possibly of equal value, and form two separate one-letter deletions. Each word has length \(4p-2\). A third rotation survives in both and forces their nonzero inverse pairs to coincide. Every original rotation survives in at least one deletion. Every cyclically adjacent unequal-reflection pair would survive in both deletions, contradicting their RGR property. Therefore \(w\) is RGR.

- **SOURCE00:16–24,40 — ranges pass.** Part (a) uses exactly the accepted INV*-FEW scopes: \(o_F\le3\) for \(p\ge5\), and \(o_F\le4\) for \(p\ge7\). The case \(p=5,o_F=4\) is excluded. Part (b) preserves \(5o_F\le2p+4\) under every deletion used; its integer bound is \(\lfloor(2p+4)/5\rfloor\). All listed examples are correct.

- **SOURCE00:36; SOURCE04:7 — final lift passes.** RGR-LONG applies directly to the reconstructed length-\(4p-1\) word. Its stated scope imposes no additional inherited-avoider hypotheses.

All eight SHA256 pins and byte counts match. Verification used only static reads and hashes within the permitted snapshot.