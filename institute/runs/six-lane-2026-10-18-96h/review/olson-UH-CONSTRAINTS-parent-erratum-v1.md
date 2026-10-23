# UH constraints: residual-window arithmetic and free-length precision

Recorded at 2026-10-19T13:51:59-0700. Apply after proof `56327b678bf9f7fe62d6f518499ab692f00897a3ecff2c62ddecac4a42a5115c` and obstruction `f2f1a232c98b3ef6eb45fa0486912bd54170521e5adc00e09c436b1fb8c7849d`. These are parent pre-review corrections; no result is accepted yet. Main UH-A proof unchanged and whole upper-half exclusion remains UNPROVED.

1. Obstruction lines32 and52: with A=2kappa+c and b=p-1-c, the ordinary low threshold is **lambda=A-2kappa-1=p-2-b=c-1**, NOT c-2. Replace both c-2 occurrences by c-1. Proof equationW already has the correct formula. The residual R-UH statement must retain this correct threshold; no stronger residual condition may be silently assumed.
2. Obstruction line85's assertion that j=-1 can fail the free lower bound at the bottom endpoint is not true AFTER UH-A: b<=p-4, while 2kappa-2>=p-3>b throughout the current interval. Thus the displayed b<=n qualification is automatic for those residual j=-1 lengths. Keep LemmaE's exact general subset-family bounds, but withdraw the claim that an actual residual length fails this bound here. The historical pre-UH-A counting sketch is not an obstruction for the tightened residual.

These corrections do not establish R-UH or exclusion of any whole kappa cell. Necessary word constraints are not existence certificates or multiset-only nonexistence theorems.
