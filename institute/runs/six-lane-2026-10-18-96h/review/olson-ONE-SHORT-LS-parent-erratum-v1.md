# ONE-SHORT-LS parent editorial and trust erratum v1

Recorded at 2026-10-19T12:11:07-0700. Read after proof `c544aad2ab0cadc4c76870dc97382b6a749bbdda85f96596bdb128efe9b19ffc` and package `46a23fd0f1ae9f47762587e617ecab72cd666e45e83514fb00fc0b3d2cc07343`. Disposes six MINOR findings of Claude `d718f61eee3445ca407fa11d066df05a0bf3e99f75152aac4cc9fdb33ee4142c`; all theorem/new-lemma verdicts ACCEPT,0F/0M. Codex `dd2ec5570d1be85fbff8e6fe710b3a4d61e14caccbf3ca400ea0a2be1d5b7220` had0findings. No theorem domain, case split or mathematical argument changes. Each Old span occurs exactly once in the named immutable file.

## MINOR1 standing hypotheses

Source: /Users/jinleic/repos/aifours/mathematics/evidence/six-lane-20261018-96h/olson/continuations/one-short-ls/proof-ONE-SHORT-LS-v2.md

Old:
````text
Corollary IP'. If, for an odd generator g with M = v_g(Y),
````

New:
````text
Corollary IP'. Under Lemma IP's standing hypotheses on p, kappa and Y (not an assumed long zero-sum), if, for an odd generator g with M = v_g(Y),
````

## MINOR2 nonzero Lev generator

Source: /Users/jinleic/repos/aifours/mathematics/evidence/six-lane-20261018-96h/olson/continuations/one-short-ls/proof-ONE-SHORT-LS-v2.md

Old:
````text
x_u >= 1 (one of them 1) with mu_u = x_u a (mod p) and
````

New:
````text
x_u >= 1 (one of them 1) with mu_u = x_u a (mod p). The term with x_u = 1 equals a; it is nonzero since U' is zero-sum-free, so a != 0 and ord(a) = p. Thus
````

## MINOR3 all nonzero lifts

Source: /Users/jinleic/repos/aifours/mathematics/evidence/six-lane-20261018-96h/olson/continuations/one-short-ls/proof-ONE-SHORT-LS-v2.md

Old:
````text
the other candidates
x~ +- p have absolute value >= p-d0 >= l;
````

New:
````text
every other lift
x~ + m*p with integer m != 0 has absolute value >= p-d0 >= l;
````

## MINOR4 Lev trust cells

Source: /Users/jinleic/repos/aifours/mathematics/evidence/six-lane-20261018-96h/olson/continuations/one-short-ls/proof-ONE-SHORT-LS-v2.md

Old:
````text
used once (Sec. 5) exactly as in G-LS; its
````

New:
````text
used once (Sec. 5, case (I)) for every e >= 2. Its statement-level form matches G-LS, but its cells do not: this proof uses Lev also at e = 2, while G-LS is Lev-free there. Its
````

## MINOR4 package counterpart

Source: /Users/jinleic/repos/aifours/mathematics/evidence/six-lane-20261018-96h/olson/continuations/one-short-ls/review-package-ONE-SHORT-LS-v1.md

Old:
````text
statement-level external Lev 2022 Theorem 2 (used once, in case (I)), exactly as G-LS.
````

New:
````text
statement-level external Lev 2022 Theorem 2 (used once in case (I) for every e >= 2). The form matches G-LS, not its Lev-free e=2 coverage.
````

## MINOR5 constant citation

Source: /Users/jinleic/repos/aifours/mathematics/evidence/six-lane-20261018-96h/olson/continuations/one-short-ls/proof-ONE-SHORT-LS-v2.md

Old:
````text
| Dichotomy | K = p-2e+1; (I) d <= e-2 (70-71) |
````

New:
````text
| Dichotomy | K = p-2e+1 (proof-ROW-v1.md:62); (I) d <= e-2 (G-LS case split70-71) |
````

## MINOR6 failed-method scope

Source: /Users/jinleic/repos/aifours/mathematics/evidence/six-lane-20261018-96h/olson/continuations/one-short-ls/proof-ONE-SHORT-LS-v2.md

Old:
````text
exclude b = -2 when S = n (U' then consists of involutions); only Lemma IP excludes it.
````

New:
````text
exclude b = -2 when S = n (U' then consists of involutions); the displayed Lemma IP argument does exclude it. No assertion about all possible methods is made.
````

