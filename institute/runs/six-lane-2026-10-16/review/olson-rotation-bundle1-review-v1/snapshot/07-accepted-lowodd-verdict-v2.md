# Olson inverse normalization: GRX and rotation rigidity for at most two odd constant blocks

Parent at 2026-10-18T03:03:38-07:00: **CORRECTNESS-ACCEPTED at the exact partial scope below**, with required errata. Not full ROT/INV*, not ordered Olson, not a new breakthrough gate, not Lean and no novelty claim.

## Accepted statements

1. **GRX:** the exact identity2p-selection criterion in `notes-GRX-v1.md` for every word over D_(2p), p odd prime, arbitrary rotation multisets, empty rotation gaps permitted, and every cyclic constant-reflection-block representation. The group convention is(v,e)(v',e')=(v+ev',ee'), rho_x=(x,+1),sigma_y=(y,-1); identity selections have even reflection parity.
2. **PM*:** merging across an even constant reflection block preserves avoidance and the full rotation multiset, in the original-to-reduced direction only. Intermediate block representations need not remain maximal.
3. **K1/K2 and ROT-o2:** for every prime p>=5, a length4p-2 avoider whose **maximal cyclic constant reflection blocks include at most two odd-length blocks** has rotations all in one nonzero pair{rho_c,rho_-c}. The o=0 case is impossible; o=1 forces2p-1 equal rotations and2p-1 reflections. No assertion about reflection-run constancy follows. The number of ordinary reflection runs is not the parameter o.

Accepted texts, unchanged and read with this overlay:
- [proof-ROT-lowodd-v1.md](../../../../mathematics/evidence/six-lane-20261016/olson/inverse-normalization-20261018/rotation/proof-ROT-lowodd-v1.md), `8ba3e6c7eeff5ec556166b76eb014d8141d5541c9c702ec3f537e602522f9785`.
- [notes-GRX-v1.md](../../../../mathematics/evidence/six-lane-20261016/olson/inverse-normalization-20261018/rotation/notes-GRX-v1.md), `afc6c31a2f9c9502655e3666595e535f4a003ccd7670ddbe993ebe4b620b1a30`.
- Snapshot and LF count/hash pins: [manifest](olson-rotation-lowodd-review-v1/manifest.json).

## Independent verification

| Route | Result | Boundary |
|---|---|---|
| Codex gpt-6.1-sol |ACCEPT,0FATAL/MAJOR/requiredMINOR;590.7s|Only the pinned texts; no supplied parent derivation or finite outputs; read-only sandbox|
| Claude claude-opus-5-5 |ACCEPT-WITH-FIXES,0FATAL/MAJOR,7MINOR;983.6s|No tools; LF-numbered texts inlined; group-law source not in packet, checked separately by parent|
| Parent written derivation |GRX, PM*, inverse-sequence lemmas and K1/K2 packing/threshold proof re-derived|[DERIVATION](olson-rotation-lowodd-parent-v1/DERIVATION.md),d99f4093…d50a; no finite premise|
| Parent independent finite aid |1176/1176 exact GRX/raw ordered-product DP comparisons|[RESULT](olson-rotation-lowodd-parent-v1/RESULT.json),09095f77…a04f; pre-pinned source, no worker code/native child; not universal proof|

Notes: [Codex](olson-rotation-lowodd-codex-v1.note.md) `6fba60f7b0ec27bbff63ac46d57d07c85675afe1af6cd4ce1f8b382d38978f12`; [Claude](olson-rotation-lowodd-claude-v1.note.md) `d9219c78ab1c3c962cc3a0e921587f7716cd3ee3c2e1373867e845d145059c6a`. Both receipts report actual requested model identities and successful self-exit. Neither reviewer was shown the other's note. Their only substantive theorem import is classical EGZ for C_p; the two-disjoint-p-term application is explicitly checked. Z1/Z2 are proved, not imported inverse theorems. The parent checked the actual convention at `proof-dihedral-partial.md:11-15`; it matches GRX's contribution formula.

## Errata adopted (Claude M1–M7)

- **M1 required:** PM*, K1 and K2 are stated for any cyclic constant-block representation, allowing empty rotation gaps and adjacent equal blocks. Maximality is required only when defining the original invariant o for ROT-o2. The proofs themselves use no maximality, so their iteration is valid.
- **M2 required:** explicitly name the group law above and the even selected-reflection parity. Under the opposite convention the sign of T changes; do not mix conventions. For a literal rho_V product formula first normalize z1=+1; global sign reversal preserves the zero condition.
- **M3:** cancellation lengths1+e_h are even. The cumulative threshold crossing in K2 uses that parity to bound the pre-crossing total by2t and the crossing by4t.
- **M4:** if o=0, PM* leaves one even block but K1 forces the reflection count2p-1 odd, contradiction. Do not leave the exclusion implicit.
- **M5:** use a new symbol for cumulative cancellation lengths, distinguish sequence terms from partial sums, and define H=sum floor(l_i/2). “Only pattern” in K1 means up to global sign; the symbol for a signed sum is not a reflection element.
- **M6:** the final parity relation is always o≡R mod2 at total length4p-2; replace the garbled parenthetical accordingly.
- **M7:** reviewer observes the argument may extend to p=3. This verdict keeps p>=5 and does not promote that extension.

These wording/scope repairs change no formula or proof object. Old files are preserved. Source/clock labels are not retroactively converted into preregistration.

## What remains open

ROT for o>=3, conditional reflection-run rigidity, full INV*(p), and ordered Olson for D_(2p). The worker's later `proof-ROT-o3-v2.md` and finite ROT(7) frontier are **not covered by this verdict**. Their lemmas require their own review. The accepted [RGR-LONG theorem](olson-runs-parent-verdict-v1.md) cannot be applied to arbitrary words merely because ROT-o2 holds on a subclass.

Navigation erratum: v1 (`79137b2481e31525ff028d8f02b033962e42c5ecda856fc741dbecf4b5912541`) used one too few parent traversals in the two lane links. v2 changes those two links only and preserves the failed v1.
