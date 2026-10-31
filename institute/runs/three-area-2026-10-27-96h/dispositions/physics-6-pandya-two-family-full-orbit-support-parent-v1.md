# Pandya 60-support phase families: every local GL(6,C)^4 orbit element has at least 60 nonzero terms

Native clock observed before writing: **2026-10-28T18:57:31-0700 PDT** (last `/bin/date` observation in the parent kernel before this write; the f71 return records 18:41:46 PDT). Same-harness written support plus finite exact certificates; not formal/kernel, human, configured-family, independent-model or novelty acceptance. Prospective authority: [contract addendum 2](../contract-addendum-2-frontier-first-owner-direction-v1.json).

## Adopted statement (exact scope)

Let T_S(theta) be the two explicit AME(4,6) phase families built from the pinned public Pandya Table 1 / Eq. (6) transcription, S in {P, P'} (the all-K supports of the two parity faces) with arbitrary independent unit phases on the twelve S terms. For every element of the GL(6,C)^4 orbit (hence every local-unitary image) of T_S(theta), the number of nonzero computational-basis coefficients is at least 60, attained at the identity. This is an orbit statement for these two families only: it is not a global AME(4,6) support bound (the published global bound is 38; the owner's separate global >=42/>=44 claims are WITHHELD under review wave f89), it does not identify the global minimum, and it does not classify orbits.

## Evidence actually bound

Owner root `/Users/jinleic/repos/aifours/physics/evidence/three-area-20261027-96h/parallel-18/ame46-support/`.

| Item | SHA-256 | LF | Parent read |
|---|---|---|---|
| Pinned table `frontier-20261028-pandya-table-v1.txt` | `cad24229c112b65f2cb624903745095a353513384af6fbce49447c9f6499da38` | 38 | complete |
| Base proof `frontier-20261028-unrestricted-orbit-60-barrier-v1.md` | `d21c734fa2830bf20e7330e118f03d3e1367f1794815c82162075c7df6dac251` | 146 | complete |
| Two-face extension `frontier-20261028-two-face-unrestricted-orbit-60-v1.md` | `8af3381ec64c50d7e9f17e485e1c91093be35fa9057ad2829de66474e41af5cf` | 44 | complete |
| f70 written review `review-waves/f70-ame-unrestricted-orbit-written-review/review-v1.md` | pinned in checkpoint056 | - | complete: FATAL 0 / MAJOR 0 / MINOR 1 (wording of the support minimum on a specified parity face) |
| f71 certificate review `review-waves/f71-ame-unrestricted-orbit-certificate-review/review-v1.md` | pinned in checkpoint056 (reviewer-reported `35398467...`) | - | complete: minor-only, m1-m4 |

f71 independently reconstructed, from the pinned transcription and from the public arXiv HTML v1 (`10711bc7...`), every finite hypothesis of the written argument with a reviewer-authored standard-library checker (strict table grammar; exact Z[sqrt2] and Z[i] arithmetic; 21 fault controls all rejected): Table 1 equals the transcription on all 60 positions; Eq. (6) gives P and P' in order; colour relabelling sends P to the even and P' to the odd class, both sharply 2-transitive; the 48 E terms are signed Paulis, one each of I, X, Z, J per pair; the structural zeros; F F^T = 2 I_36 exactly in all three cuts for both faces; the phase-independent block structure (12 monomial S rows/columns disjoint from the 24 E rows/columns with E Gram 2 I_24) paying the arbitrary-phase claim; the exhaustive 50625 mask 4-tuples giving exactly 17 patterns for each parity class; and the Bloch/Pauli identity as a degree-bounded polynomial identity on all 3^8 grid points. The written complex argument (sections 3-7 of the base proof and 2-3 of the extension) was re-derived line by line in both reviews.

Parent same-harness check: `review-waves/f71-ame-unrestricted-orbit-certificate-review/parent-source-mask-bloch-result-v1.json` (SHA-256 `ff9a5a63a67d3e3c393d3419120f444f8a33d6521d82ce4c80d4ad494708987d`): exact Gaussian-integer Pauli/Bloch trace coefficients with the common-conjugation y sign, the sixteen Pauli Frobenius pairs and the four-vectors/three-axes obstruction, and the 17-mask lists for both parities (agreeing with f71, which did not use this file). The earlier parent sector check for the one-restricted-party result is a separate record.

## Carried qualifications

f71 m1: the base section 7 implicitly uses rank != 0 for mixed covectors (follows from F F^dagger = 2I); m2: the author's two checkers share one lenient parser, so they are one read of the table, not two; m3: the source reconstruction obligation is discharged from the HTML v1 rendering only, not the TeX source or companion repository; m4: "all such rank-one B covectors lie in W_t" is a necessary condition, not a characterisation. f70 MINOR: wording of the support minimum on a specified parity face. The F7 search and the sampling diagnostics are not part of the proof.

## Not established

Any statement about other AME(4,6) orbits or the global support minimum; orbit inequivalence or the paper's classification claims; novelty or priority (the paper states the overlap bound and the global >=38 bound; whether it states this orbit minimum was not assessed); human, kernel or independent-model acceptance.
