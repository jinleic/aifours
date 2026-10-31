# Three-copy d=4 rank-two certificate: q3(C) >= 0 for every complex C of rank <= 2 on (C^4)^{x3}

Native clock observed before writing: **2026-10-28T18:57:31-0700 PDT** (last `/bin/date` observation in the parent kernel before this write; the f62 return records 18:50:58 PDT). Computer-assisted same-harness written support; not formal/kernel, human, configured-family, independent-model or novelty acceptance. Prospective authority: [contract addendum 2](../contract-addendum-2-frontier-first-owner-direction-v1.json).

## Adopted statement (exact scope)

For d=4 and three copies, every complex matrix C of rank at most 2 on (C^4)^{x3} satisfies q3(C) = ||C||^2 - (1/2) sum_i ||Tr_i C||^2 + (1/4) sum_{i<j} ||Tr_ij C||^2 - (1/8) |Tr C|^2 >= 0 (unnormalized partial traces), as a computer-assisted proof whose trust base is: the public Tomar v3 certificate data (archive SHA-256 `2314805738a4f41b79eb3c1593e694ad337fe6f52d13e18a70db1acc726ff5e3`, identical for the v4 download); the written elementary bridge (isometric lift and swap identity, twirl covariance, commutant tensor factorization, symmetrization to orbit sums, congruence preservation of PSD) hand-verified by two reviewers and the parent; the finite commutant witness for n in {2,4} (three implementations, two primes) replacing Schur-Weyl at those sizes; and CPython 3.14 / numpy / python-flint arithmetic. This independently certifies the paper's own claimed d=4 statement; it is not a new discovery, not a general-d result, and carries no physical (distillability) interpretation.

## Evidence actually bound

Owner root `/Users/jinleic/repos/aifours/physics/evidence/three-area-20261027-96h/parallel-18/werner3-ququart/`.

| Item | SHA-256 | Parent read |
|---|---|---|
| `frontier-20261028-d4-certificate-bridge-and-independent-identity-v1.md` (135 LF) | `cc9a354a16b9d3abf6ac1ef8ff6fcc6e2041a88d435216b9d9b326a85f348a66` | complete |
| `frontier-20261028-d4-certificate-verification-addendum-v1.md` | `176eac7dcf96c9819c5d73488787b18a201be0a0b5a46061b26ac83f67a14340` | complete |
| `frontier-20261028-d4-consolidated-operator-certificate-proof-v1.md` | `a6fb579592ffacd71cb0d8c115e5aea20209fc07395304be9b79651dbf1f646e` | complete |
| `frontier-20261028-d4-four-replica-commutant-finite-rank-proof-v1.md` | `49df4f874bf8c4a4da60d61f1b76d9b8028e2acfca5fe6d8c2b378a324501a23` | complete |
| `frontier-20261028-d4-all-gram-physical-bridge-audit-v1.md`, `frontier-20261028-d4-canonical-orbit-source-audit-v1.md` | pinned in the f62 manifest / owner root | complete |
| Independent global identity checker `frontier-20261028-independent-d4-global-identity-check.py`, data-only loader, aux equality check, saved-PSD check | `b6b6f5ee...`, `bb9cf61e...`, `0949e494...`, `7e564331...` | read |
| f19 review `review-waves/f19-werner-d4-independent-identity/review-v1.md` (193 LF) | pinned in checkpoint053 context | complete: 0F/0M/1m (MINOR = overstatement about two base-matrix checks) |
| f62 audit `review-waves/f62-werner-d4-parent-certificate-audit/review-v1.md` (30249 B) | `b032753e99238015cfd77473e2c6b7ec2e6849fdc6e4ddbdc46e7d64ff4ab989` | complete: MINOR, no FATAL/MAJOR |

Reviewer-established predicates (f62, code sharing nothing with author or first reviewer beyond the pinned bytes): the 4675-orbit certificate identity is exactly zero by an own evaluator with an independently recomputed height bound over 338 twenty-bit primes (CRT, P > 2B); all 1237 corrected multipliers are positive definite by exact Sylvester minors (4149 minors); the four-replica U(2)/U(4) commutant spans are the permutation spans (70 -> 56+14, 2716 -> 2692+24); the physical lift/swap/twirl/Gram/equality/objective bridge was re-derived by hand and its load-bearing conventions were confirmed by falsifying mutations (abb order, transposed coupled rule, complement trace: 1142/1828/1142 nonzero residues). f19 earlier established the identity by a FLINT-integer route plus CRT over 424 primes, exact PSD by three methods and the commutant ranks mod 65521.

Parent same-harness checks (receipts in `review-waves/f62-werner-d4-parent-certificate-audit/`): `parent-corrected-psd-v1.py` (standard-library Fraction Schur strict-PD on all 1237 saved matrices, 4149 positive pivots, four intended-reason controls); `parent-global-identity-replay-v1.py` (replay of the inspected global checker, 4675/4675 zero - shared engine, not an independent implementation); `parent-commutant-rank-v1.py` (own constraint rows mod 65521, n=2: 70 -> 56+14, n=4: 2716 -> 2692+24). A parent physical-binding script was written and launched; its result was not observed and is not relied on here.

## Carried qualifications

f62 MINOR items: the first reviewer's "independently written" global checker mirrors the author's `ep3core` architecture (documentation precision; f62's route is the architecture-independent one); two fail-open ingestion paths in the global checker (unknown equality group silently dropped, negative index would wrap) that cannot produce a false PASS and are not triggered; the global checker does not re-check `format/k/d/nrow` or the archive hash (covered by pins); float PD margins reach about 4e-12, so only exact checks are evidential. f19 MINOR: an overstatement about two base-matrix checks. The 329 versus 272 equality-coefficient count is explained (272 + 57 correction coordinates); the paper's Appendix A "1347" wording remains a documentary inconsistency only. The equality-index/compression-key correspondence is not load-bearing for soundness.

## Not established

General d; any physical distillability statement; the paper's Lean claims (not read); novelty or priority (the published paper claims the full target); human, kernel or independent-model acceptance. Historical held or quarantined outcomes in this lane are not rehabilitated by this disposition.
