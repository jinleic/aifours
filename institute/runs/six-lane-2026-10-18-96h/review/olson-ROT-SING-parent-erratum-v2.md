# ROT-SING parent editorial and trust-scope erratum v2

Recorded at 2026-10-19T12:25:13-0700. Read after immutable proof `ae5feaa1cd99aad9d2c0c35d1521ec27c3a1e5516225b102b4cb4bb793a4b1f1` and parent erratumv1 `aad62a162f1fb25cc786ea0b96f1ceaeacf8cad8532bd16a36c15058d612d25b`. Disposes Claude `f53a8a78d056177cef70c76949adea85e77ca5999e1c9bfec96c45683c97ee0a`: main and strengthened statement ACCEPT,0F/0M/4nonblockingMINOR. No theorem, step or inequality changes. Every Old span occurs once in its named source.

## m1 positive heavy count

Source: /Users/jinleic/repos/aifours/mathematics/evidence/six-lane-20261018-96h/olson/continuations/terminal-p-singletons/proof-ROT-SING-v2.md

Old:
````text
so there are at most two (3(p-2) > 2p-4), and the excess
````

New:
````text
so there are at most two (3(p-2) > 2p-4) and at least one (the excess below is positive), and the excess
````

## m2 odd length, not ambiguous block count

Source: /Users/jinleic/repos/aifours/mathematics/evidence/six-lane-20261018-96h/olson/continuations/terminal-p-singletons/proof-ROT-SING-v2.md

Old:
````text
with k odd constant blocks S_i
````

New:
````text
with k constant blocks S_i, each of odd length,
````

## m3 restriction to displayed selection family

Source: /Users/jinleic/repos/aifours/institute/runs/six-lane-2026-10-18-96h/review/olson-ROT-SING-parent-erratum-v1.md

Old:
````text
otherwise full coverage is unavailable; the argument still contradicts avoidance if the actual target lies in D-B_2 in case (i), or D+B_2 in case (ii).
````

New:
````text
otherwise this displayed selection family does not cover Z_p; it still contradicts avoidance if the actual target lies in D-B_2 in case (i), or D+B_2 in case (ii). This is not an assertion about all possible selections for that arc.
````

## m4 explicit sequence context, not a premise

(S1_(p-1)) here means every zero-sum has length<=2p-2. The displayed sequence g^(2p-1)(3g)^(p-1) has no2pzero-sum: if i+j=2p, i+3j=0mod2p forcesp|j, butj<=p-1 andi<=2p-1. It has the long zero-sum g^(p+3)(3g)^(p-1), length2p+2 and coefficient sum4p. Thus it failsS1 at sequence level. This is the same excluded endpoint context in the now-accepted [ONE-SHORT verdict](/Users/jinleic/repos/aifours/institute/runs/six-lane-2026-10-18-96h/review/olson-ONE-SHORT-LS-parent-verdict-v1.md); no word avoider is asserted and no such premise is used in ROT-SING. The old pending ASSEMBLY-LS/ONE-SHORT prose is historical only; word assembly still needs its own verdict.

## CT scope clarification (I4)

The STAB-delta verdict's item6 explicitly accepts primep>=5,0<=kappa<=p-1. That self-scoped CT interface, not the introductory default range for LS/LS+/STAB claims, governs CT at kappa=p-1. No expansion of CT is inferred here.
