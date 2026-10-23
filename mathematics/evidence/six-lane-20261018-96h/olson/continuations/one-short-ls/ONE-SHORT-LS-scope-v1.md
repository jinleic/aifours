# Frozen scope: ONE-SHORT-LS (sequence level, exact length p+2kappa), v1

Owner OlsonAssemblyLS. Frozen after /bin/date 2026-10-19T10:17:32-0700, BEFORE any derivation for this target.
Authority: Main's IRC instruction of 2026-10-19 (after the ASSEMBLY-LS review freeze
review/olson-ASSEMBLY-LS-review-freeze-v1.json, sha256 0cff43de416972e84e37fde55e65fcd654984b9e1a684803a989e70d3b5b1b6f).
The assembly-ls directory is frozen and untouched; ASSEMBLY-LS stays CANDIDATE. Status of everything below: target statement
only, NOT a proof or verdict. Written research only: no computation, enumeration, script, solver, test, build or model CLI.
Writes only in this directory, exclusive create, versioned names; every old file is read-only.

## Exact target
ONE-SHORT-LS(p, kappa). Let p >= 7 be prime and kappa an integer with floor(2p/3)+1 <= kappa <= p-2. Every sequence Y of odd
elements of C_(2p) with EXACTLY |Y| = p+2kappa that satisfies (ZP_kappa) (no zero-sum occurrence subsequence of length in
[2kappa+2, 2p]) satisfies (S1_kappa) (every zero-sum occurrence subsequence has length <= 2kappa; equivalently, under (ZP_kappa),
none of length >= 2p+2).
- Excluded endpoint kappa = p-1: the sequence g^(2p-1)(3g)^(p-1) (g an odd generator) has length 3p-2 = p+2(p-1), satisfies
  (ZP_(p-1)) and contains the zero-sum g^(p+3)(3g)^(p-1) of length 2p+2; nothing is claimed there.
- Not in scope: kappa <= floor(2p/3) (accepted S1-sharp, length-free); |Y| >= p+2kappa+1 (accepted G-LS, Lev-conditional for
  e = p-kappa >= 3); |Y| < p+2kappa; p = 5 (floor(10/3)+1 = 4 > p-2 = 3, empty range).
- The G-LS threshold p+2kappa+1 is NOT lowered by assertion. Purely sequence level: no word realizability is assumed; any
  o_F = p (terminal k = p) consequence stays conditional on the pending ASSEMBLY-LS and a separate word-level review.

## Allowed routes (either outcome is a valid deliverable)
(R1) Structural proof, e.g. adapting the accepted G-LS few-sums/core argument (stab-round2/proof-general-LS-Lev-v1.md) to
     |Y| = p+2kappa, with EVERY changed constant re-derived; or another written argument.
(R2) An explicit mathematical falsifier: exact p, kappa, Y with |Y| = p+2kappa, (ZP_kappa) and a zero-sum of length >= 2p+2,
     verified in writing (no enumeration). A family or a single cell both count; a partial-range outcome is reported as such.
If neither closes, deliver an obstruction note: exact failing step, exact blocking hypothesis, smallest missing lemma, with
every failed branch preserved.

## Admissible inputs (original domains only, with exact parent verdicts)
- Accepted interfaces read at their ORIGINAL scopes, each checked for whether it applies at EXACT length p+2kappa (several are
  stated at the threshold p+2kappa+1): RED/SLZ/EXT/PROP (KPS-SLZ verdict item 4), CF(a), DGM-p, LS-threshold dichotomy, LS-II',
  AP (CF-XT/ROW/LS-II verdict items), AP' (general-LS verdict m1 standalone admission), SLZ3 (SLZ3 verdict), S1-sharp, G-LS
  (only at its own threshold), and accepted LS+/BASE1 cell bounds only through their exact parent verdicts.
- External: Lev 2022 Theorem 2 at the statement level exactly as admitted by the general-LS verdict; classical imports carried
  by accepted interfaces. No pending narrower candidate (BASE2 normalization/closure, S3/P1-P3 bodies, etc.) is imported.

## Trust and claims
Every new claim is CANDIDATE_UNVERIFIED. No novelty, priority, Lean or human-review claim; never "first". Transitive
computer-assisted imports are disclosed where present. Not claimed: LS+, STAB, any word-level statement, INV*, ordered Olson.
