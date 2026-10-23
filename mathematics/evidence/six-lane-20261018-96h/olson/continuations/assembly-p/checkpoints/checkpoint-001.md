# Checkpoint 001 -- ASSEMBLY-P (Target 1) proof of record written; package and manifest next

Owner OlsonAssemblyP. Written after /bin/date 2026-10-19T11:42:56-0700. Active work 11:24:41 -> 11:42:56.
No computation, enumeration, solver, test, build or model CLI. Shell use: /bin/date, mkdir, shasum, wc, diff, chmod a-w on my
own frozen files, and one `cp -n` to start v2 as a new file. Nothing outside assembly-p/ was written.

## Frozen so far (all CANDIDATE_UNVERIFIED)
- Scope v1 (frozen 11:30:13, before derivation): ASSEMBLY-P-scope-v1.md
  5a4d9064b05e7dfbc9ac478ba3df95e89de00b573be379c3ce968ec848c2f64f.
- Scope addendum 1 (frozen 11:35:16, before deriving Corollary ASSEMBLY-P0): ASSEMBLY-P-scope-v1-addendum-1.md
  d75211261e4108eff5ec9ada3f702d8408fbf235b8b0ff6570a2106f5727a2d9.
- Proof of record: proof-ASSEMBLY-P-v2.md 059033b00b669e10f0fa49bdb2fdb55a135a85644f792ef2b3b3d6eb61dacfb5 (320 lines,
  37,385 B). Preserved never-sent draft: proof-ASSEMBLY-P-v1.md
  2f6e8468c060448b05b51bffc8a435cc8e04f224f1484652cacd905b33293b4d (v1 -> v2: LED row domain wording, EGZ attribution,
  S1-sharp probe record, o_F = F = p normal-form reason; no statement or step change).

## Actual result (candidate)
Theorem ASSEMBLY-P (conditional on pending ONE-SHORT-LS and ROT-SING): for prime p >= 7, (A) INV* for length-(4p-2) avoiders
with o_F <= p; (B) identity 2p-subword for length-(4p-1) words with o_F <= p. Route: k <= p-1 accepted ROT-LS; k = p:
kappa^ in {0,1} accepted ROT-KP item 1 (K01 does not cover k = p); 2..floor(2p/3) S1-sharp + ROT-KP+; floor(2p/3)+1..p-2
[ONE-SHORT-LS] at |Y| = p+2kappa^ + ROT-KP+; kappa^ = p-1 [ROT-SING]; restricted REFL (o_F <= p); ledger B = p; RGR-LONG.
Refinement (Proposition DEP): accepted LS+2 / LS+ linear band / BASE1+ replace ONE-SHORT-LS except on U(p); U(7) empty, so
p = 7 needs ROT-SING only and is Lev-free. Corollary ASSEMBLY-P0 (no pending premise): o_F <= p-1, or o_F = p with
kappa(w) not in U(p) u {p-1}. p = 5 not claimed.

## Exact blocker
None for Target 1.

## Next bounded action
Write review package and excerpt manifest (<= 100 KB total), verify every manifest entry, report to parent, then freeze the
Target 2 scope (terminal k = p+1, 0 <= kappa^ <= p-2) before any derivation.
