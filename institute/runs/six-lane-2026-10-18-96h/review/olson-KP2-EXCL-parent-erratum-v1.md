# KP2-EXCL: exact-antecedent and ancillary-proof erratum

Recorded at 2026-10-19T13:17:22-0700. Apply to immutable proof `8be43069c0a7935db902ba2ae4dda533b661ae0c981517f62f0e2b64e518b002`. Disposes Codex `5e4eb5ed47c7d45b90a98ff2a27f67a4833c8bac2797b5273726c58535909ce8`: main theorems ACCEPT, packet ACCEPT-WITH-FIXES, **0 FATAL/1 MAJOR (scope wording)/1 MINOR (ancillary interface)**. The unrestricted multiset-only reading is withdrawn, not accepted. Every exact-cell main statement and proof is unchanged.

## MAJOR1 exact antecedent

Source: /Users/jinleic/repos/aifours/mathematics/evidence/six-lane-20261018-96h/olson/continuations/terminal-pplus1-kp2-exclusion/proof-KP2-EXCL-v1.md, lines 36-37.

Old:
````text
Logical consequence (no further input): the hypothesis of the pending ROT-PP1-TOP is never satisfied, so it holds vacuously
and its rotation multisets rho_c^A rho_(-c)^(3p-5-A) describe no avoider. No step below uses p >= 7 beyond p >= 5; p = 5 is not
````

New:
````text
Logical consequence: ROT-PP1-TOP holds vacuously under its FULL antecedent: a length-4p-2 avoider having SOME admissible normal form with terminal k=p+1, kappa^=p-2. Its listed rotation multisets occur in no avoider with that exact antecedent; no multiset-only exclusion outside it is asserted. No step below uses p>=7 beyond p>=5; p=5 is not
````

## MINOR2 ancillary F1 derivation

Source: /Users/jinleic/repos/aifours/mathematics/evidence/six-lane-20261018-96h/olson/continuations/terminal-pplus1-kp2-exclusion/proof-KP2-EXCL-v1.md, lines 226-229.

Old:
````text
  (F1) Single-run omission counts in the style of PP1-EXCL (Lemma SR, K = p-1 omitted letters, n = 2p-4): with b letters != a,
       a run with A - alpha_i >= p-1 has b + alpha_i - beta_i nonzero weights, so OM' forces alpha_i <= beta_i + (p-2-b). For
       b = p-2 this gives alpha_i <= beta_i and two empty runs, but for b = p-3 (alpha_i <= beta_i + 1) and b = p-4
       (alpha_i <= beta_i + 2) single runs alone do not force empty runs; the set window (W) with Step 4 is what closes these.
````

New:
````text
  (F1) Re-derived single-run omission count, using no pending SR/OM' interface. Take z=-1 on run i, omit exactly p-1 letters
       to select n=2p-4, and assume A-alpha_i>=p-1 signed-a letters outside that run. Among the other letters the number of
       nonzero deviations from signed value a is b+alpha_i-beta_i. If this is >=p-1, choose p-1 such occurrences; their
       nonzero deviations have all of Z_p as subset sums by RS(b). Supplement any chosen subset with outside signed-a
       occurrences to omit exactly p-1 letters. The complementary selections attain every signed sum, including T, so SEL2
       contradicts avoidance. Thus b+alpha_i-beta_i<=p-2. If b=p-2 then A=2p-3 and at most one run fails the filler hypothesis
       (two would require 2p-2>A a-letters); each nonempty remaining run consumes a non-a letter, giving at least two empty
       runs. For b=p-3 or p-4 this same counting argument allows alpha_i<=beta_i+1 or +2 and does not itself give that
       empty-run bound; the set window and light-set argument in section 4 supply it.
````

The last word "not" in the first replacement is completed by unchanged line38 "claimed." No broader p=5 statement is added. The new F1 derivation is a written justification of an ancillary remark, not a new import or an exclusion outside the frozen cell. Both families must assess the corrected snapshot before any parent acceptance.
