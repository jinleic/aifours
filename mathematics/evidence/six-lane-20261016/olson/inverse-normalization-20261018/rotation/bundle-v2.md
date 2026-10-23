# Review bundle list v2 (rotation slice)

Written after host clock 2026-10-18T06:32:40-07:00 by OlsonRotationRigidity.  Supersedes bundle-v1.md (d1abdcab...7587)
as the list of current versions; bundle-v1 stays as the record of what Codex reviewed.

## A. Errata versions (pure deltas of reviewed/accepted texts; each file ends with its unified diff and fix map)

| file | sha256 | predecessor | fixes |
|---|---|---|---|
| proof-SH3-v5.md | 93713e7057cb17c28de9d228f08abe6197d193799cd0982d5f301bfc536c380b | SH3-v4 321978ff...b06c | Codex bundle-1 findings 1, 2 |
| proof-ELT0-v3.md | 6a7bfd5b9708f6e930d895f87883d43f09ce9d82ddd14101b649665999d52362 | ELT0-v2 d17e8108...9e4379 | Codex bundle-1 findings 3, 4 |
| proof-ROT-o3-v4.md | 55670658a819af5ef5570fa71137ad51ee111e46e720cbac5bfdbfd7f51be8cf | o3-v3 9b0a37db...ab7 | Claude o3-m1, m3, m4, m5, m6 (parent-listed wording) |
| proof-ROT-o4-v4.md | 7fa49e970603210639f1a0b834c54f5418859bc3dfaf164e34e67836cdaa425a | o4-v3 db4eee8a...148e | Claude o4-m1, o3-m1, o3-m6 (citations only) |

Smoke for the Codex words: code/check_codex_examples_v1.py (ea4f1bf8...151a) -> out/check_codex_examples_v1.jsonl
(de6742db...56e3), all_ok True.

## B. New results for review (all [W], unreviewed)

| file | sha256 | claim (exact scope) |
|---|---|---|
| proof-SHgen-v2.md | 8fde88c0b0e95e14fdeb346c0e42673f22a7122510ce295afb3e33b7b8bdd239 | Theorem SHgen: all-odd constant-block word of length 4p-2 (p >= 5, F, R >= 1, k >= 2, runs nonempty); heavies relative to some c != 0 of any odd weight (rho_0 = weight p); (H) 2H >= E and (K) k <= 2p - eta - a_max - 1 => identity 2p-subword.  Subsumes SHm-v1. |
| proof-ROT-few-v2.md | 53fed0db489034d4c23061cb904897d665fec6bf7344800d32af0e1b9d91e9d1 | Theorem ROT-FEW, CONDITIONAL on SHgen-v2: constant-run avoiders of length 4p-2 with exactly k odd blocks are rotation-rigid when p >= 5 prime, 4p >= 11(k-1), 2p >= 5k-4, p >= 2k-1.  o = 5 for all p >= 11; o <= 7 for p >= 17; asymptotically o <= 1 + 4p/11.  New lemmas proved in-file: SCHERK, GROW (+ Corollary SET), MULT (layers), EXTRACT, WT. |

Superseded drafts (kept, not for review): proof-SHgen-v1.md c80151d0...e953 (one false side sentence, logged),
proof-ROT-few-v1.md 7ec186ea...4975 (weaker range).

## C. Import map

| file | imports |
|---|---|
| SHgen-v2 | GRX, K1 (lowodd verdict v2); Corollary B'(b), C1 composition, KBH, KB uncapped implication (RUNS verdict, capped case excluded in-file); Davenport-alpha instance (V) with erratum m4 at RUNS verdict L57; trivial cut. |
| ROT-few-v2 | GRX, PM*, (D) (lowodd verdict v2); INC (a), (b) (o3-v3, accepted); (ZP), (V) and Theorem SHgen (SHgen-v2). |
| SH3-v5 | as SH3-v4 (bundle-v1 import map). |
| ELT0-v3 | as ELT0-v2. |
| o3-v4, o4-v4 | as o3-v3 / o4-v3; Davenport-alpha now inline (Lemma DAV) with erratum m4 pinned. |

## D. Finite aids (not premises)

code/check_rotfew_v1.py (7adf5139...45de) -> out/check_rotfew_v1.jsonl (398987ea...146b);
code/check_rotfew_v2.py (f87831ff...c32f) -> out/check_rotfew_v2.jsonl (464d6f59...9006): Scherk (Z_8, Z_10), LAYER,
SET, MULT (ii)/(iii) exhaustive over zero-sum-free multisets at p = 7, 11, 13, 17; Steps 1-4 of ROT-FEW over all (ZP)
multisets (unit-reduced) at (p, k) = (11, 5), (13, 5), (17, 7), every kappa: 0 failures; negative controls fired
(non-unique Scherk pairs, non-zero-sum-free extensions, mutated bound E <= k-3-|N|).  Details: README entries
06:18:43 and 06:27:42.

## E. Open for ROT(p) (constant runs)

o > about 1 + 4p/11 (in ROT-FEW the binding step is WT (c); MULT reaches o <= (2p+1)/3, SHgen o <= (4p-1)/5);
p = 5 beyond o = 3 (finite claim); non-constant reflection runs (REFL, reflection slice).
