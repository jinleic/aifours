# Erratum 2 to the RUH2 packet: repairs of Codex MAJOR 1 and MINOR 1-5 (no statement changes)

Owner OlsonPP1Exclusion. Written after /bin/date 2026-10-19T17:51:11-0700. Authority: Main's IRC after the Codex review
RUN/review/olson-RUH2-codex-v1.prompt.stdout.txt, whole-file SHA256 0c683ec64f8540b6d3df4ea35c2cbbf0192410ba56681bb7d3caa850e0bd8a9c
(RUN=/Users/jinleic/repos/aifours/institute/runs/six-lane-2026-10-18-96h). Read after the immutable files below; none is edited.
Each Old span occurs exactly once in its named file. Status unchanged: CANDIDATE_UNVERIFIED; this repair accepts no prior
candidate. Round-3 work (directory upperhalf-RUH-round3) is separate and does not cite this erratum.
- P  = proof-RUH2-v1.md, SHA256 f391b08f2df02036b4a7cfc66c1f118e7f20c6dfb8d89af2a10e121ea58df4e2
- PE = erratum-1-proof-RUH2-v1.md, SHA256 a3c673137ed35b81220b51f9e19997f0c31b10a32bcb5dc7b222e641f50f3f61
- R  = residual-RUH2-v1.md, SHA256 267bd0354543568a1dbb7b3aa56327afedb415335b96f204c92b3aa3b435059b
- RE = erratum-1-residual-RUH2-v1.md, SHA256 52871fb8f9dc796a35fef55367764335506131856e1e24a96e3c204027ac94ac

## M1 (Codex MAJOR 1; P lines 146-147, PE lines 35-36): non-wrapping induction for c=9

In P, Old:
````text
contains [1,t+5]. For a set Y of empty runs with m intervals, s(Y)+[m,m+4] is in M; it must meet [1,t_max+5] (else |M|>=11),
so M contains [1,s(Y)+m+4] and s(Y)+m<=5, where s(Y)>=|Y|>=m. Hence E<=4, and E=4 means four consecutive empty runs with t=1.
````

New:
````text
contains [1,t+5] for each lift t; with t_max the largest lift, M contains B0':=[1,t_max+5], |B0'|>=6. For a set Y of empty
runs let s(Y) be the INTEGER sum of the lifts t_i in [1,4] and l(Y):=s(Y)+m(Y); for m(Y)<=5 the forced residues of Y (lengths
j in [m,m+4], all free by E2) are the residues of the integers [l(Y),l(Y)+4]. Claim: l(Y)<=5 for every set Y of at most five
empty runs. Singletons: l=t+1<=5. Induction on |Y|: if Y'=Y u {i} with |Y'|<=5 and l(Y)<=5, then m(Y')<=m(Y)+1 and t_i<=4
give 2<=l(Y')<=10<p. If the integer interval [l(Y'),l(Y')+4] contains p, its residues contain 0, which is not in M:
impossible. Otherwise it lies in [2,p-1], where residues are distinct; its five residues cannot avoid B0' (|M|<=9), so the
integer intervals meet, M contains [1,max(t_max+5,l(Y')+4)], and l(Y')+4<=9. Hence l(Y)<=5 for all such Y. Five empty runs
would give l>=5+1: so E<=4, and E=4 forces s=4, m=1: four consecutive empty runs, all with t=1.
````

In PE (the parenthetical after item E2), Old:
````text
(In the c=9 case the bound E<=4 applies the interval rule to a set of five empty runs, with m<=5 and j<=9; and an interval
s(Y)+[m,m+4] that met [1,t_max+5] while reaching p would contain p, i.e. 0, which is not in M; so no residue wraps.)
````

New:
````text
(In the c=9 case the bound E<=4 applies the interval rule only to sets of at most five empty runs, with m<=5 and j<=9. Its
non-wrapping is proved by the induction in item M1 of erratum-2-RUH2-v1.md, which supersedes the earlier remark: that remark
excluded only intervals crossing p, not intervals lying wholly above p.)
````

## N1 (Codex MINOR 1; P line 117): scope of Lemma L in Sec. 7

Old:
````text
Here R=3p-11, A=2p-10+c, b=p-1-c, |M|<=c, Lemma L reads: sets avoiding h have d<=c-1 (m=1), d<=c-3 (m=2), d<=c-5 (m>=3).
````

New:
````text
Here R=3p-11, A=2p-10+c, b=p-1-c, |M|<=c, Lemma L reads: sets avoiding h have d<=c-1 (m=1), d<=c-3 (m=2), d<=c-5
(3<=m<=5; Lemma L is not claimed for m>5, and every application below has m<=5).
````

## N2 (Codex MINOR 2; P line 119): delete the false blanket distinctness sentence

Old:
````text
(N1) at 2j=9-c. All residues used are integers in [-4,10], distinct mod p (p>=13). E>=2; |Q|<=c-1; E+|Q|>=c+1. For a set P
````

New:
````text
(N1) at 2j=9-c. Residue convention (replacing a false blanket claim: at p=13, -4=9 and -3=10 mod p): each forced set below
is a set of cyclically consecutive residues; if it contains 0 the case is excluded (0 is not in M); otherwise it is the residue
set of a unique integer interval inside [1,p-1], where residues are distinct, and every overlap or inclusion below compares
such interval lifts (with the base interval [2,4] or [1,4]). E>=2; |Q|<=c-1; E+|Q|>=c+1. For a set P
````
(The singleton, pair and triple lists for c=5,...,8 are unchanged; they compare interval lifts as stated.)

## N3 (Codex MINOR 3; P line 139): the adjacent (1,1) pair at c=8

Old:
````text
s+[1,5], non-adjacent s+[2,6]): (1,1) allowed (M contains [1,8]); (1,2) adjacent only (non-adjacent needs 9); any pair with a 3,
````

New:
````text
s+[1,5], non-adjacent s+[2,6]): (1,1) allowed (an adjacent pair forces only [1,7] in M, a non-adjacent pair [1,8]); (1,2)
adjacent only (non-adjacent needs 9); any pair with a 3,
````

## N4 (Codex MINOR 4; R lines 27-29): toggle-path diagnosis in route F1

Old:
````text
(F1) m=e window when 3e>p+2: in the proof of (MWe) the branch r<=e-2 with r>=p-2e+2-eps is no longer empty, so MW only gives
     phi>=p-1+2(p-2e+2-eps)+eps=3p-4e+3-eps, not phi>=p+kappa. The toggle path then certifies a jump of the weaker gap only;
     no super-heavy run follows.
````

New:
````text
(F1) m=e window when 3e>p+2: in the proof of (MWe) the branch r<=e-2 with r>=p-2e+2-eps is no longer empty, so MW only gives
     phi>=p-1+2(p-2e+2-eps)+eps=3p-4e+3-eps, not phi>=p+kappa. If N=p+1>=2e+2 (e<=(p-1)/2), the toggle path of proof Sec. 3
     exists and certifies only a jump across the weaker gap, so no super-heavy run follows by this route. If e=(p+1)/2
     (N=2e), the only sets with m=e are the two alternating sets, no single-run toggle path preserves m=e, and the route is
     unavailable.
````

## N5 (Codex MINOR 5; RE lines 16-17): fixed-delta qualification in route F2

Old:
````text
     and this is compatible with A'<=b-delta=p-1-c-delta whenever c<=2e-4.
````

New:
````text
     and, for a given delta, this is compatible with A'<=b-delta=p-1-c-delta exactly when kappa+1-c/2<=p-1-c-delta, i.e.
     c+2delta<=2e-4 (for delta=0: c<=2e-4); a statement about all profiles must make the quantifier over delta explicit.
````

## Effect
No statement of P, PE, R or RE changes. Lemma L, Theorem A, Theorem B, Corollary B and residuals R1/R2 stand as stated, with
Theorem B's c=9 case argued by the induction of M1, the Sec. 7 conventions of N1/N2, and the corrected c=8 parenthetical of N3.
N4 and N5 qualify failed-route descriptions only. Every claim remains CANDIDATE_UNVERIFIED; the parent owns review and verdict.
