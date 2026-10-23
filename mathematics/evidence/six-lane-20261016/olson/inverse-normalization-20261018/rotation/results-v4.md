# Rotation slice: consolidated results v4 (state at 07:40 PDT)

Written after host clock 2026-10-18T07:36:37-07:00 by OlsonRotationRigidity.  Supersedes results-v3.md (652787cb...91d5,
kept) as the summary; README.md remains the append-only log.  Labels: [ACC] parent-accepted, [CDX] Codex-reviewed
(disposition), [W] written and unreviewed, [O] observation.  o_F(w) = number of odd maximal constant reflection blocks
(maximal cyclic decomposition); kappa = p - 1 - (F - o_F)/2.  No novelty claim anywhere.

## 1. What is proved (exact scopes and dependencies)

| result | file (sha256 prefix) | status | scope |
|---|---|---|---|
| ROT-o2, ROT-o3, ROT-o4 | lowodd-v1, ROT-o3-v3 (+v4 wording), ROT-o4-v3 (+v4 wording) | [ACC] | rotations in one {rho_c, rho_-c} for avoiders with o_F <= 3 (p >= 5), o_F = 4 (p >= 7); any reflection runs |
| SHgen | proof-SHgen-v2.md 8fde88c0 | [CDX ACCEPT round B] | heavies of any odd weight with 2H >= E and k <= 2p - eta - a_max - 1 => solvable (all-odd, nonempty runs) |
| ROT-FEW | proof-ROT-few-v3.md 5f158d69 | [CDX ACCEPT, cond. SHgen] | constant runs, 5 o_F <= 2p + 4 => rotations in one pair |
| ELT0-FEW | proof-ELT0-FEW-v2.md d4ee7081 | [CDX ACCEPT] | constant runs, kappa = 0, 3 o_F <= 2p + 1 => all rotations equal (no SHgen) |
| ROT-FEW-E | proof-ROT-few-E-v2.md cb4bca7b (errata of v1, CDX A-W-F) | [W] | any runs, 5 o_F <= 2p + 4: ROT, cond. SHgen and REFL |
| INV*-FEW | proof-INVstar-few-v1.md 026753c9 | [W], in Codex round C | INV* for o_F <= 3 (p >= 5) / = 4 (p >= 7) cond. REFL-few-odd only; for 5 o_F <= 2p + 4 cond. also SHgen |
| KAPPA01 | proof-KAPPA01-v2.md efda5e07 | [W], in round C | INV* for kappa in {0,1} and 3 o_F <= 2p + 1, cond. SHgen + REFL-few-odd |
| OLSON-FEW | proof-OLSON-few-v2.md d19e5a30 (v1 2d29fcd2 in round C) | [W] | ORDERED OLSON at length 4p-1 for words with o_F <= 3 (p >= 5) / <= 4 (p >= 7), cond. REFL-few-odd only; for 5 o_F <= 2p + 4, cond. also SHgen |
| RIGID-STRUCT | notes-RIGID-STRUCT-v1.md 23ffb490 | [W] note, accepted imports only | every RGR-shape avoider: (I) kappa = 0, all rotations equal; or (II) kappa = k - 1 >= 1, k <= p, one run c^(2p-1), each other run one -c |
| SH3+-, SHm, SH-ROT, ELT0 | SH3-v5 93713e70, SHm-v1 ecc91a52, SHROT-v1 d1c506c6, ELT0-v3 6a7bfd5b | [CDX] (errata applied) | heavy-specific cases; ELT0: kappa = 0 tradeoff N + E <= 4p - 2 under FULL |

External input used: reflection/proof-REFL-fewodd-r2.md (OlsonReflectionRigidity; db16274f...c2c6; [W], inputs
parent-accepted RED + small-k verdict): REFL(p) for avoiders with o_F <= p.

## 2. Open, with the exact obstruction

* ROT for o_F > (2p + 4)/5 (general kappa): the binding step is WT (b) of ROT-FEW (the most frequent generator's
  multiplicity G must exceed 2kappa + w_+); beyond it, EXTRACT needs 2kappa <= p, MULT 3 o_F <= 2p + 1 and SHgen's (H)
  3 o_F <= 2p + 1.  The Davenport-tight avoiders (kappa = o_F - 1, type II of RIGID-STRUCT) are the generic survivors; for
  o_F >= p the all-plus pattern alone gives no structure and patterns with Phi >= 2 are needed.
* kappa = 0 beyond 3 o_F <= 2p + 1: reduced to S(p) (notes-SC-lengthp-v2.md 0c991ac3: every zero-sum-free sequence of p odd
  elements of Z_(2p) has Savchev-Chen form); proved there: S(p) => S(L) for L >= p, S(p) <=> SAT(p-1), and the stuck AP
  process is impossible when 3s <= p + 3; open: s >= (p + 4)/3 with the most frequent generator.
* REFL for o_F > p and non-constant runs beyond REFL-few-odd: reflection slice.
* General ordered Olson: equivalent here to INV*(p) for the remaining avoiders.

## 3. Finite aids and observations (not premises)

check_rotfew_v1/v2/v3, flexa_check_v1, check_codex_examples_v1, sc_explore_v1 (README entries 06:18 to 07:22);
observation (README 06:42:14): all listed avoiders at p = 5, 7 are of types (I)/(II) with o_F up to p.

## 4. Defects recorded

SHgen-v1 (false side sentence), ROT-few-v1/v2 (weaker), ELT0-FEW-v1 (range remark), KAPPA01-v1 (over-claimed kappa = 1
range; caught before sending), notes-SC-lengthp-v1 (garbled sentence), OLSON-few-v1 (weaker deletion choice), EXP2-v1
(x = 0 weight sentence), check_rotfew_v1 Part A negative controls (did not fire; replaced).
