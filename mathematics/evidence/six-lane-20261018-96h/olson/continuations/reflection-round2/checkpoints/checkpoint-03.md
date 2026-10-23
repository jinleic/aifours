# Reflection round 2 (Slice B), checkpoint 03

Written after host clock 2026-10-19T05:45:04-0700.  Written research only; no computation, no model CLI.

## Candidates sent to parent (all CANDIDATE_UNVERIFIED)

| file | sha256 | content |
|---|---|---|
| proof-REFLHI-arcs-v3.md | 2889509abcd5d2b857e95ca9db2cd32a1acae6a196347d4aceb84a9519512f8f | Lemma ARC, Theorem FP, Cor FP-1 (R = p, any B), ETA |
| proof-REFLHI-arcs-v3-erratum-1.md | 1fba1b3353e94f5b06d1085ad1363955de4ce8eaa0a33c46f01ce47e89d45ee3 | scope sentence |
| proof-REFLHI-arcs-v4.md | 7683eb17905ab0c9d21046f4e4a0de2fc7e868a9c394e1c874308bf4a2a77f0e | + Lemma BAL, Theorem K2P (k >= 2p+3, k >= 3 kappa+3) |
| proof-REFLHI-arcs-v4-addendum-K2Pplus-v1.md | 7f5b3dc598fc6e346adc1c129e228074eb4c0ca51a884c559312d50e165a383f | K2P+ (k >= 2p+1), Cor IIIb-X |

Unsent drafts kept unchanged: proof-REFLHI-tools-v1.md (79741c7c...7a6e), proof-REFLHI-arcs-v2.md (667e4373...f4ed).

## Scientific state

- REFL-HI(p) / RES-HI(p): OPEN.  New exclusions (candidate): all-odd words with rotations in one pair and
  k >= max(2p + 1, 3 kappa + 3), any B; R = p words under (K) and a value-diversity bound; the extreme IIIb family for p >= 7.
- Remaining: p + 1 <= k <= 2p (every B) outside FP-1 and the accepted B = 0 ranges; k >= 2p + 1 with H - delta <= 1.

## Next obligations (written)

1. Lower the threshold below 2p + 1: count value diversity (arcs with nu >= 3) and loss-free balancing.
2. Small H - delta (kappa near p - 1 or large runs): handle giant runs separately (single run with r >= 2H).
3. Middle-regime eta-arcs (arcs spanning nonempty runs, ETA-type windows) as a second supply of Cauchy-Davenport terms.
