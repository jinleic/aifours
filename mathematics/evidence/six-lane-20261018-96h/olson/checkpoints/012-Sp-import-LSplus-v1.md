# Checkpoint 012: S(p) imported (Xia-Yuan); KPS v4 unconditional relative to it; LS reduced to a 2-cover-free residue; LS+

Owner ContinueOlson.  Written after /bin/date 2026-10-19T03:24:44-0700.  Continues checkpoint 011 (f95442d2...7e03).

## Actual result
- Import note evidence/import-Sp-XiaYuan-v1.md d4d515cd4ff7b848d703f9337a3e9b6f12f85bd99319173207014519961381d7: S(p) <=> IDX1-odd(p+1) as a classical corollary of
  Xia-Yuan 2010 Thm 3.1 (via Peng-Sun's restatement), the index-one theorem and Lemma SPLIT (proved); parity of both families
  at n = 2p checked; trust boundary recorded (primary text unread).
- evidence/proof-KPS-v4.md 68c4e7a7ff898219bfebee028052415cdb785b4b460b87e5cd4e7a6370510170: v3 made unconditional relative to the import (no mathematical step changed): Theorem
  ROT-KP+ (terminal k = p, kappa^ >= 1, (S1) at kappa^ => rotation rigidity) and Corollary INV*/ordered Olson for o_F <= p,
  kappa(w) <= floor(2p/3), p >= 7.
- evidence/disposition-S1sharp-ZengYuan-v1.md 439b80debaafb015721730c940de8d4cbf45d5d59db042507b6910d3bd176315: Steps 4/6/7 of S1-sharp routine given Zeng-Yuan 2011; rest not
  located (bounded); verdict and statement unchanged.
- evidence/notes-LS-propagation-v1.md be14d640f97f47e119f31d2e9b4bc5d7ef8c4f33129346e953435c6334c0de5d: EXT' (|V| >= p + kappa + t0), EXT-p [S(p)], PROP+ [S(p)], PAIR
  [S(p) + LS(kappa - 1)], and the sharper conjecture LS+ (|Y| <= 3kappa + 1 for (ZP)-and-not-(S1)) with its exact extremal
  family h^(3kappa-p+2) (3h)^(p-1); probe v12 maxima equal 3kappa + 1.

## Reduction recorded (written, not a claim)
LS+ for kappa <= p - 2 would give (S1) at kappa^ in every terminal cell with 2 <= k <= p - 1 (R = 2p + 2kappa^ - k >=
3kappa^ + 2 since kappa^ <= k - 1 and 2k <= 2p - 1) and with k = p, kappa^ <= p - 2 (R = p + 2kappa^); then ROT-FB (a) (k <= p - 1)
and ROT-FB (b) with KPS v4 (k = p) give rotation rigidity there.  LS (threshold p + 2kappa + 1) suffices for k <= p - 1 only.

## Exact blocker
LS residue (relative to S(p) and inductively LS(p, kappa - 1)): a length-(p + 2kappa + 1) (ZP_kappa) sequence in which no term
meets all long zero-sums and no two terms meet all 2kappa-zero-sums.  No argument yet uses the full length beyond these
covering properties.

## Next bounded action
Parent review packet: KPS v4 + import note + SLZ-EXT v2 (+ notes as context).  Lane: attempt LS+ in the two-atom case
(shortest long zero-sum of length >= 3kappa + 1 has two atoms), with S1-sharp's exchange inequality (MC) and FB.
