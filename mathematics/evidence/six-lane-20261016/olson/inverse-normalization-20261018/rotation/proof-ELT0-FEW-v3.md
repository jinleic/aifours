# Corollary ELT0-FEW: the kappa = 0 slice of ROT for 3o <= 2p + 1 (conditional on SHgen), v3

Owner OlsonRotationRigidity.  Written after host clock 2026-10-18T06:37:56-07:00.  v3 written after host clock
2026-10-18T08:12:29-07:00: REPAIR of v2 (sha256 d4ee70819a9000264b13168966747e52b66ff323181c668582cfd7c98912246a) for the Claude engine review
R/olson-rotation-engine-claude-v1.note.md (v2 ACCEPT-WITH-FIXES, MAJOR M1: the final step imported Corollary ELT0-ROT
of proof-ELT0-v3.md, which is unreviewed and not accepted).  v3 replaces that step by the reviewer's audited route (b)
through Theorem SHgen and is therefore CONDITIONAL on SHgen; shared MINOR 11 applied; fix map at the end.  v3 itself
unreviewed.
v2 supersedes proof-ELT0-FEW-v1.md (kept unchanged): v1's range remark said "o <= 3 at p = 5, 7"; at p = 7 the
condition 3o <= 2p + 1 = 15 gives o <= 5.  No other change.
Imports: Lemma PM*, GRX (accepted, lowodd verdict v2); Lemma MULT (i), (ii), (iii) of proof-ROT-few-v3.md (with Lemma
SCHERK, GROW, Corollary SET there, all proved in that file; Codex round-B and Claude engine ACCEPT); Theorem SHgen with
its setting and weights (proof-SHgen-v2.md 8fde88c0...d239; Codex round-B and Claude engine ACCEPT), which itself
imports K1, B'(b), C1, KBH, the uncapped KB and (V).  Corollary ELT0-ROT and proof-ELT0-v3.md are no longer used.

## Statement

**Corollary ELT0-FEW.**  Let p >= 5 be prime and w an avoider of length 4p-2 over D_(2p) whose maximal cyclic
reflection runs are all constant, k >= 1 of them of odd length, with 3k <= 2p + 1, and with kappa = 0, i.e.
H := (F - k)/2 = p - 1.  Then all rotation letters of w are equal to one rho_c, c != 0.

## Proof

If R = 0 there is nothing to prove.  Iterated Lemma PM* (k >= 1 odd block) gives an avoider w^ of length 4p-2 with the
same rotation multiset, all k blocks odd, runs nonempty and blocks maximal, and the same F and H (each merge
R_i S_i R_(i+1) S_(i+1) -> R_i R_(i+1) sigma_(y_(i+1))^(l_i + l_(i+1)), l_i even, keeps the length, F, the odd-block count
and H, as floor((l_i + l_(i+1))/2) = l_i/2 + floor(l_(i+1)/2), and merged runs stay nonempty), so kappa = 0 and
R = 2p - k.  The all-plus pattern of GRX (Phi = 0, C_max = 2H = 2p - 2) forbids every zero-sum of even length in
[2, 2p] among Y(x) over the rotations: the sequence Y of length L = R = 2p - k is zero-sum-free in Z_(2p), with
e := 2p - 1 - L = k - 1.
Case k = 1: e = 0, so Lemma MULT (i) gives m >= 2p - 1 - 2e = 2p - 1 = L for the largest multiplicity m: Y = g^(2p-1)
for one odd g, a generator ((1,0) twice would be a zero-sum); every rotation is one rho_c, c != 0.
Case k >= 2: as 3e + 2 = 3k - 1 <= 2p, Lemma MULT (iii), (ii) gives a generator g = (1, c), c != 0, with
Y = g^m (d_1 g) ... (d_q g), d_j odd >= 3 and sum_j (d_j - 1) <= e = k - 1, so d_j <= k.  3k <= 2p + 1 gives k <= 3 = p - 2
at p = 5 and k <= (2p+1)/3 <= p - 2 for p >= 7.  Relative to c (SHgen-v2 Sec. 0) the lights are rho_c and rho_-c, and
d_j g = (1, d_j c) is a heavy of SHgen weight d_j, an odd integer in [3, p-2]; none is rho_0 (that would need d_j = p > k)
and rho_-c does not occur (g (-g) would be a zero-sum).  Hence eta = q, E = sum_j (d_j - 1) <= k - 1, eta <= (k-1)/2
and a_max <= k.  w^ is in the form of SHgen-v2 Sec. 0 (k >= 2 odd blocks, nonempty runs, F, R >= 1).
(H): 2H = 2p - 2 >= k - 1 >= E.  (K): 2p - eta - a_max - 1 >= 2p - (k-1)/2 - k - 1 >= k, i.e. 4p >= 5k + 1, which
follows from 3k <= 2p + 1 and p >= 4.  If eta >= 1, Theorem SHgen gives w^ an identity 2p-subword, contradicting PM*;
so eta = 0, Y = g^(2p-k), and every rotation of w^, hence of w, is rho_c.  []

## Scope and remarks

* With kappa = 0 the conclusion is stronger than ROT: all rotations are equal (B = 0), as in the accepted rigid
  normal form.
* Range: every o with 3o <= 2p + 1 (o <= 3 at p = 5; o <= 5 at p = 7; o <= 7 at p = 11; o <= 9 at p = 13; o <= 11 at p = 17), only
  for kappa = 0.  ROT-FEW (proof-ROT-few-v3.md) covers every kappa but only 5o <= 2p + 4; both are conditional on SHgen.
* CONDITIONAL REMARK (no import): if the Savchev-Chen structure (Y = g^m times heavies d_j g with sum (d_j - 1) <= e)
  were supplied for zero-sum-free odd sequences of length >= p in Z_(2p), the same proof would give the kappa = 0 slice
  for every o with 5o <= 4p - 1 (SHgen's (K) is then the binding condition); the v2 remark 'every o < p' relied on the
  withdrawn ELT0 route.
* Observation [O] (existing data, not a premise): among the normalised avoiders listed in out/bases_p5_N18.txt (3,730)
  and out/bases_p7_N26.txt (3,738), all have constant runs, o <= p, and kappa in {0, o - 1}; kappa = 0 occurs for every
  o from 1 to p.
* Not ROT(p), INV*(p) or ordered Olson; no novelty claim.

## Errata diff and fix map (proof-ELT0-FEW-v2.md -> proof-ELT0-FEW-v3.md)

Fix map (Claude engine review R/olson-rotation-engine-claude-v1.note.md):
MAJOR M1 (SOURCE02:6-9, 25-27: final step rests on the unaccepted Corollary ELT0-ROT) -> repair (b) as audited by the
reviewer: header (now CONDITIONAL on SHgen), title, imports, and the proof from 'Case k = 1' on.  The (FULL)/ELT0-ROT
sentences are removed.  Consequential: Scope bullet 'Range' (both results conditional on SHgen) and the CONDITIONAL
REMARK (the Savchev-Chen extension now reaches 5o <= 4p - 1, not o < p, since SHgen's (K) binds).
Shared MINOR 11 (PM* preserves length, F, H and odd-block count; merged runs nonempty) -> first proof sentence.
The statement (hypotheses and conclusion) is unchanged except that it is now conditional on SHgen.
Generated by unique string replacement from proof-ELT0-FEW-v2.md (sha256 d4ee70819a9000264b13168966747e52b66ff323181c668582cfd7c98912246a); body diff:

```diff
--- proof-ELT0-FEW-v2.md
+++ proof-ELT0-FEW-v3.md (body)
@@ -1,12 +1,17 @@
-# Corollary ELT0-FEW: the kappa = 0 slice of ROT for 3o <= 2p + 1 (no SHgen), v2
+# Corollary ELT0-FEW: the kappa = 0 slice of ROT for 3o <= 2p + 1 (conditional on SHgen), v3
 
-Owner OlsonRotationRigidity.  Written after host clock 2026-10-18T06:37:56-07:00.  Status [W], UNREVIEWED.
+Owner OlsonRotationRigidity.  Written after host clock 2026-10-18T06:37:56-07:00.  v3 written after host clock
+2026-10-18T08:12:29-07:00: REPAIR of v2 (sha256 d4ee70819a9000264b13168966747e52b66ff323181c668582cfd7c98912246a) for the Claude engine review
+R/olson-rotation-engine-claude-v1.note.md (v2 ACCEPT-WITH-FIXES, MAJOR M1: the final step imported Corollary ELT0-ROT
+of proof-ELT0-v3.md, which is unreviewed and not accepted).  v3 replaces that step by the reviewer's audited route (b)
+through Theorem SHgen and is therefore CONDITIONAL on SHgen; shared MINOR 11 applied; fix map at the end.  v3 itself
+unreviewed.
 v2 supersedes proof-ELT0-FEW-v1.md (kept unchanged): v1's range remark said "o <= 3 at p = 5, 7"; at p = 7 the
 condition 3o <= 2p + 1 = 15 gives o <= 5.  No other change.
-Imports: Lemma PM*, GRX (accepted, lowodd verdict v2); Corollary ELT0-ROT of proof-ELT0-v3.md (errata version of
-ELT0-v2, which Codex reviewed ACCEPT-WITH-FIXES in R/olson-rotation-bundle1-codex-v1.note.md; v3 applies those fixes);
-Lemma MULT (ii), (iii) of proof-ROT-few-v3.md (with Lemma SCHERK, GROW, Corollary SET there; all proved in that file).
-Does NOT use Theorem SHgen, KB, KBH, B'(b) or C1.
+Imports: Lemma PM*, GRX (accepted, lowodd verdict v2); Lemma MULT (i), (ii), (iii) of proof-ROT-few-v3.md (with Lemma
+SCHERK, GROW, Corollary SET there, all proved in that file; Codex round-B and Claude engine ACCEPT); Theorem SHgen with
+its setting and weights (proof-SHgen-v2.md 8fde88c0...d239; Codex round-B and Claude engine ACCEPT), which itself
+imports K1, B'(b), C1, KBH, the uncapped KB and (V).  Corollary ELT0-ROT and proof-ELT0-v3.md are no longer used.
 
 ## Statement
 
@@ -17,24 +22,34 @@
 ## Proof
 
 If R = 0 there is nothing to prove.  Iterated Lemma PM* (k >= 1 odd block) gives an avoider w^ of length 4p-2 with the
-same rotation multiset, all k blocks odd, runs nonempty and blocks maximal, and the same H, so kappa = 0 and
+same rotation multiset, all k blocks odd, runs nonempty and blocks maximal, and the same F and H (each merge
+R_i S_i R_(i+1) S_(i+1) -> R_i R_(i+1) sigma_(y_(i+1))^(l_i + l_(i+1)), l_i even, keeps the length, F, the odd-block count
+and H, as floor((l_i + l_(i+1))/2) = l_i/2 + floor(l_(i+1)/2), and merged runs stay nonempty), so kappa = 0 and
 R = 2p - k.  The all-plus pattern of GRX (Phi = 0, C_max = 2H = 2p - 2) forbids every zero-sum of even length in
 [2, 2p] among Y(x) over the rotations: the sequence Y of length L = R = 2p - k is zero-sum-free in Z_(2p), with
-e := 2p - 1 - L = k - 1.  As 3e + 2 = 3k - 1 <= 2p, Lemma MULT (iii), (ii) of proof-ROT-few-v3.md gives a generator
-g = (1, c), c != 0, with Y = g^m (d_1 g) ... (d_q g), d_j odd >= 3, sum_j (d_j - 1) <= e and m >= e + 1.  In the
-notation of ELT0 (weights a_x with (1, x) = a_x g) the weights are m ones and d_1, ..., d_q; listed in increasing order
-each weight is at most 1 plus the sum of the smaller ones (d_j <= e + 1 <= m + 1), so (FULL) holds (ELT0-v3 Sec. 3).
-Corollary ELT0-ROT (N = 4p-2, kappa = 0, (FULL), w^ avoids, all-odd RGR-shape form) gives E = 0: every rotation of w^,
-hence of w, is rho_c.  []
+e := 2p - 1 - L = k - 1.
+Case k = 1: e = 0, so Lemma MULT (i) gives m >= 2p - 1 - 2e = 2p - 1 = L for the largest multiplicity m: Y = g^(2p-1)
+for one odd g, a generator ((1,0) twice would be a zero-sum); every rotation is one rho_c, c != 0.
+Case k >= 2: as 3e + 2 = 3k - 1 <= 2p, Lemma MULT (iii), (ii) gives a generator g = (1, c), c != 0, with
+Y = g^m (d_1 g) ... (d_q g), d_j odd >= 3 and sum_j (d_j - 1) <= e = k - 1, so d_j <= k.  3k <= 2p + 1 gives k <= 3 = p - 2
+at p = 5 and k <= (2p+1)/3 <= p - 2 for p >= 7.  Relative to c (SHgen-v2 Sec. 0) the lights are rho_c and rho_-c, and
+d_j g = (1, d_j c) is a heavy of SHgen weight d_j, an odd integer in [3, p-2]; none is rho_0 (that would need d_j = p > k)
+and rho_-c does not occur (g (-g) would be a zero-sum).  Hence eta = q, E = sum_j (d_j - 1) <= k - 1, eta <= (k-1)/2
+and a_max <= k.  w^ is in the form of SHgen-v2 Sec. 0 (k >= 2 odd blocks, nonempty runs, F, R >= 1).
+(H): 2H = 2p - 2 >= k - 1 >= E.  (K): 2p - eta - a_max - 1 >= 2p - (k-1)/2 - k - 1 >= k, i.e. 4p >= 5k + 1, which
+follows from 3k <= 2p + 1 and p >= 4.  If eta >= 1, Theorem SHgen gives w^ an identity 2p-subword, contradicting PM*;
+so eta = 0, Y = g^(2p-k), and every rotation of w^, hence of w, is rho_c.  []
 
 ## Scope and remarks
 
 * With kappa = 0 the conclusion is stronger than ROT: all rotations are equal (B = 0), as in the accepted rigid
   normal form.
 * Range: every o with 3o <= 2p + 1 (o <= 3 at p = 5; o <= 5 at p = 7; o <= 7 at p = 11; o <= 9 at p = 13; o <= 11 at p = 17), only
-  for kappa = 0.  ROT-FEW (proof-ROT-few-v3.md, conditional on SHgen) covers every kappa but only 5o <= 2p + 4.
-* CONDITIONAL REMARK (no import): if the Savchev-Chen structure theorem for zero-sum-free sequences of length > p in
-  Z_(2p) were supplied with its exact statement, the same proof would give the kappa = 0 slice for every o < p.
+  for kappa = 0.  ROT-FEW (proof-ROT-few-v3.md) covers every kappa but only 5o <= 2p + 4; both are conditional on SHgen.
+* CONDITIONAL REMARK (no import): if the Savchev-Chen structure (Y = g^m times heavies d_j g with sum (d_j - 1) <= e)
+  were supplied for zero-sum-free odd sequences of length >= p in Z_(2p), the same proof would give the kappa = 0 slice
+  for every o with 5o <= 4p - 1 (SHgen's (K) is then the binding condition); the v2 remark 'every o < p' relied on the
+  withdrawn ELT0 route.
 * Observation [O] (existing data, not a premise): among the normalised avoiders listed in out/bases_p5_N18.txt (3,730)
   and out/bases_p7_N26.txt (3,738), all have constant runs, o <= p, and kappa in {0, o - 1}; kappa = 0 occurs for every
   o from 1 to p.
```
