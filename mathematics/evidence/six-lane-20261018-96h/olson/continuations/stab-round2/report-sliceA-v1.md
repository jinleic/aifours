# Slice A (STAB / LS+ / LS) report v1: candidates, dependencies, exact target delta, remaining obstruction

Owner OlsonSTABSuccessor.  Written after /bin/date 2026-10-19T06:14:09-0700.  Directory: /Users/jinleic/repos/aifours/mathematics/evidence/six-lane-20261018-96h/olson/continuations/stab-round2/.
Labels: ACCEPTED = parent verdict exists; CANDIDATE = written proof [W], unreviewed or under review.  No novelty, Lean, human-review
or ordered-Olson claim.  Sequence level only throughout; no INV*/word-level consequence is claimed here.

## 1. Files (sha256)
Scope: STAB2-scope-v1.md c98182632eb9ef39904c43ef75815919b56142ade2137f30c5d99482dcaa4e89.
ACCEPTED (run review/olson-CFXT-ROW-LSII-parent-verdict-v1.md ca6e4ca75bba7f88024667951e160ffb8555d99389d50e34fd2cceef31b420e0, exact scopes there):
  proof-CF-XT-v1.md aa602d45e154a7787ac3f0270a3c26deb5e8c6a70736cf4a82c700f5368c191f; proof-ROW-v1.md a7b73415a83a6d898589c820d311e5ad084e864521adf937f1eee05d69fc4b2d; note-STAB-range-v1.md 5b8faa3ab578c373e6fa01be32b10b476950f450f93a00580dd082366a630115;
  erratum-1-CF-XT-ROW-range.md 767fe8f8605019b3b3b7aa1ff6a610f088279ede30b9b3429544d4c8487c1db7; proof-LS-caseII-v2.md 3df159ff61784cb3345b27a6cf9da873900051df92dbb3be019e846578d73a43; erratum-2-prereq-consolidated.md fb136e6ef71f7250774c3102a35c88a9709fee827091df84f67b433fb13106d5.
CANDIDATE, delta package (delta-review-package-v1.md 23a5be43a94cc7fa39cf067769bfac2d9248aaf6f882607c0ddd9868670e861b):
  proof-LS-caseII-v2-addendum-1.md c289db226c86ea7703af4a23c4a93dce543669cb911d36b5845e70aad2c98718; proof-LS-caseI-smalldelta-v1.md 2ad172a026ee64441f00fd228b8b402a0a5f2e0d85df04512c87f0e70e5a68b1 + erratum-1-delta-APprime.md
  e035f8d14b6bcb57c0af0d5beb170ddf3471674490583e66b75d0d34cc90c461; proof-STAB-base-p1mod3-v1.md 8a41189cb8d2c254394c4ac44963d7a64f7f6ace00a9ad829f7e0af96def0985; proof-LSplus-e2-v1.md 2effb09ea4e28553ab0321a64b3e660c422d767ef940fcf58615dec8edc208b1; proof-LS-lin-v1.md
  434a5dfd38e3f82ef596b7c23cdf528069207e35581c573e83e1613626c19aec; lemma-CTgen-v1.md 462d52aa1c6708a1071e06e0d88d0558b7f58e00c14bd42565655a123f92e5ad; addendum-credit-scope-delta-v1.md 273a871c71ab232ae788e15e53a6dbf72a40dbc585dd3a3e3d12566d9dee664b.
CANDIDATE, after the delta list: proof-LSplus-red-v1.md 166fbac828e7e55a8f2139648930c82c5df1e8823bf9d8c4f84daf36086b4c27; proof-LSplus-red-v1-addendum-1.md 6a79deb851f27d9e3d33c764559085894f5cbbeda40b957aef4030bb32341299.
Superseded/never sent: proof-LS-caseII-v1.md ceb27e1b373d02b058530b6c1c3cd515f3fe0b571fbaaf5ce8f09fdbb9e9c3fa.
Imports used anywhere: accepted S1-sharp, SLZ3, RED; the index-one record (n = p and n = 2p); Cauchy-Davenport.  Unreviewed lane texts
TV, MAX, RED+, SHIFT, STAB => LS+ are not imported (needed instances re-derived).

## 2. Exact target delta (p prime, kappa0 := floor(2p/3) < kappa <= p - 2, e := p - kappa)
- LS (weaker sufficient bound, |Y| >= p + 2kappa + 1 => no long zero-sum) [CANDIDATE]: every cell with e = 2 (p >= 7), e = 3 (p >= 11),
  e = 4 (p >= 13), and every cell with p >= 6e - 10.  Open in this lane: the band 5 <= e, p < 6e - 10, i.e. (p + 10)/6 < p - kappa <= (p - 1)/3.
- LS+ (|Y| <= 3kappa + 1) [CANDIDATE]: every cell with e = 2 (all p >= 7, sharp by E2/E3), and kappa = (2p + 1)/3 for p = 1 (mod 3).
  For e >= 3 and p >= 10e - 13, LS+ is reduced exactly to one configuration: a generator g with v_g >= 2p - 3e + 4 whose CF core is
  U' = (x_u (-1/2)) (mostly involutions), delta' + E' <= e - 1.  The two-heavy-value case and the a = -1 case are excluded.
- STAB [CANDIDATE]: holds at kappa = (2p + 1)/3, p = 1 (mod 3) (BASE1).  ACCEPTED: STAB extended to kappa = p - 1 is false for every
  prime p >= 7 (E5), p = 5 undecided; the E3 half of the XT three-term statement only for kappa >= kappa0 + 2.
- No counterexample to LS, LS+ or STAB in their stated range was found; none is claimed.
- The three-occurrence transversal TR remains unproved; the direct CT/CF route above replaces it for the covered cells.

## 3. Remaining obstruction (exact) and next distinct levers
(a) LS+ for p >= 10e - 13: case (alpha) with a = -1/2.  Lever: mirror of addendum-1 Steps 1-4 with the involution as unit (residue
    -tau/2 for integer x-sum tau) plus even deletion of involution pairs (a long zero-sum must contain >= 2p + 1 non-involution terms, so
    it omits at most E' - delta' - 1 <= e - 4 of them); the two possible long patterns are listed in addendum 1.
(b) LS / LS+ for e comparable to p/3 (the band above): index one on the zero-sum-free core and the integer no-wrap step fail there.
    Scout v3 [INFERENCE] names Gao-Li-Yuan-Zhuang 2015 Thm 3 (odd n >= 50) and the Chen-Savchev 'shorter long' theorem (n >= 10,
    manuscript status) as applicable in C_p coordinates; a BASE1-type equality analysis (S1-sharp/SLZ3 machinery) is the other lever
    near kappa0 + 1, including the uncovered base cell p = 2 (mod 3), kappa = (2p + 2)/3.
(c) STAB beyond BASE1 needs the equality analysis of (a)/(b) at length 3kappa + 1 (CT at n = kappa - 1 gives the analogous dichotomy).

## 4. Process deviations
- First checkpoint late (slice start ~03:55; checkpoint-001 after 04:45).
- lemma-CTgen-v1.md header cites the 06:00:33 clock read; a later read (06:05:49) preceded writing (checkpoint-006).
- proof-LSplus-red-v1-addendum-1.md Step 1 contains one garbled inequality chain, corrected in its own Editorial line (no statement
  change).
- proof-LS-caseII-v1.md was superseded by v2 before sending.
- No computation, probe, CLI review or native launch was run by this worker; only date/shasum shell calls.
