# Candidate excess-two NMH theorem for every prime p>=5 (computer-assisted)

Written 2026-10-17T20:52:15-0700, task OlsonRunCount5, cycle 6.  Status: **candidate [W+F], unverified and NOT promoted**.  This combines a written
universal implication with load-bearing finite arithmetic, whose independent parent/cross-vendor/third-checker gates remain open.
It is not a proof of general NMH, MIX_DEF_HIGH, RUNS, PAR, INV, INV* or ordered Olson.

## 1. Candidate theorem and larger-prime part

**Candidate theorem.**  Every NMH word with E=R-k=2 and R<=2p-3, every prime p>=5, has an identity 2p-subword, all run structures and
placements included.

For p>=31 use the candidate E2-layer theorem of c6/proof-E2layer.md.  Its finite-constant certificate has SHA
  cba0206dd7db29b7b840eca3aa35b77720e6591bf5ab75ca558292bb67f22b86
and its 175 balanced +140 small-g rows are load-bearing; it is not merely a check of primes below some cutoff.  Read the weak
seed import with the review-repaired proof-SEEDGstar-r1.md and the profile import with proof-SEEDG-cls-r1.md.  Correcting the
minimum wording and removing automatic PIN changes none of the constant certificate obligations or values.  The independent
verification requirements of that candidate remain requirements of this combined candidate.

## 2. All smaller primes: a complete finite class universe, not a word census

For an NMH word E<=p-4 (R<=2p-3 and k>=p+1).  At p=5, even E cannot equal2, so there is no case.  The remaining primes below31 are
7,11,13,17,19,23,29.  The class enumeration in seedX3.py includes every NMH parameter tuple (p,k,kappa,B) under the necessary
identities and inequalities; E2_small_primes.py filters E=2 and records every class ID with its criterion verdict, without
executing any map/IND* label code.

The finite [F] result is:

| p | E2 classes | X* criterion pass | finite supplement needed |
|---|---:|---:|---:|
|7|3|3|0|
|11|21|21|0|
|13|36|36|0|
|17|78|78|0|
|19|105|105|0|
|23|171|170|1|
|29|300|293|7|
|total|714|706|8|

For each of the 706 passing classes the exact criterion verifies every arithmetic profile, actual-configuration hull seed ranges,
weak endpoint and P2 tests or actual-empty guaranteed weights, as in reviewed Corollary X*.  E=2 itself supplies C0+ case(i), so the
written implication excludes every word of each passing class.  This is [W+F], not an empirical search for avoiders.

## 3. The eight supplement classes have explicit ordinary mixed-single recipes

The X* sufficient test fails in these eight classes (this does not produce an avoider):
 (p,k,kappa,B)=(23,41,19,18),
 (29,52,24,21),(29,52,24,22),(29,52,24,23),
 (29,53,25,21),(29,53,25,22),(29,53,25,23),(29,53,25,24).

E2_low_supplement.py checks actual ordinary mixed-single configurations for each possible target weight d=-3..3 DIRECTLY at those
parameters.  It does not apply a p>=31 theorem to a smaller prime.  The construction is the elementary RZ ordinary-run argument
already written in E2-tip: n1_al>=p+g-3+f_d, n1_an>=B-4, with f_d=(4,2,0,1,0,0,1).  For a proposed type (y,m) the finite conditions
  m-y even, 0<=y<=m, m-y<=B-7, 2m<=p+g-6+f_d, 2m+2<=k
supply i=(m-y)/2 ordinary anti runs and j=(m+y)/2 ordinary aligned runs, separated from each other and the target.

The recipes are:
 - g>=3: m=(p-3)/2, choose c=2 or3 matching m-g, y=g+c.  Availability is checked at each of the three relevant parameter classes
   (the D=4,g=3 class and the D=3,g=3,4 classes).
 - g=1,2,D=3: the two fixed-offset recipes of proof-E2smallg.md's g/rho/d table, evaluated and checked directly at p=23 or29.
 - g=1,2,D=4: the corresponding small-g constant rows of the pinned certificate, evaluated and checked directly at p=29.

The finite receipt checks every no-wrap inequality, exact two-pattern endpoint, canonical intersection and quality inequality for
all possible target weights.  Each resulting intersection is quality or actually empty, so ORIGINAL quality SEED-G with C0+
case(i) excludes the class.  This supplement itself needs no weak-seed or count-free-finisher claim.
Literal controls: 32 actual words, 2,640 configurations, all block/isolation/mass and independent c5 slow_lambda interval checks
pass; 119 intersections are actually empty.  Removing the ordinary-run restriction changes the required mass in440 mutated
configurations.  These controls support the availability proof and finite inequalities; no raw group counterexample is claimed.

## 4. Combined scope and remaining gates

The p>=31 implication, the impossible p5 case, the finite706 criterion applications and the eight direct recipe supplements exhaust
all primes>=5 for E=2.  Thus, CONDITIONAL on the independent acceptance of the named mathematical imports and finite certificate,
the candidate theorem follows.  Positive excess E>=4 remains untouched except for the separately stated explicit regions; even if
this candidate is accepted, no full RUNS/PAR/inverse/ordered-Olson conclusion follows.

The strict finite-constant checker, its intended-reason mutation fixtures, byte-exact generator replay and producer-only status are
documented in proof-E2layer.md.  These independent gates have not been performed by this worker.  The additional small-prime
checks use seedXstar3.py/seedX3.py, with exact integer bounds and hash headers (E2_small_primes.py), and the direct supplement
script, which also prints all exec-source hashes.  No model CLI, network or independent-checker claim is hidden in this work.

Receipts: out/E2_small_primes.txt (706+8 class split, every class ID), out/E2_low_supplement.txt (all eight recipe checks).  All .err
files are empty.  Peak child RSS is 36,519,936 bytes for the supplement; native CPU/file-size limits.  Every file was created with
mode x; old candidates and receipts are unchanged.
