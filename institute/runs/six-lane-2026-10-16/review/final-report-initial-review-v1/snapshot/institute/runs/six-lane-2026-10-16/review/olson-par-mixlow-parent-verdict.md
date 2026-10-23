# Theorems M and P (MIX_low and PAR for dihedral D₂ₚ) — parent verdict (math-2) — 2026-10-17 23:28:06 PDT (host clock)

**Disposition: CORRECTNESS-ACCEPTED (written proof), PARTIAL — not a gate.** These are inverse-structure components of the ordered-Olson programme for D₂ₚ. They do not prove ordered Olson for D₂ₚ, which still needs RUNS(p) and INV*(p).

## Accepted statements (lane `mathematics/evidence/six-lane-20261016/olson/inverse-parity/mixdef-low/c2/`)

- **Theorem M — MIX_low(p) for every prime p ≥ 5.** Let D₂ₚ = ⟨r,s | rᵖ = s² = 1, srs = r⁻¹⟩, and take a cyclic RGR word of length 4p−2: k nonempty rotation runs over {r, r⁻¹} alternating with k nonempty constant reflection runs, every reflection run of odd length. Let A ≥ B ≥ 1 count r and r⁻¹, H = Σ⌊l_j/2⌋ and κ = p−1−H. If k ≤ p and B < κ ≤ k−1, the word contains 2p letters, in increasing index order, whose product is the identity. Text: `proof-R4-closure-r1.md` §2 (r1:61–80).
- **Theorem P — PAR(p) for every prime p ≥ 5.** Every inherited avoider w′ in RGR₍₄ₚ₋₂₎(p) with k ≤ p, F, R ≥ 1, has all 2k runs odd. "Inherited" means the five conditions (E), (P), (V), (Pairs), (D0) of `proof-INV-reduction.md:14–16`. Text: `proof-R4-closure-r1.md` §3 (r1:84–91).

| File | sha256 |
|---|---|
| proof-R4-closure-r1.md | `4432a2d840a2651540e38d4c2b2ad102d3ba7ad21fc25f74606b1d5c9f9f8837` |
| proof-Rstar-r4.md | `3b27db3f16341b2493bab1ef259e7cec8a1ce4d6d523b74518909bac541d3fa9` |
| proof-PAR-assembly-r2.md | `0bb78d1f948e4646665ec89fbfe8048f81aa138bbd4d66af1328acbf82276648` |
| proof-MIX-low-partial-r2.md (import, reviewed earlier) | `adf8cb7014c91e6c7c19bef894f2e5d2f75e36a34291c7cad4993a1f85716a22` |
| ../../../inverse-run-count/proof-RUNS.md (Lemma M0 §12) | `e3682f4d02ab0062cddfda8d4199f4307860936581cf75b843a93e91dec40661` |

Imports with earlier review status:
- Lemma GR and Lemma WAS (Claude review).
- PAR/RUNS/DR-Res reduction (Claude review).
- Lemma H, Lemma BC and Theorem K0 (Codex ACCEPT).
- Lemma OR, K1, K1′, S1′, A1′ and KB (Codex ACCEPT-WITH-FIXES, delta-checked).
- Lemma S, Lemma K and MIX-R (Codex ACCEPT-WITH-FIXES, delta-checked).
- KL, W, B1, A, G1, KS and AC (Codex ACCEPT and Claude ACCEPT-WITH-FIXES).

New in this cycle: Lemmas ZP and C, Lemma R4, Corollary R4-av, and Lemma M0 (independently reviewed for the first time here).

## Evidence

1. **Hostile reviews of the unreviewed closure** (snapshot incl. Lemma M0):
   - [Codex](olson-par2-closure-codex-review-v1.note.md) `2ee09b8efa1de3e0f3f176484bda27edc633fcb207fb4de9c457ca09592f38a1`: ACCEPT-WITH-FIXES, 0 FATAL / 0 MAJOR / 3 MINOR. It independently checked M0 and ran small-prime HW/ordered-product controls, including exhaustive normalized checks at p = 5, 7.
   - [Claude](olson-par2-closure-claude-review-v1.note.md) `bfd7038b2eee400c87eb68ea18be5ef9966ee879f9e6415fc764fe3508f9f314`: ACCEPT-WITH-FIXES, 0 / 0 / 11. The most consequential item: Theorem M had to be derived from avoider data, not from the interval-feasible corollary.
2. **Parent mathematical spot check** ([note](olson-par-math-parent-spot-v1.md)): re-derived the R4 dichotomy algebra and M0 window monotonicity. It flagged one ordering clarification (properness of S before c(S)), now fixed.
3. **Delegated parent delta check** ([delta-check.md](olson-par2-delta-v1/delta-check.md) `4df664fc5e96f3150601222a82e62c2c9beaced7cded3c36d96b0761a74efb2d`): all 15 items handled, so all three files are DELTA-ACCEPT-WITH-NOTES. Codex delta review: ACCEPT-WITH-FIXES, 0 FATAL / 0 MAJOR, 4 MINOR plus 2 NOTE, about declarations, stale status lines and paths. The desk verified:
   - Theorem M now runs from avoider data only (trivial cut; M0; S1′ when B′ = 0; else Lemma S → Corollary R4-av → Lemma R4).
   - The BH(S) chain and the properness of S.
   - Z0⁺ ≠ ∅.
   - Theorem P's hypothesis chain is exhaustive in κ and B.
   - No theorem depends on census output.
4. **Priority:** NONE-FOUND-IN-SCOPE ([scout transcription](olson-par-priority-scout-v1.md)). No ordered inverse result at length 2|G|−2 for any non-abelian, non-p-group was located. Rated a **modest extension**: it changes no published bound on z(D₂ₚ). Side finding, not used here: Godara–Joshi–Mazumdar's Conjecture 5.1 (arXiv:2407.01148) fails for odd dihedral groups.

## Non-blocking notes and limits

- Remaining text issues in the new files: overstated "nothing else changed" lines; stale status text (r4:31 M0 status; r4:231 "(open)"); undeclared deletion of one evidence-only sentence; some unresolved relative paths; r1:61–62 should read "R = A+B".
- Stale lines remain in unchanged imports: `proof-PAR-K0.md:4` and `proof-PAR-Kplus-partial-r2.md:133`. They are recorded in assembly r2 and not used by any proof.
- Not established: RUNS(p), INV*(p), unrestricted INV and MIX_DEF, ordered Olson for D₂ₚ, and p = 3 (S₃ separately exhaustive in the lane).
- No Lean formalization.
- The finite census aids (rstar_census*.cpp) remain unreviewed code and are not premises.

## What this changes in the lane's obligation map

Given Theorem P, ordered Olson for D₂ₚ (p ≥ 5) reduces to INV*(p) + RUNS(p) (`obligations-after-PAR.md`, e9034201…). RUNS(p) for o_F ≤ p follows conditionally via Corollary RL, which is unreviewed. The open parts are the o_F ≥ p+1 residual (O2d; owned by OlsonRunCount5, with large progress under review) and INV*(p), whose only partial result is the rigid half (GR0-r1, unreviewed).
