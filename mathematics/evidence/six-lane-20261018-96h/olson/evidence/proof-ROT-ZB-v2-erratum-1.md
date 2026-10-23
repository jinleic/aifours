# Erratum 1 to evidence/proof-ROT-ZB-v2.md (sha256 65dbedbf8f679b583a0186c84d64ede9c0564fc15ca8b13404c4766019f4f5f1)

Owner ContinueOlson.  Written after /bin/date 2026-10-19T01:15:05-0700.  Responds to the two hostile reviews launched by the parent:
run review/olson-rotzb-codex-v1.prompt.stdout.txt (sha256 960a6033a611abe50f0afd06b5de4bb2f2de194ac07c6fd007df4a38d36af7f2; ACCEPT on all four items, no findings) and
run review/olson-rotzb-claude-v1.prompt.note.md (sha256 6c1b7108365682e986eb3c6a9d60a6bae858803f44653f46a72d1b6114fc72f2; BAL1, ROOM, ROT-ZB ACCEPT; Corollary
ACCEPT-WITH-FIXES, 0 FATAL / 0 MAJOR / 6 MINOR).  The v2 text is not edited.  No statement of BAL1, ROOM, ROT-ZB or the
Corollary changes; m1 records a redundancy, m2/m3 replace comparison/residual wording (and withdraw the Sec. 6 cell
counts), m4/m5/m6 add citations and notation.

## m1 (redundant hypothesis; dead residual clause)
Every branch of (B) forces kappa^ <= (p - 1)/2 (B1: 4kappa^ <= 2p - 1; B2 with DAV: kappa^ <= min(k - 1, p - k);
Lambda1: 8kappa^ <= 4p - 1; Lambda2: kappa^(2kappa^ - 1) < p), so with k <= p - 1 the hypothesis 2kappa^ + k <= 2p - 1 of
Theorem ROT-ZB is automatic (2kappa^ + k <= 2p - 2).  It is kept as an explicit, redundant hypothesis.  Plain S1+ (the
accepted S1(a)) suffices for (S1); the (S') generality is correct but not load-bearing for ROT-ZB.  For 2 <= k <= p - 1
(Lambda) is contained in B1 (Lambda1's bound is B1's plus 3 - k, equal by parity at k = 2; Lambda2 with B1 failing would need
(2kappa^ - 3)(kappa^ - 1) < 0), and B2 is contained in B1 once 3k >= 2p - 1; so in the new range (B) is just B1.  The
clause '2kappa^ + k > 2p - 1' in Sec. 7's residual describes no cells and is deleted.

## m2 (residual; unrecorded T3/T4)
'T3/T4' (Sec. 6 bullet 2, Sec. 7) were unrecorded planning functions of the worker's kernel, not accepted results; NO cells
are subtracted for them.  The Sec. 6 cell counts (p = 31: 28 of 202; p = 61: 129 of 803; p = 101: 386 of 2255) depend on
them and are WITHDRAWN (they were never premises; the same counts quoted in checkpoint 005 and in the parent notice are
withdrawn with them).  Corrected residual statement after ROT-ZB (rotation half, relative to the cited accepted results):
- terminal k = p with kappa^ >= 2; OR
- (2p + 1)/3 < k <= p - 1 with kappa^ >= 2 and 4kappa^ >= 2p - k + 2 (B1 failing),
only.  (k = 1 is K1; 3k <= 2p + 1 is the ZX terminal criterion with S1-sharp; kappa^ <= 1 is K01.)

## m3 (uniform comparison)
Sec. 6 bullet 1 is replaced by: for (2p + 1)/3 < o_F <= p - 1 the accepted uniform bands were F - o_F >= 2p - 6 (p >= 7) and
F - o_F >= 2p - 8 (p >= 17); the new band 2F >= 2p + 3o_F - 5 contains both (the first because o_F <= 2p - 7, the second
because o_F <= 2p - 11, true for o_F <= p - 1 once p >= 10).  For 3o_F <= 2p + 1 the accepted S1-sharp coverage already
holds for every F, so no comparison is made there.

## m4 (terminal chain for 3k <= 2p + 1)
Sec. 5(a) bullet 2 is replaced by: '3k <= 2p + 1 and k >= 2: DAV gives kappa^ <= k - 1, so 3kappa^ <= 2p - 2 and
kappa^ <= floor(2p/3); GRX gives (ZP) at kappa^ for the rotation sequence of w^; Lemma S1-sharp gives (S1); the ZX
terminal criterion (as applied in the S1-sharp parent verdict) finishes.'  This holds even when o_F > (2p + 1)/3.

## m5 (source of k >= 1)
Sec. 5(a)'s 'every admissible normal form has 1 <= k <= o' is cited to the accepted normal form (proof-ROT-few-E-v4.md
Sec. 0; ROT-ZR verdict m4: F, R >= 1, odd terminal blocks, kappa^ >= 0): F = 0 is excluded by the rotations-only EGZ bound
(here F >= 5 anyway, from 2F >= 2p + 3o - 5 >= 2p - 5 >= 9), and the terminal form is either 1 <= k <= o odd blocks or one
even block, the latter impossible by K1/Davenport; hence k >= 1.

## m6 (citations and notation)
- Sec. 4 line 1: cite ZX overlay 1 (the integer-domain condition S1+ needs) AND ZX overlay 2 (existential reading of the
  normal form).
- Sec. 4 SHgen-E caller, replaced by the ROT-ZR verdict's discharge: 'Empty runs use SHgen-E: expansions preserve k and
  odd blocks; base words have length 4p - 2, one nonzero pair, and o_F(u°) <= k <= p - 1, so restricted REFL and the accepted
  V3 caller apply.  The normal form preserves rotation letters.'
- Sec. 1: the item 'the ZX terminal criterion (with S1-sharp)' is cited to the S1-sharp parent verdict (run
  review/olson-s1sharp-parent-verdict-v1.md bd4a0a60...4f41), not to 'exactly as used by ROT-ZR's verdict'.
- Sec. 2: the prefix sums P_i are renamed T_i (T_0 = 0, T_i = s_1 + ... + s_i); P_0 denotes only the complement P - P_c.
- Sec. 2: the fill of [0, W] is REALIZE's proof, bullet 2 (the statement gives [2, W]; 0 is empty and 1 is a unit, m >= 3).
