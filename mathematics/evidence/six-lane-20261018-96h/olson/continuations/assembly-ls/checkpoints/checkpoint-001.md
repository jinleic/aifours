# Checkpoint 001 -- ASSEMBLY-LS scope frozen; every load-bearing interface read at its original scope; no blocker found

Owner OlsonAssemblyLS. Written after /bin/date 2026-10-19T09:59:19-0700. Active work began 09:47:10 (first /bin/date).
No computation, enumeration, solver, test, build or model CLI. Python: none so far. Writes only in this directory.

## Actual result so far
- Frozen BEFORE derivation: ASSEMBLY-LS-scope-v1.md, sha256 53be77405c8b1369dfbde986a090350829a00cf2a83c3749fb7e87ff09c172a1 (09:53:20).
- Read in full: general-LS verdict (811e5807...), S1-sharp verdict (bd4a0a60...), FB verdict (8d6d4967...) with proof-FB-v1.md
  (339dcadc...) and erratum 1 (33de46d2...), KPS-SLZ verdict (23d1a488...), REFL-few-odd, K0*/RED, small-k, RUNS, ROT-KP,
  ZX/S1(c), SC0/ZX-SC, K01, lowodd v2, few-odd (+addendum), p5-lift, BAL-full/ROT-ZB, ROT-ZR, ZS v2 verdicts; source lines of
  the normal form (proof-ROT-few-E-v4.md L28-43), GRX, SHgen-v3 L20-37, DAV (proof-ROT-o3-v4.md L50-57), K1, ROT-K01,
  REFL-few-odd r4 L21-25, deletion ledger (proof-OLSON-few-v3.md L26-47), RGR class (RUNS assembly v4 L39-40, L72).
  Every pinned hash re-checked equal to its verdict pin.
- Interface findings (to be written as the proof): (i) every admissible normal form of a length-(4p-2) avoider with
  o_F <= p-1 has 1 <= k <= p-1; (ii) for k >= 2, 0 <= kappa^ <= k-1 <= p-2 (GRX, DAV) and |Y| = 2p+2kappa^-k >= p+2kappa^+1, so
  LS-ALL gives (S1_kappa^); (iii) k=1: K1; kappa^=0: ROT-K01; kappa^>=1: ROT-FB(a) (accepted for every 2<=k<=p-1, p>=7, no
  3k<=2p+1); (iv) restricted REFL (o_F<=p); (v) ledger Cases 1-3 preserve o_F<=p-1; RGR-LONG gives (B).
- p=5: (A)/(B) at o_F<=4 are exactly items 1-2 of the accepted p5-lift verdict (computer-assisted C5); ROT-FB is p>=7 only,
  so the LS route itself is not claimed at p=5.
- Trust: Lev-conditional only through G-LS cells floor(2p/3)+1 <= kappa^ <= p-3 (empty at p=7).

## Exact blocker
None found. All interfaces fit at their original scopes.

## Next bounded action
Write proof-ASSEMBLY-LS-v1.md with the interface table (paths, inclusive line ranges, sha256, verdict/item, original domain,
hypothesis discharge) and the residual description (o_F = p; o_F > p); then the review package and an excerpt manifest
(<= 100 KB of embedded text); report path+SHA256 to the parent.
