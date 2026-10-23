# KP4 checkpoint 001: p>=11 route derived in writing; p=7 is the open sub-case

Owner OlsonPP1Exclusion. /bin/date 2026-10-19T16:16:14-0700. Scope frozen 16:04:10, KP4-EXCL-scope-v1.md SHA256
ba13fdd35cb02b11b179c8a9087737cf35e55f9197ae4512dac62edf9cc51c4f. No candidate file frozen yet (notes only).

Actual result derived by hand (CANDIDATE_UNVERIFIED, not yet frozen), every prime p>=11, full NF antecedent:
- SR: all even C in [Phi,Phi+6] (H=3 split arbitrarily), n even in [max(0,2p-6-2m), min(2p-2m,R)], R=3p-9.
- Re-derived pairing (p-1 pairs need 2(p-1)<=R, true for p>=7), dominant >=2p-7 in common class {a,-a}, a!=0; A'<=p-4,
  A<=2p-1 (the length 2p needs p>=9).
- MW (exact omission counts): m=2 gives dominant >=2p-5 (p>=8); m=3 and m=4 give >=2p-4 (needs p>=10, i.e. 3e<=p+2).
- m=4 toggle path P0={0,2,4,6} -> complement (N=p+1>=9) gives a super-heavy h, d_h>=p+1+delta; all sets avoiding h are
  ordinary-low; lambda>=0; >=2 empty runs; A=2p-8+c, c=1..7, b=p-1-c, |M|<=c; E+|Q|>=c+1, |Q|<=c-1; strong bounds for sets
  avoiding h: m=2: d<=c-3; m=3,4: d<=c-4.
- Free length j (n=2p-2j) iff 2j>=8-c; r=8-c-2j>=1 gives only "not in G_{>=r}".
  c=1,2,4 die by M-intervals directly; c=3 dies by no-independent-triple in S=E u Q -> Q empty, E=4 -> triple of empties
  forces 0 in M; c=5 -> exactly two empties (t=1,-1) -> |Q|=4 -> m2/m3 sets; c=6 -> two adjacent empties t=1 -> |Q|=5;
  c=7 -> t<=3, non-adjacent pairs t=1, E<=3 (consecutive if 3) -> |Q|>=5 -> m2/m3/m4 sets with d over the strong bounds.
- p=7 (kappa=3=(p-1)/2, R=12, 8 runs): MW gives only "dominant != 8" for m=2,3, nothing for m=1,4; the super-heavy route
  fails. Re-derived so far at p=7: A>=7, A'<=3, window d<=A-7 or d>=7-A'; pure case (all rotations a): arcs never hold
  exactly 6 letters, runs <=5 letters (pure-heavy lift argument), lifts additive on low arcs.
- Blocker: p=7 general (impure) case. Next bounded action: attempt a complete p=7 argument (pure case via lifts, then the
  impure cases); if not closed within the next checkpoint, freeze O3: proof for p>=11 plus exact p=7 obstruction.
