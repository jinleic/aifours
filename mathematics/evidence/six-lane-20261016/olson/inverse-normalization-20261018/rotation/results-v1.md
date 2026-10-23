# Rotation slice (half (a) of INV*): consolidated results, exact scopes, residual

Owner OlsonRotationRigidity.  Written after host clock 2026-10-18T05:18:24-07:00.  Contract
R/../screening/math-2-invstar-continuation-contract-v1.json (sha256 9a362a94...0512).  No full ROT(p), INV*(p) or
ordered-Olson claim.  No novelty claim.  Statuses: [ACC] parent-accepted; [CDX] Codex-reviewed only; [W] written,
unreviewed; [F] finite-exact computation (aid, never a universal premise); [O] observation/conjecture.

Target ROT(p): every avoider of length 4p-2 over D_(2p) has all rotation letters in one {rho_c, rho_-c}, c != 0.
o := number of odd maximal constant reflection blocks of the avoider.

## 1. Proved

| result | scope | status | file (sha256 prefix) |
|---|---|---|---|
| Lemma GRX (exact criterion, every word, any constant-block representation incl. empty runs) | all p odd | ACC | notes-GRX-v1.md (afc6c31a) |
| Lemma PM*, Props K1, K2, Corollary ROT-o2 (o <= 2) | p >= 5 | ACC (verdict R/olson-rotation-lowodd-parent-verdict-v2.md, 0853f4ac) | proof-ROT-lowodd-v1.md (8ba3e6c7) |
| Lemma INC, Lemma DEL, Prop K2', Theorem ROT-o3 (o = 3) | p >= 5 | CDX ACCEPT (R/olson-rotation-o3o4-codex-v1.note.md, 86061f1c); Claude pending | proof-ROT-o3-v3.md (9b0a37db) |
| Prop K3', Theorem ROT-o4 (o = 4), Corollary ROT-o<=4 | p >= 7 | v2 CDX ACCEPT-WITH-FIXES; fixes in v3 [W] | proof-ROT-o4-v3.md (db4eee8a); v2 878fd123 |
| Theorem EXP (any o): heavy rotations expanded in place + reflection pairs deleted; under fullness (X1) and pairs (X2), RGR-shape and #rho_-c <= #rho_c, contradiction with accepted Cor. B'(b) / C1 composition | p >= 5 | W | proof-EXP-v2.md (4315e873) |
| Prop SH-ROT: rho_-3 sigma_2^(2p-5) rho_1^(2p-1) sigma_0 is a non-rigid avoider of length 4p-4 (sharpness, not a counterexample) | p >= 5 | W | proof-SHROT-v1.md (d1c506c6) |

p = 5 for o = 4 (and ROT(5) in general) rests only on the lane's prior exhaustive D10 claim (pins in proof-ROT-o4-v3.md
Sec. 5), pending parent provenance audit.

## 2. Finite-exact [F] (GRX classifier; Python v1-v3 and C++ v2; every non-rigid hit re-verified by fresh raw DP)

Via Lemma DEL (o odd blocks at 4p-2 -> o-1 at 4p-3), no non-rigid avoider with at most o odd blocks:
p = 7: o <= 7; p = 11: o <= 6; p = 13: o <= 6; p = 17: o <= 5; p = 19, 23: o <= 4.  Neighbourhood search: 0 non-rigid
avoiders among one/two-letter modifications (188,447,532 words) of all 3,738 p = 7 RGR avoiders.  Runs stopped by their
own CPU limits are UNKNOWN (S(7,25,7); S(k,17,5) for k >= 6).  Logs: README.md.

## 3. Observations [O] (data only)

ELT (excess-length tradeoff): let E_min(w) = min over generators g of the sum over heavy rotations (weight a not +-1)
of (min(a, 2p-a) - 1).  Every non-rigid avoiding datum found (lengths 4p-4 .. 4p-7, p = 7, 11, 13, k <= 4) satisfies
N + E_min <= 4p-2, with equality attained (e.g. SH-ROT).  ROT(p) is exactly the case N = 4p-2 of ELT.
SH1: at lengths 4p-4 and 4p-5 every non-rigid avoider found has exactly one heavy rotation, of value +-3c.

## 4. Exact residual of ROT(p)

ROT(p) remains open (p >= 7) for avoiders with o >= 5 odd blocks such that, for every generator choice, Theorem EXP does
not apply: (i) a heavy rotation with too few light rotations in its own run (fullness (X1) fails; SH-ROT shows such
"thin" heavies occur in avoiders of length 4p-4), (ii) heavy values near -c (weight close to 2p-1; expansion cost exceeds
the available reflection pairs (X2)), including the boundary case B = kappa - 2 for a single -3c, (iii) non-constant
maximal reflection runs (empty runs; EXP then needs the reflection slice's REFL(p)).

## 5. Failed or limited routes (concrete)

* Run-replacement monotonicity (replace a run multiset by a rigid one with smaller subset-sum profile): fails already
  for two-element runs {a, b}, b != +-a.
* Same-length local SPEC replacements of a thin heavy: any rigid replacement of sigma_u h sigma_v or sigma_u^l h sigma_v^l'
  of equal length has a size/product pair outside Spec(X) (checked by hand, notes in the session; not written as a lemma).
* Iterating Lemma DEL twice: fails, S(2, 4p-4) and S(3, 4p-4) have non-rigid avoiders (K2' is sharp in length).
* Zero pattern alone: decides o' = k + s <= 2 at kappa <= 2 and all kappa for o' = 3 (via K2'), but leaves many
  survivors when H is small (out/zp_spectrum_p7.jsonl).
* Expansion EXP-LONG (no pair deletion) + RGR-LONG: works only when count constraints are trivial (kappa = 0) and subset
  sums are full; each DEL used to fatten a thin heavy costs one letter, exactly the slack ELT says is unavailable.
* Stochastic local search at p = 7 (generic and H-small classes): its positive controls failed to find even rigid
  avoiders, so all its misses are uninformative.
