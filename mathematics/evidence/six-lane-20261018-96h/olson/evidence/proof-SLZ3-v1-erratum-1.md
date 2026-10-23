# Erratum 1 to evidence/proof-SLZ3-v1.md (sha256 0cfe637f919bdaab937f8292fa527d7fbd54e3af7d55bb07ddf137c0ad263c1c)

Owner ContinueOlson (review-errata ownership only).  Written after /bin/date 2026-10-19T03:56:28-0700.  Answers, in one round, run
review/olson-SLZ3-codex-v1.prompt.stdout.txt (sha256 29820717a8852727a15e76a4b794f61e75f94c77a92be1be865055c899fc9d49; ACCEPT-WITH-MINOR-FIX, 0 FATAL / 0 MAJOR / 2 MINOR) and run
review/olson-SLZ3-claude-v1.prompt.note.md (sha256 3579005a33ea332f2b197defd2ff75971c58ac801c417e258cf0b57253b8e0ec; ACCEPT-WITH-FIXES, 0 FATAL / 0 MAJOR / MINOR M1-M11).  The v1
text is not edited.  The statement of Theorem SLZ3 and its proof strategy are unchanged.

## M1 (Claude) = Codex 1: delta >= 3
Sec. 2's 'delta >= 3 since kappa >= (2p + 1)/3 >= (p + 3)/2 for p >= 5' (false at p = 5) is replaced by: 'kappa > 2p/3, so
delta = 2kappa - p > p/3 > 1 (indeed delta >= (p + 2)/3); delta is odd, so delta >= 3; kappa <= p - 1 gives delta <= p - 2.'
## M2: Step 3
(i) T0 is a (kappa - 1)-long zero-sum of T (length >= 2kappa); T satisfies (ZP_(kappa-1)), so |T0| >= 2p + 1, and by parity
|T0| >= 2p + 2 >= 2kappa + 2: T0 is a kappa-long zero-sum of Y.  (ii) 'long' is indexed: 'shortest (kappa - 1)-long zero-sum
T0 of T', 'kappa-long zero-sum of Y'.  (iii) Step 3 keeps S1-sharp erratum 1's closing line (A-m2): Step 1 applied to the
proper zero-sum Q' gives l <= u, i.e. D >= 0.  (Optional shortcut, noted: T0 != T would be a proper zero-sum of T of length
>= u, excluded by the case assumption; so T0 = T and N <= 3kappa - 2.)
## M3: Steps 6-7, range-sensitive inequalities written out
m >= (p + 3delta)/2 >= 2delta >= D + 2 (delta <= p, D <= 2delta - 2); D <= 2delta - 2 <= 2p - 6 (delta <= p - 2), so the first
crossing prefix W has 2p <= A_W <= 2p + D < 4p and is proper; g^r is in Q as r <= D < m; g^s is in Q as 1 <= s <= D + 1 <= m.
## M4: Sec. 3 hypothesis map (rewritten)
- H: N >= 3kappa + 2.  With 3kappa >= 2p + 1 it gives N >= 2p + 3, hence N >= 2p + 4 by parity; this (not (ZP_kappa)) is the
  source of N > 2p.
- Step 1 uses only the minimality of N (S1-sharp erratum A-m2); with H: D <= kappa - 2, l >= kappa + 2; with N > 2p:
  D <= 2delta - 2, l >= p - delta + 2.
- Step 2 uses N > 3kappa.  Step 3 uses N > 3kappa - 2 (induction) and N > 2p ((ZP_(kappa-1)) for T).  Step 4 uses |Q| = 2kappa
  and kappa <= p - 1 (S_Q nonempty); it uses no l.  Steps 6-7 use delta <= p - 2 (from kappa <= p - 1) and D <= 2delta - 2;
  Step 7 uses N > 3kappa.  Step 9 uses l >= kappa + 2 (base >= 4) and l >= p - delta + 2.
- (ZP_kappa) for Y is not invoked in the proof; the Theorem's statement is NOT changed on that account (no claim beyond the
  stated hypotheses).
## M5: title
The title reads '... (floor(2p/3) < kappa <= p - 1)'.  (kappa <= p - 1 is necessary: at kappa = p, g^(4p) has shortest long
zero-sum of length 4p > 3p + 1.)
## M6: Sec. 0, Sharpness
g is an odd generator (g = p violates (ZP)); 'its NONEMPTY zero-sums g^i (3g)^j have i + 3j in {2p, 4p}'; for p = 1 (mod 3),
ceil((p - 3)/3) = (p - 1)/3, so the proper lengths 2p - 2j are <= 2p - 2(p - 1)/3 = (4p + 2)/3 = 2kappa.  For p = 2 (mod 3) and
kappa = (2p + 2)/3: N is even, so N <= 3kappa + 1 = 2p + 3 gives N <= 2p + 2 = 3kappa, and F1 (largest proper zero-sum length
2floor(2p/3) + 2 = 2kappa) attains it.  No sharpness is claimed for kappa >= floor(2p/3) + 2.  (Claude's remark that the same
steps give N <= 3kappa for kappa >= floor(2p/3) + 2, attained at kappa = (2p + 4)/3 by g^(p+6) (3g)^(p-2), is recorded as the
referee's observation, not adopted as a claim.)
## M7: Sec. 0, 'Equivalently' (derivation added)
Theorem => form 2: apply the Theorem with Y := T (a zero-sum with (ZP_kappa) and |T| >= 3kappa + 2 is kappa-long); its shortest
kappa-long zero-sum has length <= 3kappa + 1 < |T|, so it is proper.  Form 2 => Theorem: a shortest kappa-long zero-sum T of Y
satisfies (ZP_kappa) (hereditary); if |T| >= 3kappa + 2, a proper long zero-sum of T would be a shorter long zero-sum of Y.
## M8: Sec. 0, Consequence
'whenever kappa <= p - 1' is replaced by 'for every kappa in the SLZ3 range'.
## M9: Sec. 1, imports
Add: S1-sharp's acceptance is relative to S1+ (transitive import) and the index-one theorem; S1-sharp erratum 1
(evidence/proof-S1-sharp-v1-erratum-1.md, bf504cdf8b8cfd3e96a26609d00162d365415b3481ca3a7dcbd7112af82f9507; items A-m1, A-m2, A-m6, A-m8) is a mandatory overlay for the Steps marked
'Unchanged'; the index-one parent import record is run of 2026-10-16 review/olson-index-one-primary-statement-parent-v1.md,
sha256 e461514461d23287beeecf04fa26334efd91d3de51caa33312f6c5b10b4d35c6.
## M10: notation
In Steps 5-9 the terms of Q' other than g are written R (Q' = g^(t') R; R_low for Y_low); the word 'non-unit' is replaced by
'other than g'.  Y denotes only the ambient sequence.
## M11 (Claude) = Codex 2: Sec. 4
thr := p + 2kappa + 1 (the threshold of LS, evidence/LS-scope-v1.md, 80ae8041118d68f4c1417a67a2891ceaceeba181a375b29dfd73820957cfddfa).  If |Y| >= thr, then
|Y - T| >= thr - (3kappa + 1) = p - kappa.  SLZ3 bounds |T|, not |Y|; no LS, LS+, INV*, ordered-Olson or dihedral consequence
follows from it.
