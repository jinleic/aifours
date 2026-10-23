# Erratum 1 to proof-S1-sharp-v1.md (no statement change): disposition of both hostile reviews

Owner ContinueOlson.  Written after /bin/date 2026-10-19T00:32:00-0700.  Applies to the frozen text
evidence/proof-S1-sharp-v1.md, sha256 992ab63f40aa08626560ccf121b0004a08588fdb24805ff4eb30d25a2150cb0c (unchanged).
Reviews (run review/): Codex gpt-6.1-sol (receipt-reported identity) olson-s1sharp-codex-v1.prompt.stdout.txt
19467d14c4bae4fbff9c06b4a3e599181d3583cc3771a653cdde94cbdc8b39d6: (A) and (B) ACCEPT-WITH-FIXES, 0 FATAL/0 MAJOR, 3 MINOR;
Claude claude-opus-5-5 (receipt-reported init model) olson-s1sharp-claude-v1.prompt.note.md
4a44a9d14f07e35e719f5061665edd6b0fcf94e1ccd34a73e3c6c030754ec18f: (A) ACCEPT-WITH-FIXES 0/0/9, (B) ACCEPT-WITH-FIXES 0/0/5.
Lemma S1-sharp and Corollary S1-sharp-INV/OLSON are UNCHANGED in statement.  Read v1 through the replacements below;
where a replacement and v1 differ, the replacement governs.  Model acceptance is not mathematical verification.

## Fix map

Codex 1 / Claude A-m4 (Sec. 0, sharpness).  Replace the F1/F2 sentences by:
- (F1) For every prime p >= 5, T = g^(p+3)(3g)^(p-1): a proper nonempty zero-sum is g^a(3g)^b with a + 3b = 2p,
  ceil((p-3)/3) <= b <= floor(2p/3), of length 2p - 2b; the only other nonempty zero-sum is T (coefficient sum 4p,
  length 2p+2).  The largest proper length is 2 floor(2p/3) + 2.  Hence (ZP_kappa) holds exactly for
  kappa >= floor(2p/3) + 1, and among these integers (S1_kappa) fails exactly for kappa <= p.  So the implication fails
  for every kappa in [floor(2p/3)+1, p], for every prime p >= 5 (general arithmetic; no finite enumeration is needed).
- (F2) For p = 1 (mod 3), c = (2p+1)/3 (odd), T = g^(2p-1)(cg)^3: the nonempty zero-sums are g^((4p-1)/3)(cg),
  g^((2p-2)/3)(cg)^2 and T, of lengths (4p+2)/3, (2p+4)/3, 2p+2 ((a, b) with a + cb in {2p, 4p}, a <= 2p-1, b <= 3).
  (ZP_kappa) holds exactly when kappa >= (2p+1)/3; among these integers (S1_kappa) fails exactly when kappa <= p.

Codex 2 / Claude A-m5 (Sec. 3, 'where the sharp families break').  Replace the diagnostic by:
- p = 1 (mod 3), kappa = (2p+1)/3: Steps 1-8 remain valid arguments at this kappa (Step 2 needs only 3kappa <= 2p+1,
  Step 7 only p >= 3delta-2; see A-m3), and the displayed decompositions of F1 (Q = g^(p+1)(3g)^((p-1)/3),
  Q' = g^2(3g)^((2p-2)/3), t' = 2, b_min = 3) and F2 (Q = g^((4p-1)/3)(cg), Q' = g^(c-1)(cg)^2, t' = c-1, b_min = c) satisfy
  all structural conclusions of Steps 1-8; both have base = 2, which is exactly the obstruction to the Step 9 counting
  ('at most one term of Y above t'' needs base >= 3).
- p = 2 (mod 3), kappa = (2p+2)/3 (separate sharpness observation): F1 decomposes as Q = g^(p+2)(3g)^((p-2)/3),
  Q' = g(3g)^((2p-1)/3), with t' = base = 1 and 3kappa = N = 2p+2, so Step 2's displayed contradiction and Step 7's
  contradiction are unavailable there (the minimality of the proper zero-sums of F1 holds by direct coefficient
  arithmetic).  'Fails only base >= 3' is a statement about the family, not about the argument, in this class.

Codex 3 / Claude B-m2 (Sec. 1 third bullet and Sec. 5(a)).  Read: 'GRX (all-plus pattern with zero rotations; H >= p
would already be an identity selection) gives kappa^ >= 0, and DAV gives kappa^ <= k - 1.'

Claude A-m1 (Step 4).  Add: 'nor 1 (every term would be 0, which is even)'.  The divisors of 2p are 1, 2, p, 2p because
p is prime.

Claude A-m2 (Steps 1 and 3).  In Step 1 read the parenthetical as '(a proper one of length >= u+2 would contradict the
minimality of N)'; (ZP) is idle there.  D >= 0 is not claimed in Step 1; add at the end of Step 3: 'Step 1 applied to
the proper zero-sum Q' gives l <= u, i.e. D >= 0.'  (D >= 0 is first used in Step 5.)

Claude A-m3 (Sec. 3 hypothesis map).  Replace the first bullet by:
| use | condition actually needed |
| Step 2 | 3kappa <= 2p+1 |
| Step 4 | delta >= 3 (length >= p+2); p prime (divisors of 2p) |
| Step 7 | p >= 3delta - 2 |
| Step 9 | 3delta <= p, i.e. base >= 3 (the only binding use of kappa <= floor(2p/3)) |
| induction base S1+ | p >= 5 prime; see A-m7 |
For prime p, 3delta <= p means p >= 3delta + 2 (p != 3delta).

Claude A-m6 (Step 9).  Add: 'If t' <= 2 then X = t' - base <= -1 < 0, already a contradiction (every summand of X is
>= 0); the two-term argument is needed only for t' >= 3.'

Claude A-m7 (Sec. 1 first bullet).  Cite S1+ at its primary acceptance: R/olson-zx-s1c-parent-verdict-v1.md (sha256
2f8d376b524bdbac7e0a3ff5fa588744bd26a49b2858c9d0f0bb1db6dbeee6af), statement 2, as restated in the S1(g) verdict
(cc9e27fb...605e) statement 2.  It is a statement about every sequence of odd elements of Z_2p, of any length; Step 3
applies it (via the induction) to the sequence T itself, which is within that form.

Claude A-m8 (Sec. 1 second bullet).  Add: 'This is the general C_n statement of the import record with n = 2p
(composite), applied to a minimal zero-sum of length p + delta >= p + 3 >= floor(n/2) + 2; ord(a) = 2p is derived from
the oddness of the terms (Step 4), not assumed.'

Claude A-m9 (Sec. 4).  Add: 'Probe v1 is not a premise and not a classification: its search space is built from the
conclusions of Steps 3-8, so it is circular as a check of those steps.  The independent aids are probes v2/v3
(evidence/probe-v2, probe-v3: every shortest long zero-sum with support size <= 3; exact; not premises), which found
F1/F2 at kappa = floor(2p/3)+1 and nothing at kappa = floor(2p/3) for p = 13, 31, 37, 41, 43, 47, 53, 59, 61.'

Claude B-m1 (Sec. 5, 'Effect on the residual map').  Replace by: 'Every terminal pair left by S1(g) (S1(g) verdict,
statement 4: (p+delta*+2)/2 <= kappa^ <= k-1 <= floor((2p+1)/3) - 1) is discharged; in particular (21, 20) at p = 31.
New coverage exists only for p >= 31; for p <= 29 the Corollary restates accepted coverage.'  The Q1a/Q1b description
is unreviewed lane context (bundle-v5 Sec. 5 terminology), not part of the Corollary.

Claude B-m3 (Sec. 5(a)).  Read the conclusion verbatim as in the ZX verdict: 'the original rotations lie in one nonzero
pair'.

Claude B-m4 (Sec. 1 third bullet).  Replace the line reference 'proof-ROT-ZX-v1.md L204-206' by: ZX verdict statement 3
with its overlays 1-4 and 8.

Claude B-m5 (Sec. 5(a) first sentence).  Read: 'Some (indeed every) admissible normal form w^ has k <= o and k = o
(mod 2); the case split k = 1 / k >= 2 is that of ZX overlay 3; no new k-case is introduced.'  The terminal criterion is
existential.

## Recorded observations (no change needed)

- Both reviewers re-derived Steps 1-9 independently and found no gap; Codex also re-derived the ordered deletion
  ledger (Cases 1-3) for (b).  Claude notes the Corollary uses the Lemma only at 3kappa^ <= 2p-2 (p >= 3delta+4,
  base >= 5), so neither the Lemma's endpoint nor the tight Step 9 margin is used by the Corollary.
- Neither review assessed novelty or priority; no Lean; this lane made no literature search for the Lemma, and a miss
  would not be evidence of novelty.
