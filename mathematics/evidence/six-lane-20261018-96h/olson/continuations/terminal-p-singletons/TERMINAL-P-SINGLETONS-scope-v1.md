# Frozen scope: rotation rigidity at the endpoint terminal k = p, kappa^ = p-1 (all-singleton terminal blocks), v1

Owner OlsonAssemblyLS. Frozen after /bin/date 2026-10-19T10:50:41-0700, BEFORE any written derivation for this target.
Authority: Main's IRC instruction of 2026-10-19 (after the ONE-SHORT-LS review freeze
review/olson-ONE-SHORT-LS-review-freeze-v1.json, sha256 90a0121949af62e748331a4b75b6a90274cf3004d84536514bf048cedc7a3d92).
assembly-ls/ and one-short-ls/ are frozen and untouched; ASSEMBLY-LS and ONE-SHORT-LS stay CANDIDATE. Status of everything
below: target statement only, NOT a proof or verdict. Written research only: no computation, enumeration, script, solver,
test, build or model CLI. Writes only in this directory, exclusive create, versioned names; old files read-only.

## Exact target (word level)
Theorem ROT-SING. Let p >= 7 be prime and w an avoider of length 4p-2 over D_(2p) (no 2p letters in increasing original index
order with identity product). Suppose SOME admissible normal form w^ of w (accepted PM*/fusion process, existential reading of
ZX overlay 2) has terminal k = p and kappa^ = p-1; then H^ = 0, every one of the p terminal blocks is a single reflection,
F = p and R = 3p-2. Claim: every rotation letter of w lies in one set {rho_c, rho_-c} with c != 0.
Optional strengthening, to be proved or dropped explicitly: the rotation multiset is exactly rho_c^(2p-1) rho_(-c)^(p-1).
No hypothesis on o_F(w); nothing is claimed about reflection runs.

## Allowed outcomes
(R1) A written proof. (R2) A fully specified WORD-level counterexample (explicit p, letters and order), with avoidance verified in
writing through GRX. (R3) A precisely proved obstruction with the smallest missing lemma. The sequence g^(2p-1)(3g)^(p-1) by itself
is NOT a word realization and cannot falsify the target.

## Boundaries
- ONE-SHORT-LS excludes kappa = p-1 and is NOT extended here; no (S1) at kappa^ = p-1 is assumed (it can fail at sequence level).
- ROT-KP+ (needs (S1) at kappa^) and ROT-FB(b) (needs every zero-sum of length <= 2kappa^-2) are read at their original scopes
  only as context; they are not applicable premises at kappa^ = p-1.
- Inputs to be read before the proof and used only at accepted scopes: the normal form (proof-ROT-few-E-v4.md Sec. 0; ZX overlays
  1-3; lowodd overlays M1, M4), GRX for every cyclic constant-block representation with arbitrary (non-constant) sign patterns,
  including the accepted ARC form (proof-ROT-KP-v1.md Sec. 0; ROT-KP verdict), Lemma CT (STAB-delta item 6), and the classical
  Cauchy-Davenport theorem.
- Not claimed: reflection rigidity or INV*, any o_F = p assembly (separate until ONE-SHORT-LS is accepted), ordered Olson for
  D_(2p) or all groups, p = 5, novelty, priority, Lean or human review. Every new claim is CANDIDATE_UNVERIFIED.
