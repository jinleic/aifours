# Scope: option (b), written attack on R = p and small kappa

Frozen after /bin/date observation 2026-10-19T08:08:20-0700 by OlsonReflectionSuccessor.  Parent offered ONE written slice;
I choose option (b), not option (a).  This is the existing ordered-Olson reflection slot, not a replacement target.
Ownership remains this reflection-round2 directory.  New exclusive files only; earlier records remain unchanged.
No computation, probes, tests/builds, model calls, CLI reviews or process launches.  Parent owns reviewers and verdicts.
Checkpoints no more than 1800 seconds apart while active; read /bin/date before every timestamp.

## Exact target and success criterion

Prime p >= 11; w has length 4p - 2 over D_(2p), rotations in one nonzero pair, exactly R = p rotation letters; all maximal
cyclic CONSTANT reflection blocks are odd; 2 <= kappa < ceil((p + 1)/4).  Prove no avoider exists (any B, including the
RES_< cases 0 <= B < kappa).  The smallest cell is p = 11, kappa = 2 (B = 1 remains after the accepted B = 0 exclusions).
Success: a complete written proof excluding this whole R = p small-kappa region, or at minimum the p = 11, kappa = 2 cell;
if the proof fails, preserve a precise obstruction/counterexample to the proposed lemma and distinguish it from an avoider.
No finite search, model agreement, novelty or formal-verification claim.

## Accepted inputs

Parent verdict read in full and hash checked:
/Users/jinleic/repos/aifours/institute/runs/six-lane-2026-10-18-96h/review/olson-REFLHI-v5-parent-verdict-v1.md,
13ee1ba86245fc549bd79c130a9fe15248ecc3fe9fc8428e875ca939c940a547.
Its text of record is proof-REFLHI-arcs-v5.md (4e463746...cff1c) through errata 1-5 (especially 40832206...25f4), with all
verdict bindings S1/m1-m7.  Needed interfaces only: Lemma W (H0 windows), Fact 2.1 (floor-type range), Fact 2.2 (R >= p,
run length <= 2(R-p)+1).  All are parent-accepted at setting (S), with no B<kappa or run-purity hypothesis.
At R = p an avoider therefore has p one-letter nonempty runs, 2 kappa empty runs and k = p + 2 kappa odd blocks.
Separate SEG-k/TRANSFER/region-B/B-prime candidates are NOT imports for this slice.

## Written attack

Combine count parity and H0 value in C_(2p): for floor-type patterns, transform the killed half-window into one fixed
cyclic interval of length p+1, independent of E+.  Avoidance may then allow a simultaneous integer lift across the graph
of patterns with m in [kappa+1, (p+1)/2].  Prove that graph's connectivity explicitly (including P to P^c); do not infer it
from earlier graph statements at a different scope.  Then attack the resulting bounded integer signed-sum condition by a
cyclic sign-stretch argument, using that empty runs have nonzero even lifts while one-letter runs have odd lifts.
Everything after the accepted window interfaces is a NEW proof obligation, not an assumed theorem.

## Remaining global boundary

The target is R = p only.  R > p, unrestricted REFL-HI/RES-HI, rotation rigidity, INV* and ordered Olson remain open.
Any broader theorem emerging from the same argument must have its exact quantifiers written and proved separately.
