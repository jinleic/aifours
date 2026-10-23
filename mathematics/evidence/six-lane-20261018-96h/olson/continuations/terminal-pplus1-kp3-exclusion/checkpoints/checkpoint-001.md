# KP3 checkpoint001: candidate complete written route (not yet a frozen proof)

Owner OlsonPP1Exclusion. /bin/date 2026-10-19T13:58:09-0700. Scope frozen13:54:42, SHA256
58ca7d6281f5532b85536efb1cb7c0fb6e30dcabbca3bac3e0fea7b8c678c169.

Actual result now derived by hand, CANDIDATE_UNVERIFIED: full exact-cell exclusion k=p+1,kappa^=p-3 for every primep>=7,
arbitrary H=2 distribution, no o_F/run/rotation-pair assumption. Route:
- SR: all even C in[Phi,Phi+4], so m3 admits n=2p-10,2p-8,2p-6. Re-prove M/P/U and MW only at m3: signed dominant>=2p-3.
- Complementary m3 comb-path forces h with d_h>=p+1+delta. Every set avoiding h is ordinary-low; lambda>=0 and >=2 empty runs.
  Hence A=2kappa+c with c=1..5 (no UH-A premise). lambda=c-1, strong m3 low bound outside h is c-3.
- c1: M* singleton, empty t=-2; pair n=2p-6 contradicts it. c2: M*={1,2}, empty t=-1; pair n=2p-4 hits0. c3: all-plus n>A
  gives1 inM*; with2 inM* and single-empty intervals, t=-1; same pair contradiction. c4: M*={1,2,3,4}, empty t=1; pair
  n=2p-6 demands5, contradiction.
- c5: |M*|<=5, base{1,2}, each empty t+[1,3] inM*,tau!=0. If t>=3 (canonical), M*={1,2,t+1,t+2,t+3}, whose only allowed
  three-interval is t+[1,3]; a second empty has same t and either adjacency forces t=0 or non-adjacency forces t=-1. Thus
  t in{1,2}; any t=2 with second empty forces6 outside M*. Therefore all t=1. Nonadjacent pair would force all1..6 intoM*;
  so exactly two adjacent empties, M*={1..5}.
- With E=2,b=p-6,ordinary lambda4: there are exactly four pure-a singleton runs outside h. Cycle lemma (>=8 vertices):
  four marked runs Q plus a disjoint adjacent empty pair E admit a set P⊂Q∪E with m3 and at least3 marked runs. If Q has
  an independent triple, use it; otherwise Q is a path4 or two disjoint adjacent pairs. A suitable empty vertex supplies a
  third interval (drop one marked endpoint in the sole gap2 configuration). Strong m3 bound d(P)<=2 then fails.

No inverse/critical sumset theorem assumed; the parent sketch's classification/exhaustive reduction has been proved directly
at the needed small missing-set size. No pending result used. Next: freeze full self-contained proof, review package and
<=100KB manifest, then parent review/park. No computation/enumeration/CLI/Lean/runtime.
