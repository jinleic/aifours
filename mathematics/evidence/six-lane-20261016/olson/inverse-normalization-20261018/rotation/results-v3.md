# Rotation slice (ROT half of INV*): consolidated results v3

Written after host clock 2026-10-18T06:47:08-07:00 by OlsonRotationRigidity.  Supersedes results-v2.md (276ea1f7...682d,
kept) as the summary; the README is the append-only log.  Labels: [ACC] parent-accepted, [CDX] Codex-reviewed
(disposition given), [W] written and unreviewed, [F] finite-exact, [O] observation.  Nothing here is ROT(p), INV*(p),
REFL(p) or ordered Olson; no novelty claim.  "Constant-run avoider" = avoider of length 4p-2 over D_(2p) all of whose
maximal cyclic reflection runs are constant; o = number of odd such runs; kappa = p - 1 - H, H = (F - o)/2.

## 1. ROT coverage for constant-run avoiders (current best)

| range | statement | status / dependency |
|---|---|---|
| o <= 3, every prime p >= 5 | rotations in one {rho_c, rho_-c} | [ACC] lowodd v2 verdict; o3 verdict (proof-ROT-o3-v3.md; wording errata v4) |
| o = 4, primes p >= 7 | same | [ACC] o3o4 verdict (o4-v2 reviewed, v3 restated, wording errata v4); p = 5 is a separate unaudited finite claim |
| 5o <= 2p + 4, p >= 5 | same | [W] Theorem ROT-FEW (proof-ROT-few-v3.md), CONDITIONAL on Theorem SHgen [W] |
| kappa = 0 and 3o <= 2p + 1 | all rotations equal | [W] Corollary ELT0-FEW (proof-ELT0-FEW-v2.md): ELT0-v3 [CDX ACCEPT-WITH-FIXES on v2, fixes applied] + MULT [W]; no SHgen |

Largest o covered by ROT-FEW: p = 11: 5; 13: 6; 17: 7; 19: 8; 23: 10; 29: 12; 31: 13; 37: 15; 41: 17; 101: 41.
Two-parameter form (remark, derived from the explicit inequalities in ROT-few-v3 Steps 1-5, not a separate theorem
file): the proof needs only 3o + 2kappa <= 2p + 2, o + 4kappa <= 2p + 2 and 3o <= 2p - 1 (o >= 3); the theorem's
single condition 5o <= 2p + 4 is these at the worst case kappa = o - 1 allowed by Davenport-alpha.

## 2. Results and exact scopes

* SHgen [W] (proof-SHgen-v2.md 8fde88c0...d239): all-odd constant-block word of length 4p-2, runs nonempty,
  F, R >= 1, k >= 2; heavies relative to some c != 0 of odd weights (rho_0 weight p); 2H >= E and
  k <= 2p - eta - a_max - 1 => identity 2p-subword.  Imports: GRX, K1, B'(b), C1, KBH, KB uncapped (capped case
  excluded in-file), Davenport-alpha instance, trivial cut.  Finite aid: Lemma FLEXa's case analysis checked exactly
  over 82,913,588 integer tuples (p <= 13), 0 failures, negative control fired (README 06:46:53).
* SH3+- [CDX ACCEPT-WITH-FIXES on v4; errata v5 93713e70...380b], SHm [CDX ACCEPT, ecc91a52...dadb] (subsumed by
  SHgen), SH-ROT sharpness [CDX ACCEPT, d1c506c6...387e], ELT0 [CDX ACCEPT-WITH-FIXES on v2; errata v3
  6a7bfd5b...2362], EXP2 [W, known defect in its x = 0 weight sentence, b5287e76...6eb13], EXP-v2 [W].
* ROT-FEW [W] (proof-ROT-few-v3.md 5f158d69...efaa): uses only the all-plus pattern (ZP), Davenport-alpha (V), PM*,
  INC (a), (b) and SHgen; new elementary lemmas proved in the file: SCHERK (unique-zero sumset bound), GROW and
  Corollary SET (zero-sum-free set D of odd elements: |A(D)| >= 2|D|), MULT (layer decomposition: max multiplicity
  >= L - e; Savchev-Chen form once it is >= e + 1), EXTRACT (ZP => short zero-sum part of size <= 2kappa plus a
  zero-sum-free part), WT (weight bounds; (c) balances negatives with any positive terms).
* ELT0-FEW [W] (proof-ELT0-FEW-v2.md d4ee7081...246a): kappa = 0 slice, 3o <= 2p + 1, all rotations equal.
* Wording errata of accepted texts: proof-ROT-o3-v4.md 55670658...e8cf, proof-ROT-o4-v4.md 7fa49e97...425a (pure
  wording deltas per the parent's list; diffs in-file).

## 3. Finite aids (none is a premise)

check_rotfew_v1/v2/v3 (README 06:18:43, 06:27:42, 06:37:49): Scherk (Z_8, Z_10), LAYER, SET, MULT exhaustive over
zero-sum-free multisets at p = 7, 11, 13, 17; ROT-FEW Steps 1-4 over all (ZP) multisets (unit-reduced) at (11,5),
(13,5), (17,7), (19,8) in scope and (7,5), (13,6), (11,6), (13,7) out of scope: 0 failures everywhere; negative
controls fired (non-unique Scherk pairs; non-zero-sum-free extensions; mutated bound E <= k-3-|N|).
check_codex_examples_v1 (README 06:26:01): Codex's explicit words confirmed by a fresh raw DP.
flexa_check_v1 (README 06:46:53): see SHgen above.  Earlier aids: results-v2.md Sec. 4-6.

## 4. Observation [O]

The listed normalised avoiders out/bases_p5_N18.txt (3,730) and out/bases_p7_N26.txt (3,738) all have constant runs,
o <= p and kappa in {0, o - 1}; both values occur for every o from 1 to p (README 06:42:14).  So avoiders with many odd
blocks exist (rigid ones); the open ROT region is not empty of avoiders.

## 5. Open part of ROT and the exact obstruction

* Constant runs, o > (2p+4)/5: open in general.  Within the ROT-FEW route: WT (b) needs G >= 2kappa + w_+ (G = the
  multiplicity of the main generator, >= (4p - 3o + 1)/2), which fails first; EXTRACT needs 2kappa <= p; MULT's
  elementary multiplicity bound needs 3o <= 2p + 1; SHgen needs 3o <= 2p + 1 (for (H) at E = o - 1) and 5o <= 4p - 1.
  For kappa = o - 1 (Davenport-alpha tight) SHgen's (H) caps the route at o <= (2p+1)/3 even with perfect structure;
  for o >= p the all-plus pattern alone gives no structure (the zero-sum-free part has length <= p), so the
  remaining region needs the Phi >= 2 patterns.
* kappa = 0, o > (2p+1)/3: would follow from ELT0 with the Savchev-Chen structure for zero-sum-free sequences of
  length > p in Z_(2p) (conditional only; no import made).
* p = 5, o >= 4: only the lane's unaudited D10 census.
* Non-constant reflection runs: need REFL (reflection slice).

## 6. Defects recorded and superseded drafts

proof-SHgen-v1.md (one false side sentence; logged), proof-ROT-few-v1/v2 (weaker ranges), proof-ELT0-FEW-v1 (wrong
range remark at p = 7), proof-EXP2-v1 (x = 0 weight sentence), check_rotfew_v1 Part A negative controls did not fire
(replaced by v2's working controls), one aborted generation attempt (06:36:47, no file written).  Approximate time
labels: addendum-timestamps-v3.md (fb423070...81bb).

## 7. Manifest (sha256, computed 06:43:14 unless stated)

| file | sha256 |
|---|---|
| proof-SHgen-v2.md | 8fde88c0b0e95e14fdeb346c0e42673f22a7122510ce295afb3e33b7b8bdd239 |
| proof-ROT-few-v3.md | 5f158d697ce5308cf75a7fa0305818089ebdc48098c97a315b3a6e3de500efaa |
| proof-ELT0-FEW-v2.md | d4ee70819a9000264b13168966747e52b66ff323181c668582cfd7c98912246a |
| proof-SH3-v5.md | 93713e7057cb17c28de9d228f08abe6197d193799cd0982d5f301bfc536c380b |
| proof-ELT0-v3.md | 6a7bfd5b9708f6e930d895f87883d43f09ce9d82ddd14101b649665999d52362 |
| proof-ROT-o3-v4.md | 55670658a819af5ef5570fa71137ad51ee111e46e720cbac5bfdbfd7f51be8cf |
| proof-ROT-o4-v4.md | 7fa49e970603210639f1a0b834c54f5418859bc3dfaf164e34e67836cdaa425a |
| proof-SHm-v1.md | ecc91a52cffcbf14a74e714cd275a50a0b6fc1dde877d937c58a9bbcb246dadb |
| proof-SHROT-v1.md | d1c506c685913644b2752ef51604cf5a50bcb490595d1e23993d21b28ba9387e |
| proof-EXP2-v1.md | b5287e761fc8efbb64c8a1c0a9b54a643b8cff042f68407268ce13bd32d6eb13 |
| proof-EXP-v2.md | 4315e873b182eae8a6255dc45d801a95ad3b87b5900eee286be5308dfe57a2d9 |
| proof-ROT-lowodd-v1.md | 8ba3e6c7eeff5ec556166b76eb014d8141d5541c9c702ec3f537e602522f9785 |
| proof-ROT-o3-v3.md | 9b0a37dbcb30b9f989c530d74a9106b8ea312072860fae349232492a329b9ab7 |
| proof-ROT-o4-v3.md | db4eee8a5a43aee17a4bef38f79792a3488c9c7a4b8de4e6bcaa3e599550148e |
| notes-GRX-v1.md | afc6c31a2f9c9502655e3666595e535f4a003ccd7670ddbe993ebe4b620b1a30 |
| bundle-v2.md | 376c2dfd5a152d7f6768c12b12cf0310bf774b27b61a113785b0702b4efa8165 |
| addendum-timestamps-v3.md | fb423070d1762aee39d10f64863365cd7af56d64dd9edde26c95b78db4f681bb |
| code/check_rotfew_v2.py | f87831ffc199c8cab8ab5be3d1f972cd1c3125d59dc4c21aafb327b01ce1c32f |
| code/check_rotfew_v3.py | 6c3e37fbfece1c052a5b5ca4fb0bac65258fe14b652b5d92329c60a5c87fde89 |
| code/check_codex_examples_v1.py | ea4f1bf879efaca5d384b2db362b4ddbcbf17bc235555f93704005e697a7151a |
| code/flexa_check_v1.cpp (06:46:53) | 5801f84af39f6b78348e31fbbfa6f8f54d1c45e5663c2c09bf671970cf8823a4 |
| out/check_rotfew_v2.jsonl (06:31:00) | 464d6f594a066a5062e5c873843db101e2cd5fa51396547970ecf9d7235a9006 |
| out/check_rotfew_v3.jsonl (06:46:49) | 0e87030014ad66ad199e4f382bc83713dec206dd3e74ca1f3c923c7907f448c4 |
| out/check_codex_examples_v1.jsonl (06:26:01) | de6742db9db473c9bc947610f7467687a68a0f60f276b5e6510f2c2a4bfd56e3 |
| out/flexa_check_v1.jsonl (06:47:08) | 03b0541be4bca9db11514aa858d275c3cf122212ff8f6bed961164f659bc8e38 |
