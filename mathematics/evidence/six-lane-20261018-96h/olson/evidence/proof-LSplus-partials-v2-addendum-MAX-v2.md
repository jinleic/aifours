# Addendum to evidence/proof-LSplus-partials-v2.md: Lemma MAX (E2, E3 admit no one-term extension) and the reduction
# LS+ <= STAB, v2

Owner ContinueOlson.  Written after /bin/date 2026-10-19T03:43:20-0700.  Status: CANDIDATE PARTIALS, written proofs [W], UNREVIEWED.  v2 (after /bin/date 2026-10-19T03:43:30-0700) supersedes v1 (ff00f979...c43b, never sent):
'base >= 4' in the side observation corrected to 'base >= 3' (sufficient for Step 9); nothing else changed.  Scope:
evidence/LSplus-scope-v1.md (7dc04949c1152907eef9938c4680248eeb24d5830ab751f67f1355ba6e0e2cbc).  Uses proof-LSplus-partials-v2.md (eedfa0f16572f1636bfa4f387e3a1566b87864ae4ced6fddcf063cddaedcb6b2) and the candidate SLZ3
(evidence/proof-SLZ3-v1.md 0cfe637f919bdaab937f8292fa527d7fbd54e3af7d55bb07ddf137c0ad263c1c).  LS+ and STAB are NOT proved and not assumed.  e := p - kappa;
kappa0 + 1 <= kappa <= p - 2, so e <= (p - 1)/3 (3kappa >= 2p + 1).

## Lemma MAX
For every generator h and every odd y, the sequences E2 y and E3 y (E2 = h^(3kappa-p+2) (3h)^(p-1),
E3 = h^(3kappa-2p+2) (3h)^(2p-1)) violate (ZP_kappa).
Proof.  Write y = c h, c odd in [1, 2p - 1].  For c in {1, 3} the sequence is h^a (3h)^b with a + b = 3kappa + 2 and still has
a long zero-sum, so Lemma TV forces a violation of (ZP_kappa).  Let c >= 5 (indeed c >= 3 suffices below).
E2 (a = 3kappa - p + 2 = 2p - 3e + 2, b = p - 1).  Zero-sums y h^i (3h)^j with c + i + 3j = 4p, 0 <= i <= a, 0 <= j <= b have
length 1 + 4p - c - 2j; the feasible j form the interval [j1, j2], j1 := max(0, ceil((2p + 3e - 2 - c)/3)),
j2 := min(p - 1, floor((4p - c)/3)); the length lies in [2kappa + 2, 2p] iff j in [w1, w2], w1 := (2p + 1 - c)/2,
w2 := (2p + 2e - 1 - c)/2 (integers; w2 - w1 = e - 1 >= 1).  The two intervals meet: w1 <= p - 1 (c >= 3) and
w1 <= (4p - c)/3 (c >= 3 - 2p), so w1 <= j2; (2p + 3e - 2 - c)/3 <= w2 (c <= 2p + 1) and 0 <= w2, so j1 <= w2;
(2p + 3e - 2 - c)/3 <= p - 1 (c >= 3e + 1 - p, true as 3e <= p - 1) and <= (4p - c)/3 (3e - 2 <= 2p), so j1 <= j2; w1 <= w2.
E3 (a = 3kappa - 2p + 2 = p - 3e + 2, b = 2p - 1).  Use c + i + 3j = 6p: feasible j in [j1, j2] with
j1 := max(0, ceil((5p + 3e - 2 - c)/3)), j2 := min(2p - 1, floor((6p - c)/3)); length 1 + 6p - c - 2j lies in [2kappa + 2, 2p]
iff j in [w1, w2], w1 := (4p + 1 - c)/2, w2 := (4p + 2e - 1 - c)/2.  w1 <= 2p - 1 and w1 <= (6p - c)/3 (both c >= 3);
(5p + 3e - 2 - c)/3 <= w2 (c <= 2p + 1); (5p + 3e - 2 - c)/3 <= 2p - 1 (c >= 3e + 1 - p) and <= (6p - c)/3 (3e - 2 <= p).
So in both cases some zero-sum through y has length in [2kappa + 2, 2p].  []

## STAB (conjecture, not assumed) and the reduction
STAB(p, kappa): every (ZP_kappa) sequence of length exactly 3kappa + 1 that fails (S1_kappa) is E2 or E3 for some generator h.
Proposition.  STAB(p, kappa) implies LS+(p, kappa).
Proof.  Let Y be a counterexample to LS+(p, kappa); by Lemma RED+ (a) WLOG |Y| = 3kappa + 2.  By SLZ3 a shortest long
zero-sum T has |T| <= 3kappa + 1 < |Y|; take y in Y - T.  Y - y has length 3kappa + 1, satisfies (ZP_kappa) and fails
(S1_kappa) (it contains T), so by STAB it is E2 or E3, and Y = (Y - y) y violates (ZP_kappa) by Lemma MAX: contradiction.  []
Support for STAB (aids, not premises): in the three complete cells of probe v12 the multisets of length 3kappa + 1 are exactly
E2 and E3: p = 11, kappa = 8 and 9 (canonical DFS: 2 multisets each, 1^15 3^10 / 1^21 15^4 and 1^18 3^10 / 1^21 15^7);
p = 7, kappa = 5 (non-canonical DFS: 12 multisets = 2 families x 6 generators of Z_14).

## Side observation on SLZ3 (internal; not a claim beyond the SLZ3 text)
Re-running SLZ3's Steps at N = 3kappa + 1 (kappa odd) gives base = (3kappa + 3 - 2p)/2 >= 3 whenever 3kappa >= 2p + 3 (3kappa + 3 - 2p is even), so
for kappa >= kappa0 + 2 the bound improves to N <= 3kappa; F1 shows N = 3kappa + 1 occurs at kappa = (2p + 1)/3.  In all
cases N <= max(3kappa, 2p + 2).
