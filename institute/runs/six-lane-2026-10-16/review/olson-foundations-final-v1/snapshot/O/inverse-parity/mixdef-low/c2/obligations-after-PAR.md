# Obligation map after PAR (assuming Theorems M and P are accepted)

Owner OlsonParity2.  Written after host clock 2026-10-17T18:29:57-07:00 (freeze time in out/freeze.txt).  A map [W/I];
the only new statement is Corollary RL (Sec. 3, [W], unreviewed, a citation proof).  Assumption throughout: Theorem M and
Theorem P of c2/proof-R4-closure.md (sha256 74929e9c...33f6) are accepted; their hostile reviews (olson-par2-closure-*)
were commissioned by the parent at 18:2x and are not yet returned.  Ownership confirmed with OlsonRunCount5 by IRC
(18:2x): it owns RUNS item (iii) only (mixdef-high/c6/); nobody owns INV*.

## 1. Top-level chain

Target (frozen, olson/README.md Sec. 1, G = D_{2p}, p prime): every word of length 4p-1 over D_{2p} has an identity
2p-subword in increasing index order.
* p = 3: S3 = D6, exhaustive over all words of length 11 (olson/README.md Sec. 5.1) [F].
* p >= 5: Corollary DR' (../../../proof-DR.md, reviewed: Claude max, correct) with Theorem DR replaced by Theorem DR-Res
  (../../../proof-INV-reduction.md Sec. 1, reviewed: Claude max, correct with minor fixes):
      INV*(p) + INV_Res(p)  =>  ordered Olson for D_{2p}.
  [The substitution is valid: the proof of DR' uses INV(p) only through the conclusion of Theorem DR, "every word in
  RGR_{4p-1}(p) has an identity 2p-subword", which is exactly the conclusion of Theorem DR-Res under INV_Res(p).]
  INV_Res(p) = PAR(p) + RUNS(p) for inherited avoiders (proof-INV-reduction.md Sec. 2).
So, for p >= 5:  ordered Olson for D_{2p}  <=  INV*(p) + PAR(p) + RUNS(p).  Not needed: INV(p) in its non-inherited
form, the conjectured exact shape INV+(p) (repr-WAS.md Sec. 4.2-4.3).

## 2. Obligation table

| # | obligation | status | owner / file |
|---|---|---|---|
| O1 | PAR(p), all primes p >= 5 | Theorem P [W]; reviews running (olson-par2-closure-*); chain and imports: c2/proof-PAR-assembly-r1.md Sec. 2, 4 | OlsonParity2: c2/proof-R4-closure.md, c2/proof-Rstar-r3.md |
| O2a | RUNS(p) for B = 0 (all k, all parities) and for kappa = 0 | [W]; the RUNS -> MIX_DEF reduction was reviewed (review/olson-kbh-codex-review-v1: ACCEPT-WITH-FIXES, covers proof-RUNS.md) | OlsonRunCount: inverse-run-count/proof-RUNS.md Sec. 11 |
| O2b | RUNS(p) for B >= 1 and o_F <= p | Corollary RL (Sec. 3) [W, unreviewed] from Lemma OR, Theorem M, Theorem KB | OlsonParity2: this file |
| O2c | RUNS(p) for B = kappa >= 1, o_F >= p + 1 | Theorem KBH [W], Codex ACCEPT-WITH-FIXES (review/olson-kbh-codex-review-v1) | OlsonRunCount: inverse-run-count/kappaB-high/proof-KBH.md |
| O2d | RUNS(p) for 1 <= B < kappa, o_F >= p + 1 (MIX_DEF_HIGH(p) <= NMH(p), proof-MH.md Sec. 1) | R >= 2p - 2: c2/proof-C2.md (Codex ACCEPT); k = 2p - 1: Theorem ALT (proof-RUNS.md Sec. 2); k = p + 1, kB = 1 with (4.1): Lemma ZSI-B (proof-MH.md, [W]; I located no review note for proof-MH.md); item (iii) (R <= 2p - 3): W-ALL, SEED, SEED-B, SEED-G, SEED-G*, IND*, C, C+ (mixdef-high/c3-c6, reviews per c6/README.md); OPEN residual = all-single-letter classes with B >= 4 and 2B + kB >= p - 1 outside SA/PA, and excess-word classes failing the count condition of Theorem C+ or the seed part (exact map: mixdef-high/c6/README.md Secs. 11, 15-18) | OlsonRunCount5: inverse-run-count/mixdef-high/c6/ |
| O3 | INV*(p): every avoider of length 4p-2 over D_{2p} lies in RGR_{4p-2}(p) | [F] p = 5 only (all 3,730 normalised D10 avoiders of length 18 are RGR, olson/README.md Sec. 5.1); INV*(7) untested; no written result for any p | unowned until 18:29; OlsonParity2 starts it in c2/ (Sec. 4) |
| O4 | reviews of the above | per row; Lemma M0 (proof-RUNS.md Sec. 12) is inside the olson-par2-closure reviews | parent |

Hence, given O1 (Theorem P) and Corollary RL, the full statement needs exactly: O2d's open residual (OlsonRunCount5),
O3 = INV*(p) (open, no partial result), and the pending reviews.

## 3. Corollary RL (RUNS on the low-odd side) [W, unreviewed]

**Corollary RL.**  Let p >= 5 be prime and w' an inherited avoider in RGR_{4p-2}(p), normalised B <= A, with o_F(w') <= p.
Then k(w') <= p.
Proof.  Suppose k >= p + 1.  By proof-RUNS.md Sec. 11 (RUNS for B = 0 and for kappa = 0), B >= 1 and kappa >= 1; the zero
condition (Lemma H, ../../proof-PAR-K0.md Sec. 1; A, B <= 2p - 1 as w' avoids) gives B <= kappa.  Lemma OR
(../../proof-PAR-Kplus-partial-r2.md Sec. 1): the merged word w~ avoids, all its k~ = o_F <= p reflection runs are odd,
and A, B, kappa are those of w'; (V) gives kappa <= o_F - 1 = k~ - 1.  If B = kappa, Theorem KB (same file, Sec. 6; its
hypotheses (V), o_F <= p and, in its capped case, (D0) are inherited) gives an identity 2p-subword of w'.  If B < kappa,
w~ satisfies the hypotheses of MIX_low(p) (all reflection runs odd, k~ <= p, A >= B >= 1, B < kappa <= k~ - 1), so
Theorem M (c2/proof-R4-closure.md Sec. 2) gives an identity 2p-subword of w~.  Both contradict avoidance.  []
Consequence: given Theorem M, RUNS(p) <= O2c + O2d (the side o_F >= p + 1); the earlier remark of proof-RUNS.md Sec. 12
("remaining ... words with o <= p") is closed.

## 4. INV*: exact open statement and the first step (plan [I])

INV*(p) has two halves (they are the two steps (a), (b) of the proof of Corollary DR'):
 (a) the rotation values of every avoider of length 4p-2 lie in one set {rho_x, rho_-x}, x != 0 (no rho_0, no third value);
 (b) every maximal cyclic reflection run of such an avoider is constant.
Weaker sufficient form [I, by the proof of DR']: INV*_del(p): every one-letter deletion of an avoider of length 4p-1 is RGR.
Available tools for general words (not RGR): Theorem P, Doubling, Davenport-alpha, Theorem R, Corollary R'
(../../../proof-dihedral-partial.md, reviewed), Theorem T0 (../../../proof-T0.md, reviewed); residual class
../../../residual-class.md.
First step (c2/, OlsonParity2): half (b) for words whose rotations already lie in {rho_x, rho_-x}.  Every such word is an
alternation of possibly EMPTY rotation runs and constant reflection blocks (cut every maximal reflection run at each
change of letter); Lemma GR's proof (../../../proof-GR.md Sec. 2) never uses that a rotation run is nonempty, so Lemma GR
and Lemma WAS stay exact for these "generalised RGR" words (to be written as Lemma GR0).  Then (b)-rigid is: no avoider of
length 4p-2 has an empty rotation run between two blocks of different value.  Plan: Lemma GR0 [W]; exact searches at
p = 5 (control: must agree with the exhaustive D10 list) and p = 7 [F]; then check which PAR lemmas survive r_t = 0.
