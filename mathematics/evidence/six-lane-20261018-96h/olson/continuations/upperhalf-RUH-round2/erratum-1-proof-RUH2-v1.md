# Erratum 1 to proof-RUH2-v1.md (author's line audit; two justification gaps closed, no statement changes)

Owner OlsonPP1Exclusion. Written after /bin/date 2026-10-19T17:27:14-0700. Read after the immutable proof-RUH2-v1.md, SHA256
f391b08f2df02036b4a7cfc66c1f118e7f20c6dfb8d89af2a10e121ea58df4e2 (frozen 17:25:14). The proof file is not edited. Each Old span
occurs exactly once.

## E1 (Sec. 7, c=5): a pair with s=-4 must be excluded by the length j=4, not j=3

Old:
````text
non-adjacent, both free) put 7 or 8 in M: impossible. So all t in {-1,-2}, M contains [1,4]; a pair needs s+3 in M (j=3 free
for m=1,2), so s=-2 and both t=-1; three empty runs give s+3=0 in M. So E=2, |Q|=4. If Q has >=3 components, one run from each
````

New:
````text
non-adjacent, both free) put 7 or 8 in M: impossible. So all t in {-1,-2}, M contains [1,4]; a pair needs s+3 and s+4 in M
(j=3,4 are free and admissible for m=1 and m=2); s=-3 gives s+3=0 and s=-4 gives s+4=0, so s=-2 and both t=-1; three empty
runs give s+3=0 in M (j=3 admissible for m<=3). So E=2, |Q|=4. If Q has >=3 components, one run from each
````
(Without the j=4 clause, s=-4 would only give s+3=-1, which is not excluded by |M|<=5 alone.)

## E2 (Sec. 7, preamble): range of the free condition n>=b

Old:
````text
Lengths for a set of empty runs with m intervals: j in [m,m+4]; free iff 2j>=10-c (n<=A; n>=b holds for j<=7 as p>=13);
````

New:
````text
Lengths for a set of empty runs with m intervals: j in [m,m+4]; free iff 2j>=10-c (n<=A; n>=b means j<=(p+1+c)/2, which holds
for every length used below: j<=7 when c<=8, and j<=9 for the sets of at most five empty runs used when c=9, as p>=13);
````
(In the c=9 case the bound E<=4 applies the interval rule to a set of five empty runs, with m<=5 and j<=9; and an interval
s(Y)+[m,m+4] that met [1,t_max+5] while reaching p would contain p, i.e. 0, which is not in M; so no residue wraps.)
