# Frozen scope: rotation rigidity at terminal k = p+1, kappa^ = p-1 (all-singleton terminal blocks), v1

Owner OlsonAssemblyLS. Frozen after /bin/date 2026-10-19T10:59:40-0700, BEFORE any written derivation for this target.
Authority: Main's IRC instruction of 2026-10-19 (after the ROT-SING review freeze review/olson-ROT-SING-review-freeze-v1.json,
sha256 e8ae90a285013c66e24e8b6a12eb306d35bd9fd2ab17f5c0f8646a8b5103acf1). assembly-ls/, one-short-ls/ and terminal-p-singletons/
are frozen and untouched; ASSEMBLY-LS, ONE-SHORT-LS and ROT-SING stay CANDIDATE. Status of everything below: target statement
only, NOT a proof or verdict. Written research only: no computation, enumeration, script, solver, test, build or model CLI.
Writes only in this directory, exclusive create, versioned names; old files read-only.

## Exact target (word level)
Theorem ROT-SING+ (k = p+1). Let p >= 7 be prime and w an avoider of length 4p-2 over D_(2p). Suppose SOME admissible normal
form w^ of w (accepted PM*/fusion process, existential reading of ZX overlay 2) has terminal k = p+1 and kappa^ = p-1; then
H^ = 0, every one of the p+1 terminal blocks is a single reflection, F = p+1 and R = 3p-3. Claim: every rotation letter of w lies
in one set {rho_c, rho_-c} with c != 0.
Any classification of the rotation multiset used on the way is a NEW lemma proved here at the changed length (3p-3 rotations;
an arc pattern omits only p-1 rotations), never inherited from the k = p case. No hypothesis on o_F(w); nothing is claimed about
reflection runs or about any other k, kappa^ or o_F.

## Allowed outcomes
(R1) A written proof. (R2) A fully specified WORD-level counterexample (explicit p, letters and order) with avoidance verified in
writing through GRX. (R3) A precisely proved obstruction: exact failing step, exact missing hypothesis, smallest missing lemma,
with every failed branch preserved.

## Inputs (accepted scopes only, re-derived where constants change)
The accepted normal form (proof-ROT-few-E-v4.md Sec. 0; ZX overlays 1-3; lowodd overlays M1, M4); GRX for every cyclic
constant-block representation and every sign pattern (lowodd verdict item 1), including multi-change patterns; Lemma CT
(STAB-delta item 6) and Lemma RS(a) (CFXT verdict item 4) at the new length; classical Cauchy-Davenport and any other classical
statement used, each stated explicitly. NOT premises: (S1) at any kappa, ONE-SHORT-LS, ROT-SING, ASSEMBLY-LS, ROT-KP/KP+, ROT-FB,
restricted REFL.

## Not claimed
Reflection rigidity, INV*, any o_F >= p+1 or k >= p+1 statement beyond this exact cell, ordered Olson for D_(2p) or all groups,
p = 5, novelty, priority, Lean or human review. Every new claim is CANDIDATE_UNVERIFIED.
