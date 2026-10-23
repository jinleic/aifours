# Checkpoint 014: LS+ scope frozen; partials (TV, RED+, SHIFT, MAX); LS+ reduced to STAB at length 3kappa + 1

Owner ContinueOlson.  Written after /bin/date 2026-10-19T03:44:31-0700.  Continues checkpoint 013 (16fd235de3b857d07a3da71f8ecd714af988fa7bcd5bed1292ce02dabe173bba).

## Actual result since 013
- Scope: evidence/LSplus-scope-v1.md 7dc04949c1152907eef9938c4680248eeb24d5830ab751f67f1355ba6e0e2cbc (frozen before any proof text).
- CANDIDATE partials (unreviewed): evidence/proof-LSplus-partials-v2.md eedfa0f16572f1636bfa4f387e3a1566b87864ae4ced6fddcf063cddaedcb6b2:
  Lemma TV (unconditional): h^a (3h)^b with (ZP_kappa) and not (S1_kappa) has a + b <= 3kappa + 1, equality exactly at
  E2 = h^(3kappa-p+2) (3h)^(p-1) and E3 = h^(3kappa-2p+2) (3h)^(2p-1);
  Lemma RED+ (cut to length 3kappa + 2; under H(kappa) a 2kappa-zero-sum in every long-containing subsequence of length
  >= 3kappa - 1); Lemma SHIFT (a zero-sum of length z <= 2(p - kappa) disjoint from a long zero-sum forces
  |Y| <= 3kappa + 1 - z/2 under LS+(kappa - z/2)); corollaries incl. the LS version.
- CANDIDATE addendum: evidence/proof-LSplus-partials-v2-addendum-MAX-v2.md 4b0be3e304199cc61180e2b5bdad7eb63acb8b2c6e5ada6e95cfb0e099a451c7: Lemma MAX (E2 y, E3 y violate
  (ZP_kappa) for every odd y) and Proposition STAB => LS+ (STAB: every (ZP_kappa), not-(S1_kappa) sequence of length
  3kappa + 1 is E2 or E3); v12's complete cells agree with STAB (aid).  Side remark: SLZ3's steps give
  N <= max(3kappa, 2p + 2).

## Exact blocker
STAB (an inverse theorem at length 3kappa + 1).  Neither the induction on kappa (removing three terms that meet every
2kappa-zero-sum while keeping a long zero-sum is not guaranteed in general) nor SHIFT (E2/E3-like sequences have no short
zero-sums) closes it; the C_p/EGZ route (two disjoint odd-size subsequences with x-sum 0 and total size in the window) needs a
size-flexible EGZ statement not available here.

## Pending with the parent
Claude review of KPS v4 / import / SLZ-EXT (then ONE combined erratum: Codex M1-M3 + import n-range update); both reviews of
SLZ3; reviews of the LS+ partials when the parent decides.

## Next bounded action
STAB: attempt the induction 'STAB(kappa - 1) => STAB(kappa)' through three-term removals in the two-atom case, or a
level-analysis generalisation of Lemma TV to sequences with all but O(1) terms in {h, 3h}.
