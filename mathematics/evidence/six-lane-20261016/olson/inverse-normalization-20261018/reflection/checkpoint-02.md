# Checkpoint 02 (OlsonReflectionRigidity), host clock 2026-10-18T04:10 PDT

Scope: REFL-RES(p) = no avoider in RES_<(p) with kappa >= 2, all primes p >= 5 (proof-RED-r2.md Sec. 5). Not proved in full.

## New exactly scoped sub-theorem [W, unreviewed]

Theorem B0S (proof-B0S-r2.md, sha256 bd854fe85f34f4976acfaecfae79311bc504c34f42d99a909dc7cbe93dfe7170).
Statement: every word of length 4p - 2 whose rotation letters are all equal (B = 0), whose maximal reflection blocks are all odd,
with k <= p blocks and kappa >= 1, has an identity 2p-subword. Any number of empty runs is allowed.
Corollary: RES_<(p) has no avoider with B = 0 and k <= p, for every prime p >= 5.
Imports: Lemma H0 only (on GR0 = accepted GRX). No RGR theorem, no finite computation.
Where empty runs enter:
- Step 1 (eight-case lift bound): runs with small R - r_t.
- Empty-defect range x_t in [1 - kappa, -1].
- Case II (Phi(Z) <= 2 kappa), which needs >= 2 empty defects and is killed by adding isolated bh = 1 runs.
Superseded: proof-B0S-r1.md, sha256 c848d060e8b59377c74ad3b5d1726c89ac52b1b84d38a419c288bf35daf44408. The r1 -> r2 changes are
arithmetic in two displayed bounds; the fix map is in Sec. 7.
This also supersedes the "open sub-lemma S1'-G" of notes-RES-B0-r1.md. Erratum to that file: its Sec. 2 claim that every
non-defect has bh = 1 is wrong. The correct facts are s <= g_Z - 2 m_Z and |Z| <= kappa - m_Z (proof-B0S-r2.md Sec. 5).

## Aids (finite, not premises)

- plan-E8.md: 37773b4443408db0c4fb6f021db6f5a9b17ad9357fe98570d1bb840d6040ebe0
- code/e8_b0s_replay.py: 1c4c50331e21352819722cbc8996b450fa54b7b88115de2a87447d9780733743
- out/e8_b0s_replay.json: 47ca8253a54ee18383f6094f3bc36ab49be5465cf5f61413372dbaea58f2cfe5
- plan-E8b.md: ba3668b317472f440d5451b71e7dad8f4a4148638092d09be0688ad5bd91ab1f
- code/e8b_lift_sampled.py: 20546ba7dd1015b3652cd52cd15d04b0a1c1363b5ebebc93116b44ad92617e15
- out/e8b_lift_sampled.json: 24202342310eb8d942049899820ede5630f460db33d632219b008e682451692d

Results:
- The proof pattern was built and checked on 130 E8 family words (Case I 87, Case II 43) and 1994 E8b words (all Case I).
  There were 0 failures of (U1)-(L3) or of the actual hit.
- Mutation control: replacing a W item by a run adjacent to Z left a kill in only 15 of 43 cases.
- Raw DP found every word solvable: 657 of 657 in E8 and 1500 of 1500 in E8b (p <= 11).

## Still open inside REFL-RES(p)

- (a) B = 0 with k >= p + 1. The RGR route, C0-B' plus the Depth Lemma (proof-RUNS.md Secs. 9-11), has a Step 1 that uses
  k + r_t <= R + 1. That fails for G-words, and the pair patterns of the Depth Lemma may contain empty runs.
- (b) Every class with 1 <= B < kappa and pure runs (MIX type, k <= p and k >= p + 1).

## Earlier files (unchanged)

- proof-K0star-r2.md: 6681676e4f80018e792c7117ce9fc524a31aeb397c35880f57468ada9c0396e1
- proof-RED-r2.md: c4e7697f0f691980e19ef3332a1e2c6b0dbdc76ba268e87c32eb563f4d3fd3d7
- results.md: d0b5fcf40c7b0fd2eadbd9d72ee38deba9fd77535f2580c67a994059d16dd384
