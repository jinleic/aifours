# BOTTOM checkpoint 003: a full bottom-cell closure candidate has been derived; writing the companion proof

Owner OlsonPP1Exclusion. /bin/date 2026-10-19T18:52:50-0700. Previous checkpoint-002.md SHA256
099fbe1607a800aef3ac46fb46462e939b0ec2aa49a504aef1daaeea1533d636 (18:43:18). Frozen first proof:
proof-BOTTOM-parity-v1.md b648411f7ed7b2b17fdd9bcc4a51f2df24ca7a1540eb88cd4c7fbd2e6080a9f3 (18:47:44), E=0 + necessary escape.
NEW hand derivation (CANDIDATE, not yet frozen): among all INTERIOR low critical patterns, g=2r+1, r+2<=m<=e-r-1, choose
smallest g. Every singleton rotation is signed -a (flipping signed a gives the even-window contradiction; flipping 3a
violates rigidity). A singleton -a can flip only out of this m-interval, so m is a boundary. At a sole lower boundary all
singletons are isolated, giving s1<=g+2; at a sole upper boundary they are flat, giving s1<=g. LEN then bounds every L_i<=g.
But w0=p-1-g<N ensures a pure signed-a run, necessarily length >=2; flipping it gives either the even-window contradiction
or a smaller interior odd g (or g=0, forbidden). So both boundaries must coincide: e odd, g=e-2, m=(e+1)/2. Hence no interior
critical pattern for e even; for e odd every such pattern is that top one.
- e even: all escapes are g=e-1,m=k0. Low cap e-1 at m<=k0 gives a run of length >=p-1 via the toggle path, impossible with
  E=0 and p other positive runs (R=2p-2).
- e odd: all escapes are g=e-2,m=k0. Low cap e-2 gives a run of length >=p-3+delta. Hence there are >=p-1+delta singleton
  runs, but every singleton is signed -a at the top interior critical pattern, whose entire minority has only w0=e letters.
  Since p-1>e this is impossible.
Thus the whole specified bottom cell appears excluded uniformly. Next: freeze proof-BOTTOM-close-v1.md with these arguments,
line audit, failed-route/closeout ledger, <=100KB review package + manifest, notify Main with exact pins, park.
