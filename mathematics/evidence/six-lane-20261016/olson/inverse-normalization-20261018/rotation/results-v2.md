# Rotation slice (half (a) of INV*): consolidated results, exact scopes, residual

Owner OlsonRotationRigidity.  v2 written after host clock 2026-10-18T05:20:33-07:00; v1 (sha256 39c28e3a...3afc)
kept unchanged.  Change: Sec. 5 zero-pattern bullet corrected (v1 misstated which cases the zero pattern alone
decides); Sec. 6 manifest added.  Contract
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
* Zero pattern alone (o' := k + s for k all-odd blocks at length 4p-2-s): decides o' <= 2 (K1, K2); for o' = 3, 4 it
  leaves non-rigid survivors (e.g. g^(2p-4)(3g) at kappa = 0) that need one-run windows (K2', K3'); when H is small it
  leaves very many survivors (out/zp_spectrum_p7.jsonl).
* Expansion EXP-LONG (no pair deletion) + RGR-LONG: works only when count constraints are trivial (kappa = 0) and subset
  sums are full; each DEL used to fatten a thin heavy costs one letter, exactly the slack ELT says is unavailable.
* Stochastic local search at p = 7 (generic and H-small classes): its positive controls failed to find even rigid
  avoiders, so all its misses are uninformative.

## 6. Manifest (sha256, computed by the slice; full list in README.md closing entry)

notes-GRX-v1.md afc6c31a2f9c9502655e3666595e535f4a003ccd7670ddbe993ebe4b620b1a30
proof-ROT-lowodd-v1.md 8ba3e6c7eeff5ec556166b76eb014d8141d5541c9c702ec3f537e602522f9785
proof-ROT-o3-v1.md 0ab9ae7d242da303f9b2010f7fbce335424c3b4415d65111cccb7f0721cccfea (superseded)
proof-ROT-o3-v2.md 2c02086c8d4cb5feee13d0f7b4d4fecf5c9f21b4305a3ca7a07a000cd3c57ae0 (superseded; INC slip)
proof-ROT-o3-v3.md 9b0a37dbcb30b9f989c530d74a9106b8ea312072860fae349232492a329b9ab7
proof-ROT-o4-v1.md 11d7dd035c8826de17d29340d4a1119430bffd5da7d7402e02c036fe6be9d44b (superseded)
proof-ROT-o4-v2.md 878fd123cf69941b0e4f0f86e0dde20ab7fb29481c61c30a4b81e8b34fa1e741 (reviewed; superseded by v3)
proof-ROT-o4-v3.md db4eee8a5a43aee17a4bef38f79792a3488c9c7a4b8de4e6bcaa3e599550148e
proof-EXP-v1.md bbae26e47607c6b312fd81cefb4df5400b3ca2832fa3fdfaa3f76e4e41038900 (superseded)
proof-EXP-v2.md 4315e873b182eae8a6255dc45d801a95ad3b87b5900eee286be5308dfe57a2d9
proof-SHROT-v1.md d1c506c685913644b2752ef51604cf5a50bcb490595d1e23993d21b28ba9387e
addendum-timestamps-v2.md 01d42b3abb34b63b51b26451055794ae25aa0faa597d189b16981ca8d1b19aec (v1 276c4f01... superseded)
code/rawdp.py 9e0d92194ef24d9b8c9f3d20254b12b398bc2dc123d68948b99319e5d2cbac01
code/grx.py e8f546efe7f11a114b2f0629824aca33a33b62570a2cc10325658a52fe81416a
code/kblock_exact_v2.cpp 5a78a05f74c65be265f0de33e7d65469b61ab4971cf6aed91b26faf2fe194816
code/kblock_exact_v3.py 7a8d600fbaca0f8c512e9f51141c81bb6f3e7ee988c61aabfe84a81d17e3a164
code/verify_kblock_hits_v1.py 34be9599b7675d8b5fee639934c44b96f1e30a1ec55b96238ba9d364a493800d
code/check_inc_v1.py 1846b8ffba457db4ecc2cd78eb032863368a2bee716f233dce3c51d14cdc6f94
code/check_zero_lemmas_v1.py a7061689a7c256567f3bd72f42d73cd6a291a170ac669544f17fe32d08048abf
code/sharp_rot_family_v1.py 378825a1b6a25b9cafdef5ab9187414418989942d567e6dbf765d367ee459030
code/rot_nbhd.cpp 3f7dfd3f4fbc93e40e39e346a5d3648d98fbcf0aeeb0b6b6b8d82d6914567dec
code/test_grx_v1.py e4eb8a8ca52de7ba92e44b525a8f54b986a26ad3c2a16b27b3e87955e1a6cd2d
code/gate_v1.sh 0292511a24268e69a37c6de7d3d93bbfd7305e9895b7bdd2da7dc65d22634e5a
