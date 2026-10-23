# Checkpoint 004: S1-sharp accepted; Q1b word-level route via balance

Owner ContinueOlson.  Written after /bin/date 2026-10-19T00:38:55-0700.  Continues checkpoint 003 (5749e3b2...44ec).

## Actual result
- Parent verdict (run review/olson-s1sharp-parent-verdict-v1.md, sha256 bd4a0a60cdea0765517ca33a9a2ddefb664b24fad7b20e709835bbdec1e94f41):
  Lemma S1-sharp and the uniform INV*/ordered-Olson corollary under 3 o_F <= 2p+1 CORRECTNESS-ACCEPTED SCOPED PARTIAL,
  read through erratum 1 (evidence/proof-S1-sharp-v1-erratum-1.md bf504cdf...f9507) and the parent overlay.
- Observation for Q1b (lane derivation, unreviewed): in the accepted ROT-ZR setting, ZX's Step F ('room' argument via the
  exchange with U = T) gives, whenever the longest zero-sum Z is balanced (sum s_i = n+) and 2kappa + k <= 2p,
  W <= 2p - 1 - n+, hence E <= k - 1 - 2kappa + 2t - n- <= k - 1 (instead of EBOUND's k - 1 + G(kappa)).  Then SHgen's (H)
  holds when 2kappa^ + k <= 2p - 1 and (K) holds for every k <= p - 1 (KETA).  The only missing input outside LAMBDA's
  range is BALANCE.  If balance held for every k <= p-1 with 2kappa^ + k <= 2p-1, the rotation residual would lose
  roughly half of its terminal cells (planning arithmetic: p = 31: 103 of 202 cells; p = 61: 454 of 803).
- Aid: probe v5 (receipt evidence/probe-v5/RECEIPT-run1-v1.md) found no unbalanced longest zero-sum in any completed item
  beyond LAMBDA's range (support <= 3; p = 13, 17, 19 partly).

## Exact blocker
A proof of balance (sum s_i = n+) for k <= p-1, kappa <= floor(2p/3), 2kappa + k <= 2p-1 without LAMBDA's hypotheses.
Known partial facts (written): sub-multisets N_0 of the negatives with sum in [2p - m, W] are forbidden when
2t + e' < 2p; unbalance forces m + n+ <= 4t - 3 and L <= 4t - 3.

## Next bounded action
Written attempt at Lemma BAL (balance) and, if it closes, a frozen candidate 'ROT-ZR+' terminal criterion with uniform
corollary; otherwise a precise statement of the remaining balance obstruction.
