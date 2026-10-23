# Lane log (phys-1 replacement: T7 dual-unitary isolation, d = 3), host-clock PDT

## 2026-10-17 01:12–01:31 PDT — freeze, two implementations, hand proof

- 01:12:57 target frozen by parent (contract in the run directory). 01:14 lane created; pinned source PDF copied
  (SHA-256 bc8ee8fc… identical to the parent pin); ref. [44] (arXiv:2212.06737v2, SHA-256 740ee6e0…) downloaded and
  read: Theorem 1 (one LU class of 2-unitaries of order 9) with proof via no two-qutrit universal entanglers.
- P9 = source matrix (C7), ones extracted from PDF word coordinates (sources/c7page.bbox.html):
  (0,0),(1,8),(2,4),(3,5),(4,1),(5,6),(6,7),(7,3),(8,2) = |ab> -> |2a+b, a+b>. The source's three other P9
  descriptions are explicit local-permutation images of (C7).
- README §0 frozen between 01:14:44 and 01:27:00 (exact time not recorded; before any computation). Runs (python-flint 0.9.0 / stdlib, -B, 1 thread):
  01:27:00 implementation A (1.4 s, 90 MB): dual and T-dual kernels 33 = orbit tangent 33 at P9 and all variants;
  129x129 minor det 512; tangent minor det -27; mutation (cut 12|34) kernel 81; d = 4: kernel 136 vs tangent 61.
  01:27:10 implementation B (0.3 s): ranks 129 mod two primes; tau-group order 6, free, 12 orbits -> 9 + 24 = 33;
  orbit basis = tangent span; A's kernel bases satisfy B's equations (0 violations); d = 4: Klein group, 136.
- review/PROOF.md: complete hand proof (perfect tetracode, tau involutions, regular-value + compactness), corollary
  via [44], controls. Status CANDIDATE pending parent re-derivation, Claude hostile review, priority audit.
- 01:32:01 PDT erratum in PROOF.md §1.4: M_{14} = (U^Γ)^T S9 (was written as (S9 U^Γ S9)^T); unitarity equivalence and all results unchanged; SHA256SUMS regenerated.
