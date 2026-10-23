# Checkpoint 002 -- ASSEMBLY-LS written assembly, review package and excerpt manifest frozen; no blocker; parking

Owner OlsonAssemblyLS. Written after /bin/date 2026-10-19T10:12:11-0700. Active work 09:47:10 -> 10:12:11.
No computation, enumeration, solver, test, build or model CLI. Python was used ONLY for byte/hash/line-range metadata of this
packet (range sizes, whole-file SHA256, JSON manifest written with exclusive create mode 'x', manifest round-trip/hash check)
and for removing write permission from my own frozen files. Every file here was created new; nothing outside this directory
was written.

## Frozen deliverables (all CANDIDATE_UNVERIFIED)
- Scope (frozen 09:53:20, before derivation): ASSEMBLY-LS-scope-v1.md
  53be77405c8b1369dfbde986a090350829a00cf2a83c3749fb7e87ff09c172a1.
- Proof of record: proof-ASSEMBLY-LS-v2.md ac854c31ae1446c4710f3c19bb1beb80d8c25333aeb6b350c7f7d4dc7fafcfb3 (263 lines,
  30,115 B), with the interface table (Sec. 2), proofs of ROT-LS/(A)/(B) (Secs. 3-5), route answers (Sec. 6) and residual
  description (Sec. 7).
- Preserved superseded draft, never sent: proof-ASSEMBLY-LS-v1.md b308e20d5c9ddc42dbfd94636461acb67e171e6aee74e2ea663eaf2f5aa8ff2d.
  Exact v1 -> v2 diff: title/header provenance, and row FB's BAL-full overlay-5 citation line 31 -> 33 (my own line audit).
- Review package: review-package-ASSEMBLY-LS-v1.md fd710d3ec509a65a2b6f18d689d3744c8dde8f7009f5a09a0987812e08296295 (6,753 B).
- Governing excerpt manifest: review-excerpts-ASSEMBLY-LS-v1.json
  b5158d37abc8c59dedd452c3bc93a63d631b7d18ef213959d58946242198c09d (12,536 B): 55 ranges, 34 files, 77,462 selected B;
  every entry re-verified (whole-file SHA256, inclusive in-bounds range). Package + manifest + selected = 96,751 B.

## Candidate result and trust boundary
Theorem ASSEMBLY-LS: for prime p >= 7, (A) every length-(4p-2) avoider over D_(2p) with o_F <= p-1 satisfies INV*;
(B) every length-(4p-1) word with o_F <= p-1 has an increasing-index identity 2p-subword. Intermediate Proposition ROT-LS:
some admissible normal form with terminal 1 <= k <= p-1 gives rotation rigidity (no o_F hypothesis). Route: K1 (k = 1);
GRX + DAV give 0 <= kappa^ <= k-1 <= p-2 and (ZP); |Y| = 2p+2kappa^-k >= p+2kappa^+1 so LS-ALL gives (S1); ROT-K01 (kappa^ = 0);
ROT-FB(a) (kappa^ >= 1; no 3k <= 2p+1 needed, ZX criterion unused); restricted REFL (o_F <= p); ledger (B = p-1) + RGR-LONG.
Lev 2022 Theorem 2 (statement level) enters only through G-LS cells floor(2p/3)+1 <= kappa^ <= p-3 (p >= 11); p = 7 is Lev-free.
p = 5 only as a citation union with the accepted p5-lift verdict (computer-assisted C5). Nothing claimed at o_F >= p.

## Exact blocker
None for the frozen target. Residual (not a claim): o_F = p cells where every admissible normal form has k = p,
kappa(w) >= floor(2p/3)+1 and (S1) fails at the one-short length p+2kappa(w) (smallest missing lemma: one-short LS; the
sequence version fails at kappa = p-1 by the ZS v2 V6 sequence); o_F > p needs REFL beyond o_F <= p (RES_<(p), k >= p+1) and
terminal k >= p+1 rotation input.

## Next bounded action
Report paths and hashes to the parent; park pending parent-frozen reviews. No further science in this slice without a new
parent instruction.
