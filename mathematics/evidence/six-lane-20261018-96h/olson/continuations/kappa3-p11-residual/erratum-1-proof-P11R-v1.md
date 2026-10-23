# Erratum 1 to proof-P11R-v1.md (wording of two route remarks in Sec. 8; no claim changes)

Owner OlsonPP1Exclusion. Written after /bin/date 2026-10-20T00:14:31-0700. Read after the immutable proof-P11R-v1.md, SHA256 6ee3df0985f02d01e6cde08c88944791b91dbc76e389e20f16e6b9accec87ac4.
Each Old span occurs exactly once. Theorem P11R, Lemmas N11, ARC, FULL11, PAIR, BOTH and Theorem NR are unchanged.

## E1 (Sec. 8, missing claim): the K3 final cases are a route description, not a premise
Old:
````text
sum theta = B*-2nu0-22 (Lemma C) and the K3 sorting give B*<=16 (or B*<=14 if a first-three set lies in M), and the final cases of
K3 Sec. 6 then apply at p=11 (their counts p-9+nu0>=3 unit runs, etc., hold at p=11). By Lemma FULL11(c) every P-split pattern is
````
New:
````text
sum theta = B*-2nu0-22 (Lemma C) and the K3 sorting give B*<=16 (or B*<=14 if a first-three set lies in M), and a case analysis
like that of K3 Sec. 6 (the untrusted candidate, cited here only as a route description; it would have to be re-derived) is
then expected to finish (its counts p-9+nu0>=3 unit runs, etc., hold at p=11). By Lemma FULL11(c) every P-split pattern is
````

## E2 (Sec. 8, failed route F1): the example multiset is itself excluded
Old:
````text
Failed routes, kept. (F1) Single empty runs: (SR) with window [6,16] only restricts tau_e to a few residues (e.g. all labels 1,
nu0=0 leaves tau_e in {2,4,7,9}); no contradiction.
````
New:
````text
Failed routes, kept. (F1) Single empty runs: (SR) with window [6,16] only restricts tau_e to a few residues (illustration with
the label multiset of sixteen 1's: tau_e in {2,4,7,9}; that multiset itself is excluded by CJ''', the point is only that the
single-run test leaves several residues); no contradiction.
````
