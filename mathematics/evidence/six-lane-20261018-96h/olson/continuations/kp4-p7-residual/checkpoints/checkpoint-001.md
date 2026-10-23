# R7 checkpoint 001: complete hand route found for every non-pure p=7 case (not yet frozen)

Owner OlsonPP1Exclusion. /bin/date 2026-10-19T16:56:34-0700. Scope frozen 16:40:24, R7-scope-v1.md SHA256
6310d69356c0ae85662dded3b3ff2d45d9ca3f8bf2ea42b0ffb01206092e8b39. All work below is written/hand mathematics; no script,
assertion, enumeration or computation over scientific data was run.

Route (CANDIDATE_UNVERIFIED, to be frozen next):
- Re-derived at p=7: pairing (6 unequal pairs at n=6) gives a dominant value of multiplicity >=7 in a common class {a,-a},
  a!=0, for EVERY non-constant pattern; normalize a=1 by the automorphism (v,e)->(v/a,e). Window: for every proper nonempty
  set P of runs, d(P)=alpha(P)-beta(P) avoids the band [A-6, 6-A'].
- Input change: accepted UH-A gives A>=9, so b=12-A in {1,2,3}.
- All-plus lengths 8,10,12 force the non-a letters' weights omega=(beta-1)/2 to avoid 3 (all subsets), 2 (subsets of size
  >=b-2) and total 1: exactly twelve multisets B: {-1},{2},{4}; {3,2},{3,4},{3,-1},{4,-1},{-1,-1}; {2,2,2},{3,4,-1},
  {3,-1,-1},{-1,-1,-1}.
- Empty-run lengths give per configuration: E=0 for {3,2},{3,4},{2,2,2},{3,4,-1},{3,-1,-1}; E<=1 for {2},{4},{3,-1},{4,-1},
  {-1,-1}; E<=2 for {-1} (opposite t) and {-1,-1,-1} (both t=-1).
- Eliminations: heavy single run + light sets + run count forces E>=2 in the five E=0 configurations; band-avoiding subset
  sums of run weights with explicit partition lists kill {2},{4},{3,-1},{4,-1},{-1,-1}; the pair cases {-1},{-1,-1,-1} reduce
  to finitely many weight profiles, each killed by the exact epsilon-interval tables (m=2,3 sets with epsilon 4 or 8) or by
  t-value tables (Allow_1(3),Allow_1(5),Allow_2(5),Allow_2(7)). The pure case also follows in 4 lines (profile (7,1^5)).
- Blocker: none in the route. Next bounded action: freeze the full written proof with every branch, the review package and
  manifest (<=100 KB), closing checkpoint, IRC Main, park.
