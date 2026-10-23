# Erratum 1 to residual-RUH2-v1.md (wording of route (F2) only)

Owner OlsonPP1Exclusion. Written after /bin/date 2026-10-19T17:27:31-0700. Read after the immutable residual-RUH2-v1.md, SHA256
267bd0354543568a1dbb7b3aa56327afedb415335b96f204c92b3aa3b435059b. No claim changes; the Old span occurs exactly once.

Old:
````text
(F2) Ordinary first passage: a high single run is forced only if Lambda-lambda>lambda, i.e. c<=p-2e+3+delta; light sets need
     A<2 Lambda, i.e. A'<kappa+1-c/2 fails to be excluded in general (two disjoint high sets need A'>=kappa+1-c/2, which is
     compatible with A'<=b-delta when c<=2e-4).
````

New:
````text
(F2) Ordinary first passage: a high single run is forced only if Lambda-lambda>lambda, i.e. c<=p-2e+3+delta. Light sets by
     this route need A<2 Lambda, i.e. A'<kappa+1-c/2, which is not guaranteed: two disjoint high sets need A'>=kappa+1-c/2,
     and this is compatible with A'<=b-delta=p-1-c-delta whenever c<=2e-4.
````
