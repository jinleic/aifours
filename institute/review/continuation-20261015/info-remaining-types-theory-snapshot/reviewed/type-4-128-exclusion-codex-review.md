ACCEPT.

No required mathematical fixes. The scoped exclusion is valid, and the supplied prior proofs—with the stated errata—supply H1–H4 for the actual balanced target.

- **Application of the prior lemmas: no gaps found.** The bijection \(b=B^Ta\), equal half-support XORs and opposite canonical phases give \(R(b)=\eta(b)W_f(a)\). The canonical transforms yield \(\widehat p\in\{0,\pm64\}\). I checked both slack identities, all seven triples and their exclusions: they force \(z=8,c=0\). The zero-moment argument then gives an affine three-flat; balance makes it linear. The next-bit proof supplies the full Pfaffian quartic, not merely a degree bound. Locations: [PROOF.md §1](/Users/jinleic/repos/aifours/institute/review/continuation-20261015/info-zero-exclusion-snapshot/PROOF.md:22), [imported report §§1–5](/Users/jinleic/repos/aifours/institute/review/continuation-20261015/info-zero-exclusion-snapshot/inputs/odd-pair-codex-attempt.txt:98).

- **Conditional H1–H4 theorem: no errors found in normalization or geometry.** The radical vector with quadratic value one makes the normalization linear. The stabilizer subgroup proves transitivity at each \(\tau\); invariance of the radical prevents merging these classes. The counts \(1680/210/1\), inverse composition \(p'=p\circ A^{-1}\), Fourier map \(A^T\), and preservation of the quartic class are correct. Location: [PROOF.md §§2–3](/Users/jinleic/repos/aifours/institute/review/continuation-20261015/info-zero-exclusion-snapshot/PROOF.md:36).

- **Conditional theorem: the extension and character arguments are complete.** The wedge-map rank is \(16\), and the \(\tau=1\) quartic obstruction is valid. Restriction rank \(80\) gives the complete thirteen-dimensional kernel \(D\mathcal B\). Both particular extensions have the required restrictions and quartic part. Their radical invariance, together with the kernel’s constant-coefficient radical dependence, forces one character on **every** \(D=1\) point. Location: [PROOF.md §§4–5](/Users/jinleic/repos/aifours/institute/review/continuation-20261015/info-zero-exclusion-snapshot/PROOF.md:86).

- **Conditional theorem: the projection contradiction has the correct normalization.** The identity \(p=-3(-1)^E\) is correct. The projector preserves all 128 magnitude-three entries, giving squared norm at least \(1152\). Its Fourier slice gives
  \[
  \|P_\chi p\|_2^2\le \frac{2^{8-\tau}64^2}{256}
  =1024\ \text{or}\ 512,
  \]
  contradicting that lower bound. Location: [PROOF.md §6](/Users/jinleic/repos/aifours/institute/review/continuation-20261015/info-zero-exclusion-snapshot/PROOF.md:134).

- **Appendices: no errors found.** Appendix A correctly handles the zero frequency separately; its quadratic-vanishing kernel is exactly \(\{0,q\}\), and \(9216>4096\). Appendix B correctly shifts a zero to balance, obtains at least four zeros from the first moments, and uses even weight to raise peak \(>28\) to peak \(\ge32\), hence \(NL\le240\). It claims no attainment. Locations: [Appendix A](/Users/jinleic/repos/aifours/institute/review/continuation-20261015/info-zero-exclusion-snapshot/PROOF.md:172), [Appendix B](/Users/jinleic/repos/aifours/institute/review/continuation-20261015/info-zero-exclusion-snapshot/PROOF.md:194).

Read-only, in-memory checks confirmed both specified hashes, all 18 manifest-listed payloads, all 1891 flat certificates and stabilizer maps, restriction rank/kernel completeness, and all 8192 extensions at each surviving representative. I also checked all 256 three-variable sign tables and all 65536 five-variable quadratics. No files were written.

The acceptance covers this residue type and the separate zero-count corollary. Seven other types remain; residue extensions are not Boolean functions, and the carry probe supplies no exclusion.