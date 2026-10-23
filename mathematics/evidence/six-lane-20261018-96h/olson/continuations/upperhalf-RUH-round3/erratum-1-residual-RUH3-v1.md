# Erratum 1 to residual-RUH3-v1.md (precision of MC1b and of one justification; no claim changes)

Owner OlsonPP1Exclusion. Written after /bin/date 2026-10-19T18:16:53-0700. Read after the immutable residual-RUH3-v1.md, SHA256
38c6d830174da3e78c8b8bf4c2b2920ed057afebd9aeb6a4e63c0c9447e3b283. Each Old span occurs exactly once.

## E1 (Sec. 4, MC1b): which interval count replaces k''
At e=(p+1)/2, k''=min(e,floor((p+2-e)/2))=floor((e+1)/2), so 2k''-1>=e can fail (e even) and (e+1)/2<=k'' can fail; the
reduction must use k''':=floor(e/2)+1 instead.
Old:
````text
       mechanism replacing MW where c-d is odd. With these, R3-ext Secs. 4-6 would apply (Lemma E* already holds there).
````
New:
````text
       mechanism replacing MW where c-d is odd. With these, R3-ext Secs. 5-6 would apply with k'' replaced by
       k''':=floor(e/2)+1 (then 2k'''-1>=e, c-e<=e-1<2k''', m(P')=E/2+1<=k''', and in branch (alpha) e+2k'''>=2e+1=p+2>p-2+eps);
       Lemma E* already holds there. This is a route statement only.
````

## E2 (Sec. 2): the bound g<=p-1 behind "j<=p"
Old:
````text
  or g>=2(e-m(P))+2 (if g/2+1<=m(P)<=e-g/2, the g+1 lengths j in [e-g/2,e+g/2] are admissible, 1<=j<=p, and counted, against
````
New:
````text
  or g>=2(e-m(P))+2 (if g/2+1<=m(P)<=e-g/2, the g+1 lengths j in [e-g/2,e+g/2] lie in [m,m+e-1], are admissible since
  1<=m<=j and j<=e+g/2<=p (g=c-d(P)<=c+A'=p-1-delta), and are counted, against
````
