# KP4 checkpoint 002: p>=11 proof checked by hand; p=7 pure case proved; p=7 impure is the residual

Owner OlsonPP1Exclusion. /bin/date 2026-10-19T16:23:21-0700. Previous checkpoint-001.md SHA256
ca75158f18eaaeb8c227c18e967c344033c406e54f6a1272c89cd9131254af83 (16:16:14). No candidate frozen yet.

Actual results (hand-derived, CANDIDATE_UNVERIFIED, to be frozen next):
- p>=11: complete exclusion (route of checkpoint 001; every step re-checked: SR4 from GRX's C range, pairing needs
  2(p-1)<=R, MW at m=2 (>=2p-5), m=3,4 (>=2p-4), m=4 toggle path N>=9, light sets, c=1..7 case analysis with exact
  free/non-free lengths r=8-c-2j and n>=b (needs p>=10 for j<=6), wrap-around checked for p=11,13).
- p=7 (kappa=3=(p-1)/2): A>=7, A'<=3, dominant>=7 in {a,-a}; MW only excludes dominant 8 at m=2,3.
  NEW Proposition (pure case): if all 12 rotation letters are equal, contradiction. Route: exact attained intervals
  x=nu-q; arcs never hold 6 letters; m=2 and m=3 sets never hold 4, 6 or 8 letters; single empty t in {1,2}; two
  non-adjacent empties give t-sum in {2,3,4} against allowed {-1,0,1}, so E<=2 (adjacent if 2); a complete profile
  enumeration for E=0,1,2 (run sizes) is contradictory in every profile.
- Observation (route failure): in the pure p=7 case every run has <=5 letters, so the super-heavy-run mechanism of the
  p>=11 proof is not available at p=7 at all.
- Blocker: p=7 with a non-constant rotation multiset (A<=11 after orientation). Decision: deliver O3 now = full proof for
  p>=11 + p=7 pure-case proposition + exact p=7 obstruction note; next action: freeze proof, obstruction, package.
