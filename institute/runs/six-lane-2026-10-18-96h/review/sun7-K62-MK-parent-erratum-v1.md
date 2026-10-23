# K62-MK parent scope, commentary and provenance erratum v1

Recorded at 2026-10-19T11:36:36-0700. Read after proof K62-MK-v2 `ab7cfcb6ccebb19465eb6dfc3f96580d58c599a2507aee697604f691ad5abee9` and package `a7ce91e134d47c074c53ee1fafa99bb6f380778f84cee7033550b3ad011e4255`. Codex review `b6c1e05b63080e84c2f4607805103ed173d56ff09c9d36d6570402fd8f8fd1d1` accepted all five claims with 0 FATAL / 0 MAJOR / 3 MINOR findings. I1/M1/M2 below dispose those findings. P1 is an additional parent wording correction: the original TRI statement is false for a graph with at most one triangle; its proof and downstream uses require only the corrected universal pair statement. No theorem claim or proof step changes. Every Old span occurs once in its named immutable source.

## I1 scope

Source: /Users/jinleic/repos/aifours/mathematics/evidence/six-lane-20261018-96h/sun-coset7/continuations/k62-regimes/K62-MK-v2.md

Old:
````text
cross-checks; Lemmas 3.1-3.3 re-prove them for every v in O
````

New:
````text
cross-checks; RC is re-proved for any vertex; GR gives granularity 6 off t; CI* applies at any O-vertex with its own-family granularity 6
````

## M1 mutation

Source: /Users/jinleic/repos/aifours/mathematics/evidence/six-lane-20261018-96h/sun-coset7/continuations/k62-regimes/K62-MK-v2.md

Old:
````text
(4) drop E3-L2: three entries 1 in a row would change
  val(c0);
````

New:
````text
(4) withdrawn: c0 has value r + (4-r) + 3/2 = 11/2 regardless of the number r of entries 1, and its feasibility proof also does not require r <= 2;
````

## M1 package counterpart

Source: /Users/jinleic/repos/aifours/mathematics/evidence/six-lane-20261018-96h/sun-coset7/continuations/k62-regimes/review-package-MK-v1.md

Old:
````text
Without E3-L2, val(c0) changes.
````

New:
````text
The former E3-L2 mutation is withdrawn: val(c0) = r + (4-r) + 3/2 = 11/2, and its feasibility does not require r <= 2.
````

## M2 provenance

Source: /Users/jinleic/repos/aifours/mathematics/evidence/six-lane-20261018-96h/sun-coset7/continuations/k62-regimes/K62-MK-v2.md

Old:
````text
Sun(2) (EQ*, R4*), Sun(3)
````

New:
````text
Sun(2) (CI*, EQ*, R4*), Sun(3)
````

## M2 package counterpart

Source: /Users/jinleic/repos/aifours/mathematics/evidence/six-lane-20261018-96h/sun-coset7/continuations/k62-regimes/review-package-MK-v1.md

Old:
````text
Sun(2) (EQ*, R4*), Sun(3)
````

New:
````text
Sun(2) (CI*, EQ*, R4*), Sun(3)
````

## P1 parent TRI wording

Source: /Users/jinleic/repos/aifours/mathematics/evidence/six-lane-20261018-96h/sun-coset7/continuations/k62-regimes/K62-MK-v2.md

Old:
````text
most two triangles, and two of its triangles share an edge (a diamond).
````

New:
````text
most two triangles, and any two distinct triangles share an edge (hence two triangles form a diamond).
````

E3-a is used only as Z11(a), the proof sub-claim inside the accepted C2 proof, not as a strengthened Lemma 2 statement. Its original marker and orientation hypotheses hold in K; the corrected second-family review must check them independently.
